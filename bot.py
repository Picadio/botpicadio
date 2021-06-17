import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random

import os
import psycopg2
import datetime
b=int(-38918391)
c=int(-83193912)
m=int(-63721733)
regim=int(0)
p=int(0)
r=0
stavka = int(0)
color = str("")

db_url = str(os.environ.get("DATABASE_URL"))
db_url=db_url.replace("postgres://", "")
x=db_url.split(":")
db_user=x[0]
db_password=x[1].split("@")[0]
db_host=x[1].split("@")[1]
db_name=x[2].split("/")[1]


Bot = commands.Bot(command_prefix='!')
@Bot.event
async def on_ready():
    print("Bot is online")
@Bot.command(pass_context=True)
async def playcasino(ctx, color, stavka):
	if int(stavka) > 0:
		if str(ctx.message.channel) == "⛔│админские-настройки" or str(ctx.message.channel) == "⚡│играть-с-ботом":
			conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
			cursor = conn.cursor()
			cursor.execute('SELECT * FROM test')
			row = cursor.fetchone()
			w=bool(0)
			q=bool(0)
			while row is not None:
				if ctx.message.author.id in row:
					w=bool(1)
					if row[1] >= int(stavka):
						money = row[1]-int(stavka)
						q=bool(1)
						cursor.execute('''UPDATE test SET bal={0} WHERE id={1}'''.format((row[1]-int(stavka)),ctx.message.author.id))
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
				print(r)
				if (r == 0 or r == 1) and color == "green":
					await ctx.message.channel.send("Поздравляю вы выиграли +" + str(int(stavka)*100))
					d=ctx.message.author.id

					conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        			password=db_password, host=db_host)
					cursor = conn.cursor()
					cursor.execute('SELECT * FROM test')
					row = cursor.fetchone()
					while row is not None:
						if ctx.message.author.id in row:
							a=row[1]+int(p)
							break
						row = cursor.fetchone()
					cursor.execute('''UPDATE test SET bal={0} WHERE id={1}'''.format(str(int(stavka)*100+money),d))
					conn.commit()
					cursor.close()
					conn.close()
				elif r >1 and r <= 50 and color == "red":
					await ctx.message.channel.send("Поздравляю вы выиграли +" + str(int(stavka)*2))
					d=ctx.message.author.id

					conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        			password=db_password, host=db_host)
					cursor = conn.cursor()
					cursor.execute('SELECT * FROM test')
					row = cursor.fetchone()
					while row is not None:
						if ctx.message.author.id in row:
							a=row[1]+int(p)
							break
						row = cursor.fetchone()
					cursor.execute('''UPDATE test SET bal={0} WHERE id={1}'''.format(str(int(stavka)*2+money),d))
					conn.commit()
					cursor.close()
					conn.close()
				elif r >50 and r <= 100 and color == "black":
					await ctx.message.channel.send("Поздравляю вы выиграли +" + str(int(stavka)*2))
					d=ctx.message.author.id

					conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        			password=db_password, host=db_host)
					cursor = conn.cursor()
					cursor.execute('SELECT * FROM test')
					row = cursor.fetchone()
					while row is not None:
						if ctx.message.author.id in row:
							a=row[1]+int(p)
							break
						row = cursor.fetchone()
					cursor.execute('''UPDATE test SET bal={0} WHERE id={1}'''.format(str(int(stavka)*2+money),d))
					conn.commit()
					cursor.close()
					conn.close()
				else:
					await ctx.message.channel.send("Увы вы проиграли -"+str(stavka))
	else:
		await ctx.message.channel.send("Так нельзя!")
				
@Bot.command(pass_context=True)
async def table_bal(ctx):
	conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        password=db_password, host=db_host)
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM test')
	row = cursor.fetchone()
	emb=discord.Embed(title="Топ по баллам", colour= 0x39d0d6)
	while row is not None:
		f = ctx.message.channel.members
		for line in f:
			if line.id == row[0]:
				emb.add_field(name=str(line.name)+" : ", value=str(row[1]))
		row = cursor.fetchone()
	
	emb.set_footer(text="Вызвано:{}".format(ctx.message.author.name),icon_url=ctx.message.author.avatar_url)
	await ctx.message.channel.send(embed=emb)	

	cursor.close()
	conn.close()
