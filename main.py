import random
import re
import asyncio
import os
import sys
from dotenv import load_dotenv
from telethon import TelegramClient, events
import nltk
from nltk.corpus import words
from utils import get_valid_words, format_string

# Configure stdout to handle UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables from .env file
load_dotenv()

# Define your API ID and API hash
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

if not api_id or not api_hash:
    raise ValueError("API_ID and API_HASH environment variables must be set")

# Define bot username
bot_username = 'OctopusEN_Bot'

# Initialize group_username as None
group_username = None

# Create the Telegram client
client = TelegramClient('octoplay', api_id, api_hash)

# Download the words corpus if not already available
nltk.download("words")

# Load the dictionary from nltk
word_list = set(words.words())

async def main():
    await client.start()

    # Event handler for the /play command to set the group
    @client.on(events.NewMessage(pattern='/play', outgoing=True))
    async def set_group(event):
        global group_username
        try:
            group_username = event.chat_id
            await event.reply(f'Group set to {event.chat.title}')
        except Exception as e:
            await event.reply(f'An error occurred: {e}')

    # Event handler for the /end command to stop the bot
    @client.on(events.NewMessage(pattern='/end', outgoing=True))
    async def end_group(event):
        global group_username
        try:
            if group_username == event.chat_id:
                group_username = None
                await event.reply('Bot has stopped playing in this group.')
        except Exception as e:
            await event.reply(f'An error occurred: {e}')

    # Event handler for new messages in the group
    @client.on(events.NewMessage)
    async def handler(event):
        global group_username
        try:
            if group_username and event.chat_id == group_username and event.sender.username == bot_username:
                # Extract only the string part of the message, excluding emojis
                message_text = re.sub(r'[^\w\s,.!?]', '', event.message.message)
                print(message_text)
                second_last_line = message_text.split('\n')[-2].strip()
                print(f'Second last line: {second_last_line}')
                content = format_string(second_last_line)
                print(f'Content: {content}')
                last_line = message_text.split('\n')[-1].strip()
                print(f'Last line: {last_line}')
                result = get_valid_words(content, last_line.replace(" ", ""), word_list)
                if not result:
                    print("Skip this")
                    # Click the "skip" or "pass" button
                    buttons = await event.get_buttons()
                    print(buttons)
                    for button_row in buttons:
                        for button in button_row:
                            print(button.text)
                            if button.text == "Pass ♻️":
                                print("Pass Button")
                                await asyncio.sleep(7)
                                await button.click()
                                print("Got clicked")
                                break
                else:
                    print("Output:", result)
                    await asyncio.sleep(random.randint(4, 7))
                    for res in result:
                        await client.send_message(group_username, res)
                    # Check if the same question is still there
                    new_message = await client.get_messages(group_username, limit=1)
                    new_message_text = re.sub(r'[^\w\s,.!?]', '', new_message[0].message)
                    print(new_message_text)
        except Exception as e:
            print(f"An error occurred in handler: {e}")

    print(f'Listening for messages from {bot_username}...')
    await client.run_until_disconnected()

# Run the client
with client:
    client.loop.run_until_complete(main())
