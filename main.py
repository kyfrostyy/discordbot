import discord
from discord.ext import commands

client = commands.Bot(command_prefix='префикс вашего бота')



@client.event
async def on_ready():
    print('Бот живой!!')



client.run('токен вашего бота')

