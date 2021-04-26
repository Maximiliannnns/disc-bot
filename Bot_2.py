import discord
from discord.ext import commands
import json
import requests

TOKEN = 'ODM1OTI5NDQ4NDMxMzUzOTA4.YIWl9w.VJkFocBGgIuIlAmC9Whd9qeOdGE'

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("Я готов {0.user}".format(bot))


@bot.command()
async def start(ctx):
    print("старт")
    await ctx.message.channel.send("Поехали!")


@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9900, title='Случайная лисичка)')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@bot.command()
async def YT(ctx):
    embed = discord.Embed(
        title="Нажмите для перехода!",
        description="Ссылка для перехода на YouTube",
        url='https://www.youtube.com/',
    )
    await ctx.send(embed=embed)


@bot.command()
async def admin_vk(ctx):
    embed = discord.Embed(
        title="Нажмите для перехода!",
        description="Ссылка для перехода на ВК администратора",
        url='https://vk.com/maximilian711',
    )
    await ctx.send(embed=embed)


@bot.command()
async def music(ctx):
    await ctx.channel.send("А вот и время послушать музыку :)")
    embed = discord.Embed(
        title="Нажмите для перехода!",
        description="Яндекс.музыка",
        url='https://music.yandex.ru/home',
    )
    await ctx.send(embed=embed)


@bot.command()
async def start_delta(ctx):
    embed = discord.Embed(
        title="Привет всем! Я Бот Дельта",
    )
    await ctx.channel.send(embed=embed)

bot.run(TOKEN)
