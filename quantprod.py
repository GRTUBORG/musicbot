import discord
import asyncio
import os
import random
import youtube_dl
import json
import requests
import typing
import datetime
import time
import re
import lib
import const
import functools
import feedparser
import vk
import io
import pymorphy2


from gtts import gTTS
from bs4 import BeautifulSoup
from pyowm import OWM
from covid import Covid
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
from requests import get 
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord import Spotify
from discord import User
from PIL import Image, ImageDraw
from os import system
from datetime import date, time, timedelta
from Cybernator import Paginator as pag
from random import choice
from translate import Translator

#-----------------------------license------------------------------#
#------------------------------------------------------------------#
#quantprod's united code by ratratrat
#created on python
#based on DNC and ready to support.
#------------------------------------------------------------------#

intents = discord.Intents.all()

#ТЕКУЩЕЕ ВРЕМЯ (СТРОГО ДЛЯ КОНСОЛИ)

delta = datetime.timedelta(hours = 3, minutes = 0)
t = (datetime.datetime.now(datetime.timezone.utc) + delta)
nowtime = t.strftime("%d.%m в %X")

async def greatSender():
    channel = Bot.get_channel(756990788516446280)
    await channel.send(f'Я перезапустился {nowtime}')

Bot = commands.Bot(command_prefix = ["/", "!", "qp!", "бот ", "quantprod ", "quant "], intents = discord.Intents.all())
Bot.remove_command('help')



bad_words = ['сервер говно', 
             'бот говно', 
             'админы говно', 
             'satoemari лох', 
             'крыса лох', 
             'пидорский сервер', 
             'администрация говно', 
             'dnc говно', 
             'дно сервер', 
             'вы все лохи'
            ]

words_reaction = ['я не крыса', 
                  'я мышь!', 
                  'я мышь', 
                  'я крыса, да', 
                  'я не крыса!'
                  'я крыса',
                  'я не кріса']

haha_words = ['бот пошути',
              'бот, пошути',
              'мемы',
              'бот дай мем',
              'бот, мемы',
              'бот мем',
              'мемный бот']

ladno_for_satoemari = ['ладно',
                       'ладнo',
                       'лaдно']

prancs_words = ['я для тебя шутка какая-то?']



#РАБОТАЕТ ЛИ БОТ?

@Bot.event
async def on_ready():
    await Bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "за Dark Neon City 👀"))
    print('{0.user} в онлайне!'.format(Bot))
    print('Деплой бота был', nowtime)
    await greatSender()

    

#ВЫДАЧА РОЛЕЙ

@Bot.event
async def on_member_join(member):
    await member.add_roles(discord.utils.get(member.guild.roles, name = "Unit"))
    embed = discord.Embed(color = 0x4ace40)
    embed.add_field(name = "Приветственное сообщение", value = "Добро пожаловать на ламповый сервер Dark Neon City!\n"
                                                               '\n'
                                                               f"Перед тем, как пользоваться сервером, прочитай `#правила`. Это обязательно, а то атата!)\n"
                                                               '\n'
                                                               'Тебе дана роль `@Unit`, поэтому, пока что, тебе доступны не все функции сервера. Но ты можешь участвовать в ивентах, чтобы повысить свой ранг!\n'
                                                               "Для тебя открыты все комнаты в доме *unit'ов*, выбирай любую, которая не занята, зови друзей на сервер и наслаждайся общением, благодаря качественной связи!\n"
                                                               "Chill'овая беседка - самое уютное место для общения на различные темы! Заглядывай туда, в `#смскер`, или же в войс-чат под ним!\n"
                                                               '\n'
                                                               "На сервере, как ты заметил, присутствует собственный бот, информацию о нём можешь найти в `#quantupdates`, а также, вбив команду `/help` в `#dnc-cmd`.\n"
                                                               '\n'
                                                               'По интересующим вопросам обращайся к `@Смотрящий`.\n'
                                                               'Оу да, и по вопросам разбана тоже пиши `@Смотрящий`, ну, то есть `@•Satoemari•#0001`, да.\n'
                                                               '\n'
                                                               'Не забывай следить за новостями в `#news` и обновлениями правил в `#правила`. Будь активен на сервере и однажды появишься на `#доска-почёта`!\n'
                                                               '\n'
                                                               'С наилучшими пожеланиями, администрация сервера.')
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
        embed = discord.Embed(color = 0x8B0000)
        embed.add_field(name = 'Ошибка выполнения команды!', value = f':x: Внимание, {author.mention}! Данной команды __не существует__! Проверьте правильность '
                                                                     'написания, либо же пропишите команду `/help`')
        embed.set_footer(text = f"supports by quantprod")
        await ctx.send(embed = embed)



@Bot.event
async def on_message(message):
    channel = Bot.get_channel(644599042869035019)  #фильтрация чата и отправка нарушителя в спец. чат
    author = message.author
    await Bot.process_commands(message)
    msg = message.content.lower()
    if msg in words_reaction:
        with open ('word_reaction_ratratrat.txt', 'r') as file:
            lines = file.readlines()
        await message.channel.send(random.choice(lines))
    if msg in haha_words:
        with open ('memes.txt', 'r') as file:
            lines = file.readlines()
        await message.channel.send(random.choice(lines))
    if msg in ladno_for_satoemari:
        with open ('ladno.txt', 'r') as file:
            lines = file.readlines()
        await message.channel.send(random.choice(lines))
    if msg in prancs_words:
        await message.channel.send(f'да, ты шутка, {author.mention}')
    if msg in bad_words:
        await message.delete()
        embed = discord.Embed(title = "Замечено оскорбление!", description = f'Прошу дать по попе {author.mention}', color = 0x8B0000)
        message = await channel.send(embed = embed)
        await asyncio.sleep(6 * 3600)
        await message.delete()
  


#АКТУАЛЬНАЯ ВЕРСИЯ БОТА

@Bot.command(aliases = ['v'])
@commands.has_any_role("admin", "Смотрящий", "elite")
async def version(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title = "Актуальная версия бота", description = '__Апдейт был 26.10.2020 до v. 6.9__.\n'
                          'Добавлено/обновлено:\n'
                          '• Бот переехал на хостинг 24/7, теперь будет работать до смерти самого хостинга :D\n'
                          '• Исправлены костыли и баги в коде\n'
                          '• Временно вырезана команда `/play [запрос]`, но всё также работает команда `/play [ссылка]`\n'
                          '• Обновлена команда `/help`\n'
                          '\n'
                          'P.S.: если есть какие-то идеи, или же желание помочь в развитии бота/сервера, просьба написать\n'
                          'либо <@394858317572472832>, либо <@394850460420538389>', color = 0x428325)
    await ctx.send(embed = embed)



#ПОГОДА

@Bot.command(aliases = ["погода"])
async def weather(ctx, *, city = None):
    await ctx.message.delete()
    if city == None:
        city = 'Москва'
    city = str(city)
    city = city.capitalize()
    author = ctx.message.author
    try:
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        owm = OWM('0d16f6ffb7d46c30c1202a765e2cb0fc', config_dict)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        w = observation.weather
        cloud = str(w.detailed_status)
        clouds = str(w.clouds) 
        temp = w.temperature('celsius')['temp']
        if temp >= 15.00:
            with open ('for_weather_from_15.txt', 'r') as file:
                lines = file.readlines()
            answer = random.choice(lines)
            embed = discord.Embed(title = f'Виджет погоды для города {city}', description = answer, color = 0x428325) 
            embed.add_field(name = 'Температура:', value = f'Сейчас в твоём городе `{temp}°C`', inline = False)
            embed.add_field(name = 'Осадки:', value = f'Небо затянуто на `{clouds}%`, {cloud}', inline = False)
            embed.set_thumbnail(url = 'https://kindertravelguide.com/wp-content/uploads/2015/11/SUN-1200x1117.jpg')
            embed.set_footer(text = "supports by quantprod")
            await ctx.author.send(embed = embed)
        elif temp < 15.00:
            with open ('for_weather_from_10.txt', 'r') as file:
                lines = file.readlines()
            answer = random.choice(lines)
            embed = discord.Embed(title = f'Виджет погоды для города {city}', description = answer, color = 0x428325) 
            embed.add_field(name = 'Температура:', value = f'Сейчас в твоём городе `{temp}°C`', inline = False)
            embed.add_field(name = 'Осадки:', value = f'Небо затянуто на `{clouds}%`, {cloud}', inline = False)
            embed.set_thumbnail(url = 'https://kindertravelguide.com/wp-content/uploads/2015/11/SUN-1200x1117.jpg')
            embed.set_footer(text = "supports by quantprod")
            await ctx.author.send(embed = embed)
        elif temp <= 5.0:
            with open ('for_weather_from_0.txt', 'r') as file:
                lines = file.readlines()
            answer = random.choice(lines)
            embed = discord.Embed(title = f'Виджет погоды для города {city}', description = answer, color = 0x428325) 
            embed.add_field(name = 'Температура:', value = f'Сейчас в твоём городе `{temp}°C`', inline = False)
            embed.add_field(name = 'Осадки:', value = f'Небо затянуто на `{clouds}%`, {cloud}', inline = False)
            embed.set_thumbnail(url = 'https://kindertravelguide.com/wp-content/uploads/2015/11/SUN-1200x1117.jpg')
            embed.set_footer(text = "supports by quantprod")
            await ctx.author.send(embed = embed)
    except:
        await ctx.send('Ты допустил ошибку в названии, либо, к сожалению, я пока что не знаю такого города :c\n')



