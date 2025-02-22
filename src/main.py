import random
import re
import asyncio
import os
import sys
import time
from dotenv import load_dotenv
from telethon import TelegramClient, events
import nltk
from nltk.corpus import words
from utils import get_valid_words, format_string
from startup import startup_banner, progress_bar, animated_loading

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

# Initialize group_username and speed_mode
group_username = None
speed_mode = "normal"

# Create the Telegram client
client = TelegramClient('octoplay', api_id, api_hash)

# Download the words corpus if not already available
nltk.download("words")

# Load the dictionary from nltk
word_list = set(words.words())

async def send_welcome_message():
    me = await client.get_me()
    await client.send_message('me', f"""
    🎉 **Welcome to Octomod!** 🎉

    Hi {me.first_name},

    Thank you for using Octomod. The bot is now up and running. You can use the following commands to interact with the bot:

    - `/play` : Start the bot in a group.
    - `/end` : Stop the bot from playing in the group.
    - `/pf` : Play fast (no delay).
    - `/pn` : Play normal (default delay).

    If you have any questions or need assistance, feel free to reach out.

    Best regards,
    **Octomod Team**
    """)

async def main():
    await client.start()
    await send_welcome_message()

    # Event handler for the /play command to set the group
    @client.on(events.NewMessage(pattern='/play', outgoing=True))
    async def set_group(event):
        global group_username
        try:
            group_username = event.chat_id
            await event.reply(f'Octomod is now playing in {event.chat.title}')
        except Exception as e:
            await event.reply(f'An error occurred: {e}')

    # Event handler for the /end command to stop the bot
    @client.on(events.NewMessage(pattern='/end', outgoing=True))
    async def end_group(event):
        global group_username
        try:
            if group_username == event.chat_id:
                group_username = None
                await event.reply(f'Octomod has stopped playing in {event.chat.title}')
        except Exception as e:
            await event.reply(f'An error occurred: {e}')

    # Event handler for the /pf command to play fast
    @client.on(events.NewMessage(pattern='/pf', outgoing=True))
    async def play_fast(event):
        global speed_mode
        speed_mode = "fast"
        await event.reply('Octomod is now playing fast!')

    # Event handler for the /pn command to play normal
    @client.on(events.NewMessage(pattern='/pn', outgoing=True))
    async def play_normal(event):
        global speed_mode
        speed_mode = "normal"
        await event.reply('Octomod is now playing at normal speed.')

    # Event handler for new messages in the group
    @client.on(events.NewMessage)
    async def handler(event):
        global group_username, speed_mode
        try:
            if group_username and event.chat_id == group_username:
                sender = await event.get_sender()
                if sender and sender.username == bot_username:
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
                                    await asyncio.sleep(6)
                                    await button.click()
                                    print("Got clicked")
                                    break
                    else:
                        print("Output:", result)
                        if speed_mode == "normal":
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

# Run the fancy startup sequence
startup_banner()
progress_bar()
animated_loading()

# Run the client
with client:
    client.loop.run_until_complete(main())
