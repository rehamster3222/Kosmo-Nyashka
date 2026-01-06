try:
	import time, os, platform, random
	from datetime import datetime
except ImportError as impe:
	print(f"ошибка импорта! {impe}")

oldir = os.getcwd()

#metrics
G = 6.67430e-11
AU = 1.496e11
DT = 3600 * 24
#asteroid
ash = random.uniform(0, 1)
am = random.uniform(0.0001, 3)
an = random.choice(["Kenos", "Jebos", "Masos", "Rafus", "Egas", "Vatos", "Karas"])
ann = random.choice(["GJ", "GF", "GM"])
annn = random.choice(["I", "II", "III", "IV", "V","VI", "VII", "VIII", "IX", "X"])
ar = random.uniform(0.1, 1000)
ax = random.uniform(-999999, 999999)
ay = random.uniform(-999999, 999999)
az = random.uniform(-999999, 999999)

assx = random.uniform(-3250, 3250)
assy = random.uniform(-3250, 3250)
assz = random.uniform(-3250, 3250)

asss = random.uniform(0.01, 50)
	
#black holes
#sh
bhn = random.choice(["Sagittarius", "Stranger", "Toflatos", "Taronos", "Ton"])
bhnn = random.choice(["*", "J", "M", "L"])
bhnnn = random.randint(1, 999)
bhsh = random.uniform(0, 1)
#metric bh
bhm = random.uniform(1000, 	100000000)
bhr = random.uniform(100000, 100000000000)
bhx = random.uniform(-999999, 999999)
bhy = random.uniform(-999999, 999999)
bhz = random.uniform(-999999, 999999)
#speed
bhssx = random.uniform(-3500, 3500)
bhssy = random.uniform(-3500, 3500)
bhssz = random.uniform(-3500, 3500)
	


#planets
plg = random.choice(["Andromeda", "Milky Way", "Triangulum", "Large Magellanic Cloud", "Small Magellanic Cloud", "Sombrero", "Whirlpool", "Pinwheel", "Bode's", "Cigar", "Sculptor", "Messier 87", "Messier 49", "Messier 60", "Messier 64"])
pln = random.choice(["Charlie", "Gilbert", "Egrinch", "Etarius", "Ratus", "Manches", "Ompus", "Olimpus", "Kertys", "Tynys", "Mechas", "Lampos", "Karatus", "Kenos", "Rembatros", "Nekas"])
plnn = random.choice(["I","II","III","IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX"])
plr = random.uniform(0.01, 9000000)
plt = random.uniform(-273.15, 1700)
plm = random.uniform(0.01, 1100)
plx = random.uniform(-99999, 99999)
ply = random.uniform(-99999, 99999)
plz = random.uniform(-99999, 99999)
plssx = random.uniform(-3250, 3250)
plssy = random.uniform(-3250, 3250)
plssz = random.uniform(-3250, 3250)



