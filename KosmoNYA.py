try:
	import time, os, platform, random
	from datetime import datetime
except ImportError as impe:
	print(f"ошибка импорта! {impe}")


stm = random.uniform(0.01, 600)
stl = random.uniform(100, 2500)
stn = random.randint(100, 30000)
stg = random.choice(["Andromeda", "Milky Way"])
stt = random.randint(1000, 42000)
ste = random.uniform(0.01, 13.8)
sty = random.uniform(-99999, 99999)
stx = random.uniform(-99999, 99999)
stz = random.uniform(-99999, 99999)
stssx = random.uniform(-1250, 1250)
stssy = random.uniform(-1250, 1250)
stssz = random.uniform(-1250, 1250)

countt = int(1)
		

lsd = os.listdir()

ps = platform.system()
tm = datetime.now()
hst = str("False")

def chkst():
	with open("stars.txt", "r") as str:
		cntst = str.read()
		print(cntst)
def savst():
	with open("stars.txt", "a") as sts:
		sts.write(f'''\nstar-{stn}-galaxy-{stg}\nmass sun-{stm:.2f}\nlight year-{stl:.2f}\ntemperature-{stt}\nlife-{ste:.3f}-billion years\n\n''')
		sts.write(f'''координаты в галактике {stg}\n''')
		sts.write(f"x: {stx:.3f}-light year\n")
		sts.write(f"y: {sty:.3f}-light year\n")
		sts.write(f"z: {stz:.3f}-light year\n")
		sts.write(f'''speed:\nx:{stssx:.2f}км/с\n''')
		sts.write(f"y:{stssy:.2f}км/с\n")
		sts.write(f"z:{stssz:.2f}км/с\n")
		
		sts.write("\nпо температуре:\n")
		if stt < 3700:
			sts.write('''\nэто красный карлик!''')
			sts.write("\nобозначение: M\n\n")
		elif stt < 5200:
			sts.write('''\nэто оранжевый карлик!''')
			sts.write("\nобозначение: K\n\n")
		elif stt < 6000:
			sts.write('''\nэто желтый карлик!''')
			sts.write("\nобозначение: G\n\n")
		elif stt < 7500:
			sts.write('''\nэто желто-белый карлик!''')
			sts.write("\nобозначение: F\n\n")
		elif stt < 10000:
			sts.write('''\nэто белый карлик!''')
			sts.write('''\nобозначение: A\n\n''')
		elif stt < 30000:
			sts.write('''\nэто бело-голубой карлик!''')
			sts.write("\nобозначение: B\n\n")
		elif stt > 30000:
			sts.write('''\nэто голубой карлик!''')
			sts.write("\nобозначение: O\n\n")
		else:
			sts.write('''поздравляю! вы открыли новую звезду которую еще никогда не находили!:D''')

def clear():
	global ps
	if ps == "Windows":
		os.system("cls")
	else:
		os.system("clear")
def chkhst():
	with open("history.txt", "r") as ef:
		cnt = ef.read()
		print(cnt)
def savhst():
	with open("history.txt", "a") as et:
		et.write(f"\n{hst}")
def lt():
	os.system("touch history.txt")
	os.system("touch stars.txt")
def wt():
	os.system('''powershell "touch history.txt"''')
	os.system('''powershell "touch stars.txt"''')

def wtdst():
	try:
		os.system('''powershell "rm stars.txt"''')
		print("удалено!;)\n")
	except PermissionError as perme:
		print(f'''ошибка прав! {perme}''')
def wtdhst():
	try:
		os.system('''powershell "rm history.txt"''')
		print("удалено!:D\n")
	except PermissionError as perme:
		print(f'''ошибка прав! {perme}''')

