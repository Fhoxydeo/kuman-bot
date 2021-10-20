import discord
from discord.ext import commands
import random

from discord.ext.commands import bot

class general(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rules(self, ctx):
        await ctx.send('https://media.discordapp.net/attachments/803233395021709312/880077552515964988/Screen_Shot_2019-03-17_at_12.16.56_PM.png?width=488&height=230')

    @commands.command()
    async def crot(self, ctx):
        await ctx.send('crat crot crat crot, brisik, bodoh, stop coli, stop menghabiskan sperma dalam tubuhmu biar kamu tidak mati lemas karena hipotensi, kunjungi website ini bila anda mengalami gejala hipotensi https://www.alodokter.com/hipotensi')

    @commands.command()
    async def rushia(self, ctx):
        await ctx.send('bacot')
        await ctx.send('https://tenor.com/view/wide-vladimir-putin-russian-walking-gif-17506944')
        await ctx.send(':flag_ru:')

    @commands.command()
    async def say(self, ctx, *,arg):
        amount = 1
        try:
            amount = int(arg)
        except Exception: pass
        await ctx.channel.purge(limit=amount)      
        await ctx.send(arg)

    @commands.command()
    async def gaplok(self, ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
        slapped = ", ".join(x.name for x in members)
        await ctx.send("{} just got gaplok'd for {}".format(slapped, reason))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('berak'):
            await message.channel.send('Berak bos ?')

    @commands.command()
    async def roll(self, ctx):
        await ctx.send(random.randrange(1, 99))