@Bot.command(pass_context=True)
async def vopros(ctx):
	r = random.randint(1, 100)
	if r >= 1 and r <=5:
		await ctx.message.channel.send("Пошел нахуй")
	elif r >= 6 and r <= 40:
		await ctx.message.channel.send("Да")
	elif r >= 41 and r <= 75:
		await ctx.message.channel.send("Нет")
	elif r >= 76 and r <= 100:
		await ctx.message.channel.send("Возможно")
@Bot.command(pass_context=True)
async def table_size(ctx):
	conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        	password=db_password, host=db_host)
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM test')
	row = cursor.fetchone()
	emb=discord.Embed(title="Топ по бибе", colour= 0x39d0d6)
	s=[]
	while row is not None:
    
	    s.append((row[0], row[2]))

	    row = cursor.fetchone()
	s.sort(key=lambda x: x[1])
	s.reverse()
	
	for i in range(10):
		f = ctx.message.channel.members
		for line in f:
			if line.id == s[i][0]:
			strin += str(line.name)+" : "+str(s[i][1])+"\n"
	emb.add_field(name="TOP", value=strin)
	emb.set_footer(text="Вызвано:{}".format(ctx.message.author.name),icon_url=ctx.message.author.avatar_url)
	await ctx.message.channel.send(embed=emb)  

	cursor.close()
	conn.close()
	
	
	
