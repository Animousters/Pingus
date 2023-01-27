import disnake
from disnake.ext import commands

# Creating a commands.Bot() instance, and assigning it to "bot"
bot = commands.Bot()

# When the bot is ready, run this code.
@bot.event
async def on_ready():
    print(f'We have logged on as {bot.user}!')

@bot.slash_command()
async def ping(inter):
    await inter.response.send_message("Pong!")

@bot.slash_command()
async def membercount(inter):
    await inter.response.send_message(f'Server: {inter.guild.name}\nTotal Members: {inter.guild.member_count}')

@bot.slash_command()
async def user(inter):
    await inter.response.send_message(f"Your tag: {inter.author}\nYour ID: {inter.author.id}")

# Login to Discord with the bot's token.
bot.run("MTAyNzAxODkyNDgzNzA0ODMzMA.GghdJZ.hVGfquJTFe_ydDOR5OI-kqtvhcO4fakAaSkyus")