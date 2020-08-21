import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import sqlite3
import os
b=int(-38918391)
c=int(-83193912)
m=int(-63721733)
regim=int(0)
p=int(0)
r=0
stavka = int(0)
color = str("")

Bot = commands.Bot(command_prefix='!')
@Bot.event
async def on_ready():
    print("Bot is online")
@Bot.command(pass_context=True)
async def playcasino(ctx, stavka, color):
	if str(ctx.message.channel) == "админские-настройки" or str(ctx.message.channel) == "играть-с-ботом":
		 conn = sqlite3.connect("mybase.sqlite")
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM test')
		row = cursor.fetchone()
		w=bool(0)
		q=bool(0)
		while row is not None:
		    if str(ctx.message.author.id) in row:
			w=bool(1)
			if row[1] >= stavka:
			    q=bool(1)
			    conn.commit()
			else:
			   await ctx.message.channel.send("Ставка слишком велика, на вашем счету недостаточно баллов!")
			break
		    row = cursor.fetchone()
		if w==0:
		    await ctx.message.channel.send("Вы не зарегистрированы. Пропишите !reg")
		cursor.close()
		conn.close()
		if q and w:
			r = random.randint(0, 100)
			if r == 0 and color == "green":
				await ctx.message.channel.send("Поздравляю вы выиграли +" + str(stavka*10))
				d=str(user.id)

				conn = sqlite3.connect("mybase.sqlite")
				cursor = conn.cursor()
				cursor.execute('SELECT * FROM test')
				row = cursor.fetchone()
				while row is not None:
				    if str(user.id) in row:
					a=row[1]+int(p)
					break
				    row = cursor.fetchone()
				cursor.execute('''UPDATE test SET bal=? WHERE id=?''',(str(stavka*10),d,))
				conn.commit()
				cursor.close()
				conn.close()
			elif r >=1 and r <= 50 and color == "red":
				await ctx.message.channel.send("Поздравляю вы выиграли +" + str(stavka*2))
				d=str(user.id)

				conn = sqlite3.connect("mybase.sqlite")
				cursor = conn.cursor()
				cursor.execute('SELECT * FROM test')
				row = cursor.fetchone()
				while row is not None:
				    if str(user.id) in row:
					a=row[1]+int(p)
					break
				    row = cursor.fetchone()
				cursor.execute('''UPDATE test SET bal=? WHERE id=?''',(str(stavka*2),d,))
				conn.commit()
				cursor.close()
				conn.close()
			elif r >50 and r <= 100 and color == "black":
				await ctx.message.channel.send("Поздравляю вы выиграли +" + str(stavka*2))
				d=str(user.id)

				conn = sqlite3.connect("mybase.sqlite")
				cursor = conn.cursor()
				cursor.execute('SELECT * FROM test')
				row = cursor.fetchone()
				while row is not None:
				    if str(user.id) in row:
					a=row[1]+int(p)
					break
				    row = cursor.fetchone()
				cursor.execute('''UPDATE test SET bal=? WHERE id=?''',(str(stavka*2),d,))
				conn.commit()
				cursor.close()
				conn.close()
			else:
				await ctx.message.channel.send("Увы вы проиграли -"+str(stavka))
				conn = sqlite3.connect("mybase.sqlite")
				cursor = conn.cursor()
				cursor.execute('SELECT * FROM test')
				row = cursor.fetchone()
				while row is not None:
					if str(ctx.message.author.id) in row:
						cursor.execute('''UPDATE test SET bal=? WHERE id=?''',((row[1]-stavka),ctx.message.author.id,))
						conn.commit()
						break
					row = cursor.fetchone()
				cursor.close()
				conn.close()
	
	
@Bot.command(pass_context=True)
async def create(ctx):
	if str(ctx.message.channel) == "админские-настройки" or str(ctx.message.channel) == "играть-с-ботом":
		b=str(ctx.message.author.id)
		conn = sqlite3.connect("twobase.sqlite")
		cursor = conn.cursor()
		try:
			cursor.execute('''CREATE TABLE test (id text, cm integer)''')
		except:
			pass
		cursor.execute('SELECT * FROM test')
		row = cursor.fetchone()
		q=bool(1)
		while row is not None:
			if str(ctx.message.author.id) in row:
				await ctx.message.channel.send("Вы уже создали себя")
				q=bool(0)
				break
			row = cursor.fetchone()
		if q==1:
			cursor.execute('''INSERT INTO test (id,cm) VALUES (?,0)''', (b,))
			conn.commit()
			await ctx.message.channel.send("Создание выполнено упешно")
		cursor.close()
		conn.close()

