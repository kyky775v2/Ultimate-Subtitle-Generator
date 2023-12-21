import os
import srt
import time
import json
import torch
import pathlib
import os.path
#import whisper
import datetime
import threading
import subprocess
import nvidia_smi
import configparser
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from faster_whisper import WhisperModel

model = None
cWindow = None
config = None
lp = None

def gcd(path):
	return f'{pathlib.Path().resolve()}\{path}'

window = tk.Tk()
window.iconbitmap(gcd('img/icon.ico'))
window.title("Ultimate Subtitle Generator")
window.geometry("600x750+100+100")
window.resizable(False, False)

hwacc = tk.IntVar()
lang = tk.StringVar()
mdtype = tk.StringVar()
srcFile = tk.StringVar()
dstFile = tk.StringVar()

lang.set("en")

def load_config():
	global config, lp, lang
	config = configparser.ConfigParser()
	if os.path.isfile(gcd('conf/config.ini')) is True:
		config.read(gcd('conf/config.ini'), encoding='utf-8')
		lang.set(config['userdata']['lang'])
		if config['userdata']['hwacc'] == "True":
			hwacc.set(1)
		else:
			hwacc.set(0)
		mdtype.set(config['userdata']['mtype'])
	else:
		config['userdata'] = {}
		lang.set("en")
		config['userdata']['lang'] = "en"
		hwacc.set(0)
		config['userdata']['hwacc'] = "False"
		mdtype.set('large-v3')
		config['userdata']['mtype'] = "large-v3"
	with open(gcd('conf/config.ini'), 'w', encoding='utf-8') as config_file:
		config.write(config_file)
	with open(gcd(f'lang/{lang.get()}.json'), 'r', encoding='utf8') as f:
		lp = json.load(f)

load_config()

def log(txt):
	global console
	console.insert(tk.END, f'{txt}\n')

# window.configure(bg='#1F1F1F')
_lang = lp["name"]
desc_img = tk.PhotoImage(file=gcd("img/desc.png"))
entry_img = tk.PhotoImage(file=gcd("img/entry.png"))
config_img = tk.PhotoImage(file=gcd("img/config.png"))
console_img = tk.PhotoImage(file=gcd("img/console.png"))
config_btn_img = tk.PhotoImage(file=gcd("img/configbtn.png"))
folder_button_img = tk.PhotoImage(file=gcd("img/folder.png"))
start_img = tk.PhotoImage(file=gcd(f'img/startbtn_{_lang}.png'))

