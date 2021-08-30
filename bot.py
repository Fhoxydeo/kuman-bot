import discord
from discord.ext import commands

#prefix
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Berak Bos')

@client.command()
async def ping(ctx):
    await ctx.send(f'Berak! {round(client.latency * 1000)}ms')

@client.command()
async def rules(ctx):
    await ctx.send('https://media.discordapp.net/attachments/803233395021709312/880077552515964988/Screen_Shot_2019-03-17_at_12.16.56_PM.png?width=488&height=230')


client.run('ODc0MTgxMzkwOTYxMzUyNzI1.YRDO3Q.5-tDgnuFGOhiyeX6-wtKzo2e1KE')

