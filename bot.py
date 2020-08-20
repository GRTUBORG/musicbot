import discord
import asyncio
import os
import random
import youtube_dl
import json
import requests
import typing

from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from Cybernator import Paginator as pag
from discord import Spotify


#ссылка на него же - яндекс.диск: https://yadi.sk/d/osZvfRlApkFIGA


players = {}


Bot = commands.Bot(command_prefix = "/")
Bot.remove_command('help')
bad_words = ['сервер говно', 'бот говно', 'админы говно', 'satoemari лох', 'крыса лох', 'пидорский сервер', 'администрация говно', 'dnc говно', 'дно сервер', 'вы все лохи']



#работает ли бот?

@Bot.event
async def on_ready():
    await Bot.change_presence(activity= discord.Activity(type= discord.ActivityType.watching, name= "за Dark Neon City 👀"))
    print("Бот в онлайне! Радуйся!")



#обработчик ошибок

@Bot.event
async def on_command_error(ctx, error):
    pass

@Bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        author = ctx.message.author
        embed=discord.Embed(color = 0x4ace40)
        embed.add_field(name= 'Ошибка выполнения команды!', value= f':x: *Внимание, {author.mention}! Данной команды __не существует__, либо у Вас __нет прав__ на её использование!*')
        embed.set_footer(text="supports by quantprod")
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
        emb = discord.Embed(title="Замечено оскорбление!", description= f'Прошу дать по попе {author.mention}', color=0x4ace40)
        message = await channel.send(embed=emb)
     
#spootify, кто что слушает

@Bot.command(aliases=['spot', 's'])
async def spotify(ctx, user: discord.Member=None):
    user = user or ctx.author
    for activity in user.activities:
        if isinstance(activity, Spotify):
            await ctx.send(f"{user} слушает {activity.title}, by {activity.artist}")

#актуальная версия бота

@Bot.command(aliases=['v'])
@commands.has_any_role("admin", "Смотрящий", "elite")
async def version(ctx):
    emb = discord.Embed(title="Актуальная версия бота", description= '__Апдейт был 19.08.2020 до v. 2.4__. \n' 'Исправлен вывод команды `/help`. Теперь она представлена как некая "книга". \n **Посмотрите!**', color=0x4ace40)
    await ctx.send(embed=emb)



#музыка с ютуба

@Bot.command(aliases=['p'])
async def play(ctx, url):
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove('song.mp3')
            print('[logs] Старый файл успешно удалён')
    except PermissionError:
        print('[logs] Не удалось удалить файл') 
    await ctx.send('Минуточку ожидания')
    voice = get(Bot.voice_clients, guild = ctx.guild)
    ydl_opts = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192'
        }],
    }  
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print ('[logs] Начинаю загрузку музыки...')
        ydl.download([url])
    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print(f'[logs] Создаю новое название файлу {file}')
            os.rename(file, 'song.mp3')
    
    voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: print(f'[logs] {name}, музыка закончила своё проигрывание'))
    
    nname = name.rsplit("-", 2)
    await ctx.send(f"We play: {nname[0]}")
    print("playing\n")
    
