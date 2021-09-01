import discord
import random
from discord.ext import commands
intents = discord.Intents.all()

prefix = '!'
bot = commands.Bot(command_prefix = prefix, intents = intents)

@bot.event
async def on_ready():

    print(bot.get_guild(806480753537581106).members)
    game = discord.Game('기록')
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="장충즈 개소리"))

# @bot.command(aliases = ['사전', '전체사전', '링크'])
# async def dictionary(ctx):
#     embed = discord.Embed(title = '장충즈를 위한 단어사전이에요!', description = '위의 "사전" 을 누르면 전체 사전 링크로 이동해요.', color=6666666)
#     embed.set_author(name="사전", url="https://yoonshin07.github.io/jchz_dictionary/jchz_dic", icon_url="https://media.discordapp.net/attachments/830047064867078184/840588916478443520/fde2093b6caf79a1.png")
#     embed.set_thumbnail(url = "https://media.discordapp.net/attachments/830047064867078184/840588916478443520/fde2093b6caf79a1.png")
#     await ctx.channel.send(embed=embed)

@bot.event
async def on_message(msg):

    await bot.process_commands(msg)

    if "<@!840220950250520596>" in msg.content:
        variable = [
            "도움이 필요하신가요?",
            "말씀해주세요.",
            "네!"]
        await msg.channel.send(random.choice(variable))

# 가희 ***********************************************************************************************
gh = None
@bot.command(aliases = ['기하학'])
async def geometry(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 805967133368516649:
            global gh
            gh = i
    await ctx.send(gh.mention + ", 웃을 때 내는 소리이다.")

# 서희 ***********************************************************************************************
sh = None
@bot.command(aliases = ['따당'])
async def ddadang(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 770576567075078184:
            global sh
            sh = i
    await ctx.send(sh.mention + ", 🔫 이모지와 함께 쓰인다. 의도치 않게 이모티콘의 방향이 자신을 가리켜 자살을 의미하게 되었다.")

# 은교 ***********************************************************************************************
ek = None
@bot.command(aliases = ['뀨'])
async def ggyu(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 805950761972137994:
            global ek
            ek = i
    await ctx.send(ek.mention + ", 본인의 귀여움을 표현하는 말이다.")

# 지민 ***********************************************************************************************
jm = None
sh = None
@bot.command(aliases = ['조용히애이새끼야'])
async def quietbird(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 805951202747219970:
            global jm
            jm = i
        if i.id == 770576567075078184:
            global sh
            sh = i
    await ctx.send(jm.mention + ', ' + sh.mention + '의 이모티콘 도배 때문에 조용히 하라고 말한 것에서 유래되었다.')

# 희윤 ***********************************************************************************************
hy = None
@bot.command(aliases = ['표준어'])
async def standardlng(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 773906164466843700:
            global hy
            hy = i
    await ctx.send(hy.mention + ', ' + hy.mention + '의 욕이 비속어 같지 않고 표준어처럼 들린다는 뜻에서 유래되었다.')

token = 'ODQwMjIwOTUwMjUwNTIwNTk2.YJVCvQ.K0boSoOcDBJ4ANzN1FslTn0O3ag'

bot.run(token)