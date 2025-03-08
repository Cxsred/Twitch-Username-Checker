# Discord Twitch Username Availability Checker

This is a Discord bot that allows users to check if a Twitch username is available.

## Features
- **Twitch username check**: Checks whether a given Twitch username is available or already taken.
- **Slash command support**: Use `/tw <username>` to check if the username is available.
- **Prefix command support**: You can also use `!tw <username>` as a prefix command.

## Setup

### Prerequisites
Before running the bot, you'll need to set up the following:

1. **Discord Bot Token**:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications) and create a new bot to get your token.

2. **Twitch Client ID** and **Twitch Access Token**:
   - Register your application on [Twitch Developer Portal](https://dev.twitch.tv/docs/authentication/register-your-application) to get the Client ID and Access Token.

3. **.env File**:
   - Create a `.env` file and add the following keys:

```env
DISCORD_BOT_TOKEN=<your_discord_bot_token>
TWITCH_CLIENT_ID=<your_twitch_client_id>
TWITCH_APP_ACCESS_TOKEN=<your_twitch_access_token>
