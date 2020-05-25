#Program to Convert Text To Speech 
from gtts import gTTS 
import os
f=open("test.txt") #The File Which It Will Read
text=f.read()
# Change The Language If Needed And Change slow=True if you Want the speed to be increased
out=gTTS(text=text,lang='en',slow=False)
# Saves the File In The Programs Destination
out.save("spc.mp3")
# For Playing The File ( Its Plays the song via the default MP3 Player )
os.system("start spc.mp3")
 
