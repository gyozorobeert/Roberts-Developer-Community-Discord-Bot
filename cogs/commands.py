import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

GUILD_ID = os.getenv("GUILD_ID")
RULES_CHANNEL_ID = os.getenv("RULES_CHANNEL_ID")
HAPPY_ID = os.getenv("HAPPY_ID")

class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="rules", description="Szerver és Guild szabályzat")
    async def rules(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"A szerver és guild szabályzatát itt éred el: <#{RULES_CHANNEL_ID}>.", ephemeral=True)

    @app_commands.command(name="help", description="Segítségre van szükséged?")
    async def help(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Ha segítségre van szükséged, fordulj <@{HAPPY_ID}>-hez.", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Commands(bot))