@Bot.command(pass_context=True)
async def upg(ctx):
	if str(ctx.message.channel) == "⛔│админские-настройки" or str(ctx.message.channel) == "⚡│играть-с-ботом":
		print(1)
		conn1 = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
		cursor1 = conn1.cursor()
		cursor1.execute('SELECT * FROM test')
		row1 = cursor1.fetchone()
		w1=bool(1)
		while row1 is not None:
			if ctx.message.author.id in row1:
				size = int(row1[2])
				w1=bool(0)
				break
			row1 = cursor1.fetchone()
		cursor1.close()
		conn1.close()
		if w1:
			await ctx.message.channel.send("Вы не зарегистрированы. Пропишите !reg")
		else:
			conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
			cursor = conn.cursor()
			cursor.execute('SELECT * FROM test')
			row = cursor.fetchone()
			w=bool(0)
			
			while row is not None:
				
				if ctx.message.author.id in row:
					w=bool(1)
					
					if (datetime.datetime.now()-datetime.datetime.strptime(row[3], "%Y%m%d%H%M%S")).total_seconds()//3600 >= 5:
						cursor.execute('''UPDATE test SET date_try={0} WHERE id={1}'''.format(datetime.datetime.now().strftime("%Y%m%d%H%M%S"),ctx.message.author.id))
						conn.commit()
						
						r = random.randint(0, int(size/10+1))
						conn1 = psycopg2.connect(dbname=db_name, user=db_user, 
                        				password=db_password, host=db_host)
						cursor1 = conn1.cursor()
						cursor1.execute('SELECT * FROM test')
						row1 = cursor1.fetchone()
						if r >= 0 and r <= 10:
						
							while row1 is not None:
								if ctx.message.author.id in row1:
									await ctx.message.channel.send(str(ctx.message.author.mention)+" Повезло, +1 см к бибе")
									cursor1.execute('''UPDATE test SET cm={0} WHERE id={1}'''.format((size+1),ctx.message.author.id))
									conn1.commit()
									break
								row1 = cursor1.fetchone()
						else:
							while row1 is not None:
								if ctx.message.author.id in row1:
									await ctx.message.channel.send(str(ctx.message.author.mention)+" Не повезло, -1 см от бибы")
									cursor1.execute('''UPDATE test SET cm={0} WHERE id={1}'''.format((size-1),ctx.message.author.id))
									conn1.commit()
									break
								row1 = cursor1.fetchone()
					else:
						await ctx.message.channel.send("Будет доступно через {0}:{1}:{2}".format(int((18000-((datetime.datetime.now()-datetime.datetime.strptime(row[3], "%Y%m%d%H%M%S")).total_seconds()))//3600), int((18000-((datetime.datetime.now()-datetime.datetime.strptime(row[3], "%Y%m%d%H%M%S")).total_seconds()))%3600//60), int((18000-((datetime.datetime.now()-datetime.datetime.strptime(row[3], "%Y%m%d%H%M%S")).total_seconds()))%3600%60)))
					break
				row = cursor.fetchone()
				
			if w==0:
				await ctx.message.channel.send("Вы не зарегистрированы. Пропишите !reg")
		cursor.close()
		conn.close()
@Bot.command(pass_context=True)
async def set_size(ctx, user:discord.Member, p):
	if "343279631807545356" == str(ctx.message.author.id):
		d=user.id
		await ctx.message.delete()
		conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
		cursor = conn.cursor()
		cursor.execute('''UPDATE test SET cm={0} WHERE id={1}'''.format(p,d))
		conn.commit()
		await ctx.message.channel.send("Длина бибы у игрока {} изменена на {}".format(user.name, p))


		cursor.close()
		conn.close()
	else:
		await ctx.message.channel.send("У вас нет прав для выполнения этой команды")

@Bot.command(pass_context=True)
async def size(ctx):
    conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test')
    row = cursor.fetchone()
    y=bool(0)
    while row is not None:
        if ctx.message.author.id in row:
            y=bool(1)
        row = cursor.fetchone()
    if y==1:
        cursor.execute('SELECT * FROM test')
        row = cursor.fetchone()
        while row is not None:
            if ctx.message.author.id in row:
                await ctx.message.channel.send("Длина бибы:"+str(row[2]))
                break
            row = cursor.fetchone()
    else:
        await ctx.message.channel.send("Вы не зарегистрированы. Пропишите !reg")
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
        
        conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM test')
        row = cursor.fetchone()
        w=bool(0)
        while row is not None:
            if ctx.message.author.id in row:
                w=bool(1)
                if row[1] >= 1000:
                    cursor.execute('''UPDATE test SET bal={0} WHERE id={1}'''.format((row[1]-1000),ctx.message.author.id))
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
    r=ctx.message.author.id
    conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test')
    row = cursor.fetchone()
    w=bool(0)
    while row is not None:
        if ctx.message.author.id in row:
            
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
    r=ctx.message.author.id
    conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test')
    row = cursor.fetchone()
    w=bool(0)
    while row is not None:
        if ctx.message.author.id in row:
            
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
    conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test')
    row = cursor.fetchone()
    w=bool(0)
    while row is not None:
        if ctx.message.author.id in row:
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
    conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test')
    row = cursor.fetchone()
    y=bool(0)
    while row is not None:
        if ctx.message.author.id in row:
            y=bool(1)
        row = cursor.fetchone()
    if y==1:
        cursor.execute('SELECT * FROM test')
        row = cursor.fetchone()
        while row is not None:
            if ctx.message.author.id in row:
                await ctx.message.channel.send("Ваш баланс:"+str(row[1]))
                break
            row = cursor.fetchone()
    else:
        await ctx.message.channel.send("Вы не зарегистрированы. Пропишите !reg")
    cursor.close()
    conn.close()

    
@Bot.event
async def on_message(message):
    global b
    global c
    global p
    t=bool(0)
    if p == 1:
        if str(message.content) == str(int(c)+int(b)):
            b=-3918391839
            c=-7381283912
            b=message.author.id
    
            conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM test')
            row = cursor.fetchone()
            while row is not None:
                if message.author.id in row:
                    a=row[1]+20
                    break
                row = cursor.fetchone()
            cursor.execute('''UPDATE test SET bal={0} WHERE id={1}'''.format(a,b))
            conn.commit()
            await message.channel.send("Верно, вам начислено 20 балов")
    
            cursor.close()
            conn.close()


            
    if p == 2:
        if str(message.content) == str(int(c)+int(b)):
            b=-3918391839
            c=-7381283912
            b=message.author.id
    
            conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM test')
            row = cursor.fetchone()
            while row is not None:
                if message.author.id in row:
                    a=row[1]+2
                    break
                row = cursor.fetchone()
            cursor.execute('''UPDATE test SET bal={0} WHERE id={1}'''.format(a,b))
            conn.commit()
            await message.channel.send("Верно, вам начислено 2 бала")
    
            cursor.close()
            conn.close()
    if p == 3:
        if str(message.content) == str(int(c)+int(b)):
            b=-3918391839
            c=-7381283912
            b=message.author.id
    
            conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM test')
            row = cursor.fetchone()
            while row is not None:
                if message.author.id in row:
                    a=row[1]+10
                    break
                row = cursor.fetchone()
            cursor.execute('''UPDATE test SET bal={0} WHERE id={1}'''.format(a,b))
            conn.commit()
            await message.channel.send("Верно, вам начислено 10 балов")
    
            cursor.close()
            conn.close()
            
        
    await Bot.process_commands(message)
   
pas = os.environ.get("KOD")
@Bot.command(pass_context=True)
async def popln(ctx, user:discord.Member, p, kod):
    if str(kod) == "f12ua":
        d=user.id
        await ctx.message.delete()
        conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM test')
        row = cursor.fetchone()
        while row is not None:
            if user.id in row:
                a=row[1]+int(p)
                break
            row = cursor.fetchone()
        cursor.execute('''UPDATE test SET bal={0} WHERE id={1}'''.format(a,d))
        conn.commit()
        await ctx.message.channel.send("Баланс игрока {} пополнен на {} балов".format(user.name, p))
        print("Balance add:{} {}".format(p, user.name))
        
        cursor.close()
        conn.close()
    else:
        await ctx.message.channel.send("Код неверный!!!")
@Bot.command(pass_context=True)
async def set(ctx, user:discord.Member, p, kod):
    if str(kod) == "f12ua":
        d=user.id
        await ctx.message.delete()
        conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
        cursor = conn.cursor()
        cursor.execute('''UPDATE test SET bal={0} WHERE id={1}'''.format(p,d))
        conn.commit()
        await ctx.message.channel.send("Баланс игрока {} установлен на {}".format(user.name, p))
        
        
        cursor.close()
        conn.close()
    else:
        await ctx.message.channel.send("Код неверный!!!")  


@Bot.command(pass_context=True)
async def reg(ctx):
    b=ctx.message.author.id
    conn = psycopg2.connect(dbname=db_name, user=db_user, 
                        		password=db_password, host=db_host)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM test')
    row = cursor.fetchone()

    q=bool(1)
    while row is not None:
        if ctx.message.author.id in row:
            await ctx.message.channel.send("Вы уже зарегистрированы")
            q=bool(0)
            break
        row = cursor.fetchone()
    if q==1:
        

        cursor.execute('''INSERT INTO test (id,bal,cm,date_try) VALUES ({0},0, 0, {1})'''.format(b, (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y%m%d%H%M%S")) )
        conn.commit()
        await ctx.message.channel.send("Регистрация выполнена упешно")
    cursor.close()
    conn.close()
    


    



@Bot.command(pass_context=True)
async def logika(ctx):
    await ctx.message.channel.send("Я попробовал и смог (Цитата великих)")

@Bot.command(pass_context=True)
async def spam(ctx, member: discord.Member, text, colvo, lichka):
	i=0
	while i<int(colvo):
		if lichka=='1':
			await member.send(member.mention+" "+text)
		else:
			await ctx.message.channel.send(member.mention+" "+text)
		i+=1
@Bot.remove_command("help")
@Bot.command(pass_context=True)
async def help(ctx):
	emb=discord.Embed(title="Команды", colour= 0x39d0d6)
	emb.add_field(name="----------------------------------------------------------------------------------------------", value="!info @учасник - инфа про учасника\n\n !reg - регистрация в боте, для взаимодействия с ним\n\n !bal - посмотреть свой баланс\n\n !playhard / !playmedium / !playeasy - решить пример определёной сложности(дают баллы)\n\n !buy Доступ - купить роль Доступ\n\n !upg - прокачать бибу персу\n\n !size - узнать размер своей бибы\n\n !playcasino цвет(red/black/green) ставка - сыграть в казино на баллы\n\n !vopros текст - ответ на вопрос(да/нет/возможно)")

	await ctx.message.channel.send(embed=emb)
    
        

token = os.environ.get("BOT_TOKEN")
Bot.run(str(token))