#ПЕРЕВОДЧИК

language = ('`ru` - Русский, `en` - Английский, `ar` - Арабский, `zh` - Китайский, `it` - Итальянский, `ja` - Японский\n'
            '`zu` - Зулу, `yo` - Йоруба, `uk` - Украинский, `be` - Белорусский')

@Bot.command(aliases = ["переведи"])
async def translate(ctx, lang = None, to_lang = None, *, arg = None):
    try:
        if lang == '--Help' or lang == '--help':
            to_lang = None
            arg = None
            message = await ctx.send('**Список доступных языков на данный момент:** ///загружаю список///')
            await asyncio.sleep(2)
            await message.edit(content = f'**Список доступных языков на данный момент:** {language}')
            await asyncio.sleep(20)
            await ctx.message.delete()
            await message.delete()       
        else:
            translator = Translator(from_lang = str(lang), to_lang = str(to_lang))
            translation = translator.translate(str(arg))
            await ctx.send(f'**Исходный текст:** `{arg}`\n'
                            '\n'
                           f'**Результат:** `{translation}`')
    except: 
        await ctx.send('Не смог перевести :с')


        
#МУЗЫКА С ЮТУБА

@Bot.command(aliases = ['p', 'PLAY'])
async def play(ctx, *, url, volume = 0.5):  #КОМАНДА ПРОИГРЫВАНИЯ ЗВУКОВОЙ ДОРОЖКИ
    try:
        global voice
        global print_volume

        channel = ctx.message.author.voice.channel	
        voice = get(Bot.voice_clients, guild = ctx.guild)	

        song_there = os.path.isfile('song.mp3')
        picture_there_webp = os.path.isfile('picture.webp')
        picture_there_jpg = os.path.isfile('picture.jpg')
        picture_there_jpeg = os.path.isfile('picture.jpeg')

        message = ctx.message
        await message.add_reaction('✅')

        try:
            if song_there:
                os.remove('song.mp3')
                print('[logs] Старая песня успешно удалена')
                if picture_there_webp:
                    os.remove('picture.webp')
                    print('[logs] Старое изображение .WEBP успешно удалено')
                else:
                    if picture_there_jpg:
                        os.remove('picture.jpg')
                        print('[logs] Старое изображение .JPG успешно удалено')
                    else:
                        if picture_there_jpeg:
                            os.remove('picture.jpeg')
                            print('[logs] Старое изображение .JPEG успешно удалено')
        except PermissionError as e: 
            print(f'[logs] Не удалось удалить файл. Причина: {e}')
            await ctx.send(f'Не смог удалить старую композицию по причине: `{e}`. Возможны ошибки в воспроизведении музыки. Обратитесь к `@Смотрящий`')

        voice = get(Bot.voice_clients, guild = ctx.guild)
        ydl_opts = {
            'format' : 'bestaudio/best',
            'noplaylist' : True, 
            'quiet' : False, #логи загрузки, если true, то их нет
            'verbose' : True,
            'no_warnings': True,
            'writethumbnail' : True,
            'ignore-errors' : True,
            'postprocessors' : [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '320'
            }],
        }


        correct_url = url[:8]
        correct_url1 = 'https://'
        correct_search = ':' + url

        if url == 'chill':
            url = 'https://www.youtube.com/watch?v=Ote5aXaJJy8'
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:     
                print ('[logs] Начинаю загрузку музыки...')
                embed = discord.Embed(description = '**Оу май, жди)**')
                await ctx.send(embed = embed)
                print('[logs] Отправил сообщение в канал')
                ydl.download([url])
        else:
            if correct_url != correct_url1:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
                    embed = discord.Embed(description = f'**Ищу по запросу `{url}` и готовлю к воспроизведению твой трек...**')
                    message1 = await ctx.send(embed = embed)
                    url = 'ytsearch' + correct_search
                    print('[logs] Отправил сообщение в канал')
                    print('[logs] Начинаю загрузку и подготовку музыки...')
                    ydl.download([url])
                    await message1.delete()
            else:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
                    embed = discord.Embed(description = '**Жди - скачиваю и готовлю к воспроизведению твой трек...**')
                    message1 = await ctx.send(embed = embed)
                    print('[logs] Отправил сообщение в канал')
                    print('[logs] Начинаю загрузку и подготовку музыки...')
                    ydl.download([url])
                    await message1.delete()

        if correct_url == correct_url1: 
            for file in os.listdir('./'):
                if file.endswith('.mp3'):
                    name = file  
                    os.rename(file, 'song.mp3')
            nname = name.rsplit('-', maxsplit = 1)
            message = await ctx.send(f'Скачал: **{nname[0]}**, ожидайте подключения бота!')
            await asyncio.sleep(3.5) 
            
        elif correct_url != correct_url1:
            for file in os.listdir('./'):
                if file.endswith('.mp3'):
                    name = file
                    os.rename(file, 'song.mp3')
            nname = name.rsplit('-', maxsplit = 1)
            message = await ctx.send(f'Нашёл и скачал: **{nname[0]}**, ожидайте подключения бота!')
            await asyncio.sleep(3.5)  

        if voice and voice.is_connected():
            await voice.disconnect()
            await voice.move_to(channel)
            if voice and voice.is_playing() or not voice.is_playing():
                await voice.disconnect()	
                voice = await channel.connect()	
        else:	
            voice = await channel.connect()

        for file in os.listdir('./'):
            if file.endswith('.webp'):
                name = file
                os.rename(file, 'picture.webp')
                await ctx.send(file = discord.File('picture.webp'))
            elif file.endswith('.jpg'):
                name = file
                os.rename(file, 'picture.jpg')
                await ctx.send(file = discord.File('picture.jpg'))
            elif file.endswith('.jpeg'):
                name = file
                os.rename(file, 'picture.jpeg')
                await ctx.send(file = discord.File('picture.jpeg'))

        print('[logs] Подключился к каналу')
        print('[logs] Воспроизвожу музыку...')

        voice.play(discord.FFmpegPCMAudio('song.mp3'), after = None)
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = volume
        print_volume = str(volume * 100)[:2]

        if voice and voice.is_playing():  
            await message.edit(content = f'__Сейчас играет:__ **«{nname[0]}»**. \nСтандартная громкость: `{print_volume}%`. \nИзменить ты её можешь, прописав `/volume [громкость]`')
        else:
            await message.edit(content = f'__Возникла ошибка с воспроизведением:__ **{nname[0]}**')
        await Bot.join_voice_channel(channel)

        while voice and voice.is_playing(): 
            await asyncio.sleep(1)
        else:
            while voice and voice.is_connected():
                if voice and not voice.is_playing():
                    if song_there:
                        os.remove('song.mp3')
                        print('[logs] Старая песня успешно удалена')
                        if picture_there_webp:
                            os.remove('picture.webp')
                            print('[logs] Старое изображение .WEBP успешно удалено')
                        else:
                            if picture_there_jpg:
                                os.remove('picture.jpg')
                                print('[logs] Старое изображение .JPG успешно удалено')
                            else:
                                if picture_there_jpeg:
                                    os.remove('picture.jpeg')
                                    print('[logs] Старое изображение .JPEG успешно удалено')
                    await voice.disconnect()
                else:
                    await asyncio.sleep(60)

    except Exception as e:
        e = str(e)[:5]
        if e == 'query':  
            await ctx.send('Слишком частые запросы по одной и той же песне. Может послушаем что-нибудь другое?.')
        else:
            print(e)