@Bot.command(aliases=['j'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(Bot.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'Я присоединился к {channel}')
    await Bot.join_voice_channel(channel)
        
@Bot.command(aliases=['l'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(Bot.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        voice = await channel.connect()
        await ctx.send(f'Я отключился от {channel}')
        
        
        
#помощь user

@Bot.command(aliases=['h'])
async def help(ctx):
    author = ctx.message.author
    channel1 = Bot.get_channel(526099119874375710)
    embed1= discord.Embed(title= 'Помощь, страница 1', description= f'Йо, {author.mention}! Держи список команд:\n'
                        '\n'
                        '`/author` - команда разработчиков этого бота;\n'
                        '`/github` - GitHub главного разработчика бота;\n'
                        '`/math [первое число] [второе число]` - посчитает Ваши числа. \n'
                        '**ВНИМАНИЕ! Числа нужно вводить ЧЕРЕЗ пробел:**\n'
                        '__ввели__ `/math 3 4`, __вывод дал Embed с операциями__;\n'
                        )
    embed2= discord.Embed(title= 'Помощь, cтраница 2', description=
    '`/length [строка]` - узнать длину строки;\n'
    '`/pizdec` - не, ну это бан!\n'
                        '`/avatar [@пользователь]` - аватарка пользователя;\n'
                        '`/say [ваш текст]` - бот повторит за вами всё то, что вы ему напишете;\n'
                        )
    embed3= discord.Embed(title= 'Помощь, страница 3', description= 
    '`/hello` - ну-ка быстро посмотри :)\n'
                        '`/info [@пользователь]` - узнай регистрацию пользователя!;\n'
                        '`/message [@пользователь] [текст сообщения]` - отправка сообщения любому юзеру с помощью бота;\n'
                        '`/ping` - проверка скорости реакции бота;\n'
                        '\n'
                        f'И да, не забывай, что с правилами сервера ты можешь ознакомиться в {channel1.mention}')
    embeds= [embed1, embed2, embed3]
    message= await ctx.send(embed=  embed1)
    page = pag(Bot, message, only= ctx.author, use_more= False, timeout= 1*3600, embeds= embeds)
    await page.start()



#не, ну это бан!

@Bot.command(aliases=['pzdc'])
async def pizdec(ctx):
    await ctx.message.delete()
    await ctx.send(':regional_indicator_p: :regional_indicator_i: :regional_indicator_z: :regional_indicator_d: :regional_indicator_e: :regional_indicator_c:')



#пасхалочка :)

@Bot.command()
async def author(ctx):
    await ctx.message.delete()
    emb = discord.Embed(title=f'Авторы:',
                        description='**Разработчик:** https://vk.com/d.blinov79\n'
                        '**С подачи:** https://vk.com/code_authora_174',
                        color=0x4ace40)
    emb.set_footer(text="supports by quantprod")
    message = await ctx.send(embed=emb)
    await message.add_reaction('☝')

@Bot.command(aliases=['git', 'GitHub'])
async def github(ctx):
    embed=discord.Embed(color=0x4ace40, title= 'GitHub разработчика:')
    embed.set_image(url = 'https://i.ibb.co/j42cxmr/qr-code.png')
    await ctx.send(embed = embed)



#помощь admin

@Bot.command(aliases=['ha'])
@commands.has_any_role("admin", "Смотрящий", "elite", "dmoder", "moder")
async def help_adm(ctx):
    await ctx.message.delete()
    channel1 = Bot.get_channel(526099119874375710)
    author = ctx.message.author
    emb = discord.Embed(title='Команды для администрации', description= f'Привет, {author.mention}! Вот список команд, доступных тебе:\n'
    'Все команды юзеров, плюс команды администрации, такие как:\n'
    '\n'
    '`/clear [количество сообщений]` - очистка канала (полностью);\n'
    '`/say [сообщение, которое нужно повторить]` - "повторитель" всего и вся на свете;\n'
    '`/clear_member [@пользователь]` - очистка сообщений конкретного пользователя;\n'
    '`/kick [@пользователь]` - кик пользователя;\n'
    '`/court [@пользователь] [время в секундах]` - выдача роли подсудимого;\n'
    '`/tempban [@пользователь] [время в секундах] [причина]` - временный бан пользователя;\n'
    '`/ban [@пользователь] [причина]` - перма нафиг!\n'
    '`/mute [@пользователь] [время]` - мут пользователя \n'
    '\n'
    f'Кстати говоря, советую ознакомиться с правилами: {channel1.mention}', 
    color=0x4ace40)
    emb.set_footer(text="supports by quantprod")
    message = await ctx.author.send(embed=emb)



#попугайчик

@Bot.command(aliases=['repeat'])
async def say(ctx,  *, arg):
    await ctx.message.delete()
    await ctx.send(arg)



#математика (простые операции)

@Bot.command() 
async def math(ctx,  a:  int,  b:  int): 
    embed= discord.Embed(title= "Простая математика", color= 0x4ace40)
    embed.add_field(name= "Сумма: ", value= a + b, inline=False)
    embed.add_field(name= "Разность: ", value= a - b, inline=False)
    embed.add_field(name= "Деление: ", value= a / b, inline=False)
    embed.add_field(name= "Умножение: ", value= a * b, inline=False)
    embed.set_footer(text= "supports by quantprod")
    await ctx.send(embed= embed)
  


#информация о юзере

@Bot.command(aliases=['i', 'information'])
async def info(ctx, member: discord.Member):
    embed=discord.Embed(title= "Info", color=0x4ace40)
    embed.add_field(name= "❓ Когда присоединился: ", value= member.joined_at)
    embed.add_field(name= "❓ Имя юзера: ", value= member.display_name)
    embed.set_footer(text= "supports by quantprod")
    await ctx.send(embed= embed)



#приветствие

@Bot.command()
async def hello(ctx):
    await ctx.message.delete()
    author = ctx.message.author
    emb = discord.Embed(title= 'Dark Neon City', description= f'👋 Привет, {author.mention}! Рад видеть тебя на Dark Neon City!', color=0x4ace40)
    emb.set_footer(text= "supports by quantprod")
    message = await ctx.send(embed= emb)



#удаление сообщений

@Bot.command(aliases=['cm'])
@commands.has_any_role("admin", "Смотрящий", "elite")
async def clear_member(ctx, user: discord.Member, amount = 15):
    await ctx.message.delete()
    await ctx.channel.purge(limit = amount, check=lambda m: m.author==user)
    author = ctx.message.author
    await ctx.send(embed = discord.Embed(description = f'✅ {author.mention}, *удаление сообщений юзера прошло успешно!*', color=0x4ace40))

@Bot.command(aliases=['c'])
@commands.has_any_role("admin", "Смотрящий", "elite")
async def clear(ctx, amount = 30): 
    await ctx.message.delete()
    await ctx.channel.purge(limit = amount)
    author = ctx.message.author
    await ctx.send(embed = discord.Embed(description = f'✅ {author.mention}, *удаление сообщений прошло успешно!*', color=0x4ace40))



#выдача ролей

@Bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Unit') # САМА РОЛЬ КОТОРУЮ ВЫДАЕМ
    await member.add_roles(role) # ДОБАВЛЯЕМ РОЛЬ
    channel1 = Bot.get_channel(526099119874375710) #правила
    channel2 = Bot.get_channel(528281293306462248) #смскер
    channel3 = Bot.get_channel(687044254622941217) #info
    channel4 = Bot.get_channel(541231102333943832) #news
    channel5 = Bot.get_channel(741002854898073660) #доска-почёта
    channel6 = Bot.get_channel(733727409672683550) #предложения
    embed=discord.Embed(color=0x4ace40)
    embed.add_field(name="Приветственное сообщение", value="Добро пожаловать в Dark Neon City!\n"
    f"Перед тем, как пользоваться сервером, прочитай {channel1.mention}. Это обязательно, а то атата!)\n"
    '\n'
    f"Тебе дана роль `@Unit`, поэтому, пока что, тебе доступны не все функции сервера. Но ты можешь участвовать в ивентах, чтобы повысить свой ранг!\n"
    '\n'
    "Для тебя открыты все комнаты в доме unit'ов, выбирай любую которая не занята, зови друзей на сервер и наслаждайтесь общением благодаря качественной связи!\n"
    '\n'
    f"Chill'овая беседка - самое уютное место для общения на различные темы! Заглядывай туда, в {channel2.mention}, или же в войс-чат под ним!\n"
    '\n'
    f"На сервере, как ты заметил, присутствуют боты, информацию о них можешь найти в {channel3.mention}.\n"
    '\n'
    "По интересующим вопросам обращайся к `@Смотрящий`.\n"
    '\n'
    f"Не забывай следить за новостями {channel4.mention} и обновлениями правил {channel1.mention}. Будь активен на сервере и однажды появишься на {channel5.mention}!\n"
    '\n'
    f"Так же можешь подкинуть идеи в {channel6.mention}\n"
    '\n'
    "С наилучшими пожеланиями, администрация сервера!")
    embed.set_footer(text="supports by quantprod")
    await member.send(embed=embed)



#кик пользователя

@Bot.command(aliases=['k'])
@commands.has_any_role("admin", "Смотрящий", "elite")
async def kick(ctx, member: discord.Member, *, reason = None):
    channel = Bot.get_channel(526464840672346112) #логи
    author = ctx.message.author
    await ctx.message.delete()
    await member.kick(reason = reason)
    embed = discord.Embed(title= "Кик", description = f"✅ Пользователь {member.mention} был успешно кикнут пользователем {author.mention}", color=0x4ace40)
    embed.set_footer(text= "supports by quantprod")
    await ctx.send(embed= embed)
    await channel.send(f'{author.mention} **кикнул пользователя** {member.mention} **по причине:** {reason}.')



#роль подсудимого

@Bot.command()
@commands.has_any_role("admin", "Смотрящий", "elite", "dmoder", "moder")
async def court(ctx, member: discord.Member):
    channel = Bot.get_channel(526464840672346112) #логи
    author = ctx.message.author
    role = discord.utils.get(ctx.guild.roles, name="urole0")
    await ctx.message.delete()
    await member.add_roles(role)
    embed = discord.Embed(title= "Суд", description= f'✅ Пользователь {author.mention} выдал {member.mention} роль подсудимого! Кто-то скоро пойдёт на суд :)', color=0x4ace40)
    message = await ctx.send(embed= embed)
    await channel.send(f'{author.mention} **выдал роль подсудимого юзеру** {member.mention}.')



#аватарка

@Bot.command(aliases=['ava'])
async def avatar(ctx, *,  avamember: discord.Member):
    userAvatarUrl = avamember.avatar_url
    embed = discord.Embed(description= f"Аватарка пользователя {avamember.mention}", color=0x4ace40)
    embed.set_image(url = userAvatarUrl)
    await ctx.send(embed = embed)



#бан и мут пользователя

@Bot.command(aliases=['tb'])
@commands.has_any_role("admin", "Смотрящий", "elite", "dmoder", "moder")
async def tempban(ctx, user: discord.User, duration: int, *, reason= None):
    channel = Bot.get_channel(526464840672346112) #логи
    author = ctx.message.author
    await ctx.message.delete()
    await ctx.guild.ban(user)
    emb = discord.Embed(title= "Временный бан", description= f"{author.mention} забанил {user.mention}", color= 0x4ace40)
    emb.add_field(name= "Срок бана (в часах):", value= duration)
    emb.add_field(name= "По причине:", value= reason)
    emb.set_footer(text= "supports by quantprod")
    await ctx.send(embed= emb)
    await channel.send(f'{author.mention} **выдал временный бан** {user.mention}.')
    await asyncio.sleep(duration)
    await ctx.guild.unban(user)
    embed = discord.Embed(title= "Временный бан", description= f'Пользователь {user.mention} был выпущен из тюрьмы, просьба отправить ему приглашение на сервер (просто он инвалид и сам не может присоединиться)!\n'
      'https://discord.gg/rjMDwaB', color= 0x4ace40)
    embed.set_footer(text= "supports by quantprod")
    await ctx.send(embed= embed)

@tempban.error
async def tempban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Вы забыли указать аргумент!')

@Bot.command(aliases=['b'])
@commands.has_any_role("admin", "Смотрящий", "elite")
async def ban(ctx, member: discord.Member, *, reason= None):
    channel = Bot.get_channel(526464840672346112) #логи
    await member.ban(reason= reason)
    await ctx.message.delete()
    author = ctx.message.author
    emb = discord.Embed(description= f'{author.mention} выдал {member.mention} перманент', color=0x4ace40)
    emb.add_field(name= "Причина:", value= reason, inline = False)
    emb.add_field(name= "Суд:", value= "см. причину", inline = False)
    emb.set_footer(text= "supports by quantprod")
    await ctx.send(embed= emb)
    await channel.send(f'{author.mention} **выдал перманентный бан** {member.mention}. **Причина и суд:** {reason}')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Вы забыли указать аргумент!')

@Bot.command(aliases=['m'])
@commands.has_any_role("admin", "Смотрящий", "elite", "dmoder", "moder")
async def mute(ctx, member: discord.Member, duration: int):
    author = ctx.message.author
    channel = Bot.get_channel(526464840672346112) #логи
    role = discord.utils.get(ctx.guild.roles, name = "mute")
    await ctx.message.delete()
    await member.add_roles(role)
    await channel.send(f'{author.mention} **выдал мут** {member.mention}. **Время:** {duration} час')
    emb = discord.Embed(description= f'*Пользователь {member.mention} был успешно замучен!*', color=0x4ace40)
    await ctx.send(embed= emb)
    await asyncio.sleep(duration * 3600)
    await member.remove_roles(role)
    emb = discord.Embed(description= f'*Пользователь {member.mention} был успешно размучен! Напомните ему об этом :)*', color=0x4ace40)
    await ctx.send(embed= emb)

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Вы забыли указать аргумент!')



#узнать длину строки (сообщения)

@Bot.command(aliases=['len']) 
async def length(ctx): 
    embed= discord.Embed(color=0x4ace40)
    embed.add_field(name="Длина твоего сообщения вместе с командой равна:", value= '{}'.format(len(ctx.message.content)))
    embed.set_footer(text= "supports by quantprod")
    await ctx.send(embed= embed)


#отправка личных сообщений

@Bot.command()
async def message(ctx, member: discord.Member, *, arg):
    await ctx.message.delete()
    author = ctx.message.author
    emb = discord.Embed(title= 'Личное сообщение', description= f'*Тебе сообщение с сервера Dark Neon City от* {author.mention}: ' + arg, color=0x4ace40)
    emb.set_footer(text="supports by quantprod")
    message = await member.send(embed= emb)



#коннект к каналу



#пинг (а может и нет)

@Bot.command()
async def ping(ctx: commands.Context):
    author = ctx.message.author
    emb = discord.Embed(title='Pong!', description= f'{author.mention} ''`{0}`'.format(round(Bot.latency, 1)), color=0x4ace40) 
    emb.set_footer(text="supports by quantprod")
    message = await ctx.send(embed=emb)
    await message.add_reaction('👌')



#старт бота

 
token = os.environ.get('bot_token')
Bot.run(str(token))
