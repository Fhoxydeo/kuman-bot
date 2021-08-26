#kuman
import discord
from discord.ext import commands

#prefix
client = commands.Bot(command_prefix = ' ! ')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def ping():
    await client.say('Pong!')

client.run('ODc0MTgxMzkwOTYxMzUyNzI1.YRDO3Q.5-tDgnuFGOhiyeX6-wtKzo2e1KE')