def multist():
	global stm, stl, stn, stg, ste, stt
	try:
		countt = int(input(":  "))
	except ValueError as vale:
		print(f"ошибка! {vale}")
		vuvod()
		mein()
	with open("stars.txt", "a") as sts:
		for multi in range (countt):
			stm = random.uniform(0.1, 600)
			stl = random.uniform(100, 2500)
			stn = random.randint(100, 30000)
			stg = random.choice(["Andromeda", "Milky Way"])
			stt = random.randint(100, 42000)
			ste = random.uniform(0.01, 13.8)
			sty = random.uniform(-99999, 99999)
			stx = random.uniform(-99999, 99999)
			stz = random.uniform(-99999, 99999)
			stssx = random.uniform(-1250, 1250)
			stssy = random.uniform(-1250, 1250)
			stssz = random.uniform(-1250, 1250)
			sts.write(f'''\nstar-{stn}-galaxy
		{stg}\nmass sun-{stm:.2f}\nlight year-{stl:.2f}\ntemperature-{stt}c•\nlife-{ste:.3f}-billion years\n\n''')
			sts.write(f'''координаты в галактике {stg}\n''')
			sts.write(f'''x: {stx:.3f}-light year\n''')
			sts.write(f'''y: {sty:.3f}-light year\n''')
			sts.write(f'''z: {stz:.3f}-light year\n''')
			sts.write(f'''speed:\nx:{stssx:.2f}км/с\n''')
			sts.write(f'''y:{stssy:.2f}км/с\n''')
			sts.write(f'''z:{stssz:.2f}км/с\n''')
			sts.write('''\nпо температуре:\n''')
			if stt < 3700:
				sts.write('''это красный карлик!''')
				sts.write('''\nобозначение: M\n\n''')
			elif stt < 5200:
				sts.write('''это оранжевый карлик!''')
				sts.write('''\nобозначение: K\n\n''')
			elif stt < 6000:
				sts.write('''это желтый карлик!''')
				sts.write('''\nобозначение: G\n\n''')
			elif stt < 7500:
				sts.write('''это желто-белый карлик!''')
				sts.write('''\nобозначение: F\n\n''')
			elif stt < 10000:
				sts.write('''это белый карлик!''')
				sts.write('''\nобозначение: A\n\n''')
			elif stt < 30000:
				sts.write('''это бело-голубой карлик!''')
				sts.write('''\nобозначение: B\n\n''')
			elif stt > 30000:
				sts.write('''это голубой карлик!''')
				sts.write('''\nобозначение: O\n\n''')
			else:
				sts.write('''поздравляю! вы открыли новую звезду которую еще никогда не находили!:D''')
	

def ltdst():
	try:
		os.system("rm -f stars.txt")
		print("удалено!;)\n")
	except PermissionError as perme:
		print(f'''ошибка прав! {perme}''')
def ltdhst():
	try:
		os.system("rm -f history.txt")
		print("удалено!:D\n")
	except PermissionError as perme:
		print(f'''ошибка прав! {perme}''')

linx = "False"
wind = "False"

if ps == "Linux":
	lt()
	linx = "True"
elif ps == "Windows":
	wt()
	wind = "True"
else:
	print("неизвестная система!")
	time.sleep(5)
	exit()
def vuvod():
	global tm
	print("космо няшка")
	print("BY NYA18")
	print(f"\n{tm}")
	tm = datetime.now()
