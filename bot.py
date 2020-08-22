import discord
import asyncio
import os
import random
import youtube_dl
import json
import requests
import typing

from requests import get 

from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord import Spotify

from Cybernator import Paginator as pag

from datetime import datetime

from random import choice

from PIL import Image, ImageFont, ImageDraw


players = {}


Bot = commands.Bot(command_prefix = "/")
Bot.remove_command('help')
bad_words = ['сервер говно', 'бот говно', 'админы говно', 'satoemari лох', 'крыса лох', 'пидорский сервер', 'администрация говно', 'dnc говно', 'дно сервер', 'вы все лохи']



#РАБОТАЕТ ЛИ БОТ?

@Bot.event
async def on_ready():
    await Bot.change_presence(activity = discord.Activity(type= discord.ActivityType.watching, name = "за Dark Neon City 👀"))
    print("Бот в онлайне!")

    
    
#ВЫДАЧА РОЛЕЙ

@Bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name = 'Unit')  # САМА РОЛЬ КОТОРУЮ ВЫДАЕМ
    await member.add_roles(role) # ДОБАВЛЯЕМ РОЛЬ
    channel1 = Bot.get_channel(526099119874375710) #правила
    channel2 = Bot.get_channel(528281293306462248) #смскер
    channel3 = Bot.get_channel(687044254622941217) #info
    channel4 = Bot.get_channel(541231102333943832) #news
    channel5 = Bot.get_channel(741002854898073660) #доска-почёта
    channel6 = Bot.get_channel(733727409672683550) #предложения
    embed = discord.Embed(color = 0x4ace40)
    embed.add_field(name = "Приветственное сообщение", value = "Добро пожаловать в Dark Neon City!\n"
    f"Перед тем, как пользоваться сервером, прочитай {channel1.mention}. Это обязательно, а то атата!)\n"
    '\n'
    f'Тебе дана роль `@Unit`, поэтому, пока что, тебе доступны не все функции сервера. Но ты можешь участвовать в ивентах, чтобы повысить свой ранг!\n'
    '\n'
    "Для тебя открыты все комнаты в доме unit'ов, выбирай любую которая не занята, зови друзей на сервер и наслаждайтесь общением благодаря качественной связи!\n"
    '\n'
    f"Chill'овая беседка - самое уютное место для общения на различные темы! Заглядывай туда, в {channel2.mention}, или же в войс-чат под ним!\n"
    '\n'
    f"На сервере, как ты заметил, присутствуют боты, информацию о них можешь найти в {channel3.mention}.\n"
    '\n'
    'По интересующим вопросам обращайся к `@Смотрящий`.\n'
    '\n'
    f"Не забывай следить за новостями {channel4.mention} и обновлениями правил {channel1.mention}. Будь активен на сервере и однажды появишься на {channel5.mention}!\n"
    '\n'
    f"Так же можешь подкинуть идеи в {channel6.mention}\n"
    '\n'
    "С наилучшими пожеланиями, администрация сервера!")
    embed.set_footer(text = "supports by quantprod")
    await member.send(embed = embed)



#ОБРАБОТЧИК ОШИБОК

@Bot.event
async def on_command_error(ctx, error):
    pass

@Bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        author = ctx.message.author
        embed = discord.Embed(color = 0x4ace40)
        embed.add_field(name = 'Ошибка выполнения команды!', value = f':x: *Внимание, {author.mention}! Данной команды __не существует__!*')
        embed.set_footer(text = "supports by quantprod")
        await ctx.send(embed = embed)

@Bot.event
async def on_message(message):
    #фильтрация чата и отправка нарушителя в спец. чат
    channel = Bot.get_channel(644599042869035019)
    author = message.author
    await Bot.process_commands(message)
    msg = message.content.lower()
    if msg in bad_words:
        await message.delete()
        embed = discord.Embed(title = "Замечено оскорбление!", description = f'Прошу дать по попе {author.mention}', color = 0x4ace40)
        message = await channel.send(embed = embed)

                   
                   
#SPOTIFY, КТО ЧТО СЛУШАЕТ

