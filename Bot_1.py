import discord
from discord.ext import commands

TOKEN = '!'


hello_words = ['привет', 'здравствуй', 'Добрый день', 'Добрый вечер', 'Доброе утро']
info_words = ["как сделать", "куда обратиться", "помощь", "помогите", "поддержка"]
bye_words = ["пока", "прощай", "досвидания", "до свидания"]
play_words = ["игр", "game"]
prog_words = ["код", "прог"]
pogoda_words = ["погода"]

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("Я готов {0.user}".format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content.lower()

    find_hello_words = False
    for item in hello_words:
        if msg.find(item) >= 0:
            find_hello_words = True

    if find_hello_words:
        await message.channel.send("Здравствуйте, чего изволите?")

    find_info_words = False
    for item in info_words:
        if msg.find(item) >= 0:
            find_info_words = True

    if find_info_words:
        await message.channel.send("Спасибо за обращение, ожидайте, вам скоро ответит админ!")
        await message.channel.send("<@&835890735483322389>")

    find_bye_words = False
    for item in bye_words:
        if msg.find(item) >= 0:
            find_bye_words = True

    if find_bye_words:
        await message.channel.send("Было приятно пообщаться! До встречи!")

    find_play_words = False
    for item in play_words:
        if msg.find(item) >= 0:
            find_play_words = True

    if find_play_words:
        await message.channel.send("Эй, настало время развлечься!")
        await message.channel.send("<@&834454092662571028>")

    find_prog_words = False
    for item in prog_words:
        if msg.find(item) >= 0:
            find_prog_words = True

    if find_prog_words:
        await message.channel.send("Спасибо за обращение, ожидайте, вам скоро ответит специалист-программист!")
        await message.channel.send("<@&834454150107496498>")

    find_pogoda_words = False
    for item in pogoda_words:
        if msg.find(item) >= 0:
            find_pogoda_words = True

    if find_pogoda_words:
        embed = discord.Embed(
            title="Нажмите для перехода!",
            description="Расписание погоды на завтра!",
            url='https://www.gismeteo.ru/',
        )
        await message.channel.send(embed=embed)

bot.run(TOKEN)
