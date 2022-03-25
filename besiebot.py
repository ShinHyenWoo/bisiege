import asyncio, discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="!") #접두사를 지정

@bot.event
async def on_ready():
    game = discord.Game("명일방주")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command(aliases=['ㄱㅌㅇ', '태윤'])
async def 김태윤(ctx):
	await ctx.send("제발 좀 죽어!")


@bot.command(aliases=['qjtjzj'])
async def 버서커(ctx):
    embed = discord.Embed(title='버서커', description='22222', color=0x8df22e)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883023892262834236/956201381591646318/e1c11c8df4b2b678.png")
    embed.add_field(name="큰 룬", value="올 공격", inline=False)
    embed.add_field(name="작은 룬", value="7 공격 1 피흡", inline=True)
    embed.add_field(name="템", value="폭검 전검 전검 패망 대천 사낫", inline=False)
    embed.add_field(name="유물", value="듀랜 갑주 언월", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['skdlxm'])
async def 나이트(ctx):
    embed = discord.Embed(title='나이트', description='아직 몰?루', color=0x8df22e)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883023892262834236/956203454316027914/71233cbdf46cf8ac.png")
    embed.add_field(name="큰 룬", value="아직 몰?루", inline=False)
    embed.add_field(name="작은 룬", value="아직 몰?루", inline=True)
    embed.add_field(name="템", value="아직 몰?루", inline=False)
    embed.add_field(name="유물", value="아직 몰?루", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['glfepthfvm', '솔프', 'thfvm'])
async def 힐데솔프(ctx):
    embed = discord.Embed(title='힐데그림 솔로 프리스트', description='2줄', color=0x8df22e)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883023892262834236/956204818425319424/31851a2cb8922521.png")
    embed.add_field(name="큰 룬", value="올 회복", inline=False)
    embed.add_field(name="작은 룬", value="올 회복", inline=True)
    embed.add_field(name="템", value="대천 고마방 왕실휘장 연갑 연갑 연갑", inline=False)
    embed.add_field(name="유물", value="갑주 현돌 힐데", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['elfvm'])
async def 딜프(ctx):
    embed = discord.Embed(title='딜링 프리스트', description='22121', color=0x8df22e)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883023892262834236/956204818425319424/31851a2cb8922521.png")
    embed.add_field(name="큰 룬", value="올 치확", inline=False)
    embed.add_field(name="작은 룬", value="4 치확 4 공격", inline=True)
    embed.add_field(name="템", value="연건 연건 연건 연건 연완 연건", inline=False)
    embed.add_field(name="유물", value="파초 카두 궁니르", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['쿨감프', 'znfvm', 'znfrkavm'])
async def 쿨프(ctx):
    embed = discord.Embed(title='쿨타임 감소 프리스트', description='21222', color=0x8df22e)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883023892262834236/956204818425319424/31851a2cb8922521.png")
    embed.add_field(name="큰 룬", value="올 쿨감", inline=False)
    embed.add_field(name="작은 룬", value="올 쿨감", inline=True)
    embed.add_field(name="템", value="올 연건", inline=False)
    embed.add_field(name="유물", value="파초 카두 판도라", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['매지', 'aowltus', 'aowl'])
async def 매지션(ctx):
    embed = discord.Embed(title='매지션', description='2줄', color=0x8df22e)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883023892262834236/956209396050980874/94fd0ea62e1c6887.png")
    embed.add_field(name="큰 룬", value="올 쿨감", inline=False)
    embed.add_field(name="작은 룬", value="올 쿨감", inline=True)
    embed.add_field(name="템", value="올 연건", inline=False)
    embed.add_field(name="유물", value="판도라 여의봉 카두", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['vkdlxj'])
async def 파이터(ctx):
    embed = discord.Embed(title='파이터', description='11122', color=0x8df22e)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883023892262834236/956210084260769792/382b2354244a7c0b.jpeg")
    embed.add_field(name="큰 룬", value="올 공격", inline=False)
    embed.add_field(name="작은 룬", value="3 공격 2 치확 3 피흡", inline=True)
    embed.add_field(name="템", value="폭검 전검 사낫 사낫 대천 연건", inline=False)
    embed.add_field(name="유물", value="아이기스 듀랜 갑주", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['임시아처', 'dlatldkcj', 'alsdndlatldkcj'])
async def 민우임시아처(ctx):
    embed = discord.Embed(title='민우임시아처', description='11111', color=0x8df22e)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883023892262834236/956212824676392970/b5d34e9ac7693b74.png")
    embed.add_field(name="큰 룬", value="올 피흡", inline=False)
    embed.add_field(name="작은 룬", value="6 공격 2 체력", inline=True)
    embed.add_field(name="템", value="전검 전검 전검 사낫 가완 정손", inline=False)
    embed.add_field(name="유물", value="듀랜 페일 갑주", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['shxhxmfostj'])
async def 노토트랜서(ctx):
    embed = discord.Embed(title='노 토트 랜서', description='22222', color=0x8df22e)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883023892262834236/956213602161926274/Screenshot_20220324-002936_Castle_Defense_Online.jpg")
    embed.add_field(name="큰 룬", value="올 치확", inline=False)
    embed.add_field(name="작은 룬", value="4 공격 4 치확", inline=True)
    embed.add_field(name="템", value="폭검 전검 사낫 사낫 대천 연건", inline=False)
    embed.add_field(name="유물", value="바리사다 갑주 듀랜/카두", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['fostj'])
async def 랜서(ctx):
    embed = discord.Embed(title='랜서', description='22222', color=0x8df22e)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883023892262834236/956213602161926274/Screenshot_20220324-002936_Castle_Defense_Online.jpg")
    embed.add_field(name="큰 룬", value="올 치확", inline=False)
    embed.add_field(name="작은 룬", value="4 공격 4 치확", inline=True)
    embed.add_field(name="템", value="폭검 전검 사낫 사낫 대천 연건", inline=False)
    embed.add_field(name="유물", value="바리사다 갑주 토트", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['dkcj'])
async def 아처(ctx):
    embed = discord.Embed(title='아처', description='11111', color=0x8df22e)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883023892262834236/956212824676392970/b5d34e9ac7693b74.png")
    embed.add_field(name="큰 룬", value="1 피흡 1 체력", inline=False)
    embed.add_field(name="작은 룬", value="6 피흡 2 체력", inline=True)
    embed.add_field(name="템", value="폭검 전검 전검 전검 대천/정손 연건", inline=False)
    embed.add_field(name="유물", value="궁닐 페일 아론", inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("알 수 없는 명령어입니다.")

bot.run(os.environ['token'])