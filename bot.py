import discord
import requests
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_APP_TOKEN = os.getenv("TWITCH_APP_ACCESS_TOKEN")

# Start the Discord bot
intents = discord.Intents.default()
intents.message_content = True  # Grant access to message content
bot = commands.Bot(command_prefix="!", intents=intents)

# Function to check Twitch username availability
def check_twitch_name(username):
    """Checks if the Twitch username is available."""
    url = "https://api.twitch.tv/helix/users"
    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {TWITCH_APP_TOKEN}"
    }
    params = {"login": username.lower().strip()}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return len(response.json()["data"]) == 0
        else:
            print(f"Twitch API Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Prefix commands
@bot.command(name="tw")
async def twcheck_prefix(ctx, *, username: str):
    """Checks Twitch username availability with prefix command"""
    await ctx.send(f"🔍 **Twitch check:** `{username}`...")

    result = check_twitch_name(username)

    if result is None:
        await ctx.send("❌ **Error:** Unable to connect to Twitch API. Please try again later!")
    elif result:
        await ctx.send(f"✅ **Available!** You can grab the username `{username}` right now!")
    else:
        await ctx.send(f"❌ **Taken:** The username `{username}` is already in use.")

bot.run(TOKEN)
