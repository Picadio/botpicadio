import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import sqlite3
import os
b=int(-38918391)
c=int(-83193912)
p=int(0)
r=0

Bot = commands.Bot(command_prefix='!')
@Bot.event
async def on_ready():
    print("Bot is online")
    

      
@Bot.command(pass_context=True)
async def game(ctx):
    a=random.randint(1, 2)
    if a==1:
        await ctx.message.channel.send('PUBG LITE')
    if(a==2):
        await ctx.message.channel.send('Minecraft')


@Bot.command(pass_context=True)
async def qq(ctx):
    await ctx.message.channel.send("Привет {}".format(ctx.message.author.mention))

@Bot.command(pass_context=True)
async def buy(ctx,role:discord.Role):
    if role in ctx.message.author.roles:
        await ctx.message.channel.send("Роль уже куплена")
    elif str(role) == "Доступ":
        
        conn = sqlite3.connect("mybase.sqlite")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM test')
        row = cursor.fetchone()
        w=bool(0)
        while row is not None:
            if str(ctx.message.author.id) in row:
                w=bool(1)
                if row[1] >= 1000:
                    cursor.execute('''UPDATE test SET bal=? WHERE id=?''',((row[1]-1000),ctx.message.author.id,))
                    conn.commit()
                    await discord.Member.add_roles(ctx.message.author, role)
                    await ctx.message.channel.send("Покупка прошла успешно")
                else:
                   await ctx.message.channel.send("Эта роль стоит 1000. Вам не хватает {} балов".format(1000-row[1]))
                break
            row = cursor.fetchone()
        if w==0:
            await ctx.message.channel.send("Вы не зарегистрированы. Пропишите !reg")
        cursor.close()
        conn.close()
    else:
        await ctx.message.channel.send("Эту роль нельзя купить")
    






@Bot.command(pass_context=True)
async def playeasy(ctx):
    global b
    global c
    global p
    global r
    r=str(ctx.message.author.id)
    conn = sqlite3.connect("mybase.sqlite")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test')
    row = cursor.fetchone()
    w=bool(0)
    while row is not None:
        if str(ctx.message.author.id) in row:
            
            w=bool(1)
        row = cursor.fetchone()
    if w==1:
        b = random.randint(1,100)
        c = random.randint(1,100)
        await ctx.message.channel.send( "{} + {}".format(b, c))
        p=2
    else:
        await ctx.message.channel.send("Вы не зарегистрированы. Пропишите !reg")
    print("Ответ:"+ str(c+b))
    cursor.close()
    conn.close()
        

@Bot.command(pass_context=True)
async def playmedium(ctx):
    global b
    global c
    global p
    global r
    r=str(ctx.message.author.id)
    conn = sqlite3.connect("mybase.sqlite")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test')
    row = cursor.fetchone()
    w=bool(0)
    while row is not None:
        if str(ctx.message.author.id) in row:
            
            w=bool(1)
        row = cursor.fetchone()
    if w==1:
        b = random.randint(1000,10000)
        c = random.randint(1000,10000)
        await ctx.message.channel.send( "{} + {}".format(b, c))
        p=3
    else:
        await ctx.message.channel.send("Вы не зарегистрированы. Пропишите !reg")
    print("Ответ:"+ str(c+b))
    cursor.close()
    conn.close()

@Bot.command(pass_context=True)
async def playhard(ctx):
    global b
    global c
    global p
    global r
    r=ctx.message.author.id
    conn = sqlite3.connect("mybase.sqlite")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test')
    row = cursor.fetchone()
    w=bool(0)
    while row is not None:
        if str(ctx.message.author.id) in row:
            w=bool(1)
        row = cursor.fetchone()
    if w==1:
        b = random.randint(100000,10000000)
        c = random.randint(100000,10000000)
        await ctx.message.channel.send( "{} + {}".format(b, c))
        p=1
    else:
        await ctx.message.channel.send("Вы не зарегистрированы. Пропишите !reg")
    print("Ответ:"+ str(c+b))
    cursor.close()
    conn.close()


@Bot.command(pass_context=True)
async def bal(ctx):
    conn = sqlite3.connect("mybase.sqlite")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test')
    row = cursor.fetchone()
    y=bool(0)
    while row is not None:
        if str(ctx.message.author.id) in row:
            y=bool(1)
        row = cursor.fetchone()
    if y==1:
        cursor.execute('SELECT * FROM test')
        row = cursor.fetchone()
        while row is not None:
            if str(ctx.message.author.id) in row:
                await ctx.message.channel.send("Ваш баланс:"+str(row[1]))
                break
            row = cursor.fetchone()
    else:
        await ctx.message.channel.send("Вы не зарегистрированы. Пропишите !reg")
    cursor.close()
    conn.close()



