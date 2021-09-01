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

@bot.command(aliases = ['사전', '전체사전', '링크'])
async def dictionary(ctx):
    embed = discord.Embed(title = '장충즈를 위한 단어사전이에요!', description = '위의 "사전" 을 누르면 전체 사전 링크로 이동해요.', color=6666666)
    embed.set_author(name="사전", url="https://yoonshin07.github.io/jchz_dictionary/jchz_dic", icon_url="https://media.discordapp.net/attachments/830047064867078184/840588916478443520/fde2093b6caf79a1.png")
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/830047064867078184/840588916478443520/fde2093b6caf79a1.png")
    await ctx.channel.send(embed=embed)

@bot.event
async def on_message(msg):

    await bot.process_commands(msg)

    if bot.user.mentioned_in (msg):
        variable = [
        "도움이 필요하신가요?",
        "말씀해주세요.",
        "네!"]
        await msg.channel.send("{}".format(random.choice(variable)))

# 가희 ***********************************************************************************************
gh = None
@bot.command(aliases = ['기하학'])
async def geometry(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 805967133368516649:
            global gh
            gh = i
    await ctx.send(gh.mention + ", 웃을 때 내는 소리이다.")

gh = None
@bot.command(aliases = ['hit_the_hen'])
async def hitthehen(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 805967133368516649:
            global gh
            gh = i
    await ctx.send(gh.mention + ', "닥쳐" 를 직역한 것이다.')

gh = None
@bot.command(aliases = ['삼투압'])
async def osmolarity(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 805967133368516649:
            global gh
            gh = i
    await ctx.send(gh.mention + ", 삼투압은 삼투현상을 통하여 물이 농도가 낮은 곳에서 높은 곳으로 가는 현상인데 이를 반대로 말한 것에서 유래되었다.")

gh = None
hy = None
@bot.command(aliases = ['체육복'])
async def gymuniform(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 805967133368516649:
            global gh
            gh = i
        if i.id == 773906164466843700:
            global hy
            hy = i
    await ctx.send(gh.mention + ', ' + hy.mention + '의 "새우깡 먹어" 를 잘못 듣고' + ' "체육복을 먹는다고?" 라고 말한 것에서 유래되었다.')


# 서희 ***********************************************************************************************
sh = None
@bot.command(aliases = ['따당'])
async def ddadang(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 770576567075078184:
            global sh
            sh = i
    await ctx.send(sh.mention + ", 🔫 이모지와 함께 쓰인다. 의도치 않게 이모티콘의 방향이 자신을 가리켜 자살을 의미하게 되었다.")

sh = None
hy = None
@bot.command(aliases = ['꺄'])
async def kkya(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 770576567075078184:
            global sh
            sh = i
        if i.id == 773906164466843700:
            global hy
            hy = i
    await ctx.send(sh.mention + ', ' + hy.mention + '의 "ㅗ" 에 반응하는 말이다.')

sh = None
@bot.command(aliases = ['꺄충'])
async def kkyachoong(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 770576567075078184:
            global sh
            sh = i
    await ctx.send(sh.mention + ", " + sh.mention + '의 잦은 "꺄" 로 인해 붙여진 별명이다.')

sh = None
@bot.command(aliases = ['house_chak_light_ball'])
async def housechaklightball(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 770576567075078184:
            global sh
            sh = i
    await ctx.send(sh.mention + ', "집착광공" 을 직역한 것이다.')

sh = None
ek = None
@bot.command(aliases = ['옆구리'])
async def trevi(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 770576567075078184:
            global sh
            sh = i
        if i.id == 805950761972137994:
            global ek
            ek = i
    await ctx.send(sh.mention + ", " + ek.mention + '의 "트레비 터졌어" 를 잘못 듣고 "옆구리가 터졌다고?" 라고 말한 것에서 유래되었다.')

sh = None
@bot.command(aliases = ['디콕'])
async def dicok(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 770576567075078184:
            global sh
            sh = i
    await ctx.send(sh.mention + ", 본래 디코 ㄱ의 오타였지만 굳어져 하나의 고유명사가 되었다.")

# 은교 ***********************************************************************************************
ek = None
@bot.command(aliases = ['뀨'])
async def ggyu(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 805950761972137994:
            global ek
            ek = i
    await ctx.send(ek.mention + ", 지랄")

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

hy = None
@bot.command(aliases = ['와타범범', '渦打汎汎'])
async def watabumbum(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 773906164466843700:
            global hy
            hy = i
    await ctx.send(hy.mention + ', 블랙핑크 - Forever Young의 가사를 들리는 대로 발음한 "워터밤밤" 을 뜻에 맞는 한자어(渦打汎汎) 로 변환한 것이다.')

hy = None
@bot.command(aliases = ['단델리온'])
async def dandelion(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 773906164466843700:
            global hy
            hy = i
    await ctx.send(hy.mention + ', 길거리의 민들레를 보고 AB6IX - 민들레꽃이 생각나 부제목을 콩글리쉬로 읽은 것에서 유래되었다.')

hy = None
@bot.command(aliases = ['전기저항'])
async def resistance(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 773906164466843700:
            global hy
            hy = i
    await ctx.send(hy.mention + ', 시험기간 중 닉네임을 "V=I×R 전류의 세기=전압/전기 저항" 으로 해놓은 것에서 유래되어 붙여진 별명이다.')

hy = None
@bot.command(aliases = ['사랑햌'])
async def saranghaek(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 773906164466843700:
            global hy
            hy = i
    await ctx.send(hy.mention + ', 장충즈 서버 덕담방에 보낸 메시지에서 유래되어 사랑한다는 말을 할 때 쓰인다.')

hy = None
@bot.command(aliases = ['힝', '머그꺼야', '머그꺼야힝'])
async def meogukkeoyahing(ctx):
    for i in bot.get_guild(806480753537581106).members:
        if i.id == 773906164466843700:
            global hy
            hy = i
    await ctx.send(hy.mention + ', 본인이 "먹을 거야" 를 "머그꺼야" 라고 발음하는 것을 깨달아 사용하던 것에서 유래되었다.')

token = 'ODQwMjIwOTUwMjUwNTIwNTk2.YJVCvQ.K0boSoOcDBJ4ANzN1FslTn0O3ag'

bot.run(token)
