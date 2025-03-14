import discord
from discord.ext import commands

@commands.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason: str = "just cuz"):
    try:
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned. {reason} is probably why, oh well, didnt like him anyways')
    except discord.Forbidden:
        await ctx.send(f"That's embarassing! <@{ctx.author.id}> is an idiot who tried to ban a guy even though he doesn't have perms. " 
        + f"<@585621628348792872> will now ban you")
    except Exception as e:
        await ctx.send(f"Uh oh: {e}")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"That's embarassing! <@{ctx.author.id}> is an idiot who tried to ban a guy even though he doesn't have perms. " 
        + f"<@585621628348792872> will now ban you")
    else:
        await ctx.send(f"An error occurred: {error}")

async def setup(bot):
    bot.add_command(ban)