@Bot.command(pass_context=True)
async def id(ctx,user:discord.Member):
    await ctx.message.channel.send("ID:{}".format(user.id))


    
@Bot.event
async def on_message(message):
    global b
    global c
    global p
    if str(message.content) == str(int(c)+int(b)):
        b=-3918391839
        c=-7381283912
        if p == 1:
            b=str(message.author.id)
    
            conn = sqlite3.connect("mybase.sqlite")
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM test')
            row = cursor.fetchone()
            while row is not None:
                if str(message.author.id) in row:
                    a=row[1]+20
                    break
                row = cursor.fetchone()
            cursor.execute('''UPDATE test SET bal=? WHERE id=?''',(a,b,))
            conn.commit()
            await message.channel.send("Верно, вам начислено 20 балов")
    
            cursor.close()
            conn.close()


            
        if p == 2:
            b=str(message.author.id)
    
            conn = sqlite3.connect("mybase.sqlite")
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM test')
            row = cursor.fetchone()
            while row is not None:
                if str(message.author.id) in row:
                    a=row[1]+2
                    break
                row = cursor.fetchone()
            cursor.execute('''UPDATE test SET bal=? WHERE id=?''',(a,b,))
            conn.commit()
            await message.channel.send("Верно, вам начислено 2 бала")
    
            cursor.close()
            conn.close()
        if p == 3:
            b=str(message.author.id)
    
            conn = sqlite3.connect("mybase.sqlite")
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM test')
            row = cursor.fetchone()
            while row is not None:
                if str(message.author.id) in row:
                    a=row[1]+10
                    break
                row = cursor.fetchone()
            cursor.execute('''UPDATE test SET bal=? WHERE id=?''',(a,b,))
            conn.commit()
            await message.channel.send("Верно, вам начислено 10 балов")
    
            cursor.close()
            conn.close()
            
        
    await Bot.process_commands(message)
   
pas = os.environ.get("KOD")
@Bot.command(pass_context=True)
async def popln(ctx, user:discord.Member, p, kod):
    if str(kod) == str(pas):
        d=str(user.id)
        await ctx.message.delete()
        conn = sqlite3.connect("mybase.sqlite")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM test')
        row = cursor.fetchone()
        while row is not None:
            if str(user.id) in row:
                a=row[1]+int(p)
                break
            row = cursor.fetchone()
        cursor.execute('''UPDATE test SET bal=? WHERE id=?''',(a,d,))
        conn.commit()
        await ctx.message.channel.send("Баланс игрока {} пополнен на {} балов".format(user.name, p))

        
        cursor.close()
        conn.close()
    else:
        await ctx.message.channel.send("Код неверный!!!")

@Bot.command(pass_context=True)
async def set(ctx, user:discord.Member, p, kod):
    if str(kod) == str(pas):
        d=str(user.id)
        await ctx.message.delete()
        conn = sqlite3.connect("mybase.sqlite")
        cursor = conn.cursor()
        cursor.execute('''UPDATE test SET bal=? WHERE id=?''',(p,d,))
        conn.commit()
        await ctx.message.channel.send("Баланс игрока {} установлен на {}".format(user.name, p)
        
        cursor.close()
        conn.close()
    else:
        await ctx.message.channel.send("Код неверный!!!")
    


@Bot.command(pass_context=True)
async def reg(ctx):
    b=str(ctx.message.author.id)
    conn = sqlite3.connect("mybase.sqlite")
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE test (id text, bal integer)''')
    except:
        pass
    cursor.execute('SELECT * FROM test')
    row = cursor.fetchone()
    q=bool(1)
    while row is not None:
        if str(ctx.message.author.id) in row:
            await ctx.message.channel.send("Вы уже зарегистрированы")
            q=bool(0)
            break
        row = cursor.fetchone()
    if q==1:
        cursor.execute('''INSERT INTO test (id,bal) VALUES (?,0)''', (b,))
        conn.commit()
        await ctx.message.channel.send("Регистрация выполнена упешно")
    cursor.close()
    conn.close()
    


    
@Bot.command(pass_context=True)
async def info(ctx, member: discord.Member):
    emb=discord.Embed(title="Info", colour= 0x39d0d6)
    emb.add_field(name="Ник", value=member.name)
    emb.add_field(name="Присоединился", value=member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"))
    emb.set_thumbnail(url= member.avatar_url)
    emb.set_footer(text="Вызвано:{}".format(ctx.message.author.name),icon_url=ctx.message.author.avatar_url)
    await ctx.message.channel.send(embed=emb)


@Bot.command(pass_context=True)
async def logika(ctx):
    await ctx.message.channel.send("Я попробовал и смог (Цитата великих)")

    
    
        

token = os.environ.get("BOT_TOKEN")
Bot.run(str(token))