@Bot.command(aliases = ['spot', 's'])
async def spotify(ctx, user: discord.Member = None):
    user = user or ctx.author
    for activity in user.activities:
        if isinstance(activity, Spotify):
            await ctx.send(f"{user} слушает {activity.title}, by {activity.artist}")



#АКТУАЛЬНАЯ ВЕРСИЯ БОТА

@Bot.command(aliases = ['v'])
@commands.has_any_role("admin", "Смотрящий", "elite")
async def version(ctx):
    embed = discord.Embed(title = "Актуальная версия бота", description= '__Апдейт был 22.08.2020 до v. 2.7__. \n' 'Добавлено:\n'
                          '1) Поддержка музыки. Теперь бот умеет воспроизводить песни по ссылке с ютуба\n'
                          '2) Обновлены команды на стр. 4 в `/help` (добавлена команда `/pause`,\n'
                              'которая позволяет останавливать трек, и при её повторном использовании\n'
                              'возобновлять воспроизведение трека', color=0x4ace40)
    await ctx.send(embed = embed)
    await ctx.send('@everyone')

    

#МУЗЫКА С ЮТУБА

@Bot.command(aliases = ['p', 'PLAY'])
async def play(ctx, url):  #КОМАНДА ПРОИГРЫВАНИЯ ЗВУКОВОЙ ДОРОЖКИ
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove('song.mp3')
            print('[logs] Старый файл успешно удалён')
    except PermissionError: 
        print('[logs] Не удалось удалить файл. Неизвестная причина...')
    voice = get(Bot.voice_clients, guild = ctx.guild)
    ydl_opts = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '320'
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print ('[logs] Начинаю загрузку музыки...')
        embed = discord.Embed(description = '*Минуточку ожидания, готовлю к воспроизведению твой трек...*', color = 0x4ace40)
        await ctx.send(embed = embed)
        ydl.download([url])
    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            os.rename(file, 'song.mp3') 
    voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: print(f'{name}, музыка закончила своё проигрывание'))
    nname = name.rsplit('-', maxsplit = 1)
    embed = discord.Embed(description = f'🎵 __Сейчас играет:__ **{nname[0]}**', color = 0x4ace40)
    embed.set_footer(text = "supports by quantprod")
    await ctx.send(embed = embed)
    
@Bot.command(aliases = ['j', 'JOIN'])	
async def join(ctx):  #КОМАНДА ПОДКЛЮЧЕНИЯ БОТА К ГС КАНАЛУ	
    global voice	
    channel = ctx.message.author.voice.channel	
    voice = get(Bot.voice_clients, guild = ctx.guild)	
    if voice and voice.is_connected():	
        await voice.move_to(channel)	
    else:	
        voice = await channel.connect()	
        embed = discord.Embed(description = f'Я присоединился к **{channel}**', color = 0x4ace40)	
        embed.set_footer(text = "supports by quantprod")	
        message = await ctx.send(embed = embed)	
        await message.add_reaction('✅')	
    await Bot.join_voice_channel(channel)
        
