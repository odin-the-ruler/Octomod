# OCTOMOD

![OCTOMOD](/assets/logo/OCTOMOD.jpg)

## Introduction

**Octomod** is a powerful Telegram bot designed to enhance group interactions with engaging word-based gameplay. Whether you're hosting it locally, on a server, or using a cloud-based service like Replit, Octomod ensures a seamless experience. This guide will help you set up and use Octomod efficiently.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Example `.env` File

Create a `.env` file in the root directory of your project with the following content:

```
# .env
API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
```

## Running Locally

To run Octomod on your local machine, follow these steps:

```bash
python src/main.py
```

## Hosting on a Server

To host Octomod on a remote server, follow these steps:

1. Ensure Python and pip are installed on your server.
2. Clone the repository:

    ```bash
    git clone git@github.com:odin-the-ruler/Octomod.git
    ```

3. Navigate to the project directory:

    ```bash
    cd Octomod
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Create a `.env` file with your API credentials.
6. Run the bot using a process manager like `screen`, `tmux`, or `systemd` to keep it running:

    ```bash
    python src/main.py
    ```

## Running on Termux

To run Octomod on Termux (Android terminal emulator):

1. Install Termux from the Play Store or F-Droid.
2. Update and install Python:

    ```bash
    pkg update && pkg upgrade
    pkg install python git
    ```

3. Download the project ZIP file from GitHub:

    ```bash
    wget https://github.com/odin-the-ruler/Octomod/archive/refs/heads/main.zip
    ```

4. Extract the ZIP file:

    ```bash
    unzip main.zip && mv Octomod-main Octomod
    ```

5. Navigate to the project directory:

    ```bash
    cd Octomod
    ```

6. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

7. Create a `.env` file with your API credentials.
8. Start the bot:

    ```bash
    python src/main.py
    ```

## Running on Replit

To run Octomod on Replit:

1. Fork the repository to your Replit account.
2. Open the forked repository in Replit.
3. Add the required environment variables (`API_ID` and `API_HASH`) in the Replit Secrets.
4. Install dependencies in the Replit shell:

    ```bash
    pip install -r requirements.txt
    ```

5. Create a `.env` file with your API credentials.
6. Click the "Run" button in Replit to start the bot.

Alternatively, access the project on Replit via this link: [Octomod on Replit](https://replit.com/@darkiadev/Octomod?s=app)

## Available Commands

Here are the commands you can use to interact with Octomod:

- **`/po`** – Start the octomod bot in a group.
- **`/eo`** – Stop the octomod bot from playing in the group.
- **`/time <time>`** – Set a custom delay (in seconds) between messages.
## How to Use

1. Start the bot by running it locally, hosting it on a server, or running it on Replit/Termux.
2. Add the bot to your Telegram group and ensure it has the necessary permissions.
3. Send the `.p` command in the group to activate the bot.
4. The bot will start monitoring and responding to messages based on the game rules.
5. To stop the bot from playing, use the `.e` command.
6. To control the speed of responses, use `/time <time>` to set a custom delay.

## Licensing

This project is open-source and released under the MIT License. You are free to modify and distribute it under the terms of the license.

## Contact & Support

For any questions, feedback, or support, feel free to reach out via Telegram: [Contact Me](https://t.me/drecocox)

We appreciate contributions and suggestions to improve Octomod! 🚀