#stars
stm = random.uniform(0.01, 600)
stl = random.uniform(100, 2500)
stn = random.randint(100, 30000)
stg = random.choice(["Andromeda", "Milky Way", "Triangulum", "Large Magellanic Cloud", "Small Magellanic Cloud", "Sombrero", "Whirlpool", "Pinwheel", "Bode's", "Cigar", "Sculptor", "Messier 87", "Messier 49", "Messier 60", "Messier 64"])
stt = random.randint(1000, 42000)
ste = random.uniform(0.01, 13.8)
sty = random.uniform(-99999, 99999)
stx = random.uniform(-99999, 99999)
stz = random.uniform(-99999, 99999)
stssx = random.uniform(-1250, 1250)
stssy = random.uniform(-1250, 1250)
stssz = random.uniform(-1250, 1250)
nst = random.uniform(0, 1)
stsss = random.uniform(0.01, 100)
nsttt = random.uniform(0, 1)
sto = random.choice(["MD", "HD"])


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
		sts.write(f'''\nstar-{stn}-galaxy-{stg}\nmass sun-{stm:.2f}\nlight year-{stl:.2f}\ntemperature-{stt}c°\nlife-{ste:.3f}-billion years\n''')
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
	for fln in ["stars.txt","history.txt","kssys.txt"]:
		with open(fln, "w") as touch:
			pass

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
		{stg}\nmass sun-{stm:.2f}\nlight year-{stl:.2f}\ntemperature-{stt}c°\nlife-{ste:.3f}-billion years\n\n''')
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
	

def galaxies():
	global ash,asm,asr,asn,asnn,asnnn,asx
	global asy, asz, asss, assx, assy, assz
	global plm,plx,ply,plz,plt,plr,plssx,plssy
	global plssz, pln, plnn,stm,stl,stt,stx,sty
	global stz, stsss, stssx,stssy,stssz,ste
	global stg, nst,nsttt,sto,bhn,bhnn,bhnnn
	global bhx, bhy,bhz,bhsh,bhm,bhr,bhssx
	global bhssy,bhssz
	os.mkdir("galaxies")
	os.chdir("galaxies")
	glxx = random.choice(["NGC", "MGC", "JGC"])
	gllx = random.randint(1000, 9999)
	galx = (f"{glxx}{gllx}")
	with open(
	f"galaxy-{galx}.txt", "a"
	) as ksm:
		sct = random.randint(7000, 23000)
		shnc = random.uniform(0, 1)
		bhc = random.uniform(0, 1)
		for ct in range (sct):

			ksm.write("\nnewsys:\n")
			#st
			amsh = random.randint(1, 4)
			stm = random.uniform(0.01, 600)
			stl = random.uniform(100, 2500)
			stn = random.randint(100, 30000)
			stt = random.randint(1000, 42000)
			ste = random.uniform(0.01, 13.8)
			sty = random.uniform(-999999, 999999)
			stx = random.uniform(-999999, 999999)
			stz = random.uniform(-999999, 999999)
			stssx = random.uniform(-1250, 1250)
			stssy = random.uniform(-1250, 1250)
			stssz = random.uniform(-1250, 1250)
			nst = random.uniform(0, 1)
			stsss = random.uniform(0.01, 100)
			nsttt = random.uniform(0, 1)
			sto = random.choice(["MD", "HD"])
			stnr = str(f"star-{sto}{stn}")
			#pl
			plsh = random.randint(0, 8)
			pln = random.choice(["Charlie", "Gilbert", "Egrinch", "Etarius", "Ratus", "Manches", "Ompus", "Olimpus", "Kertys", "Tynys", "Mechas", "Lampos", "Karatus", "Kenos", "Rembatros", "Nekas"])
			plnn = random.choice(["I","II","III","IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX"])
			plr = random.uniform(0.01, 9000000)
			plt = random.uniform(-273.15, 1700)
			plm = random.uniform(0.01, 1100)
			plx = stx + random.uniform(-0.99, 0.99)
			ply = sty + random.uniform(-0.99, 0.99)
			plz = stz + random.uniform(-0.99, 0.99)
			plssx = stssx + random.randint(-1, 1)
			plssy = stssy + random.randint(-1, 1)
			plssz = stssz + random.randint(-1, 1)
			#ast
			ash = random.uniform(0, 1)
			am = random.uniform(0.0001, 3)
			an = random.choice(["Kenos", "Jebos", "Masos", "Rafus", "Egas", "Vatos", "Karas"])
			ann = random.choice(["GJ", "GF", "GM"])
			annn = random.choice(["I", "II", "III", "IV", "V","VI", "VII", "VIII", "IX", "X"])
			ar = random.uniform(0.1, 1000)
			ax = stx + random.uniform(-0.99, 0.99)
			ay = sty + random.uniform(-0.99, 0.99)
			az = stz + random.uniform(-0.99, 0.99)

			assx = stssx + random.randint(-1, 1)
			assy = stssy + random.randint(-1, 1)
			assz = stssz + random.randint(-1, 1)
			if nst < 0.05:
				stsss = random.uniform(100000, 12000000)
				stm = random.uniform(0.1, 45)
				ste = random.uniform(0.001, 0.25)
				stt = random.uniform(0.0001, 10000000)
				ksm.write(f'''\n\nтип: нейтронная звезда''')
				plsh = 0
				if nsttt < 0.03:
					ksm.write('''\n\nтип нейтронной звезды: магнетар''')
				elif nsttt < 0.4:
					ksm.write('''\nтип нейтронной звезды: квазар''')
				elif nsttt < 1:
					ksm.write('''\nтип нейтронной звезды: пульсар''')
				else:
					print("\n")
			else:
				ksm.write(f'''тип: обычная звезда''')
				ksm.write(f'''\nstar-{sto}{stn}-galaxy-{galx}''')
				ksm.write(f'''\nmass sun-{stm:.2f}''')
				ksm.write(f'''\ntemperature-{stt}c°''')
				ksm.write(f'''\n\nlife-{ste:.3f}-billion years''')
				ksm.write(f'''\nspeed spin-{stsss:.2f}/год\n''')
				ksm.write(f'''\n\nкоординаты в галактике {galx}''')
				ksm.write(f'''\nx: {stx:.3f}-light year''')
				ksm.write(f'''\ny: {sty:.3f}-light year''')
				ksm.write(f'''\nz: {stz:.3f}-light year''')
				ksm.write(f'''\nspeed: \nx:{stssx:.2f}км/с\ny:{stssy:.2f}км/с\nz:{stssz:.2f}км/с''')
				ksm.write('''\n\nпо температуре:\n''')
				if stt < 3700:
					ksm.write('''\nэто красный карлик!''')
					ksm.write('''\nобозначение: M\n''')
				elif stt < 5200:
					ksm.write('''\nэто оранжевый карлик!''')
					ksm.write('''\nобозначение: K\n''')
				elif stt < 6000:
					ksm.write('''\nэто желтый карлик!''')
					ksm.write('''\nобозначение: G\n''')
				elif stt < 7500:
					ksm.write('''\nэто желто-белый карлик!''')
					ksm.write('''\nобозначение: F''')
				elif stt < 10000:
					ksm.write('''\nэто белый карлик!''')
					ksm.write('''\nобозначение: A\n''')
				elif stt < 30000:
					ksm.write('''\nэто бело-голубой карлик!''')
					ksm.write('''\nобозначение: B\n''')
				elif stt < 50000:
					ksm.write('''\nэто голубой карлик!''')
					ksm.write('''\nобозначение: O\n''')
				elif stt < 100000:
					ksm.write('''\nэто голубой сверхгигант!''')
					ksm.write('''\nобозначение: O+\n''')
				elif stt > 100000:
					ksm.write('''\nэто сверх монстр с абсолютной температурой!''')
					ksm.write('''\nобозначение: O++\n''')
				else:
					ksm.write('''\nпоздравляю! вы открыли новую звезду которую еще никогда не находили!:D''')
				for pl in range (plsh):
					ksm.write(f'''\n\nplanet name: {pln} {plnn}''')
					ksm.write(f'''\nearth mass: {plm:.3f}''')
					ksm.write(f'''\nradius: {plr:.2f}км''')
					ksm.write(f'''\ngalaxy: {galx}''')
					ksm.write(f'''\nin system: {stnr}''')
					ksm.write(f'''\ntemperature: {plt:.2f}c°''')
					ksm.write('''\n\nкоординаты планеты:\n''')
					ksm.write(f'''\nx: {plx:.3f}''')
					ksm.write(f'''\ny: {ply:.3f}''')
					ksm.write(f'''\nz: {plz:.3f}''')
					ksm.write(f'''\n\nскорость:''')
					ksm.write(f'''\nx: {plssx:.2f}км/с''')
					ksm.write(f'''\ny: {plssy:.2f}км/с''')
					ksm.write(f'''\nz: {plssz:.2f}км/с\n\n''')
					if ash < 0.15:
						for et in range (amsh):
							ksm.write(f'''\n\nподраздел: {ann}''')
							ksm.write(f'''\nasteroid: {an} {annn}''')
							ksm.write(f'''\nmass: {am:.2f}''')
							ksm.write(f'''in system: {stnr}''')
							ksm.write(f'''in galaxy: {galx}''')
							ksm.write(f'''\n\nкоординаты:\n''')
							ksm.write(f'''\nx: {ax:.2f}''')
							ksm.write(f'''\ny: {ay:.2f}''')
							ksm.write(f'''\nz: {az:.2f}''')
							ksm.write('''\n\nскорость:\n''')
							ksm.write(f'''\nx: {assx:.2f}км/с''')
							ksm.write(f'''\ny: {assy:.2f}км/с''')
							ksm.write(f'''\nz: {assz:.2f}км/с\n''')
							ksm.write(f'''\nspins: {asss:.2f}/year''')

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

def sys():
	global stm, stt, ste, stg, stn,stx,sty,stz
	global stsss, stssx, stssy, stssz, plm,pln
	global plt, plx, ply, plz, sto, plssx,plssy
	global plssz, plnn
	with open("kssys.txt", "a") as ksm:
		#chance
		amsh = random.randint(1, 4)
		ash = random.uniform(0, 1)
		plsh = random.randint(0, 8)
		stsh = random.randint(1, 2)
		#asteroids
		ash = random.uniform(0, 1)
		am = random.uniform(0.0001, 3)
		an = random.choice(["Kenos", "Jebos", "Masos", "Rafus", "Egas", "Vatos", "Karas"])
		ann = random.choice(["GJ", "GF", "GM"])
		annn = random.choice(["I", "II", "III", "IV", "V","VI", "VII", "VIII", "IX", "X"])
		ar = random.uniform(0.1, 1000)
		ax = stx + random.uniform(-0.99, 0.99)
		ay = sty + random.uniform(-0.99, 0.99)
		az = stz + random.uniform(-0.99, 0.99)

		assx = stssx + random.randint(-1, 1)
		assy = stssy + random.randint(-1, 1)
		assz = stssz + random.randint(-1, 1)

		asss = random.uniform(0.01, 50)
		#stars
		stm = random.uniform(0.01, 600)
		stl = random.uniform(100, 2500)
		stn = random.randint(100, 30000)
		stg = random.choice(["Andromeda", "Milky Way", "Triangulum", "Large Magellanic Cloud", "Small Magellanic Cloud", "Sombrero", "Whirlpool", "Pinwheel", "Bode's", "Cigar", "Sculptor", "Messier 87", "Messier 49", "Messier 60", "Messier 64"])
		stt = random.randint(1000, 42000)
		ste = random.uniform(0.01, 13.8)
		sty = random.uniform(-99999, 99999)
		stx = random.uniform(-99999, 99999)
		stz = random.uniform(-99999, 99999)
		stssx = random.uniform(-1250, 1250)
		stssy = random.uniform(-1250, 1250)
		stssz = random.uniform(-1250, 1250)
		nst = random.uniform(0, 1)
		stsss = random.uniform(0.01, 100)
		nsttt = random.uniform(0, 1)
		sto = random.choice(["MD", "HD"])
		stnr = str(f"star-{sto}{stn}")
		#planets
		pln = random.choice(["Charlie", "Gilbert", "Egrinch", "Etarius", "Ratus", "Manches", "Ompus", "Olimpus", "Kertys", "Tynys", "Mechas", "Lampos", "Karatus", "Kenos", "Rembatros", "Nekas"])
		plnn = random.choice(["I","II","III","IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX"])
		plr = random.uniform(0.01, 9000000)
		plt = random.uniform(-273.15, 1700)
		plm = random.uniform(0.01, 1100)
		plx = stx + random.uniform(-0.99, 0.99)
		ply = sty + random.uniform(-0.99, 0.99)
		plz = stz + random.uniform(-0.99, 0.99)
		plssx = stssx + random.randint(-1, 1)
		plssy = stssy + random.randint(-1, 1)
		plssz = stssz + random.randint(-1, 1)
		for e in range (stsh):
			ksm.write("newsys:")
			if nst < 0.05:
				stsss = random.uniform(100000, 12000000)
				stm = random.uniform(0.1, 45)
				ste = random.uniform(0.001, 0.25)
				stt = random.uniform(0.0001, 10000000)
				ksm.write(f'''\n\nтип: нейтронная звезда''')
				plsh = 0
				if nsttt < 0.03:
					ksm.write('''\n\nтип нейтронной звезды: магнетар''')
				elif nsttt < 0.4:
					ksm.write('''\nтип нейтронной звезды: квазар''')
				elif nsttt < 1:
					ksm.write('''\nтип нейтронной звезды: пульсар''')
			else:
				ksm.write('''\n\nтип: обычная звезда''')
				ksm.write(f'''\nstar-{sto}{stn}-galaxy-{stg}''')
				ksm.write(f'''\nmass sun-{stm:.2f}''')
				ksm.write(f'''\ntemperature-{stt}c°''')
				ksm.write(f'''\n\nlife-{ste:.3f}-billion years''')
				ksm.write(f'''\nspeed spin-{stsss:.2f}/год\n''')
				ksm.write(f'''\n\nкоординаты в галактике {stg}''')
				ksm.write(f'''\nx: {stx:.3f}-light year''')
				ksm.write(f'''\ny: {sty:.3f}-light year''')
				ksm.write(f'''\nz: {stz:.3f}-light year''')
				ksm.write(f'''speed: \nx:{stssx:.2f}км/с\ny:{stssy:.2f}км/с\nz:{stssz:.2f}км/с''')
				ksm.write('''\n\nпо температуре:\n''')
				if stt < 3700:
					ksm.write('''\nэто красный карлик!''')
					ksm.write('''\nобозначение: M\n''')
				elif stt < 5200:
					ksm.write('''\nэто оранжевый карлик!''')
					ksm.write('''\nобозначение: K\n''')
				elif stt < 6000:
					ksm.write('''\nэто желтый карлик!''')
					ksm.write('''\nобозначение: G\n''')
				elif stt < 7500:
					ksm.write('''\nэто желто-белый карлик!''')
					ksm.write('''\nобозначение: F''')
				elif stt < 10000:
					ksm.write('''\nэто белый карлик!''')
					ksm.write('''\nобозначение: A\n''')
				elif stt < 30000:
					ksm.write('''\nэто бело-голубой карлик!''')
					ksm.write('''\nобозначение: B\n''')
				elif stt < 50000:
					ksm.write('''\nэто голубой карлик!''')
					ksm.write('''\nобозначение: O\n''')
				elif stt < 100000:
					ksm.write('''\nэто голубой сверхгигант!''')
					ksm.write('''\nобозначение: O+\n''')
				elif stt > 100000:
					ksm.write('''\nэто сверх монстр с абсолютной температурой!''')
					ksm.write('''\nобозначение: O++\n''')
				else:
					ksm.write('''\nпоздравляю! вы открыли новую звезду которую еще никогда не находили!:D''')
		for p in range (plsh):
			ksm.write(f'''\n\nplanet name: {pln} {plnn}''')
			ksm.write(f'''\nearth mass: {plm:.3f}''')
			ksm.write(f'''\nradius: {plr:.2f}км''')
			ksm.write(f'''\ngalaxy: {stg}''')
			ksm.write(f'''\nin system: {stnr}''')
			ksm.write(f'''\ntemperature: {plt:.2f}c°''')
			ksm.write('''\n\nкоординаты планеты:\n''')
			ksm.write(f'''\nx: {plx:.3f}''')
			ksm.write(f'''\ny: {ply:.3f}''')
			ksm.write(f'''\nz: {plz:.3f}''')
			ksm.write(f'''\n\nскорость:''')
			ksm.write(f'''\nx: {plssx:.2f}км/с''')
			ksm.write(f'''\ny: {plssy:.2f}км/с''')
			ksm.write(f'''\nz: {plssz:.2f}км/с\n\n''')
			if ash < 0.15:
				for et in range (amsh):
					ksm.write(f'''\n\nподраздел: {ann}''')
					ksm.write(f'''\nasteroid: {an} {annn}''')
					ksm.write(f'''\nmass: {am:.2f}''')
					ksm.write(f"in system: {stnr}")
					ksm.write(f"in galaxe: {stg}")
					ksm.write(f'''\n\nкоординаты:\n''')
					ksm.write(f'''\nx: {ax:.2f}''')
					ksm.write(f'''\ny: {ay:.2f}''')
					ksm.write(f'''\nz: {az:.2f}''')
					ksm.write('''\n\nскорость:\n''')
					ksm.write(f'''\nx: {assx:.2f}км/с''')
					ksm.write(f'''\ny: {assy:.2f}км/с''')
					ksm.write(f'''\nz: {assz:.2f}км/с\n''')
					ksm.write(f'''\nspins: {asss:.2f}/year''')
			pln = random.choice(["Charlie", "Gilbert", "Egrinch", "Etarius", "Ratus", "Manches", "Ompus", "Olimpus", "Kertys", "Tynys", "Mechas", "Lampos", "Karatus", "Kenos", "Rembatros", "Nekas"])
			plnn = random.choice(["I","II","III","IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX"])
			plr = random.uniform(0.01, 9000000)
			plt = random.uniform(-273.15, 1700)
			plm = random.uniform(0.01, 1100)
			plx = stx + random.uniform(-0.99, 0.99)
			ply = sty + random.uniform(-0.99, 0.99)
			plz = stz + random.uniform(-0.99, 0.99)
			plssx = stssx + random.randint(-100, 100)
			plssy = stssy + random.randint(-100, 100)
			plssz = stssz + random.randint(-100, 100)
		print('''систему можно будет найти введя 10 в главном меню''')
		input('''нажми enter для продолжения''')
		clear()
		vuvod()
		mein()
		
def csmhst():
	with open("kssys.txt", "r") as ksls:
		cnt = ksls.read()
		print(cnt)
		input('''нажми enter для продолжения''')
		cnt = ksls.read()
	
		
	


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
	global stssy, stssz, nst, stsss, ste, nsttt
	global pln, plnn, sto, plg, plt, plm, plr, plx
	global ply, plz, plssx, plssy, plssz
	print('''1.- создать звезду\n2.- посмотреть историю выбора\n3.- посмотреть историю звезд\n4.- удалить историю выбора\n5.- удалить историю звезд\n6.- создать несколько звезд\n7.- выход\n8.- создать планету\n9.- создать систему\n10.- посмотреть истрию систем\n11.- удалить историю систем\n12.- создать астероид\n13.- создать галактику (файл можно найти в папке galaxies) \n?.- обьяснение''')
	ibp = input(":  ")
	if ibp == "1":
		hst = str(f"{tm}: 1")
		savhst()
		if nst < 0.05:
			stsss = random.uniform(100000, 12000000)
			stm = random.uniform(0.1, 45)
			ste = random.uniform(0.001, 0.25)
			stt = random.uniform(0.0001, 10000000)
			print(f"\nтип: нейтронная звезда")
			if nsttt < 0.03:
				print('''тип нейтронной звезды: магнетар''')
			elif nsttt < 0.4:
				print('''тип нейтронной звезды: квазар''')
			elif nsttt < 1:
				print('''тип нейтронной звезды: пульсар''')
		else:
			print("\nтип: обычная звезда")
		print(f"\nstar-{sto}{stn}-galaxy-{stg}")
		print(f"mass sun-{stm:.2f}")
		print(f"temperature-{stt}c°")
		print(f"life-{ste:.3f}-billion years")
		print(f'''speed spin-{stsss:.2f}/год\n''')
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
		elif stt < 50000:
			print("это голубой карлик!")
			print("обозначение: O\n")
		elif stt < 100000:
			print("это голубой сверхгигант!")
			print("обозначение: O+\n")
		elif stt > 100000:
			print('''это сверх монстр с абсолютной температурой!''')
			print("обозначение: O++\n")
		else:
			print('''поздравляю! вы открыли новую звезду которую еще никогда не находили!:D''')
		savst()
		tm = datetime.now()
		input('''\nдля продолжения нажми enter''')
		stm = random.uniform(0.1, 600)
		stl = random.uniform(100, 2500)
		stn = random.randint(100, 30000)
		stg = random.choice(["Andromeda", "Milky Way", "Triangulum", "Large Magellanic Cloud", "Small Magellanic Cloud", "Sombrero", "Whirlpool", "Pinwheel", "Bode's", "Cigar", "Sculptor", "Messier 87", "Messier 49", "Messier 60", "Messier 64"])
		stt = random.randint(100, 42000)
		ste = random.uniform(0.01, 13.8)
		sty = random.uniform(-99999, 99999)
		stx = random.uniform(-99999, 99999)
		stz = random.uniform(-99999, 99999)
		stssx = random.uniform(-1250, 1250)
		stssy = random.uniform(-1250, 1250)
		stssz = random.uniform(-1250, 1250)
		nst = random.uniform(0, 1)
		stsss = random.uniform(0.01, 70)
		nsttt = random.uniform(0, 1)
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
	elif ibp == "8":
		hst = str(f"{tm}: 8")
		savhst()
		print(f'''\nplanet name: {pln} {plnn}''')
		print(f'''earth mass: {plm:.3f}''')
		print(f'''radius: {plr:.2f}км''')
		print(f"galaxy: {plg}")
		print(f"temperature: {plt:.2f}c°")
		print("\nкоординаты планеты:\n")
		print(f"x: {plx:.3f}")
		print(f"y: {ply:.3f}")
		print(f"z: {plz:.3f}")
		print(f"\nскорость:")
		print(f"x: {plssx:.2f}км/с")
		print(f"y: {plssy:.2f}км/с")
		print(f"z: {plssz:.2f}км/с\n\n")
		plg = random.choice(["Andromeda", "Milky Way", "Triangulum", "Large Magellanic Cloud", "Small Magellanic Cloud", "Sombrero", "Whirlpool", "Pinwheel", "Bode's", "Cigar", "Sculptor", "Messier 87", "Messier 49", "Messier 60", "Messier 64"])
		pln = random.choice(["Charlie", "Gilbert", "Egrinch", "Etarius", "Ratus", "Manches", "Ompus", "Olimpus", "Kertys", "Tynys", "Mechas", "Lampos", "Karatus", "Kenos", "Rembatros", "Nekas"])
		plnn = random.choice(["I","II","III","IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX"])
		plr = random.uniform(0.01, 9000000)
		plt = random.uniform(-273.15, 1700)
		plm = random.uniform(0.01, 1100)
		plx = random.uniform(-99999, 99999)
		ply = random.uniform(-99999, 99999)
		plz = random.uniform(-99999, 99999)
		plssx = random.uniform(-3250, 3250)
		plssy = random.uniform(-3250, 3250)
		plssz = random.uniform(-3250, 3250)
		vuvod()
		mein()
	elif ibp == "9":
		hst = str(f"{tm}: 9")
		savhst()
		sys()
	elif ibp == "10":
		hst = str(f"{tm}: 10")
		savhst()
		csmhst()
		clear()
		vuvod()
		mein()
	elif ibp == "11":
		hst = str(f"{tm}: 11")
		savhst()
		os.remove("kssys.txt")
		print("удалено!;)")
		vuvod()
		mein()
	elif ibp == "12":
		hst = str(f"{tm}: 12")
		savhst()
		print(f"\nподраздел: {ann}")
		print(f'''asteroid: {an} {annn}''')
		print(f'''mass: {am:.2f}''')
		print(f'''\nкоординаты:\n''')
		print(f'''x: {ax:.2f}''')
		print(f'''y: {ay:.2f}''')
		print(f'''z: {az:.2f}''')
		print('''\nскорость:\n''')
		print(f'''x: {assx:.2f}км/с''')
		print(f'''y: {assy:.2f}км/с''')
		print(f'''z: {assz:.2f}км/с\n''')
		print(f'''spins: {asss:.2f}/year''')
	elif ibp == "13":
		hst = str(f"{tm}: 13")
		savhst()
		galaxies()
		os.chdir(oldir)
		clear()
		vuvod()
		mein()
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
