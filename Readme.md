# OCTOMOD
![OCTOMOD](/assets/logo/OCTOMOD.jpg)

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Example .env file

Create a `.env` file in the root directory of your project with the following content:

```
# .env
API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
```

## Running Locally

To run the project locally, use the following command:

```bash
python src/main.py
```

## Hosting on a Server

To host the project on a server, follow these steps:

1. Ensure you have Python and pip installed on your server.
2. Clone the repository to your server.
3. Navigate to the project directory.
4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Create a `.env` file in the root directory with your API credentials.
6. Run the project using a process manager like `screen`, `tmux`, or `systemd` to keep it running in the background:

    ```bash
    python src/main.py
    ```

## Running on Replit

To run the project on Replit, follow these steps:

1. Fork the repository to your Replit account.
2. Open the forked repository in Replit.
3. Add the required environment variables (`API_ID` and `API_HASH`) in the Replit Secrets.
4. Install the required dependencies by running the following command in the Replit shell:

    ```bash
    pip install -r requirements.txt
    ```

5. Create a `.env` file in the root directory with your API credentials.
6. Run the project by clicking the "Run" button in Replit.

## How to Use

1. Start the bot by running the project locally, hosting it on a server, or running it on Replit.
2. In the Telegram group where you want to play the game, send the `/play` command.
3. The bot will set the group and start listening for messages from the specified bot (`OctopusEN_Bot`).
4. The bot will process the messages and respond with valid words based on the game rules.
5. To stop the bot from playing in the group, send the `/end` command.

## Cloning or Downloading the Project

To clone the repository, use the following command:

```bash
git clone git@github.com:odin-the-ruler/Octomod.git
```

To download the project as a ZIP file, go to the GitHub repository page and click on the "Code" button, then select "Download ZIP".

## Project Status

**This project is currently under development.** Some features may not be fully implemented or may change in the future. Contributions and feedback are welcome!

## Reminder

Please ensure that you do not break Telegram's Terms of Service while using this project.

