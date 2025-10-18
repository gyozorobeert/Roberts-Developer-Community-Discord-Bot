import os

import discord
from discord.ext import commands

import logging
import time

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix="", intents=intents)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

@bot.event
async def on_ready():
    if bot.user is not None:
        print(f'{bot.user.name} is online and connected to Discord!')
    else:
        print('Bot user is None. Failed to connect to Discord.')

    try:
        await bot.load_extension("cogs.commands")
        print("Commands cog loaded successfully.")
        await bot.load_extension("cogs.welcome")
        print("Welcome cog loaded successfully.")
        await bot.load_extension("cogs.logs")
        print("Logs cog loaded successfully.")
    except Exception as e:
        print(f'Error loading cogs: {e}')

    start_time = time.time()

    try:
        if GUILD_ID is not None:
            await bot.tree.sync(guild=discord.Object(id=int(GUILD_ID)))
            end_time = time.time()
            sync_duration = end_time - start_time
            print(f"Slash commands synchronized. Time: {sync_duration:.2f} seconds.")
        else:
            print("Error: GUILD_ID environment variable is not set.")
    except Exception as e:
        print(f"Error syncing slash commands: {e}")
    
    activity = discord.Activity(type=discord.ActivityType.watching, name="for commands")
    await bot.change_presence(activity=activity)

if TOKEN is None:
    raise ValueError("DISCORD_BOT_TOKEN environment variable is not set.")
bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)