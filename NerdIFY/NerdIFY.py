import eel
import shutil
from tkinter import filedialog
from time import sleep
import tkinter
import shortuuid
from pymongo import MongoClient
discovered=[]
eel.init('web')
client=MongoClient('mongodb+srv://budgetdiscord:discord@cluster0.bn3df.mongodb.net/budgetdiscord?retryWrites=true&w=majority')
@eel.expose()
def post(songname):
	img=filedialog.askopenfilename(initialdir='/',filetypes=(("JPG","*.jpg"),("PNG","*.png"),("GIF","*.gif")))
	file=filedialog.askopenfilename(initialdir='/',filetypes=(("MP3","*.mp3"),("WAV","*.wav")))
	imgfil=open(img,"rb")
	mpfil=open(file,"rb")
	imgdata=imgfil.read()
	mpdata=mpfil.read()
	db=client.NerdIFY
	col=db["posts"]
	col.insert_one({"songname":songname,"song":mpdata,"thumbnail":imgdata})
@eel.expose()
def recv():
	db=client.NerdIFY
	col=db["posts"]
	for x in col.find():
		if x.get("_id") in discovered:
			pass
		else:
			songname=x.get("songname")
			img=x.get("thumbnail")
			discovered.append(x.get("_id"))
			name=shortuuid.uuid()
			with open(name+".png","wb") as l:
				l.write(img)
			with open(name+'.mp3',"wb") as g:
				g.write(x.get("song"))
			shutil.move(name+".png","D:/Naman/Projects/NerdIFY/web")
			shutil.move(name+".mp3","D:/Naman/Projects/NerdIFY/web")
			return name+".png",songname,name+".mp3"
eel.start('front_page.html',size=(500,900))