@Bot.command(pass_context=True)
async def upg(ctx):
	if str(ctx.message.channel) == "админские-настройки" or str(ctx.message.channel) == "играть-с-ботом":
		print(1)
		conn1 = sqlite3.connect("twobase.sqlite")
		cursor1 = conn1.cursor()
		cursor1.execute('SELECT * FROM test')
		row1 = cursor1.fetchone()
		w1=bool(1)
		while row1 is not None:
			if str(ctx.message.author.id) in row1:
				size = int(row1[1])
				w1=bool(0)
				break
			row1 = cursor1.fetchone()
		cursor1.close()
		conn1.close()
		if w1:
			await ctx.message.channel.send("Вы не создали себя. Пропишите !create")
		else:
			conn = sqlite3.connect("mybase.sqlite")
			cursor = conn.cursor()
			cursor.execute('SELECT * FROM test')
			row = cursor.fetchone()
			w=bool(0)
			print(2)
			print(row[0])
			print(ctx.message.author.id)
			while row is not None:
				
				if str(ctx.message.author.id) in row:
					w=bool(1)
					print(3)
					if row[1] >= 100:
						cursor.execute('''UPDATE test SET bal=? WHERE id=?''',((row[1]-100),ctx.message.author.id,))
						conn.commit()
						print(3)
						r = random.randint(0, 2)
						conn1 = sqlite3.connect("twobase.sqlite")
						cursor1 = conn1.cursor()
						cursor1.execute('SELECT * FROM test')
						row1 = cursor1.fetchone()
						if r == 0 or r == 1:
							print(4)
							while row1 is not None:
								if str(ctx.message.author.id) in row1:
									await ctx.message.channel.send(str(ctx.message.author.name)+" Повезло, +1 см к бибе")
									cursor1.execute('''UPDATE test SET cm=? WHERE id=?''',((size+1),ctx.message.author.id,))
									conn1.commit()
									break
								row1 = cursor1.fetchone()
						else:
							while row1 is not None:
								if str(ctx.message.author.id) in row1:
									await ctx.message.channel.send(str(ctx.message.author.name)+" Не повезло, -1 см от бибы")
									cursor1.execute('''UPDATE test SET cm=? WHERE id=?''',((size-1),ctx.message.author.id,))
									conn1.commit()
									break
								row1 = cursor1.fetchone()
					else:
						await ctx.message.channel.send("Это действие стоит 100. Вам не хватает {} балов".format(100-row[1]))
					break
				row = cursor.fetchone()
				
			if w==0:
				await ctx.message.channel.send("Вы не зарегистрированы. Пропишите !reg")
		cursor.close()
		conn.close()
@Bot.command(pass_context=True)
async def set_size(ctx, user:discord.Member, p, kod):
    if str(kod) == str(pas):
        d=str(user.id)
        await ctx.message.delete()
        conn = sqlite3.connect("twobase.sqlite")
        cursor = conn.cursor()
        cursor.execute('''UPDATE test SET cm=? WHERE id=?''',(p,d,))
        conn.commit()
        await ctx.message.channel.send("Длина бибы у игрока {} изменена на {}".format(user.name, p))
        
        
        cursor.close()
        conn.close()
    else:
        await ctx.message.channel.send("Код неверный!!!")    

@Bot.command(pass_context=True)
async def size(ctx):
    conn = sqlite3.connect("twobase.sqlite")
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
                await ctx.message.channel.send("Длина бибы:"+str(row[1])+" см")
                break
            row = cursor.fetchone()
    else:
        await ctx.message.channel.send("Вы не создали себя. Пропишите !create")
    cursor.close()
    conn.close()
      
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
async def Puma(ctx):
    embed = discord.Embed(color = 0xff9900, title = 'VLADICK') 
    embed.set_image(url = "https://cdn.discordapp.com/attachments/421747668537311244/742863079867547698/image0.jpg") 
    await ctx.send(embed = embed)
   
@Bot.command(pass_context=True)
async def Puma_full(ctx):
    embed = discord.Embed(color = 0xff9900, title = 'Кепка VLADICKa') 
    embed1 = discord.Embed(color = 0xff9900, title = 'Толстовка VLADICKa') 
    embed2 = discord.Embed(color = 0xff9900, title = 'Штаны VLADICKa') 
    embed3 = discord.Embed(color = 0xff9900, title = 'Кросовок VLADICKa') 
    embed.set_image(url = "https://i1.rozetka.ua/goods/10885300/puma_4056204301142_images_10885300719.jpg") 
    embed1.set_image(url = "https://cdn.sportmaster.ua/static/i/2000_2000/products/244595/QA6hi001.jpeg") 
    embed2.set_image(url = "https://images.shafastatic.net/135159668") 
    embed3.set_image(url = "https://www.runnerinn.com/f/13735/137358726/puma-enzo-2.jpg") 
    await ctx.send(embed = embed)
    await ctx.send(embed = embed1)
    await ctx.send(embed = embed2)
    await ctx.send(embed = embed3)
    
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
    global regim
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
        b = random.randint(100000,1000000)
        c = random.randint(100000,1000000)
        regim = random.randint(1,2)
        if regim == 1:
            await ctx.message.channel.send( "{} + {}".format(c, b))
        if regim == 2:
            await ctx.message.channel.send( "{} - {}".format(c, b))
        if regim == 3:
            await ctx.message.channel.send( "{} * {}".format(c, b))
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
    
    t=bool(0)
    if p == 1:
        if regim==1:
            if str(message.content) == str(int(c)+int(b)):
                b=-3918391839
                c=-7381283912
                t=bool(1)
        if regim==2:
            if str(message.content) == str(int(c)-int(b)):
                b=-3918391839
                c=-7381283912
                t=bool(1)
      
        if t == 1:
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
        if str(message.content) == str(int(c)+int(b)):
            b=-3918391839
            c=-7381283912
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
        if str(message.content) == str(int(c)+int(b)):
            b=-3918391839
            c=-7381283912
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
        await ctx.message.channel.send("Баланс игрока {} установлен на {}".format(user.name, p))
        
        
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
