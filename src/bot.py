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
    await bot.load_extension(f'cogs.events')
    print(f'Logged in as {bot.user}')

@bot.command()
async def Whassup(ctx):
    await ctx.send("Straight sackin. Wbu?")

@bot.command()
async def fuckyou(ctx): 
    await ctx.send("git gud")

@bot.command()
async def youtube(ctx):
    await ctx.send("https://www.youtube.com/@BigDaddyCS2")

bot.run(TOKEN)