@Bot.command(aliases = ['l', 'LEAVE'])
async def leave(ctx):  #КОМАНДА LEAVE БОТА ИЗ ГС КАНАЛА
    channel = ctx.message.author.voice.channel
    voice = get(Bot.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        embed = discord.Embed(description = f'Я отключился от **{channel}**', color = 0x4ace40)
        embed.set_footer(text = "supports by quantprod")
        message = await ctx.send(embed = embed)
        await message.add_reaction('✅')
    else:
        voice = await channel.connect()       
 
@Bot.command()
async def pause(ctx):
    voice = get(Bot.voice_clients, guild = ctx.guild)   
    if voice and voice.is_playing():
        voice.pause()
        embed = discord.Embed(description = f'⏸️ *Музыка приостановлена...*', color = 0x4ace40)
        embed.set_footer(text = "supports by quantprod")
        message = await ctx.send(embed = embed)
        await message.add_reaction('👌')
    else:
        voice.resume()
        embed = discord.Embed(description = f'⏯️ *Продолжай наслаждаться музыкой 😋*', color = 0x4ace40)
        embed.set_footer(text = "supports by quantprod")
        await ctx.send(embed = embed)    
        

        
#ПОГОДА

@Bot.command()
async def weather(ctx, *, city: str):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    api_owm = '610db95b52ef9995408f455131444af3'
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Weather in {city_name}", color=ctx.guild.me.top_role.color, timestamp=ctx.message.created_at)
            embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")  
            await channel.send(embed=embed)
    else:
        await channel.send("City not found.")
            
                 
#ПОМОЩЬ USER

@Bot.command(aliases = ['h', 'HELP'])
async def help(ctx):
    author = ctx.message.author
    channel1 = Bot.get_channel(526099119874375710)
    embed1 = discord.Embed(title = 'Помощь, страница 1', description = f'Йо, {author.mention}! Держи список команд:\n'
                        '\n'
                        '`/spotify [@пользователь]` - узнай, что слушает юзер в данный момент, введя лишь одну команду\n'
                        '*сокращения/синонимы*: `/spot`, `/s`\n'
                        '\n'
                        '`/author` - команда разработчиков этого бота;\n'
                        '\n'
                        '`/github` - GitHub главного разработчика бота;\n'
                        '\n'
                        '`/math [первое число] [второе число]` - посчитает Ваши числа. \n'
                        '**ВНИМАНИЕ! Числа нужно вводить ЧЕРЕЗ пробел:**\n'
                        '__ввели__ `/math 3 4`, __вывод дал Embed с операциями__;\n'
                        )
    embed2 = discord.Embed(title = 'Помощь, cтраница 2', description =
                        '`/length [строка]` - узнать длину строки\n'
                        '*сокращения/синонимы*: `/len`;\n'
                        '\n'
                        '`/pizdec` - не, ну это бан!\n'
                        '*сокращения/синонимы*: `/pzdc`;\n'
                        '\n'
                        '`/avatar [@пользователь]` - аватарка пользователя\n'
                        '*сокращения/синонимы*: `/ava`;\n'
                        '\n'
                        '`/say [ваш текст]` - бот повторит за вами всё то, что вы ему напишете\n'
                        '*сокращения/синонимы*: `/repeat`;\n'
                        )
    embed3 = discord.Embed(title = 'Помощь, страница 3', description = 
                        '`/hello` - ну-ка быстро посмотри :)\n'
                        '\n'
                        '`/info [@пользователь]` - узнай регистрацию пользователя!;\n'
                        '\n'
                        '`/message [@пользователь] [текст сообщения]` - отправка сообщения любому юзеру с помощью бота;\n'
                        '\n'
                        '`/ping` - проверка скорости реакции бота;\n')
    embed4 = discord.Embed(title = 'Помощь, страница 4', description = 
                        '`/join` - для использования данной команды Вы должны зайти в гс канал\n'
                        '*сокращения/синонимы*: `/j`;\n'
                        '\n'
                        '`/play [ссылка на видео из ютуб]` - проигрывание звуковой дорожки из видео\n'
                        '*сокращения/синонимы*: `/p`;\n'
                        '\n'
                        '`/leave` - кикает бота с гс канала, для использования, Вы должны быть в канале с ботом\n'
                        '*сокращения/синонимы*: `/l`;\n'
                        '\n'
                        '`/pause` - пауза текущей песни, повторное использование возобновляет аудио.')
    embed5 = discord.Embed(title = 'Помощь, страница 4, команды в стадии разработки', description = 
                        '*пока таких команд нет, ожидайте выходов новых обновлений бота*')
    embeds = [embed1, embed2, embed3, embed4, embed5]
    message = await ctx.send(embed =  embed1)
    page = pag(Bot, message, only = ctx.author, use_more = False, timeout = 1*3600, embeds = embeds)
    await page.start()



#ПОМОЩЬ ADMIN

@Bot.command(aliases = ['h_a', 'HELP_ADM'])
@commands.has_any_role("admin", "Смотрящий", "elite", "dmoder", "moder")
async def help_adm(ctx):
    await ctx.message.delete()
    channel1 = Bot.get_channel(526099119874375710)
    author = ctx.message.author
    embed = discord.Embed(title = 'Команды для администрации и высшей инстанции в том числе', description = 
                        f'Привет, {author.mention}! Вот список команд, доступных тебе:\n'
                        'Все команды юзеров, плюс команды администрации, такие как:\n'
                        '\n'
                        '`/clear [количество сообщений]` - очистка канала (полностью)\n'
                        '*сокращения/синонимы*: `/c`;\n'
                        '\n'
                        '`/clear_member [@пользователь]` - очистка сообщений конкретного пользователя\n'
                        '*сокращения/синонимы*: `/c_m`;\n'
                        '\n'
                        '`/kick [@пользователь]` - кик пользователя\n'
                        '*сокращения/синонимы*: `/k`;\n'
                        '\n'
                        '`/court [@пользователь] [время в часах]` - выдача роли подсудимого;\n'
                        '\n'
                        '`/tempban [@пользователь] [время в часах] [причина]` - временный бан пользователя\n'
                        '*сокращения/синонимы*: `/tb`;\n'
                        '\n'
                        '`/ban [@пользователь] [причина]` - перма нафиг!\n'
                        '*сокращения/синонимы*: `/b`;\n'
                        '\n'
                        '`/mute [@пользователь] [время в часах] [причина]` - мут пользователя \n'
                        '*сокращения/синонимы*: `/m`;\n'
                        '\n'
                        f'Кстати говоря, советую ознакомиться с правилами: {channel1.mention}', 
                        color = 0x4ace40)
    embed.set_footer(text = "supports by quantprod")
    message = await ctx.author.send(embed = embed)



#НЕ, НУ ЭТО БАН!

@Bot.command(aliases = ['pzdc', 'PIZDEC'])
async def pizdec(ctx):
    await ctx.message.delete()
    await ctx.send(':regional_indicator_p:'
                   ':regional_indicator_i:' 
                   ':regional_indicator_z:' 
                   ':regional_indicator_d:' 
                   ':regional_indicator_e:' 
                   ':regional_indicator_c:')



#ПАСХАЛОЧКА :)

@Bot.command(aliases = ['AUTHOR'])
async def author(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title = f'Авторы:',
                          description = '**Разработчик:** https://vk.com/d.blinov79\n'
                          '**С подачи:** https://vk.com/code_authora_174',
                          color = 0x4ace40)
    embed.set_footer(text = "supports by quantprod")
    message = await ctx.send(embed = embed)
    await message.add_reaction('☝')

@Bot.command(aliases = ['git', 'GitHub'])
async def github(ctx):
    embed = discord.Embed(title = 'GitHub разработчика:', color = 0x4ace40)
    embed.set_image(url = 'https://i.ibb.co/j42cxmr/qr-code.png')
    await ctx.send(embed = embed)



#ПОПУГАЙЧИК

@Bot.command(aliases = ['repeat', 'SAY'])
async def say(ctx,  *, arg):
    await ctx.message.delete()
    await ctx.send(arg)


 
#МАТЕМАТИКА (ПРОСТЫЕ ОПЕРАЦИИ)

@Bot.command(aliases = ['MATH']) 
async def math(ctx,  a:  int,  b:  int): 
    embed= discord.Embed(title = "Простая математика", color = 0x4ace40)
    embed.add_field(name = "Сумма: ", value= a + b, inline = False)
    embed.add_field(name = "Разность: ", value= a - b, inline = False)
    embed.add_field(name = "Деление: ", value= a / b, inline = False)
    embed.add_field(name = "Умножение: ", value= a * b, inline = False)
    embed.set_footer(text = "supports by quantprod")
    await ctx.send(embed = embed)



#ИНФОРМАЦИЯ О ЮЗЕРЕ

@Bot.command(aliases = ['i', 'information', 'INFO', 'INFORMATION'])
async def info(ctx, member: discord.Member):
    embed = discord.Embed(title = "Info", color = 0x4ace40)
    embed.add_field(name = "❓ Когда присоединился: ", value = member.joined_at)
    embed.add_field(name = "❓ Имя юзера: ", value = member.display_name)
    embed.set_footer(text = "supports by quantprod")
    await ctx.send(embed = embed)



#ПРИВЕТСТВИЕ

@Bot.command(aliases = ['HELLO'])
async def hello(ctx):
    await ctx.message.delete()
    author = ctx.message.author
    embed = discord.Embed(title = 'Dark Neon City', description = f'👋 Привет, {author.mention}! Рад видеть тебя на Dark Neon City!', color = 0x4ace40)
    embed.set_footer(text = "supports by quantprod")
    message = await ctx.send(embed = embed)



#УДАЛЕНИЕ СООБЩЕНИЙ

@Bot.command(aliases = ['c_m', 'CLEAR_MEMBER'])
@commands.has_any_role("admin", "Смотрящий", "elite")
async def clear_member(ctx, user: discord.Member, amount = 15):  #СООБЩЕНИЯ ПОЛЬЗОВАТЕЛЯ
    await ctx.message.delete()
    await ctx.channel.purge(limit = amount, check = lambda m: m.author == user)
    author = ctx.message.author
    await ctx.send(embed = discord.Embed(description = f'✅ {author.mention}, *удаление сообщений юзера прошло успешно!*', color = 0x4ace40))

@Bot.command(aliases = ['c', 'CLEAR'])
@commands.has_any_role("admin", "Смотрящий", "elite")
async def clear(ctx, amount = 30):  #ВООБЩЕ ВСЕ СООБЩЕНИЯ
    await ctx.message.delete()
    await ctx.channel.purge(limit = amount)
    author = ctx.message.author
    await ctx.send(embed = discord.Embed(description = f'✅ {author.mention}, *удаление сообщений прошло успешно!*', color = 0x4ace40))



#РОЛЬ ПОДСУДИМОГО

@Bot.command(aliases = ['COURT'])
@commands.has_any_role("admin", "Смотрящий", "elite", "dmoder", "moder")
async def court(ctx, member: discord.Member):
    channel = Bot.get_channel(526464840672346112) #логи
    author = ctx.message.author
    role = discord.utils.get(ctx.guild.roles, name = "urole0")
    await ctx.message.delete()
    await member.add_roles(role)
    embed = discord.Embed(title = "Суд", description= f'✅ Пользователь {author.mention} выдал {member.mention} роль подсудимого! Кто-то скоро пойдёт на суд :)', color = 0x4ace40)
    message = await ctx.send(embed = embed)
    await channel.send(f'{author.mention} **выдал роль подсудимого юзеру** {member.mention}.')



#АВАТАРКА

@Bot.command(aliases = ['ava', 'AVATAR'])
@commands.has_any_role("admin", "Смотрящий", "elite", "Vip")
async def avatar(ctx, *,  avamember: discord.Member):
    userAvatarUrl = avamember.avatar_url
    embed = discord.Embed(description = f"Аватарка пользователя {avamember.mention}", color = 0x4ace40)
    embed.set_image(url = userAvatarUrl)
    await ctx.send(embed = embed)



#БАН, МУТ ПОЛЬЗОВАТЕЛЯ И КИК ПОЛЬЗОВАТЕЛЯ

@Bot.command(aliases = ['k', 'KICK'])
@commands.has_any_role("admin", "Смотрящий", "elite")
async def kick(ctx, member: discord.Member, *, reason = None):  #КИК
    channel = Bot.get_channel(526464840672346112) #LOGS
    author = ctx.message.author
    await ctx.message.delete()
    await member.kick(reason = reason)
    embed = discord.Embed(title = "Кик", description = f"✅ Пользователь {member.mention} был успешно кикнут пользователем {author.mention}", color = 0x4ace40)
    embed.set_footer(text = "supports by quantprod")
    await ctx.send(embed = embed)
    await channel.send(f'{author.mention} **кикнул пользователя** {member.mention} **по причине:** {reason}.')

@Bot.command(aliases = ['tb', 'TEMPBAN'])
@commands.has_any_role("admin", "Смотрящий", "elite", "dmoder", "moder")
async def tempban(ctx, user: discord.User, duration: int, *, reason= None):  #ВРЕМЕННЫЙ БАН
    channel = Bot.get_channel(526464840672346112) #LOGS
    author = ctx.message.author
    await ctx.message.delete()
    await ctx.guild.ban(user)
    emb = discord.Embed(title = "Временный бан", description = f"{author.mention} забанил {user.mention}", color = 0x4ace40)
    emb.add_field(name = "Срок бана (в часах):", value = duration)
    emb.add_field(name = "По причине:", value = reason)
    emb.set_footer(text = "supports by quantprod")
    await ctx.send(embed = emb)
    await channel.send(f'{author.mention} **выдал временный бан** {user.mention}.')
    await asyncio.sleep(duration)
    await ctx.guild.unban(user)
    embed = discord.Embed(title= "Временный бан", description= f'Пользователь {user.mention} был выпущен из тюрьмы, просьба отправить ему приглашение на сервер (просто он инвалид и сам не может присоединиться)!\n'
      'https://discord.gg/rjMDwaB', color = 0x4ace40)
    embed.set_footer(text = "supports by quantprod")
    await ctx.send(embed = embed)

@tempban.error
async def tempban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Вы забыли указать аргумент!')

@Bot.command(aliases = ['b', 'BAN'])
@commands.has_any_role("admin", "Смотрящий", "elite")
async def ban(ctx, member: discord.Member, *, reason = None):  #ПЕРМАНЕНТНЫЙ БАН
    channel = Bot.get_channel(526464840672346112) #логи
    await member.ban(reason = reason)
    await ctx.message.delete()
    author = ctx.message.author
    embed = discord.Embed(description = f'{author.mention} выдал {member.mention} перманент', color= 0x4ace40)
    embed.add_field(name = "Причина:", value = reason, inline = False)
    embed.add_field(name = "Суд:", value = "см. причину", inline = False)
    embed.set_footer(text = "supports by quantprod")
    await ctx.send(embed = embed)
    await channel.send(f'{author.mention} **выдал перманентный бан** {member.mention}. **Причина и суд:** {reason}')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Вы забыли указать аргумент!')

@Bot.command(aliases = ['m', 'MUTE'])
@commands.has_any_role("admin", "Смотрящий", "elite", "dmoder", "moder")
async def mute(ctx, member: discord.Member, duration: int):  #МУТ
    author = ctx.message.author
    channel = Bot.get_channel(526464840672346112) #логи
    role = discord.utils.get(ctx.guild.roles, name = "mute")
    await ctx.message.delete()
    await member.add_roles(role)
    await channel.send(f'{author.mention} **выдал мут** {member.mention}. **Время:** {duration} час')
    embed = discord.Embed(description= f'*Пользователь {member.mention} был успешно замучен!*', color = 0x4ace40)
    await ctx.send(embed = embed)
    await asyncio.sleep(duration * 3600)
    await member.remove_roles(role)
    embed = discord.Embed(description= f'*Пользователь {member.mention} был успешно размучен! Напомните ему об этом :)*', color = 0x4ace40)
    await ctx.send(embed = embed)

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Вы забыли указать аргумент!')



#УЗНАТЬ ДЛИНУ СТРОКИ (СООБЩЕНИЯ)

@Bot.command(aliases = ['len', 'LENGTH']) 
async def length(ctx): 
    embed = discord.Embed(color = 0x4ace40)
    embed.add_field(name = "Длина твоего сообщения вместе с командой равна:", value = '{}'.format(len(ctx.message.content)))
    embed.set_footer(text = "supports by quantprod")
    await ctx.send(embed = embed)


    
#ОТПРАВКА ЛИЧНЫХ СООБЩЕНИЙ

@Bot.command()
async def message(ctx, member: discord.Member, *, arg):
    await ctx.message.delete()
    author = ctx.message.author
    embed = discord.Embed(title = 'Личное сообщение', description = f'*Тебе сообщение с сервера Dark Neon City от* {author.mention}: ' + arg, color = 0x4ace40)
    embed.set_footer(text = "supports by quantprod")
    message = await member.send(embed = embed)



#ПИНГ

@Bot.command()
async def ping(ctx):
    ping_ = Bot.latency
    ping = round(ping_ * 1000)
    embed = discord.Embed(title ='Pong!', description = f"Твой пинг: `{ping}ms`", color = 0x4ace40)
    embed.set_footer(text = "supports by quantprod")
    message = await ctx.send(embed = embed)
    await message.add_reaction('👌')
    
    
    
#СТАРТ БОТА

 
token = os.environ.get('bot_token')
Bot.run(str(token))
