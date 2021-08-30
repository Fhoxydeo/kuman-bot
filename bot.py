#system shit idk
import discord
import random
from discord.ext import commands

#prefix
client = commands.Bot(command_prefix = '.')

#on ready
@client.event
async def on_ready():
    print('Berak Bos')

#commands
@client.command()
async def ping(ctx):
    await ctx.send(f'Berak! {round(client.latency * 1000)}ms, ngelek mas')

@client.command()
async def rules(ctx):
    await ctx.send('https://media.discordapp.net/attachments/803233395021709312/880077552515964988/Screen_Shot_2019-03-17_at_12.16.56_PM.png?width=488&height=230')

@client.command()
async def berak(ctx):
    await ctx.send('Berak Bos?')

#kumpulan aib
@client.command()
async def aib(ctx):
    responses = ['https://media.discordapp.net/attachments/797028363487281154/844537868868911114/817758764911820822.png?width=115&height=63',
                'https://media.discordapp.net/attachments/880497088989896704/881810226980991016/lightshot_1619587607.png?width=727&height=168',
                'https://media.discordapp.net/attachments/880497088989896704/881810235638022184/Screenshot_2021-01-03-17-15-05-56_572064f74bd5f9fa804b05334aa4f912.jpg?width=850&height=260', 
                'https://media.discordapp.net/attachments/880497088989896704/881813502082293790/Screenshot_2021-01-25-18-15-18-78.png?width=648&height=103',
                'https://media.discordapp.net/attachments/880497088989896704/881813837102333973/Screenshot_2021-02-17-08-33-46-20_572064f74bd5f9fa804b05334aa4f912.jpg?width=553&height=139',
                'https://media.discordapp.net/attachments/880497088989896704/881815052947173396/Screenshot_2021-02-21-10-36-19-21_572064f74bd5f9fa804b05334aa4f912.jpg?width=972&height=399',
                'https://media.discordapp.net/attachments/880497088989896704/881815263505428510/unknown-3.png?width=322&height=111',
                'https://media.discordapp.net/attachments/880497088989896704/881816432181137448/unknown.png?width=223&height=53',
                'https://media.discordapp.net/attachments/880497088989896704/881816673559126036/unknown-5.png?width=213&height=50',
                'https://media.discordapp.net/attachments/880497088989896704/881816805298032710/Screenshot_2021-03-28-20-12-24-32.png?width=616&height=277',
                'https://media.discordapp.net/attachments/880497088989896704/881817391347163146/Screenshot_2021-03-26-22-24-29-76.png?width=474&height=119',
                'https://media.discordapp.net/attachments/880497088989896704/881817504819867658/Screenshot_2021-03-10-22-48-45-58_572064f74bd5f9fa804b05334aa4f912.jpg?width=506&height=473',
                'https://media.discordapp.net/attachments/880497088989896704/881817950066188288/Screenshot_2021-02-27-22-34-24-26.png?width=368&height=139',
                'https://media.discordapp.net/attachments/880497088989896704/881818095390437386/unknown-4.png?width=240&height=29', ]
    await ctx.send(f'{random.choice(responses)}')




#Token
client.run('TOKEN')

