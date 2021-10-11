#system shit idk
import discord
import random
import os
from discord import embeds
from discord.ext import commands

snipe_message_author = {}
snipe_message_content = {}

#prefix
client = commands.Bot(command_prefix = '.')

#on ready
@client.event
async def on_ready():
    print('{0.user} has Berak '.format(client))

#commands
@client.command()
async def ping(ctx):
    await ctx.send(f'Berak! {round(client.latency * 1000)}ms, ngelek mas')

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
                'https://media.discordapp.net/attachments/880497088989896704/881818095390437386/unknown-4.png',
                'https://media.discordapp.net/attachments/880497088989896704/882583714197012520/unknown.png',
                'https://media.discordapp.net/attachments/803233395021709312/883577978813030431/IMG_20210902_203200.jpg',
                'https://media.discordapp.net/attachments/803233395021709312/868510856613355580/Screenshot_2021-07-24-19-04-04-40_572064f74bd5f9fa804b05334aa4f912.jpg', 
                'https://media.discordapp.net/attachments/880497088989896704/895593649772036126/unknown-2.png', ]
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def rules(ctx):
    await ctx.send('https://media.discordapp.net/attachments/803233395021709312/880077552515964988/Screen_Shot_2019-03-17_at_12.16.56_PM.png?width=488&height=230')

@client.command()
async def berak(ctx):
    await ctx.send('Berak Bos?')

@client.command()
async def crot(ctx):
    await ctx.send('crat crot crat crot, brisik, bodoh, stop coli, stop menghabiskan sperma dalam tubuhmu biar kamu tidak mati lemas karena hipotensi, kunjungi website ini bila anda mengalami gejala hipotensi https://www.alodokter.com/hipotensi')

@client.command()
async def rushia(ctx):
    await ctx.send('bacot')
    await ctx.send('https://tenor.com/view/wide-vladimir-putin-russian-walking-gif-17506944')
    await ctx.send(':flag_ru:')

@client.command()
async def say(ctx, *,arg):
    await ctx.send(arg)

@client.command()
async def gaplok(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send("{} just got gaplok'd for {}".format(slapped, reason))

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
async def roll(ctx):
    await ctx.send(random.randrange(1, 99))

initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for x in initial_extensions:
        client.load_extension(x)

#Token
client.run(os.environ['DISCORD_TOKEN'])
