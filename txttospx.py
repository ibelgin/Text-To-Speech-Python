#Program to Convert Text To Speech 
from gtts import gTTS 
import os
f=open("test.txt") #The File Which It Will Read
text=f.read()
out=gTTS(text=text,lang='en',slow=False)
out.save("spc.mp3")
os.system("start spc.mp3")
 
