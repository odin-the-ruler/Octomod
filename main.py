# GET THE QUESTION FROM THE BOT
import random
from telethon import TelegramClient, events
import asyncio
import re
import nltk
from nltk.corpus import words
import os
from dotenv import load_dotenv
import sys

sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

# Define your API ID and API hash
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

if not api_id or not api_hash:
    raise ValueError("API_ID and API_HASH environment variables must be set")
group_username = '@OctopusGame_EN'
bot_username = 'OctopusEN_Bot'

# Create the client and connect
client = TelegramClient('octoplay', api_id, api_hash)

# Download the words corpus if not already available
nltk.download("words")

# Load the dictionary from nltk
word_list = set(words.words())

def get_valid_words(letters, pattern, word_list):
    pattern = pattern.lower()
    word_length = len(pattern)
    letters = letters.lower()
    possible_words = []
    
    # Create regex pattern from the given pattern
    regex_pattern = "^" + pattern.replace("_", ".") + "$"
    
    # Filter words from nltk's word list that match the length and regex pattern
    for word in word_list:
        if len(word) == word_length and re.match(regex_pattern, word):
            if all(word.count(l) <= letters.count(l) for l in set(word)):
                possible_words.append(word)
    
    return possible_words if possible_words else ""

# Input values
letters = "OMERYM"
pattern = "M E _ O _ Y"
pattern = pattern.replace(" ", "")  # Removing spaces

def format_string(input_str):
    # Split the input string into parts
    parts = input_str.split()
    
    # Remove the first two elements (the number and the word "letter")
    letters = parts[2:]
    
    # Convert to uppercase and join
    result = "".join(letters).upper()
    
    return result


async def main():
    await client.start()

    # Get the group entity using the username
    group = await client.get_entity(group_username)

    last_question = None

    @client.on(events.NewMessage(chats=group))
    async def handler(event):
        # Check if the message is from the bot
        if event.sender.username == bot_username:
            # Extract only the string part of the message, excluding emojis
            message_text = re.sub(r'[^\w\s,.!?]', '', event.message.message)
            print(message_text)
            second_last_line = message_text.split('\n')[-2].strip()
            print(f'Second last line: {second_last_line}')
            content= format_string(second_last_line)
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
                        if button.text=="Pass ♻️":
                            print("Pass Button")
                            await asyncio.sleep(7)
                            await button.click()
                            print("Got clicked")
                            break
            else:
                print("Output:", result)
            await asyncio.sleep(random.randint(4, 7))
            for res in result:
                await client.send_message(group,res) 
            # await asyncio.sleep(2)
                # Check if the same question is still there
            new_message = await client.get_messages(group, limit=1)
            new_message_text = re.sub(r'[^\w\s,.!?]', '', new_message[0].message)
            print(new_message_text)

            
    print(f'Listening for messages from {bot_username} in {group_username}...')
    await client.run_until_disconnected()

# Run the client
with client:
    client.loop.run_until_complete(main())
