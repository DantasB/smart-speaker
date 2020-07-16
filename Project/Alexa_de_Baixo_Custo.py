import os
import speech_recognition as sr

from gtts	   import gTTS
from datetime  import datetime
from playsound import playsound

#Speak the audio said by the user
def create_audio(audio, path):
	tts = gTTS(audio,lang='pt-br')

	#Creates and destroy the audio
	tts.save('Alexa de Baixo Custo/audio/' + path + '.mp3')
	playsound('Alexa de Baixo Custo/audio/' + path + '.mp3')
	os.remove('Alexa de Baixo Custo/audio/' + path + '.mp3')

#Function that recognizes the user microphone
def listen_microphone():
	recognizer = sr.Recognizer()
	microphone = sr.Microphone(device_index=2)

	with microphone as source:
		recognizer.adjust_for_ambient_noise(source)
		print("Say something")
		audio = recognizer.listen(source)

	try:
		frase = recognizer.recognize_google(audio,language='pt-BR')

	except sr.UnknownValueError:
		print("I didn't understand")
		return "", False

	return frase, True

def treat_time():
	now_hour   = datetime.now().strftime("%H")
	if(now_hour == "00"):
		now_hour = "meia noite"
	if(now_hour == "12"):
		now_hour = "meio dia"
	elif(now_hour.startswith("0")):
		now_hour = now_hour[1]

	now_minute = datetime.now().strftime("%M")
	if(now_minute.startswith("0")):
		now_minute = now_minute[1]
	if(now_minute == "30"):
		now_hour = "meia"

	return "São " + now_hour + " horas e " + now_minute + " minutos."

while(True):
	frase = listen_microphone()

	if(frase[1] == False):
		continue

	if(frase[0].lower().count('betina') > 0):
		create_audio("E ai ? Tudo bem com você ? ", "Listened")
		frase = listen_microphone()

		if(frase[0].lower().count('horas') > 0):	
			create_audio(treat_time(), "Listened")

		if(frase[0].lower().count('boa noite') > 0):	
			create_audio("Boa noite! Vou me desligar também!", "Listened")
			break
	