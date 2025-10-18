import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

JOIN_LEAVE_LOG_CHANNEL_ID = int(os.getenv("JOIN_LEAVE_LOG_CHANNEL_ID"))
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID"))

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="", intents=intents)

class Logs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        log_channel = self.bot.get_channel(JOIN_LEAVE_LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(0, 255, 0)
        
        log_embed = discord.Embed(
            description=f"{member.mention} {member}",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.add_field(name="Account Age", value=f"<t:{int(member.created_at.timestamp())}:R>", inline=False)

        log_embed.set_author(name="Egy új tag csatlakozott a szerverhez", icon_url=member.display_avatar.url)
        log_embed.set_thumbnail(url=member.display_avatar.url)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Join log sent for {member}.")
        else:
            print(f"Log channel with ID {JOIN_LEAVE_LOG_CHANNEL_ID} not found.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        log_channel = self.bot.get_channel(JOIN_LEAVE_LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(255, 0, 0)
        
        log_embed = discord.Embed(
            description=f"{member.mention} {member}",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.add_field(name="Account Age", value=f"<t:{int(member.created_at.timestamp())}:R>", inline=False)

        log_embed.set_author(name="Egy tag elhagyta a szervert", icon_url=member.display_avatar.url)
        log_embed.set_thumbnail(url=member.display_avatar.url)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Leave log sent for {member}.")
        else:
            print(f"Log channel with ID {JOIN_LEAVE_LOG_CHANNEL_ID} not found.")

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(255, 0, 0)
        
        log_embed = discord.Embed(
            description=f"{user.mention} {user}",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.set_author(name="Egy tag kitiltásra került a szerverről", icon_url=user.display_avatar.url)
        log_embed.set_thumbnail(url=user.display_avatar.url)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Ban log sent for {user}.")
        else:
            print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(0, 255, 0)
        
        log_embed = discord.Embed(
            description=f"{user.mention} {user}",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.set_author(name="Egy tag kitiltása feloldásra került a szerverről", icon_url=user.display_avatar.url)
        log_embed.set_thumbnail(url=user.display_avatar.url)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Unban log sent for {user}.")
        else:
            print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return  # Ignore messages from bots

        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(255, 165, 0)
        
        log_embed = discord.Embed(
            description=f"**Törölt üzenet tartalma:**\n{message.content}",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.set_author(name=f"Egy üzenet törlésre került {message.author}", icon_url=message.author.display_avatar.url)
        log_embed.set_thumbnail(url=message.author.display_avatar.url)
        log_embed.add_field(name="Csatorna", value=message.channel.mention, inline=True)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Message delete log sent for message by {message.author}.")
        else:
            print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot:
            return  # Ignore messages from bots

        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(255, 165, 0)
        
        log_embed = discord.Embed(
            description=f"**Eredeti üzenet:**\n{before.content}\n\n**Szerkesztett üzenet:**\n{after.content}",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.set_author(name=f"Egy üzenet szerkesztésre került {before.author}", icon_url=before.author.display_avatar.url)
        log_embed.set_thumbnail(url=before.author.display_avatar.url)
        log_embed.add_field(name="Csatorna", value=before.channel.mention, inline=True)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Message edit log sent for message by {before.author}.")
        else:
            print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")
    
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(0, 255, 0)
        
        log_embed = discord.Embed(
            description=f"{channel.mention} {channel}",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.set_author(name="Egy új csatorna létrehozásra került", icon_url=self.bot.user.display_avatar.url)
        log_embed.set_thumbnail(url=self.bot.user.display_avatar.url)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Channel create log sent for {channel}.")
        else:
            print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")
    
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(255, 0, 0)
        
        log_embed = discord.Embed(
            description=f"{channel.name} (ID: {channel.id})",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.set_author(name="Egy csatorna törlésre került", icon_url=self.bot.user.display_avatar.url)
        log_embed.set_thumbnail(url=self.bot.user.display_avatar.url)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Channel delete log sent for {channel}.")
        else:
            print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")
    
    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(255, 165, 0)
        
        log_embed = discord.Embed(
            description=f"**Eredeti csatorna neve:** {before.name}\n**Új csatorna neve:** {after.name}",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.set_author(name="Egy csatorna frissítésre került", icon_url=self.bot.user.display_avatar.url)
        log_embed.set_thumbnail(url=self.bot.user.display_avatar.url)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Channel update log sent for {before}.")
        else:
            print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")
    
    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(0, 255, 0)
        
        log_embed = discord.Embed(
            description=f"{role.name} {role}",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.set_author(name="Egy új szerep létrehozásra került", icon_url=self.bot.user.display_avatar.url)
        log_embed.set_thumbnail(url=self.bot.user.display_avatar.url)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Role create log sent for {role}.")
        else:
            print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")
    
    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(255, 0, 0)
        
        log_embed = discord.Embed(
            description=f"{role.name} (ID: {role.id})",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.set_author(name="Egy szerep törlésre került", icon_url=self.bot.user.display_avatar.url)
        log_embed.set_thumbnail(url=self.bot.user.display_avatar.url)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Role delete log sent for {role}.")
        else:
            print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(255, 165, 0)
        
        log_embed = discord.Embed(
            description=f"**Eredeti szerep neve:** {before.name}\n**Új szerep neve:** {after.name}",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.set_author(name="Egy szerep frissítésre került", icon_url=self.bot.user.display_avatar.url)
        log_embed.set_thumbnail(url=self.bot.user.display_avatar.url)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Role update log sent for {before}.")
        else:
            print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")
    
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(255, 165, 0)
        
        log_embed = discord.Embed(
            description=f"**Eredeti szerver neve:** {before.name}\n**Új szerver neve:** {after.name}",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.set_author(name="A szerver frissítésre került", icon_url=self.bot.user.display_avatar.url)
        log_embed.set_thumbnail(url=self.bot.user.display_avatar.url)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Guild update log sent for {before}.")
        else:
            print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.nick != after.nick:
            log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
            embed_color = discord.Color.from_rgb(255, 165, 0)
            
            log_embed = discord.Embed(
                description=f"**Eredeti becenév:** {before.nick}\n**Új becenév:** {after.nick}",
                color=embed_color,
                timestamp= datetime.datetime.now(datetime.UTC),
            )

            log_embed.set_author(name=f"{before} beceneve frissítésre került", icon_url=before.display_avatar.url)
            log_embed.set_thumbnail(url=before.display_avatar.url)

            if log_channel:
                await log_channel.send(embed=log_embed)
                print(f"Nickname update log sent for {before}.")
            else:
                print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")

    @commands.Cog.listener()
    async def on_user_join_voice(self, user, before, after):
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(0, 255, 0)
        
        log_embed = discord.Embed(
            description=f"{user.mention} {user} csatlakozott a(z) {after.channel.mention} hangcsatornához.",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.set_author(name="Egy felhasználó csatlakozott egy hangcsatornához", icon_url=user.display_avatar.url)
        log_embed.set_thumbnail(url=user.display_avatar.url)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Voice channel join log sent for {user}.")
        else:
            print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")

    @commands.Cog.listener()
    async def on_user_leave_voice(self, user, before, after):
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(255, 0, 0)
        
        log_embed = discord.Embed(
            description=f"{user.mention} {user} elhagyta a(z) {before.channel.mention} hangcsatornát.",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.set_author(name="Egy felhasználó elhagyott egy hangcsatornát", icon_url=user.display_avatar.url)
        log_embed.set_thumbnail(url=user.display_avatar.url)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Voice channel leave log sent for {user}.")
        else:
            print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")

    @commands.Cog.listener()
    async def on_user_move_voice(self, user, before, after):
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        embed_color = discord.Color.from_rgb(255, 165, 0)
        
        log_embed = discord.Embed(
            description=f"{user.mention} {user} áthelyezte magát a(z) {before.channel.mention} hangcsatornáról a(z) {after.channel.mention} hangcsatornára.",
            color=embed_color,
            timestamp= datetime.datetime.now(datetime.UTC),
        )

        log_embed.set_author(name="Egy felhasználó áthelyezte magát egy másik hangcsatornára", icon_url=user.display_avatar.url)
        log_embed.set_thumbnail(url=user.display_avatar.url)

        if log_channel:
            await log_channel.send(embed=log_embed)
            print(f"Voice channel move log sent for {user}.")
        else:
            print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            await self.on_user_join_voice(member, before, after)
        elif before.channel is not None and after.channel is None:
            await self.on_user_leave_voice(member, before, after)
        elif before.channel is not None and after.channel is not None and before.channel != after.channel:
            await self.on_user_move_voice(member, before, after)
    
    @commands.Cog.listener()
    async def on_member_role_update(self, before, after):
        if before.roles != after.roles:
            log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
            embed_color = discord.Color.from_rgb(255, 165, 0)
            
            added_roles = [role for role in after.roles if role not in before.roles]
            removed_roles = [role for role in before.roles if role not in after.roles]

            description_parts = []
            if added_roles:
                description_parts.append(f"**Hozzáadott szerepek:** {', '.join(role.name for role in added_roles)}")
            if removed_roles:
                description_parts.append(f"**Eltávolított szerepek:** {', '.join(role.name for role in removed_roles)}")
            description = "\n".join(description_parts)

            log_embed = discord.Embed(
                description=description,
                color=embed_color,
                timestamp= datetime.datetime.now(datetime.UTC),
            )

            log_embed.set_author(name=f"{before} szerepei frissítésre kerültek", icon_url=before.display_avatar.url)
            log_embed.set_thumbnail(url=before.display_avatar.url)

            if log_channel:
                await log_channel.send(embed=log_embed)
                print(f"Role update log sent for {before}.")
            else:
                print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")
    
    @commands.Cog.listener()
    async def on_member_timeout(self, member, before, after):
        if before.timed_out_until != after.timed_out_until:
            log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
            embed_color = discord.Color.from_rgb(255, 165, 0)
            
            if after.timed_out_until is not None:
                description = f"{member.mention} {member} időtúllépésre került {after.timed_out_until} időpontig."
                action = "Időtúllépés beállítva"
            else:
                description = f"{member.mention} {member} időtúllépése feloldásra került."
                action = "Időtúllépés feloldva"

            log_embed = discord.Embed(
                description=description,
                color=embed_color,
                timestamp= datetime.datetime.now(datetime.UTC),
            )

            log_embed.set_author(name=action, icon_url=member.display_avatar.url)
            log_embed.set_thumbnail(url=member.display_avatar.url)

            if log_channel:
                await log_channel.send(embed=log_embed)
                print(f"Timeout log sent for {member}.")
            else:
                print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Logs(bot))