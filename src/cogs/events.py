import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

@commands.command()
@commands.has_permissions(create_polls=True)
async def event_poll(ctx, question: str, *options: str):  
    # Creating the poll message
    poll_message = f"**{question}**\n\n"

    # Adding the options to the poll message
    for i, option in enumerate(options, start=1):
        poll_message += f"{i}. {option}\n"

    # Sending the poll message
    poll_embed = discord.Embed(title="Event Poll", description=poll_message, color=discord.Color.blue())
    poll_embed.set_footer(text=f"Poll created by {ctx.author.name}")
    poll_message = await ctx.send(embed=poll_embed)

    # Adding reactions to the poll message for voting
    for i in range(1, len(options) + 1):
        await poll_message.add_reaction(f"{i}\N{combining enclosing keycap}")

    bot.event_poll_msg_id = poll_message.id # Used for tracking this poll for reactions

@bot.command()
async def poll_results(ctx):
    # Fetch users who reacted to the last posted message.
    if not hasattr(bot, "event_poll_msg_id"):
        await ctx.send("No tracked message found.")
        return

    try:
        message = await ctx.channel.fetch_message(bot.event_poll_msg_id)
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

async def setup(bot):
    bot.add_command(event_poll)
    bot.add_command(poll_results)