import discord
from discord.ext import commands
from discord.utils import get
import os
from dotenv import load_dotenv
import textwrap

load_dotenv()

def get_env_int(var_name):
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"Environment variable '{var_name}' is not set.")
    return int(value)

WELCOME_CHANNEL_ID = get_env_int("WELCOME_CHANNEL_ID")
RULES_CHANNEL_ID = get_env_int("RULES_CHANNEL_ID")
HAPPY_ID = get_env_int("HAPPY_ID")
ADMIN_ID = get_env_int("ADMIN_ID")
ROBI_ID = get_env_int("ROBI_ID")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix="", intents=intents)

class Welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome_channel = self.bot.get_channel(WELCOME_CHANNEL_ID)

        message = textwrap.dedent(f"""
        **Üdvözlünk a Happy Squad Guild discord szerverén, {member.mention}!**
        - Ha bármilyen kérdésed van, nyugodtan fordulj <@{HAPPY_ID}>-hez vagy az <@&{ADMIN_ID}>ok-hoz.
        - Amennyiben még nem tetted meg, kérjük, olvasd el a szabályokat a <#{RULES_CHANNEL_ID}> csatornában.
        - Discord szerverrel kapcsolatos probléma esetén keresd <@{ROBI_ID}>-t.
        """)

        if isinstance(welcome_channel, discord.TextChannel):
            await welcome_channel.send(message)
            print(f"Welcome message sent to {member}.")
        elif welcome_channel is not None:
            print(f"Channel with ID {WELCOME_CHANNEL_ID} is not a TextChannel (type: {type(welcome_channel).__name__}).")
        else:
            print(f"Welcome channel with ID {WELCOME_CHANNEL_ID} not found.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Welcome(bot))