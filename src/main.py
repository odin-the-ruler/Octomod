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
from telethon.errors import FloodWaitError

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

    - `.p` : Start the bot in a group.
    - `.e` : Stop the bot from playing in the group.
    - `.f` : Play fast (no delay).
    - `.n` : Play normal (default delay).
    - `.s` : Play slow (increased delay).

    If you have any questions or need assistance, feel free to reach out.

    Best regards,
    **Octomod Team**
    """)

async def notify_user(message):
    me = await client.get_me()
    await client.send_message('me', message)

async def main():
    await client.start()
    await send_welcome_message()

    # Event handler for the /play command to set the group
    @client.on(events.NewMessage(pattern='.p', outgoing=True))
    async def set_group(event):
        global group_username
        try:
            group_username = event.chat_id
            print(f'Octomod is playing in {event.chat.title}')
            await notify_user(f'Octomod is now playing in {event.chat.title}')
            # await event.reply(f'Octomod is now playing in {event.chat.title}')
        except Exception as e:
            await event.reply(f'An error occurred: {e}')

    # Event handler for the /end command to stop the bot
    @client.on(events.NewMessage(pattern='.e', outgoing=True))
    async def end_group(event):
        global group_username
        try:
            if group_username == event.chat_id:
                group_username = None
                print(f'/end command used in {event.chat.title}')
                await notify_user(f'Octomod has stopped playing in {event.chat.title}')
                await event.reply(f'Octomod has stopped playing in {event.chat.title}')
        except Exception as e:
            await event.reply(f'An error occurred: {e}')

    # Event handler for the /pf command to play fast
    @client.on(events.NewMessage(pattern='.f', outgoing=True))
    async def play_fast(event):
        global speed_mode
        speed_mode = "fast"
        print('Octomod playing in FAST speed')
        await notify_user('Octomod is now playing fast!')
        # await event.reply('Octomod is now playing fast!')

    # Event handler for the /pn command to play normal
    @client.on(events.NewMessage(pattern='.n', outgoing=True))
    async def play_normal(event):
        global speed_mode
        speed_mode = "normal"
        print('Octomod playing in NORMAL speed')
        await notify_user('Octomod is now playing at normal speed.')
        # await event.reply('Octomod is now playing at normal speed.')

    # Event handler for the /ps command to play slow
    @client.on(events.NewMessage(pattern='.s', outgoing=True))
    async def play_slow(event):
        global speed_mode
        speed_mode = "slow"
        print('Octomod playing in SLOW speed')
        await notify_user('Octomod is now playing slow!')
        # await event.reply('Octomod is now playing slow!')

    # Event handler for new messages in the group
    @client.on(events.NewMessage)
    async def handler(event):
        global group_username, speed_mode
        try:
            if group_username and event.chat_id == group_username:
                sender = await event.get_sender()
                if sender and sender.username == bot_username:
                    # Extract only the string part of the message, excluding emojis
                    print (event.message)
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
                        elif speed_mode == "slow":
                            await asyncio.sleep(random.randint(10, 15))
                        for res in result:
                            try:
                                await client.send_message(group_username, res)
                            except FloodWaitError as e:
                                print(f"Flood wait error: Sleeping for {e.seconds} seconds")
                                await asyncio.sleep(e.seconds)
                                # After flood wait, only respond to the most recent message
                                new_message = await client.get_messages(group_username, limit=1)
                                if new_message[0].id != event.message.id:
                                    print("New message detected, ignoring previous responses.")
                                    break
                                await client.send_message(group_username, res)
                        # Check if the same question is still there
                        new_message = await client.get_messages(group_username, limit=1)
                        if new_message[0].id != event.message.id:
                            print("New question detected, ignoring previous responses.")
                            return
                        print(new_message[0].message)
        except FloodWaitError as e:
            print(f"Flood wait error: Sleeping for {e.seconds} seconds")
            await asyncio.sleep(e.seconds)
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
