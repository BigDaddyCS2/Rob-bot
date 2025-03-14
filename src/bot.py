import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import eventutils

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    # Import all extensions
    await bot.load_extension(f'cogs.admin')
    print(f'Logged in as {bot.user}')

@bot.command()
async def Whassup(ctx):
    await ctx.send("Straight sackin. Wbu?")

@bot.command()
async def users(ctx):
    online = users(ctx.guild)
    if online:
        await ctx.send("Online users:\n" + "\n".join(online))
    else:
        await ctx.send("No users are online.")

def users(guild: discord.Guild):
    return [member.name for member in guild.members if member.status == discord.Status.online]

@bot.command()
async def post_message(ctx):
    """Bot posts a message and tracks reactions."""
    message = await ctx.send("React to this message!")

    # Store the message ID so we can fetch reactions later
    bot.last_message_id = message.id
    
@bot.command()
async def reactions(ctx):
    """Fetch users who reacted to the last posted message."""
    if not hasattr(bot, "last_message_id"):
        await ctx.send("No tracked message found.")
        return

    try:
        message = await ctx.channel.fetch_message(bot.last_message_id)
        users_who_reacted = []

        for reaction in message.reactions:
            async for user in reaction.users():
                if user != bot.user and user.name not in users_who_reacted:
                    users_who_reacted.append(user.name)

        if users_who_reacted:
            await ctx.send("Users who reacted:\n" + "\n".join(users_who_reacted))
        else:
            await ctx.send("No reactions yet.")
    except discord.NotFound:
        await ctx.send("Message not found.")


bot.run(TOKEN)