canvas = tk.Canvas(window, bg="#1F1F1F", height=750, width=600, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

canvas.create_image(299.0, 627.0, image=console_img)
scroll_y = tk.Scrollbar(window)
scroll_y.place(x=0, y=0, width=0, height=0)
console = tk.Text(window, font=("consolas", 8), yscrollcommand=scroll_y.set, fg="#FFFFFF", bg='#1F1F1F')
console.place(x=17, y=524, width=567, height=207)
scroll_y.config(command=console.yview)

log(lp["logs"])

if torch.cuda.is_available() is False and hwacc.get() == 1:
	hwacc.set(0)

if hwacc.get() == 0:
	model = WhisperModel(mdtype.get(), device="cpu", compute_type='int8')
else:
	model = WhisperModel(mdtype.get(), device="cuda", compute_type='float16')

def selectSrc():
	global srcFile
	fn = filedialog.askopenfilename()
	if fn != "":
		srcFile.set(fn)
		log(lp["src_file_set_successful"])

def selectDst():
	global dstFile
	fn = filedialog.askdirectory(parent=window, title=lp["dst_file_set_request"])
	if fn != "":
		dstFile.set(fn)
		log(lp["dst_file_set_successful"])

def execPrc():
	global srcFile, dstFile, processBtn, model
	if srcFile.get() != "" and dstFile.get() != "" and model != None:
		processBtn["state"] = "disabled"
		print(srcFile.get())
		command = f'{gcd("ext/ffmpeg.exe")} -y -i {srcFile.get()} -vn -f wav -acodec pcm_s16le {dstFile.get()}/.audio.tmp.wav'
		proc = subprocess.Popen(command, shell=True)
		proc.wait()
		log('Extracted audio data. started stream to AI...')
		segments, info = model.transcribe(f'{dstFile.get()}/.audio.tmp.wav', beam_size=5)
		log(lp["subtitle_created"])
		os.remove(f'{dstFile.get()}/.audio.tmp.wav')
		log(lp["subtitle_file_created"])
		index = 0
		finalSrtArray = []
		for segment in segments:
			index += 1
			start = datetime.timedelta(seconds=segment.start)
			end = datetime.timedelta(seconds=segment.end)
			st = srt.Subtitle(index, start=start, end=end, content=segment.text)
			finalSrtArray.append(st)
		finalRawSrt = srt.compose(finalSrtArray)
		f = open(f'{dstFile.get()}/result.srt', 'w')
		f.write(finalRawSrt)
		f.close()
		log(lp["all_process_successful"])
		processBtn["state"] = "normal"

canvas.create_image(77.0, 205.0, image=desc_img)
fileSrcTxt = tk.Label(window, text=lp["src_name"], fg="white", bg="#1F1F1F", font=("Intel", 14 * -1))
fileSrcTxt.place(x=17, y=194, width=121, height=22)
canvas.create_image(349.0, 205.0, image=entry_img)
fileSrcBox = tk.Label(window, textvariable=srcFile, fg="white", bg="black")
fileSrcBox.place(x=159.0, y=192.0, width=380.0, height=26.0)
fileSrcBtn = tk.Button(image=folder_button_img, borderwidth=0, highlightthickness=0, command=selectSrc, relief="flat")
fileSrcBtn.place(x=556.0, y=190.0, width=30.0, height=30.0)

canvas.create_image(77.0, 255.0, image=desc_img)
fileDstTxt = tk.Label(window, text=lp["dst_name"], fg="white", bg="#1F1F1F", font=("Intel", 14 * -1))
fileDstTxt.place(x=17, y=244, width=121, height=22)
canvas.create_image(349.0, 255.0, image=entry_img)
fileDstBox = tk.Label(window, textvariable=dstFile, fg="white", bg="black")
fileDstBox.place(x=159.0, y=242.0, width=380.0, height=26.0)
fileDstBtn = tk.Button(image=folder_button_img, borderwidth=0, highlightthickness=0, command=selectDst, relief="flat")
fileDstBtn.place(x=556.0, y=240.0, width=30.0, height=30.0)

canvas.create_image(299.0, 370.0, image=config_img)

startBtn = tk.Button(image=start_img, borderwidth=0, highlightthickness=0, command=execPrc, relief="flat")
startBtn.place(x=13.0, y=470.0, width=536.0, height=30.0)
startTxt = canvas.create_text(281, 485, text=lp["extract"], fill="white", font=("Intel", 14 * -1))

def save_changed_cfg():
	global cWindow, hwacc, config
	if cWindow is not None:
		config['userdata']['lang'] = lang.get()
		if hwacc.get() == 0:
			config['userdata']['hwacc'] = 'False'
		else:
			config['userdata']['hwacc'] = 'True'
		config['userdata']['mtype'] = mdtype.get()
		with open(gcd('conf/config.ini'), 'w', encoding='utf-8') as config_file:
			config.write(config_file)
			cWindow.destroy()

def cancel_cfg():
	global cWindow
	if cWindow is not None:
		load_config()
		cWindow.destroy()

def show_config():
	global cWindow, mdtype, device, lang
	cWindow = tk.Toplevel()
	cWindow.iconbitmap(gcd('img/icon.ico'))
	cWindow.title("Settings")
	cWindow.geometry("500x600+150+150")
	cWindow.resizable(False, False)
	tk.Label(cWindow, font=("Arial", 8), text=lp["config_change_lang"]).place(x=50, y=50, width=400, height=30)
	tk.OptionMenu(cWindow, lang, "en", "ko").place(x=50, y=80, width=400, height=30)
	if torch.cuda.is_available():
		tk.Label(cWindow, font=("Arial", 8), text=lp["config_hwacc"]).place(x=50, y=150, width=400, height=30)
		tk.Checkbutton(cWindow, variable=hwacc).place(x=235, y=180, width=30, height=30)
	tk.Label(cWindow, font=("Arial", 8), text=lp["config_model_change"]).place(x=50, y=250, width=400, height=30)
	tk.OptionMenu(cWindow, mdtype, "large-v3").place(x=50, y=280, width=400, height=30)
	tk.Button(cWindow, overrelief="solid", width=15, command=cancel_cfg, text=lp["back"]).place(x=50, y=400, width=400, height=30)
	tk.Button(cWindow, overrelief="solid", width=15, command=save_changed_cfg, text=lp["save"]).place(x=50, y=450, width=400, height=30)
	tk.Label(cWindow, font=("Arial", 8), text=lp["change_affected"]).place(x=50, y=480, width=400, height=30)

configBtn = tk.Button(image=config_btn_img, borderwidth=0,  highlightthickness=0, command=show_config, relief="flat")
configBtn.place(x=556.0, y=470.0, width=30.0, height=30.0)

window.mainloop()