@Bot.command()
async def tts_bot(ctx, *, text = None):
    try:
        global voice

        channel = ctx.message.author.voice.channel	
        voice = get(Bot.voice_clients, guild = ctx.guild)	

        song_there = os.path.isfile('audio.mp3')
        message = ctx.message
        await message.add_reaction('✅')

        if song_there:
            os.remove('audio.mp3')
            print('[logs] Какая-то штука успешно удалена')

        audio = "audio.mp3"
        language = "ru"
        sp = gTTS(text = text, lang = language, slow = False)
        sp.save(audio)

        if voice and voice.is_connected():
            await voice.disconnect()
            await voice.move_to(channel)
            if voice and voice.is_playing() or not voice.is_playing():
                await voice.disconnect()	
                voice = await channel.connect()	
        else:	
            voice = await channel.connect()

        print('[logs] Подключился к каналу')
        print('[logs] Воспроизвожу музыку...')

        voice.play(discord.FFmpegPCMAudio('audio.mp3'), after = None)

    except:
        await ctx.send('Oops, но ты не подключён к голосовому каналу!')

@Bot.command(aliases = ['l', 'LEAVE'])
async def leave(ctx): 
    voice = get(Bot.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        song_there = os.path.isfile('song.mp3')
        picture_there_webp = os.path.isfile('picture.webp')
        picture_there_jpg = os.path.isfile('picture.jpg')
        picture_there_jpeg = os.path.isfile('picture.jpeg')
        try:
            if song_there:
                os.remove('song.mp3')
                print('[logs] Старая песня успешно удалена')
                if picture_there_webp:
                    os.remove('picture.webp')
                    print('[logs] Старое изображение .WEBP успешно удалено')
                else:
                    if picture_there_jpg:
                        os.remove('picture.jpg')
                        print('[logs] Старое изображение .JPG успешно удалено')
                    else:
                        if picture_there_jpeg:
                            os.remove('picture.jpeg')
                            print('[logs] Старое изображение .JPEG успешно удалено')
        except PermissionError: 
            print('[logs] Не удалось удалить файлы. Неизвестная причина...')

        await voice.disconnect()
        message = ctx.message
        await message.add_reaction('✅')

@Bot.command()
async def volume(ctx, *, volume: int):
    author = ctx.message.author
    ctx.voice_client.source.volume = volume / 100
    message = await ctx.send(f"{author.mention}, громкость установлена на {volume}%")
    await asyncio.sleep(5)
    await ctx.message.delete()
    await message.delete()
 
@Bot.command()
async def pause(ctx):
    voice = get(Bot.voice_clients, guild = ctx.guild)
    if voice and voice.is_playing():
        voice.pause()
        message = ctx.message
        await message.add_reaction('👌')
    else: 
        await ctx.send('Приостанавливать нечего!')

@Bot.command()
async def resume(ctx):
    voice = get(Bot.voice_clients, guild = ctx.guild)
    if voice and not voice.is_playing():
        voice.resume()
        message = ctx.message
        await message.add_reaction('👌')
    else:
        await ctx.send('Музыка уже играет!')

@Bot.command()
async def stop(ctx):
    song_there = os.path.isfile('song.mp3')
    picture_there_webp = os.path.isfile('picture.webp')
    picture_there_jpg = os.path.isfile('picture.jpg')
    picture_there_jpeg = os.path.isfile('picture.jpeg')

    message = ctx.message
    await message.add_reaction('👌')
    await ctx.voice_client.disconnect()
    if song_there:
        os.remove('song.mp3')
        print('[logs] Старая песня успешно удалена')
        if picture_there_webp:
            os.remove('picture.webp')
            print('[logs] Старое изображение .WEBP успешно удалено')
        else:
            if picture_there_jpg:
                os.remove('picture.jpg')
                print('[logs] Старое изображение .JPG успешно удалено')
            else:
                if picture_there_jpeg:
                    os.remove('picture.jpeg')
                    print('[logs] Старое изображение .JPEG успешно удалено')



#ДОБАВЛЕНИЕ (ОБНОВЛЕНИЕ) ПАКЕТОВ ЧЕРЕЗ БОТА СРАЗУ В ПРОЕКТ

@Bot.command(aliases = ['/', 'upgrade'])
@commands.has_any_role("admin", "Смотрящий")
async def install_bot(ctx, *, commands: str):
    import os
    command = commands
    error = os.system(command)
    await ctx.send(f'Закончил с ошибкой `{error}`')

    

#РАНДОМАЙЗЕР СЛУЧАЙНЫХ ЧИСЕЛ

@Bot.command(aliases = ['random'])
async def random_command(ctx, random1: int, random2: int):
    random_name = random.randint(random1, random2)
    await ctx.send(f'Твоё случайное число: `{random_name}`')

@Bot.command(aliases = ['решка', 'орёл', 'РЕШКА', 'ОРЁЛ', 'орёл или решка?', 'монета', 'money', 'монетка'])
async def heads_tails(ctx):
    random_tails_heads = random.randint(0, 1)
    if random_tails_heads == 1:
        await ctx.send('Тебе выпала `решка`!')
    else:
        await ctx.send('Тебе выпал `орёл`!')
        
        
                 
#ПОМОЩЬ USER

@Bot.command(aliases = ['h', 'HELP'])
async def help(ctx):
    await ctx.message.delete()
    author = ctx.message.author
    embed1 = discord.Embed(title = 'Помощь, страница 1', description = f'Йо, {author.mention}! Держи список команд:\n'
                        '\n'
                        '1) `/covid [страна_на_английском]` - последние новости о *covid19* как в России, так и в мире.\n'
                        '\n'
                        '2) `/spotify [@пользователь]` - узнай, что слушает юзер в данный момент, введя лишь одну команду.\n'
                        '*сокращения/синонимы*: `/spot`, `/s`;\n'
                        '\n'
                        '3) `/author` - команда разработчиков этого бота;\n'
                        '\n'
                        '4) `/math [первое_число] [второе_число]` - посчитает Ваши числа.\n'
                        '**ВНИМАНИЕ! Числа нужно вводить ЧЕРЕЗ пробел:**\n'
                        '__ввели__ `/math 3 4`, __вывод дал Embed с операциями__;\n'
                        '\n'
                        '5) `/nsfw` - строго 18+ контент)\n'
                        '*сокращения/синонимы*: `/ns`, `/порево`, `/прон`;\n'
                        '\n'
                        '6) `/weather [город]` - погода в ведённом городе.\n'
                        '*сокращения/синонимы*: `/погода`;\n'
                        '\n'
                        '7) `/tts_bot [текст]` - бот произнесёт ваш текст. __Для использования__ - \n'
                        'подключитесь к голосовому чату'
                        )
    embed2 = discord.Embed(title = 'Помощь, cтраница 2', description =
                        '1) `/length [сообщение]` - узнать длину нужного сообщения.\n'
                        '\n'
                        '2) `/pizdec` - не, ну это бан!\n'
                        '*сокращения/синонимы*: `/pzdc`;\n'
                        '\n'
                        '3) `/avatar [@пользователь]` - аватарка пользователя.\n'
                        '*сокращения/синонимы*: `/ava`;\n'
                        '\n'
                        '4) `/say [ваш_текст]` - бот повторит за вами всё то, что вы ему напишете.\n'
                        '*сокращения/синонимы*: `/repeat`;\n'
                        '\n'
                        '5) `/hentai` - ну тут сами понимаете что :D\n'
                        '*сокращения/синонимы*: `/hent`;\n'
                        '\n'
                        '6) `/монетка` - бот подбросит монетку и выдаст либо орла, либо решку.\n'
                        '*сокращения/синонимы*: `/монета`, `/орёл`, `/решка` (и куча других, мне лень их вписывать);\n'
                        '\n'
                        '7) `/translate [исходный_язык] [нужный_язык] [текст]` - переводчик с исходного языка на нужный и наоборот.\n'
                        '*сокращения/синонимы*: `/переведи`,\n'
                        'Пример: `/translate ru en здравствуйте`,\n'
                        'Список доступных языков можно посмотреть через `/translate --help`;'
                        )
    embed3 = discord.Embed(title = 'Помощь, страница 3', description = 
                        '1) `/hello` - ну-ка быстро посмотри :)\n'
                        '\n'
                        '2) `/info [@пользователь]` - узнай дату входа пользователя на сервер!\n'
                        '\n'
                        '3) `/message [@пользователь] [текст_сообщения]` - отправка сообщения любому юзеру с помощью бота;\n'
                        '\n'
                        '4) `/ping` - проверка скорости реакции бота;\n'
                        '\n'
                        '5) `/sanq` - команда благодарности боту.\n'
                        '*сокращения/синонимы*: `/спасибо`, `/thx`, `/пасибо`, `/пасиба`, `/спс`;\n'
                        '\n'
                        '6) `/random [первое_число] [второе_число]` - рандомайзер двух целых чисел;\n'
                        '\n'
                        '7) `/upper [текст]` - выведет Вам `ВоТ ТаКоЙ ВоТ ТеКсТ`;'
                        )
    embed4 = discord.Embed(title = 'Помощь, страница 4', description = 
                        '1) `/play [ссылка_на_видео_из_ютуб]` - проигрывание звуковой дорожки из видео\n'
                        '*сокращения/синонимы*: `/p`;\n'
                        '\n'
                        '2) `/volume [громкость]` - устаналивает нужную громкость;\n'
                        '\n'
                        '3) `/leave` - кикает бота с гс канала, для использования, Вы должны быть в канале с ботом.\n'
                        '*сокращения/синонимы*: `/l`;\n'
                        '\n'
                        '4) `/stop` - ну вы поняли, короче говоря :)\n'
                        '\n'
                        '5) `/pause` - пауза текущей песни;\n'
                        '\n'
                        '6) `/resume` - возобновление текущей песни;\n'
                        '\n'
                        '7) `/time` - время в трёх основных городах планеты.\n'
                        )
    embed5 = discord.Embed(title = 'Помощь, страница 4, команды в стадии разработки', description = 
                        '*Увы, но пока таких команд нет, ожидайте выходов новых обновлений бота*')
    embeds = [embed1, embed2, embed3, embed4, embed5]
    message = await ctx.send(embed = embed1)
    page = pag(Bot, message, only = ctx.author, use_more = False, timeout = 3*60, embeds = embeds)
    await page.start()
    await asyncio.sleep(10)
    await message.delete()
    

    
#ПОМОЩЬ ADMIN

@Bot.command(aliases = ['h_a', 'HELP_ADM'])
@commands.has_any_role("admin", "Смотрящий", "elite", "dmoder", "moder")
async def help_adm(ctx):
    await ctx.message.delete()
    author = ctx.message.author
    embed = discord.Embed(title = 'Команды для администрации и высшей инстанции в том числе', description = 
                        f'Привет, {author.mention}! Вот список команд, доступных тебе:\n'
                        'Все команды юзеров, плюс команды администрации, такие как:\n'
                        '\n'
                        '1) `/clear [количество сообщений]` - очистка канала.\n'
                        '*сокращения/синонимы*: `/c`;\n'
                        '\n'
                        '2) `/clear_member [@пользователь]` - очистка сообщений конкретного пользователя.\n'
                        '*сокращения/синонимы*: `/c_m`;\n'
                        '\n'
                        '3) `/kick [@пользователь] [причина_выдачи]` - кик пользователя.\n'
                        '*сокращения/синонимы*: `/k`;\n'
                        '\n'
                        '4) `/court [@пользователь] [время] [единицы_измерения*] [причина_выдачи]` - выдача роли подсудимого;\n'
                        '\n'
                        '5) `/tempban [@пользователь] [время] [единицы_измерения*] [причина_выдачи]` - временный бан пользователя.\n'
                        '*сокращения/синонимы*: `/tb`;\n'
                        '\n'
                        '6) `/ban [@пользователь] [причина_выдачи] [суд (был/не был)]` - пермабан.\n'
                        '*сокращения/синонимы*: `/b`;\n'
                        '\n'
                        '7) `/mute [@пользователь] [время] [единицы_измерения*] [причина_выдачи]` - мут пользователя.\n'
                        '*сокращения/синонимы*: `/m`;\n'
                        '\n'
                        '8) `/say_invite [сообщение]` - объявление об ивенте с "галочкой" для участия;\n'
                        '\n'
                        '9) `/add_role [@пользователь] [роль_для_выдачи] [роль_для_снятия]` - автоматически выдаёт указанную роль нужному пользователю\n'
                        '\n'
                        '*допустимые `единицы_измерения`: `mi` - минуты, `h` - часы, `w` - недели;\n'
                        '\n'
                        '__Примеры для выполнения команд:__ `/tempban @не крысакрысакрыса 1 w 1.8`;\n'
                        'При выполнении вышестоящего примера в банлист пойдёт следующее: `[см. на "Фото #1"]`\n'
                        '\n'
                        'Также хотелось бы уточнить, что при выдаче ролей бот работает только с правильными\n'
                        'названиями ролей (`Vip`, `admin` и так далее), как пример - см `Фото #2`',
                        color = 0x428325)
    await ctx.author.send(embed = embed)
    await ctx.author.send('`Фото #1:`')
    await ctx.author.send('https://i.ibb.co/XWHvgwz/1.jpg')
    await ctx.author.send('`Фото #2:`')
    await ctx.author.send('https://i.ibb.co/qg5Z7rZ/1.jpg')
    await ctx.author.send('https://i.ibb.co/M9bwQr5/2.jpg')
    embed = discord.Embed(description = 'То есть мы можем увидеть, что команда не сработала, и пользователь так и остался сидеть с ролью `Vip`', color = 0x428325)
    embed.set_footer(text = "supports by quantprod")
    await ctx.author.send(embed = embed)

    
    
#ВоТ тАкИе ВоТ сТрОкИ

@Bot.command()
async def upper(ctx, *, text):
    s = str(text)
    r = ""
    for i, c in enumerate(s):
      r += c if i % 2 else c.upper()
    await ctx.message.delete()
    await ctx.send(f'`{r}`')


    
#ПРОВЕРКА ДОСТУПНОСТИ БОТА

@Bot.command()
@commands.has_any_role("admin")
async def check(ctx):
    await ctx.message.delete()
    await ctx.send(nowtime)

@Bot.command()
@commands.has_any_role("admin", "Смотрящий")
async def ping_bot(ctx, url, timesecond: int):
    try:
        url = str(url)
        number = 0
        message = await ctx.send('Запускаю проверку доступности сайта по твоим параметрам...')
        try:
            while True:
                delta1 = datetime.timedelta(hours = 3, minutes = 0)
                mesinf = datetime.datetime.now() + delta1
                nowtime1 = mesinf.strftime("%X")
                number += 1
                r = requests.get(url)
                r = str(r)[11:][:-2]
                await message.edit(content = f'- Получил ответ от сайта __{url}__ `[{r}]`\n'
                                            f'- Время последнего запроса: `{nowtime1}`\n'
                                            f'- Всего запросов было `{number}`')
                await asyncio.sleep(timesecond)
        except Exception as e:
            await ctx.send(e)
    except Exception as e:
        await ctx.send(e)
        


#СПАСИБО)

@Bot.command(aliases = ['спасибо', 'thx', 'пасибо', 'пасиба', 'спс'])
async def sanq(ctx):
    with open ('thx.txt', 'r') as file:
        lines = file.readlines()
    await ctx.send(random.choice(lines))
    message = ctx.message
    await message.add_reaction('💚')  
    
    

#РАНДОМНЫЙ ХЕНТАЙ (ОЙ)

@Bot.command(aliases = ['hent'])
async def hentai(ctx):
    with open ('hentai.txt', 'r') as file:
        lines = file.readlines()
    await ctx.send(random.choice(lines))
    


#РАНДОМНЫЕ ДЕВА44КИ

@Bot.command(aliases = ['ns', 'порево', 'прон'])
async def nsfw(ctx):
    with open ('nsfw.txt', 'r') as file:
        lines = file.readlines()
    await ctx.send(random.choice(lines))
    

        
#НЕ, НУ ЭТО БАН!

@Bot.command(aliases = ['pzdc', 'PIZDEC'])
async def pizdec(ctx):
    await ctx.message.delete()
    await ctx.send(':regional_indicator_p: '
                   ':regional_indicator_i: ' 
                   ':regional_indicator_z: ' 
                   ':regional_indicator_d: ' 
                   ':regional_indicator_e: ' 
                   ':regional_indicator_c: ')



#SPOTIFY, КТО ЧТО СЛУШАЕТ

@Bot.command(aliases = ['spot'])
async def spotify(ctx, user: discord.Member = None):
    try:
        user = user or ctx.author
        delta_msk = datetime.timedelta(hours = 3, minutes = 0)
        for activity in user.activities:
            if isinstance(activity, Spotify):
                time_current = activity.created_at + delta_msk #начало прослушивания песни
                time_start = activity.end + delta_msk 
                nowtime1 = time_current.strftime("`%H:%M по МСК`") #поправка по часовому поясу для time_current
                nowtime2 = time_start.strftime("`%H:%M по МСК`")

                artist_correct = activity.artist.rsplit(';')
                correct_lines = ','
                new_correct_artist = correct_lines.join(artist_correct)
                album_jpg = activity.album_cover_url
                
                embed = discord.Embed(color = 0x428325)
                embed.set_thumbnail(url = album_jpg)
                embed.add_field(name = 'Трек:', value = f'{user.mention} слушает **«{activity.title}»** `{str(activity.duration)[2:][:-7]}`', inline = False)
                embed.add_field(name = 'Исполнитель:', value = f'`{new_correct_artist}`', inline = False)
                embed.add_field(name = 'Начал(а) слушать в:', value = f'`{nowtime1}`', inline = False)
                embed.add_field(name = 'Песня закончится в:', value = f'`{nowtime2}`', inline = False)
                embed.set_footer(text = "supports by quantprod")
                message = await ctx.send(embed = embed)
                await asyncio.sleep(15)
                await message.delete()
                await ctx.message.delete()
    except Exception as e:
        await ctx.send(f'Возникла ошибка "{e}"')
       


#ТЕКУЩЕЕ ВРЕМЯ И ДАТА

@Bot.command(aliases = ["time", "время"])
async def time_bot(ctx):
    delta_msk = datetime.timedelta(hours = 3, minutes = 0)
    mesinf = ctx.message.created_at + delta_msk
    nowtime1 = mesinf.strftime("**Время:** `%X (UTC +3)`\n**Дата:** `%d.%m.%Y`")

    delta_ny = datetime.timedelta(hours = -4, minutes = 0)
    mesinf1 = ctx.message.created_at + delta_ny
    nowtime2 = mesinf1.strftime("**Время:** `%X (UTC −4)`\n**Дата:** `%d.%m.%Y`")

    delta_jp = datetime.timedelta(hours = 9, minutes = 0)
    mesinf2 = ctx.message.created_at + delta_jp
    nowtime3 = mesinf2.strftime("**Время:** `%X (UTC +9)`\n**Дата:** `%d.%m.%Y`")

    embed = discord.Embed(color = 0x428325)
    embed.set_thumbnail(url = "https://i.gifer.com/LUjT.gif")
    embed.add_field(name = 'Текущее время и дата в Москве :flag_ru:', value = nowtime1, inline = False)
    embed.add_field(name = 'Текущее время и дата в Нью-Йорке :flag_us:', value = nowtime2, inline = False)
    embed.add_field(name = 'Текущее время и дата в Токио :flag_jp:', value = nowtime3, inline = False)
    embed.set_footer(text = "supports by quantprod")
    await ctx.send(embed = embed)



#COVID-19 В РОССИИ И МИРЕ

@Bot.command(aliases = ['covid19', 'COVID', 'cov', 'COVID19'])
async def covid(ctx, country = None):
    message = await ctx.send('Собираю данные, пожалуйста, подождите...')
    covid = Covid(source = "worldometers")
    covid1 = Covid()                                 
    if country == None:
        await message.delete()
        world_cases = covid1.get_total_confirmed_cases()
        recovered = covid.get_total_recovered()
        active = covid.get_total_active_cases()
        deaths = covid.get_total_deaths()
        embed = discord.Embed(title = 'Информация о заболевших по всему миру', color = 0x428325) 
        embed.add_field(name = "Всего заболевших", value = f'`{world_cases}`', inline = False)
        embed.add_field(name = "Всего выздоровевших", value = f'`{recovered}`', inline = False)
        embed.add_field(name = "Из них болеют", value = f'`{active}`', inline = False)
        embed.add_field(name = "Скончались", value = f'`{deaths}`', inline = False)
        embed.set_thumbnail(url = 'https://media1.tenor.com/images/8aaa0776480217422941d94dfab2fad3/tenor.gif?itemid=16684233')
        embed.set_footer(text = "supports by quantprod | Берегите себя и своих близких 💚")
        await ctx.send(embed = embed)
    else:
        try:
            translator = Translator(from_lang = "ru", to_lang = "en")
            translation = translator.translate(country)
            morph = pymorphy2.MorphAnalyzer()
            counties = morph.parse(country)[0]
            gent = counties.inflect({'gent'})
            gent_new = gent.word
            gent_correct = gent_new.capitalize()
            await message.delete()
            country_cases = covid.get_status_by_country_name(translation)['new_cases']
            if country_cases == 0:
                country_cases = 'Статистика обновляется. Попробуйте заново в 12:00 по МСК'
                timeout = 10
            else:
                country_cases = '+' + str(country_cases)
                timeout = 60 * 3600
            confirmed_country_cases = covid.get_status_by_country_name(translation)['confirmed']
            deaths_country_cases = covid.get_status_by_country_name(translation)['deaths']
            embed = discord.Embed(title = 'Информация по отдельной стране', description = f'__Статистика для {gent_correct}__', color = 0x428325) 
            embed.add_field(name = "Новых случаев за сутки", value = f'`{country_cases}`', inline = False)
            embed.add_field(name = "Всего заболевших", value = f'`{confirmed_country_cases}`', inline = False)
            embed.add_field(name = "Скончались", value = f'`{deaths_country_cases}`', inline = False)
            embed.set_thumbnail(url = 'https://media1.tenor.com/images/8aaa0776480217422941d94dfab2fad3/tenor.gif?itemid=16684233')
            embed.set_footer(text = "supports by quantprod | Берегите себя и своих близких 💚")
            message1 = await ctx.send(embed = embed)
            await asyncio.sleep(timeout)
            await ctx.message.delete()
            await message1.delete() 
        except Exception as e:
            await ctx.send(f'Возникла ошибка {e}. Обратитесь к <@!394858317572472832>')



#NSFW-ИНФО (ПОПОЛНЕНИЕ)

@Bot.command(aliases = ['updatebases', 'base', 'bases'])
async def nsfw_info(ctx):
    with open('nsfw_version.txt', 'r') as f:
        for i in range(0):
            f.readline()
        x = f.readline()
    await ctx.send(x)



#ЬЕЬ-ПОПОЛНЕНИЕ  

@Bot.command(aliases = ['updatememes', 'base_memes'])
async def memes_info(ctx):
    with open('update_memes.txt', 'r') as f:
        for i in range(0):
            f.readline()
        x = f.readline()
    await ctx.send(x)

   
  
#ПАСХАЛОЧКА :)

@Bot.command(aliases = ['AUTHOR'])
async def author(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title = 'Авторы:', description = '**Разработчик:** https://vk.com/d.blinov79\n'
                                                            '**С подачи:** https://vk.com/code_authora_174',
                                                            color = 0x428325)
    embed.set_footer(text = "supports by quantprod")
    message = await ctx.send(embed = embed)
    await message.add_reaction('☝')

@Bot.command(aliases = ['git', 'GitHub'])
async def github(ctx):
    embed = discord.Embed(title = 'GitHub разработчика:', description = 'https://github.com/GRTUBORG/')
    await ctx.send(embed = embed)



#ИВЕНТЫ

@Bot.command()
@commands.has_any_role("admin", "Смотрящий", "Event manager")
async def say_invite(ctx, *, arg):  
    delta1 = datetime.timedelta(hours=3, minutes=0)
    mesinf = (ctx.message.created_at) + delta1
    nowtime1 = mesinf.strftime("%X")

    await ctx.message.delete()
    embed = discord.Embed(description = arg, color = 0x428325)
    embed.set_footer(text = f"supports by quantprod | Сегодня, в {nowtime1} по МСК")
    message = await ctx.send(embed = embed)
    await message.add_reaction('✅')

    
    
#ПОВТОРЕНИЕ СООБЩЕНИЯ ЮЗЕРА (SAY)    

@Bot.command()
async def say(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg)


 
#МАТЕМАТИКА (ПРОСТЫЕ ОПЕРАЦИИ)

@Bot.command(aliases = ['MATH']) 
async def math(ctx,  a:  int,  b:  int): 
    delta1 = datetime.timedelta(hours=3, minutes=0)
    mesinf = (ctx.message.created_at) + delta1
    nowtime1 = mesinf.strftime("%X")

    embed = discord.Embed(color = 0x428325)
    embed.add_field(name = "Сумма: ", value = a + b, inline = False)
    embed.add_field(name = "Разность: ", value = a - b, inline = False)
    embed.add_field(name = "Деление: ", value = a / b, inline = False)
    embed.add_field(name = "Умножение: ", value = a * b, inline = False)
    embed.set_footer(text = f"supports by quantprod | Сегодня, в {nowtime1} по МСК")
    await ctx.send(embed = embed)



#ИНФОРМАЦИЯ О ЮЗЕРЕ

@Bot.command(aliases = ['i', 'information', 'INFO', 'INFORMATION'])
async def info(ctx, member: discord.Member = None):
    delta1 = datetime.timedelta(hours = 3, minutes = 0)
    mesinf = ctx.message.created_at + delta1
    nowtime1 = mesinf.strftime("%X")

    avatar = member.avatar_url
    
    info1 = member.created_at + delta1
    info_format = info1.strftime('%d.%m.%Y @ %X по МСК')
    info2 = member.joined_at + delta1
    info1_format = info2.strftime('%d.%m.%Y @ %X по МСК')
    roles = [role.mention for role in member.roles[1:]]

    embed = discord.Embed(color = 0x428325)
    embed.set_author(name = f'Информация о {member.name}#{member.discriminator}', icon_url = avatar)
    embed.add_field(name = "Аккаунт создан: ", value = f'`{info_format}`', inline = False)
    embed.add_field(name = "Когда присоединился: ", value = f'`{info1_format}`', inline = False)
    embed.add_field(name = "Имя юзера и его тег: ", value = f'`{member.name}#{member.discriminator}`', inline = False)
    embed.add_field(name = "Никнейм на Dark Neon City: ", value = f'`{member.display_name}`', inline = False)
    embed.add_field(name = f"Роли [{len(member.roles) - 1}]: ", value = ' '.join(reversed(roles)), inline = False)
    embed.set_thumbnail(url = avatar)
    embed.set_footer(text = f"supports by quantprod | Сегодня, в {nowtime1} по МСК")
    await ctx.send(embed = embed)



#ПРИВЕТСТВИЕ

@Bot.command(aliases = ['HELLO'])
async def hello(ctx):
    delta1 = datetime.timedelta(hours = 3, minutes = 0)
    mesinf = ctx.message.created_at + delta1
    nowtime1 = mesinf.strftime("%X")
    
    await ctx.message.delete()
    author = ctx.message.author
    embed = discord.Embed(title = 'Dark Neon City', description = f'👋 Васап, {author.mention}! Рад видеть тебя на Dark Neon City!', color = 0x428325)
    embed.set_footer(text = f"supports by quantprod | Сегодня, в {nowtime1} по МСК")
    await ctx.send(embed = embed)



#УДАЛЕНИЕ СООБЩЕНИЙ

@Bot.command(aliases = ['c_m', 'CLEAR_MEMBER'])
@commands.has_any_role("admin", "Смотрящий", "elite")
async def clear_member(ctx, user: discord.Member, amount = 15):  #СООБЩЕНИЯ ПОЛЬЗОВАТЕЛЯ
    await ctx.message.delete()
    await ctx.channel.purge(limit = amount, check = lambda m: m.author == user)
    author = ctx.message.author
    message = await ctx.send(embed = discord.Embed(description = f'✅ {author.mention}, *удаление сообщений юзера прошло успешно!*', color = 0x428325))
    await asyncio.sleep(5)
    await message.delete()

@Bot.command(aliases = ['c', 'CLEAR'])
@commands.has_any_role("admin", "Смотрящий", "elite")
async def clear(ctx, amount = 30):  #ВООБЩЕ ВСЕ СООБЩЕНИЯ
    await ctx.message.delete()

    await ctx.channel.purge(limit = amount)
    author = ctx.message.author

    message = await ctx.send(embed = discord.Embed(description = f'✅ {author.mention}, *удаление сообщений прошло успешно!*', color = 0x428325))
    await asyncio.sleep(5)

    await message.delete()



#ВЫДАЧА РОЛЕЙ ЧЕРЕЗ БОТА

@Bot.command(aliases = ['remove_role'])
@commands.has_any_role("admin", "Смотрящий")
async def add_role(ctx, member: discord.Member, role = None, *, roles = None):
    delta1 = datetime.timedelta(hours = 3, minutes = 0)
    mesinf = ctx.message.created_at + delta1
    nowtime1 = mesinf.strftime("%X")

    await ctx.message.delete()

    channel = Bot.get_channel(526464840672346112) #логи

    author = ctx.message.author

    role_vip = discord.utils.get(ctx.guild.roles, name = "Vip")
    role_moder = discord.utils.get(ctx.guild.roles, name = "moder")
    role_dmoder = discord.utils.get(ctx.guild.roles, name = "dmoder")
    role_cyber = discord.utils.get(ctx.guild.roles, name = "Cyber")
    role_unit = discord.utils.get(ctx.guild.roles, name = "Unit")
    role_admin = discord.utils.get(ctx.guild.roles, name = "admin")

    if role == 'Vip':
        await member.add_roles(role_vip)

        if roles == 'Unit':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `Vip` **с роли** `Unit`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `Vip` на сервере Dark Neon City!**')
            await member.remove_roles(role_unit)
        elif roles == 'Cyber':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `Vip` **с роли** `Cyber`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `Vip` на сервере Dark Neon City!**')
            await member.remove_roles(role_cyber)
        elif roles == 'dmoder':
            await channel.send(f'**Пользователь** {author.mention} **понизил** `{member.name}#{member.discriminator}` **до роли** `Vip` **с роли** `dmoder`, **сегодня в** `{nowtime1}`.')
            await member.send('**Упс, но теперь ты `Vip` на сервере Dark Neon City!**')
            await member.remove_roles(role_dmoder)
        elif roles == 'moder':
            await channel.send(f'**Пользователь** {author.mention} **понизил** `{member.name}#{member.discriminator}` **до роли** `Vip` **с роли** `moder`, **сегодня в** `{nowtime1}`.')
            await member.send('**Упс, но теперь ты `Vip` на сервере Dark Neon City!**')
            await member.remove_roles(role_moder)
        elif roles == 'admin':
            await channel.send(f'**Пользователь** {author.mention} **понизил** `{member.name}#{member.discriminator}` **до роли** `Vip` **с роли** `admin`, **сегодня в** `{nowtime1}`.')
            await member.send('**Упс, но теперь ты `Vip` на сервере Dark Neon City!**')
            await member.remove_roles(role_admin)


    elif role == 'admin':
        await member.add_roles(role_admin)  

        if roles == 'Unit':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `admin` **с роли** `Unit`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `admin` на сервере Dark Neon City!**')
            await member.remove_roles(role_unit)
        elif roles == 'Cyber':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `admin` **с роли** `Cyber`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `admin` на сервере Dark Neon City!**')
            await member.remove_roles(role_cyber)
        elif roles == 'dmoder':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `admin` **с роли** `dmoder`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `admin` на сервере Dark Neon City!**')
            await member.remove_roles(role_dmoder)   
        elif roles == 'Vip':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `admin` **с роли** `Vip`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `admin` на сервере Dark Neon City!**')
            await member.remove_roles(role_vip) 
        elif roles == 'moder':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `admin` **с роли** `moder`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `admin` на сервере Dark Neon City!**')
            await member.remove_roles(role_vip) 


    elif role == 'moder':
        await member.add_roles(role_moder)

        if roles == 'Unit':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `moder` **с роли** `Unit`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `moder` на сервере Dark Neon City!**')
            await member.remove_roles(role_unit)
        elif roles == 'Cyber':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `moder` **с роли** `Cyber`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `moder` на сервере Dark Neon City!**')
            await member.remove_roles(role_cyber)
        elif roles == 'dmoder':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `moder` **с роли** `dmoder`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `moder` на сервере Dark Neon City!**')
            await member.remove_roles(role_dmoder)   
        elif roles == 'Vip':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `moder` **с роли** `Vip`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `moder` на сервере Dark Neon City!**')
            await member.remove_roles(role_vip)
        elif roles == 'admin':
            await channel.send(f'**Пользователь** {author.mention} **понизил** `{member.name}#{member.discriminator}` **до роли** `moder` **с роли** `admin`, **сегодня в** `{nowtime1}`.')
            await member.send('**Упс, но теперь ты `moder` на сервере Dark Neon City!**')
            await member.remove_roles(role_admin)


    elif role == 'dmoder':
        await member.add_roles(role_dmoder)

        if roles == 'Unit':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `dmoder` **с роли** `Unit`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `dmoder` на сервере Dark Neon City!**')
            await member.remove_roles(role_unit)
        elif roles == 'Cyber':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `dmoder` **с роли** `Cyber`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `dmoder` на сервере Dark Neon City!**')
            await member.remove_roles(role_cyber)
        elif roles == 'moder':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `dmoder` **с роли** `moder`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `dmoder` на сервере Dark Neon City!**')
            await member.remove_roles(role_moder)
        elif roles == 'Vip':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `dmoder` **с роли** `Vip`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `dmoder` на сервере Dark Neon City!**')
            await member.remove_roles(role_vip)
        elif roles == 'admin':
            await channel.send(f'**Пользователь** {author.mention} **понизил** `{member.name}#{member.discriminator}` **до роли** `dmoder` **с роли** `admin`, **сегодня в** `{nowtime1}`.')
            await member.send('**Упс, но теперь ты `dmoder` на сервере Dark Neon City!**')
            await member.remove_roles(role_admin)


    elif role == 'Cyber':
        await member.add_roles(role_cyber)

        if roles == 'Unit':
            await channel.send(f'**Пользователь** {author.mention} **повысил** `{member.name}#{member.discriminator}` **до роли** `Cyber` **с роли** `Unit`, **сегодня в** `{nowtime1}`.')
            await member.send('**Поздравляю, теперь ты `Cyber` на сервере Dark Neon City!**')
            await member.remove_roles(role_unit)
        elif roles == 'moder':
            await channel.send(f'**Пользователь** {author.mention} **понизил** `{member.name}#{member.discriminator}` **до роли** `Cyber` **с роли** `moder`, **сегодня в** `{nowtime1}`.')
            await member.send('**Упс, но теперь ты `Cyber` на сервере Dark Neon City!**')
            await member.remove_roles(role_moder)
        elif roles == 'dmoder':
            await channel.send(f'**Пользователь** {author.mention} **понизил** `{member.name}#{member.discriminator}` **до роли** `Cyber` **с роли** `dmoder`, **сегодня в** `{nowtime1}`.')
            await member.send('**Упс, но теперь ты `Cyber` на сервере Dark Neon City!**')
            await member.remove_roles(role_dmoder)
        elif roles == 'Vip':
            await channel.send(f'**Пользователь** {author.mention} **понизил** `{member.name}#{member.discriminator}` **до роли** `Cyber` **с роли** `Vip`, **сегодня в** `{nowtime1}`.')
            await member.send('**Упс, но теперь ты `Cyber` на сервере Dark Neon City!**')
            await member.remove_roles(role_vip)
        elif roles == 'admin':
            await channel.send(f'**Пользователь** {author.mention} **понизил** `{member.name}#{member.discriminator}` **до роли** `Cyber` **с роли** `admin`, **сегодня в** `{nowtime1}`.')
            await member.send('**Упс, но теперь ты `Cyber` на сервере Dark Neon City!**')
            await member.remove_roles(role_admin)


    elif role == 'Unit':
        await member.add_roles(role_unit)

        if roles == 'Cyber':
            await channel.send(f'**Пользователь** {author.mention} **понизил** `{member.name}#{member.discriminator}` **до роли** `Unit` **с роли** `Cyber`, **сегодня в** `{nowtime1}`.')
            await member.send('**Упс, но теперь ты `Unit` на сервере Dark Neon City!**')
            await member.remove_roles(role_cyber)
        elif roles == 'moder':
            await channel.send(f'**Пользователь** {author.mention} **понизил** `{member.name}#{member.discriminator}` **до роли** `Unit` **с роли** `moder`, **сегодня в** `{nowtime1}`.')
            await member.send('**Упс, но теперь ты `Unit` на сервере Dark Neon City!**')
            await member.remove_roles(role_moder)
        elif roles == 'dmoder':
            await channel.send(f'**Пользователь** {author.mention} **понизил** `{member.name}#{member.discriminator}` **до роли** `Unit` **с роли** `dmoder`, **сегодня в** `{nowtime1}`.')
            await member.send('**Упс, но теперь ты `Unit` на сервере Dark Neon City!**')
            await member.remove_roles(role_dmoder)
        elif roles == 'Vip':
            await channel.send(f'**Пользователь** {author.mention} **понизил** `{member.name}#{member.discriminator}` **до роли** `Unit` **с роли** `Vip`, **сегодня в** `{nowtime1}`.')
            await member.send('**Упс, но теперь ты `Unit` на сервере Dark Neon City!**')
            await member.remove_roles(role_vip)
        elif roles == 'admin':
            await channel.send(f'**Пользователь** {author.mention} **понизил** `{member.name}#{member.discriminator}` **до роли** `Unit` **с роли** `admin`, **сегодня в** `{nowtime1}`.')
            await member.send('**Упс, но теперь ты `Unit` на сервере Dark Neon City!**')
            await member.remove_roles(role_admin)



#РОЛЬ ПОДСУДИМОГО

@Bot.command(aliases = ['COURT'])
@commands.has_any_role("admin", "Смотрящий", "elite", "dmoder", "moder")
async def court(ctx, member: discord.Member, duration: int, timecourt = None, *, reason = None):
    delta1 = datetime.timedelta(minutes = duration)
    mesinf = ctx.message.created_at + delta1

    channel = Bot.get_channel(526464840672346112) #логи

    author = ctx.message.author
    role = discord.utils.get(ctx.guild.roles, name = "urole0")

    await ctx.message.delete()

    if timecourt == 'mi':
        current_timeban = datetime.timedelta(minutes = duration)
        duration_current = mesinf + current_timeban
        duration_current1 = duration_current.strftime("`%d.%m.%Y @ %X по МСК`")

        await member.add_roles(role)
        embed = discord.Embed(description= f' Пользователь {author.mention} выдал `{member.name}#{member.discriminator}` роль подсудимого сроком до {duration_current1} по причине: `{reason}`', color = 0x428325)
        await ctx.send(embed = embed)

        await member.send(f'**Упс, ты что-то нарушил на сервере Dark Neon City** (`{reason}`)')
        await channel.send(f'{author.mention} **выдал роль подсудимого юзеру** `{member.name}#{member.discriminator}` **на срок до** `{duration_current1}`. **Причина:** `{reason}`.')

        await asyncio.sleep(duration * 60)

        await channel.send(f'**Упс, но по юзеру** {member.mention} **истёк срок дела, которое назначил** {author.mention}.')

        await member.remove_roles(role)
    


#АВАТАРКА

@Bot.command(aliases = ['ava', 'AVATAR'])
@commands.has_any_role("admin", "Смотрящий", "elite", "Vip")
async def avatar(ctx, *, user: discord.Member = None):
    delta1 = datetime.timedelta(hours = 3, minutes = 0)
    mesinf = ctx.message.created_at + delta1
    nowtime1 = mesinf.strftime("%X")

    userAvatarUrl = user.avatar_url
    embed = discord.Embed(description = f"Аватарка пользователя {user.mention}")
    embed.set_image(url = userAvatarUrl)
    embed.set_footer(text = f"supports by quantprod | Сегодня, в {nowtime1} по МСК")
    await ctx.send(embed = embed)



#ССЫЛКА-ПРИГЛАШЕНИЕ НА СЕРВЕР

@Bot.command()
async def invites(ctx):
    await ctx.send('https://discord.gg/rjMDwaB')



#БАН, МУТ ПОЛЬЗОВАТЕЛЯ И КИК ПОЛЬЗОВАТЕЛЯ

@Bot.command(aliases = ['k', 'KICK'])
@commands.has_any_role("admin", "Смотрящий", "elite")
async def kick(ctx, member: discord.Member, *, reason = None):  #КИК
    channel = Bot.get_channel(526464840672346112) #LOGS

    author = ctx.message.author
    await ctx.message.delete()

    await member.kick(reason = reason)
    embed = discord.Embed(description = f"Пользователь `{member.name}#{member.discriminator}` был успешно кикнут {author.mention} по причине: `{reason}`.", color = 0x428325)
    embed.set_footer(text = "supports by quantprod")
    await ctx.send(embed = embed)

    await channel.send(f'{author.mention} **кикнул пользователя** `{member.name}#{member.discriminator}` **по причине:** `{reason}`.')

@Bot.command(aliases = ['tb', 'TEMPBAN'])
@commands.has_any_role("admin", "Смотрящий", "elite", "moder")
async def tempban(ctx, user: discord.User, duration: int, timeban = None, *, reason = None):  #ВРЕМЕННЫЙ БАН
    delta1 = datetime.timedelta(hours=3, minutes=0)
    mesinf = ctx.message.created_at + delta1

    channel = Bot.get_channel(526464840672346112) #LOGS
    author = ctx.message.author
    await ctx.message.delete()

    if timeban == 'h':
        current_timeban = datetime.timedelta(hours = duration)
        duration_current = mesinf + current_timeban
        duration_current1 = duration_current.strftime("`%d.%m.%Y @ %X по МСК`")

        await user.send(f'**Вы были забанены на Dark Neon City до** {duration_current1} **за нарушение** `{reason}`**. Вот приглашение:** https://discord.gg/rjMDwaB\n'
        '**Вступи, когда пройдёт бан)**\n'
        '**По вопросам разбана писать** *•Satoemari•#0001*')

        await ctx.guild.ban(user, reason = reason)
        embed = discord.Embed(description = f"{author.mention} забанил `@{user.name}#{user.discriminator}` сроком на `{duration}{timeban}`", color = 0x428325)
        embed.add_field(name = "Разбан будет:", value = duration_current1)
        embed.add_field(name = "По причине:", value = f'`{reason}`')
        embed.set_footer(text = "supports by quantprod")
        await ctx.send(embed = embed)
        await channel.send(f'{author.mention} выдал временный бан `{user.name}#{user.discriminator}` на {duration}{timeban} по причине `{reason}` .')

        await asyncio.sleep(duration * 3600)
        await ctx.guild.unban(user)

    elif timeban == 'mi':
        current_timeban = datetime.timedelta(minutes = duration)
        duration_current = mesinf + current_timeban
        duration_current1 = duration_current.strftime("`%d.%m.%Y @ %X по МСК`")

        await user.send(f'**Вы были забанены на Dark Neon City до** {duration_current1} **за нарушение** `{reason}`**. Вот приглашение:** https://discord.gg/rjMDwaB\n'
        '**Вступи, когда пройдёт бан)**\n'
        '**По вопросам разбана писать** *•Satoemari•#0001*')

        await ctx.guild.ban(user, reason = reason)
        embed = discord.Embed(description = f"{author.mention} забанил `@{user.name}#{user.discriminator}` сроком на `{duration}{timeban}`", color = 0x428325)
        embed.add_field(name = "Разбан будет:", value = duration_current1)
        embed.add_field(name = "По причине:", value = f'`{reason}`')
        embed.set_footer(text = "supports by quantprod")
        await ctx.send(embed = embed)
        await channel.send(f'{author.mention} выдал временный бан `{user.name}#{user.discriminator}` на {duration}{timeban} по причине `{reason}` .')

        await asyncio.sleep(duration * 60)
        await ctx.guild.unban(user)

    elif timeban == 'w':    
        current_timeban = datetime.timedelta(weeks = duration)
        duration_current = mesinf + current_timeban
        duration_current1 = duration_current.strftime("`%d.%m.%Y @ %X по МСК`")

        await user.send(f'**Вы были забанены на Dark Neon City до** {duration_current1} **за нарушение** `{reason}`**. Вот приглашение:** https://discord.gg/rjMDwaB\n'
        '**Вступи, когда пройдёт бан)**\n'
        '**По вопросам разбана писать** *•Satoemari•#0001*')

        await ctx.guild.ban(user, reason = reason)
        embed = discord.Embed(description = f"{author.mention} забанил `@{user.name}#{user.discriminator}` сроком на `{duration}{timeban}`", color = 0x428325)
        embed.add_field(name = "Разбан будет:", value = duration_current1)
        embed.add_field(name = "По причине:", value = f'`{reason}`')
        embed.set_footer(text = "supports by quantprod")
        await ctx.send(embed = embed)
        await channel.send(f'{author.mention} выдал временный бан `{user.name}#{user.discriminator}` на {duration}{timeban} по причине `{reason}` .')

        await asyncio.sleep(duration * 10080)
        await ctx.guild.unban(user)
    
@tempban.error
async def tempban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Вы забыли указать аргумент!')

@Bot.command(aliases = ['b', 'BAN'])
@commands.has_any_role("admin", "Смотрящий", "elite")
async def ban(ctx, member: discord.Member, reason = None, *, court = None):  #ПЕРМАНЕНТНЫЙ БАН
    channel = Bot.get_channel(526464840672346112) #логи
    await member.send(f'**Увы, но ты был навсегда забанен на сервере Dark Neon City по причне:** {reason}')
    
    await member.ban(reason = reason)
    await ctx.message.delete()
    author = ctx.message.author

    if court == None:
        court = '`Причина суда не указана!`'
    
    embed = discord.Embed(description = f'{author.mention} выдал `{member.name}#{member.discriminator}` перманент', color= 0x428325)
    embed.add_field(name = "Причина:", value = f'`{reason}`', inline = False)
    embed.add_field(name = "Суд:", value = f'{court}', inline = False)
    embed.set_footer(text = "supports by quantprod")
    await ctx.send(embed = embed)

    await channel.send(f'{author.mention} **выдал перманентный бан** `{member.name}#{member.discriminator}`. **Причина:** {reason}, **суд:** {court}')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Вы забыли указать аргумент!')

@Bot.command(aliases = ['m', 'MUTE'])
@commands.has_any_role("admin", "Смотрящий", "elite", "dmoder", "moder")
async def mute(ctx, member: discord.Member, duration: int, timemute = None, *, reason = None):  #МУТ
    try:
        delta1 = datetime.timedelta(hours = 3, minutes = 0)
        mesinf = ctx.message.created_at + delta1

        author = ctx.message.author

        channel = Bot.get_channel(526464840672346112) #логи

        if timemute == 'mi':
            current_timeban = datetime.timedelta(minutes = duration)
            duration_current = mesinf + current_timeban
            duration_current1 = duration_current.strftime("`%d.%m.%Y @ %X по МСК`")
            
            role = discord.utils.get(ctx.guild.roles, name = "mute")
            await ctx.message.delete()
            await member.add_roles(role)
            
            await channel.send(f'{author.mention} **выдал мут** {member.mention} **по причине**: `{reason}`. **Время:** {duration}{timemute}')
            embed = discord.Embed(description= f'*Пользователь {member.mention} был успешно замучен!*', color = 0x428325)
            await ctx.send(embed = embed)
            await member.send(f'**Ты был замучен на сервере Dark Neon City до** `{duration_current1}` по причине `{reason}`')

            await asyncio.sleep(duration * 60)
            await member.remove_roles(role)

            await ctx.send(f'{member.mention}')
            embed = discord.Embed(description= f'*Пользователь {member.mention} был успешно размучен*', color = 0x428325)
            await ctx.send(embed = embed)

        elif timemute == 'h':    
            current_timeban = datetime.timedelta(hours = duration)
            duration_current = mesinf + current_timeban
            duration_current1 = duration_current.strftime("`%d.%m.%Y @ %X по МСК`")
            
            role = discord.utils.get(ctx.guild.roles, name = "mute")
            await ctx.message.delete()
            await member.add_roles(role)
            
            await channel.send(f'{author.mention} **выдал мут** {member.mention} **по причине**: `{reason}`. **Время:** {duration}{timemute}')
            embed = discord.Embed(description= f'*Пользователь {member.mention} был успешно замучен!*', color = 0x428325)
            await ctx.send(embed = embed)
            await member.send(f'**Ты был замучен на сервере Dark Neon City до** `{duration_current1}` по причине `{reason}`')

            await asyncio.sleep(duration * 3600)
            await member.remove_roles(role)

            await ctx.send(f'{member.mention}')
            embed = discord.Embed(description= f'*Пользователь {member.mention} был успешно размучен*', color = 0x428325)
            await ctx.send(embed = embed)
    except Exception as e:
        await ctx.send(f'Возникла ошибка: `{e}`! Обратитесь к <@!394858317572472832>')

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('`Внимание, указан несуществующий юзер!`')



#УЗНАТЬ ДЛИНУ СТРОКИ (СООБЩЕНИЯ)

@Bot.command() 
async def length(ctx): 
    embed = discord.Embed(color = 0x428325)
    embed.add_field(name = "Длина твоего сообщения:", value = '{}'.format(len(ctx.message.content.replace(" ", "")) - 7))
    embed.set_footer(text = "supports by quantprod")
    await ctx.send(embed = embed)


    
#ОТПРАВКА ЛИЧНЫХ СООБЩЕНИЙ

@Bot.command()
async def message(ctx, member: discord.Member, *, arg):
    await ctx.message.delete()
    author = ctx.message.author
    await member.send(f'**Тебе сообщение с сервера Dark Neon City от** {author.mention}\n{arg}')



#ПИНГ

@Bot.command()
async def ping(ctx):
    ping_ = Bot.latency
    ping = round(ping_ * 1000)
    embed = discord.Embed(title ='Pong!', description = f"Твой пинг: `{ping}ms`", color = 0x428325)
    embed.set_footer(text = "supports by quantprod")
    message = await ctx.send(embed = embed)
    await message.add_reaction('👌')

    

#СТАРТ БОТА

token = os.environ.get('bot_token')
Bot.run(str(token))
