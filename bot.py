#system shit idk
import discord
import random
import os
from discord import embeds
from discord.ext import commands
from cat import cat
from aib import aib
from general import general
from music import music

snipe_message_author = {}
snipe_message_content = {}

#prefix
client = commands.Bot(command_prefix = '.')

client.add_cog(cat(client))
client.add_cog(aib(client))
client.add_cog(general(client))
client.add_cog(music(client))

#on ready
@client.event
async def on_ready():
    print('{0.user} has Berak '.format(client))

#commands
@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@client.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: 
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except: 
        await ctx.send(f"ngapain sih, gak ada yang bisa di snipe! di `#{channel.name}`")
        await ctx.send("gjls snipe2")

@client.command()
async def ping(ctx):
    await ctx.send(f'Berak! {round(client.latency * 1000)}ms, ngelek mas')

#Token
client.run(os.environ['DISCORD_TOKEN'])