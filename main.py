import disnake
from disnake.ext import commands
import config

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
    memberCount = disnake.Embed(
        title=inter.guild.name,
        description=inter.guild.member_count,
        color=disnake.Color.orange(),      
    )
    memberCount.set_author(
        name=bot.user,
        url="https://github.com/Animousters/Pingus",
        icon_url="https://github.com/Animousters/Pingus/blob/main/assets/pingus.png"
    )
    memberCount.set_footer(
        text=f'{bot.user} made by 9847#6709'
    )
    await inter.send(embed=memberCount)

@bot.slash_command()
async def user(inter):
    userStats=disnake.Embed(
        title=inter.guild.name,
        description=f'Username:\n{inter.author}\n\nNickname:\n{inter.author.nick}\n\nUser ID:\n{inter.author}\n\nAccount Created At:\n{inter.author.created_at}\n\nJoined Server At:\n{inter.author.joined_at}\n\nRoles:\n{inter.author.roles}',
        color=disnake.Color.orange()
    )
    userStats.set_thumbnail(
        url=inter.author.avatar
    )
    userStats.set_author(
        name=bot.user,
        url="https://github.com/Animousters/Pingus",
        icon_url="https://github.com/Animousters/Pingus/blob/main/assets/pingus.png"
    )
    userStats.set_footer(
        text=f'{bot.user} made by 9847#6709'
    )
    await inter.send(embed=userStats)

# Login to Discord with the bot's token.
bot.run(config.TOKEN)