def mein():
	global lsd, ps, tm, hst, stm, stl, stn, stg
	global linx, wind, stt, sty, stx, stz, stssx
	global stssy, stssz
	print('''1.- создать звезду\n2.- посмотреть историю выбора\n3.- посмотреть историю звезд\n4.- удалить историю выбора\n5.- удалить историю звезд\n6.- создать несколько звезд\n7.- выход\n?.- обьяснение''')
	ibp = input(":  ")
	if ibp == "1":
		hst = str(f"{tm}: 1")
		savhst()
		ste = random.uniform(0.01, 13.8)
		print(f"\nstar-{stn}-galaxy-{stg}")
		print(f"mass sun-{stm:.2f}")
		print(f"temperature-{stt}c•")
		print(f"life-{ste:.3f}-billion years\n")
		print(f'''координаты в галактике {stg}''')
		print(f"x: {stx:.3f}-light year")
		print(f"y: {sty:.3f}-light year")
		print(f"z: {stz:.3f}-light year")
		print(f'''speed: \nx:{stssx:.2f}км/с\ny:{stssy:.2f}км/с\nz:{stssz:.2f}км/с''')
		print("\nпо температуре:\n")
		if stt < 3700:
			print("это красный карлик!")
			print("обозначение: M\n")
		elif stt < 5200:
			print("это оранжевый карлик!")
			print("обозначение: K\n")
		elif stt < 6000:
			print("это желтый карлик!")
			print("обозначение: G\n")
		elif stt < 7500:
			print('''это желто-белый карлик!''')
			print("обозначение: F")
		elif stt < 10000:
			print("это белый карлик!")
			print("обозначение: A\n")
		elif stt < 30000:
			print("это бело-голубой карлик!")
			print("обозначение: B\n")
		elif stt > 30000:
			print("это голубой карлик!")
			print("обозначение: O\n")
		else:
			print('''поздравляю! вы открыли новую звезду которую еще никогда не находили!:D''')
		savst()
		tm = datetime.now()
		input('''\nдля продолжения нажми enter''')
		stm = random.uniform(0.1, 600)
		stl = random.uniform(100, 2500)
		stn = random.randint(100, 30000)
		stg = random.choice(["Andromeda", "Milky Way"])
		stt = random.randint(100, 42000)
		ste = random.uniform(0.01, 13.8)
		sty = random.uniform(-99999, 99999)
		stx = random.uniform(-99999, 99999)
		stz = random.uniform(-99999, 99999)
		stssx = random.uniform(-1250, 1250)
		stssy = random.uniform(-1250, 1250)
		stssz = random.uniform(-1250, 1250)
		clear()
		vuvod()
		mein()
	elif ibp == "2":
		hst = str(f"{tm}: 2")
		savhst()
		tm = datetime.now()
		chkhst()
		input('''нажми enter чтобы продолжить''')
		clear()
		vuvod()
		mein()
	elif ibp == "3":
		hst = str(f"{tm}: 3")
		savhst()
		tm = datetime.now()
		chkst()
		input('''нажми enter для продолжения''')
		clear()
		vuvod()
		mein()
	elif ibp == "4":
		hst = str(f"{tm}: 4")
		savhst()
		tm = datetime.now()
		if linx == "True":
			ltdhst()
			vuvod()
			mein()
		elif wind == "True":
			wtdhst()
			vuvod()
			mein()
		else:
			print("неизвестная ошибка!\n")
			vuvod()
			mein()
	elif ibp == "5":
		hst = str(f"{tm}: 5")
		savhst()
		tm = datetime.now()
		if linx == "True":
			ltdst()
			vuvod()
			mein()
		elif wind == "True":
			wtdst()
			vuvod()
			mein()
	elif ibp == "6":
		hst = str(f"{tm}: 6")
		savhst()
		try:
			print('''выбери сколько создать звезд''')
			multist()
			print('''готово! звезды можно найти в истории звезд :D''')
			vuvod()
			mein()
		except Exception as exc:
			print(f"ой ой ой! {exc}")
			vuvod()
			mein()
	elif ibp == "7":
		hst = str(f"{tm}: 7")
		savhst()
		exit()
	elif ibp == "?":
		hst = str(f"{tm}: ?")
		savhst()
		print('''единственное что я считаю нужным обьяснить это light year, световой год в данной псевдо-программе понимается так "как далеко звезда находится от центра ее галактики"\n\nИЗМЕНЕНО: координаты xyz это световые года от центра галактики в которой они находятся, прошлая система теперь недействительна но я оставил ее на память:D\n''')
		input('''нажми enter для выхода в главное меню''')
		clear()
		vuvod()
		mein()
	else:
		print("неправильный выбор!")
		hst = (f"{tm}: {ibp}")
		savhst()
		tm = datetime.now()
		mein()
vuvod()
mein()
