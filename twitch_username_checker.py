import discord
import requests
import os
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_APP_TOKEN = os.getenv("TWITCH_APP_ACCESS_TOKEN")

# Initialize the Discord bot
intents = discord.Intents.default()
intents.message_content = True  # Add permission to access message content
bot = commands.Bot(command_prefix="!", intents=intents)

# Twitch username check function
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

# Register commands when the bot is ready
@bot.event
async def on_ready():
    """Registers commands when the bot is ready."""
    print(f'Bot logged in as {bot.user}.')
    # Add a wait to sync slash commands
    await bot.tree.sync()
    print("Slash commands have been successfully registered!")

# Slash commands
@bot.tree.command(name="tw", description="Check Twitch username availability")
async def twcheck(interaction: discord.Interaction, username: str):
    """Slash command to check Twitch username availability"""
    await interaction.response.send_message(f"🔍 **Twitch check:** `{username}`...")
    
    result = check_twitch_name(username)
    
    if result is None:
        await interaction.followup.send("❌ **Error:** Could not connect to Twitch API. Please try again later!")
    elif result:
        await interaction.followup.send(f"✅ **Available!** You can grab `{username}` right now!")
    else:
        await interaction.followup.send(f"❌ **Taken:** `{username}` is already in use.")

# Prefix commands (optional)
@bot.command(name="tw")
async def twcheck_prefix(ctx, *, username: str):
    """Prefix command to check Twitch username availability"""
    await ctx.send(f"🔍 **Twitch check:** `{username}`...")

    result = check_twitch_name(username)

    if result is None:
        await ctx.send("❌ **Error:** Could not connect to Twitch API. Please try again later!")
    elif result:
        await ctx.send(f"✅ **Available!** You can grab `{username}` right now!")
    else:
        await ctx.send(f"❌ **Taken:** `{username}` is already in use.")

bot.run(TOKEN)
