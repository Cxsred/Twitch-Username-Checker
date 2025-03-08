Twitch Username Availability Checker 🎮🔍

Welcome to the Twitch Username Availability Checker! 🎉 This bot helps you check if a Twitch username is available or already taken. Using the Twitch API, you can easily verify if your desired username is free to register. 💻
✨ Features

    Check if a Twitch username is available or not. ✅❌
    Supports both Slash Commands and Prefix Commands on Discord. 🤖
    Built with Python and the discord.py library. 📚

📦 Installation

    Clone the repository to your local machine:

git clone https://github.com/yourusername/twitch-username-checker.git

Navigate to the project folder:

cd twitch-username-checker

Create and activate a virtual environment (optional but recommended):

    For Windows:

python -m venv venv
venv\Scripts\activate

For Mac/Linux:

    python3 -m venv venv
    source venv/bin/activate

Install the required dependencies:

    pip install -r requirements.txt

🔑 .env File

The .env file should contain your Discord Bot Token and Twitch API credentials. To set this up:

    Create a file named .env in the project root.
    Add the following keys to your .env file (replace the placeholders with your actual values):

    DISCORD_BOT_TOKEN=your_discord_bot_token_here
    TWITCH_CLIENT_ID=your_twitch_client_id_here
    TWITCH_APP_ACCESS_TOKEN=your_twitch_app_access_token_here

⚙️ Running the Bot

To run the bot, use the following command:

python bot.py

🚀 Usage

    Use the Slash Command /tw <username> to check if a Twitch username is available.
    You can also use the Prefix Command !tw <username> to check availability.

📋 Requirements

    Python 3.x
    discord.py library
    requests library

These dependencies can be installed by running:

pip install -r requirements.txt

📜 License

This project is licensed under the MIT License. See the LICENSE file for more information.
