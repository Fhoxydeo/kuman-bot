#system shit idk
import discord
import random
import os
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

@client.command()
async def crot(ctx):
    await ctx.send('crat crot crat crot, brisik, bodoh, stop coli, stop menghabiskan sperma dalam tubuhmu biar kamu tidak mati lemas karena hipotensi, kunjungi website ini bila anda mengalami gejala hipotensi https://www.alodokter.com/hipotensi')

@client.command()
async def rushia(ctx):
    await ctx.send('bacot')
    await ctx.send('https://tenor.com/view/wide-vladimir-putin-russian-walking-gif-17506944')
    await ctx.send(':flag_ru:')

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
                'https://media.discordapp.net/attachments/880497088989896704/881818095390437386/unknown-4.png?width=240&height=29',
                'https://media.discordapp.net/attachments/880497088989896704/882583714197012520/unknown.png?width=1024&height=226',
                'https://media.discordapp.net/attachments/803233395021709312/883577978813030431/IMG_20210902_203200.jpg?width=648&height=151', ]
    await ctx.send(f'{random.choice(responses)}')


#Bob si kucing    
@client.command()
async def bob(ctx):
    responses = ['https://media.discordapp.net/attachments/881901579991658516/881901786531786752/image1-2.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881901786875703346/image1-1.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881901787223818270/image0-4.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881901787546800178/image0-3.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881901787920097280/image0-1.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881901788326952970/image0.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903241024114729/hskskbb.jpg?width=630&height=472',
                'https://media.discordapp.net/attachments/881901579991658516/881903241485504592/IMG_20210223_161604.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903241833635890/image1-1.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903242349522965/image1.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903242672492555/image0.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903243075153992/IMG_20210223_161536.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903243347767317/IMG_20210223_161627.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903243725262918/IMG_20210223_161545.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903244119531631/image0-1.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903244467638272/iakaknsdb.jpg?width=630&height=472',
                'https://media.discordapp.net/attachments/881901579991658516/881903466337951795/IMG_20210223_161652.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903466660888596/IMG_20210223_161638.jpg?width=417&height=472',
                'https://media.discordapp.net/attachments/881901579991658516/881903466887385140/IMG_20210223_161644.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903467239727154/IMG_20210223_162206.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903467592024074/IMG_20210223_162222.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903467852087417/IMG_20210223_163040.jpg?width=354&height=472',
                'https://media.discordapp.net/attachments/881901579991658516/881903468128923698/IMG_20210223_161830.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903468384755722/IMG_20210223_161955.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903468657401976/IMG_20210223_161855.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903468988727337/IMG_20210223_163035.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903873084768296/IMG_20210223_163417.jpg?width=354&height=472',
                'https://media.discordapp.net/attachments/881901579991658516/881903873382572062/IMG_20210223_163429.jpg?width=354&height=472',
                'https://media.discordapp.net/attachments/881901579991658516/881903873751666688/IMG_20210223_163107.jpg?width=354&height=472',
                'https://media.discordapp.net/attachments/881901579991658516/881903874015920168/IMG_20210223_163151.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881903874334670868/IMG_20210223_163423.jpg?width=533&height=472',
                'https://media.discordapp.net/attachments/881901579991658516/881903874573754410/IMG_20210223_163058.jpg?width=630&height=472',
                'https://media.discordapp.net/attachments/881901579991658516/881903875064492032/IMG_20210223_163618.jpg?width=354&height=472',
                'https://media.discordapp.net/attachments/881901579991658516/881903875278405682/IMG_20210223_163134.jpg?width=354&height=472',
                'https://media.discordapp.net/attachments/881901579991658516/881903875496476742/IMG_20210223_163339.jpg?width=354&height=472',
                'https://media.discordapp.net/attachments/881901579991658516/881903875899138058/IMG_20210223_163131.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/881904117965004810/unknown.png?width=272&height=300',
                'https://media.discordapp.net/attachments/556916767423987732/871917122232655892/image0.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/556916767423987732/871910827119243294/image0.jpg?width=630&height=472',
                'https://media.discordapp.net/attachments/881901579991658516/883525228624490496/image0-6.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525228976828477/image0-7.jpg?width=355&height=473', 
                'https://media.discordapp.net/attachments/881901579991658516/883525229299785768/image2.jpg?width=630&height=472', 
                'https://media.discordapp.net/attachments/881901579991658516/883525229719207937/image0-8.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525230444826634/image0-9.jpg?width=355&height=473', 
                'https://media.discordapp.net/attachments/881901579991658516/883525230843265034/image0-10.jpg?width=355&height=473', 
                'https://media.discordapp.net/attachments/881901579991658516/883525231229149194/image6.jpg?width=355&height=473', 
                'https://media.discordapp.net/attachments/881901579991658516/883525231682146345/image0-16.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525232055422986/image0-17.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525232495853598/image1-3.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525360652804147/image0-13.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525360950575134/image0-12.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525361256763442/image0-14.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525361739124736/image0-15.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525362074673172/image0-19.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525362406006824/image1-4.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525362900930610/image0-21.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525363223920690/image1-5.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525363551055894/image4.jpg?width=330&height=472',
                'https://media.discordapp.net/attachments/881901579991658516/883525363861446666/image1-6.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525430324363324/image0-18.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525430878023731/image0-20.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525431389724672/image1-7.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525432283115560/image0-25.jpg?width=630&height=472',
                'https://media.discordapp.net/attachments/881901579991658516/883525432614481941/image0-27.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525433168126022/image0-23.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525433499484210/image0-24.jpg?width=355&height=473',
                'https://media.discordapp.net/attachments/881901579991658516/883525433923104839/image0-29.jpg?width=355&height=473',]
    await ctx.send(f'{random.choice(responses)}')    

#myako nya nya
@client.command()
async def myako(ctx):
    responses = ['https://media.discordapp.net/attachments/699567935861162037/882475088321073172/IMG_20210829_192439.jpg',
                'https://media.discordapp.net/attachments/699567935861162037/882475089684221952/IMG_20210615_102627.jpg',
                'https://media.discordapp.net/attachments/699567935861162037/882475088799211571/IMG_20210815_222629.jpg', 
                'https://media.discordapp.net/attachments/699567935861162037/882475090057511043/IMG_20210618_230009.jpg',
                'https://media.discordapp.net/attachments/699567935861162037/882475090535657552/IMG_20210513_093157.jpg',
                'https://media.discordapp.net/attachments/699567935861162037/882475091001237554/IMG_20210330_104528.jpg', ]
    await ctx.send(f'{random.choice(responses)}')

#random angka judi mamak kau green
@client.command()
async def roll(ctx):
    await ctx.send(f'(random.sample(range(10, 30))')


#Token
client.run(os.environ['DISCORD_TOKEN'])

