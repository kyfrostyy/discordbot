import discord
import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix='префикс вашего бота')



@client.event
async def on_ready():
    print('Бот живой!!')


keep_alive.keep_alive()
client.run('токен вашего бота')

