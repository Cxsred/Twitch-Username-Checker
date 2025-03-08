Twitch Username Checker Bot

This is a Discord bot that checks if a Twitch username is available using the Twitch API. You can use the bot with a prefix command (!tw <username>) to check whether a username is available or already taken.
Features

    Check if a Twitch username is available
    Responds with whether the username is available or taken

Setup
1. Clone the Repository

git clone https://github.com/Cxsred/Twitch-Username-Checker/tree/main

2. Install Dependencies

Make sure you have Python installed. Then, install the required dependencies by running:

pip install -r requirements.txt

3. Create a .env File

Create a .env file in the root directory and add your secret keys:

DISCORD_BOT_TOKEN=your_discord_bot_token
TWITCH_CLIENT_ID=your_twitch_client_id
TWITCH_APP_ACCESS_TOKEN=your_twitch_app_access_token

Replace your_discord_bot_token, your_twitch_client_id, and your_twitch_app_access_token with your own secret keys.
4. Run the Bot

After setting up the .env file and installing dependencies, run the bot with:

python bot.py

The bot will be active and you can start checking Twitch usernames using the prefix command!
Commands

    !tw <username> – Checks if the given Twitch username is available.

License

This project is licensed under the MIT License.
