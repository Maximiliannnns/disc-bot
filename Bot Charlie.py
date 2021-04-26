import discord
from discord.ext import commands

TOKEN = 'ODM1OTI5MzUyMjUxMjQ0NTc0.YIWl4A.MhMAVA5BXk_wGgzFIvB2aeF0Dnw'


hello_words = ['привет', 'здравствуй', 'Добрый день', 'Добрый вечер', 'Доброе утро']
info_words = ["как сделать", "куда обратиться", "помощь", "помогите", "поддержка"]
bye_words = ["пока", "прощай", "досвидания", "до свидания"]
play_words = ["игр", "game"]
pogoda_words = ["погода"]
prog_words = ["код", "прог"]
hi_bot_words = ["start_charlie"]
helps_words = ["что вы умеете", "что ты уммешь", "что ты можешь", "что вы можете"]

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
        await message.channel.send("Держите расписание погоды на завтра!")

    find_hi_bot_words = False
    for item in hi_bot_words:
        if msg.find(item) >= 0:
            find_hi_bot_words = True

    if find_hi_bot_words:
        embed = discord.Embed(
            title="Привет всем! Я Бот Чарли",
        )
        await message.channel.send(embed=embed)

    find_helps_words = False
    for item in helps_words:
        if msg.find(item) >= 0:
            find_helps_words = True

    if find_helps_words:
        await message.channel.send("Я Бот Чарли, со мной моожно поболтать, что бы скоротать время, так же могу помочь"
                                   " по некоторым ссылкам")
        await message.channel.send("А подробнее про Бота Дельта указано в канале: #команды-бота.")

bot.run(TOKEN)
