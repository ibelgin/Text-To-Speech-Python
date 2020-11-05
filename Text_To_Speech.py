#Program to Convert Text To Speech 

from gtts import gTTS 
import os

#The File Which It Will Read
f=open("test.txt") 
text=f.read()

# Change The Language If Needed And Change slow=True 
# If you Want the speed to be increased

out=gTTS(text=text,lang='en',slow=False)

# Saves the File In The Programs Destination

out.save("spc.mp3")

# For Playing The File ( Its Plays the song via the default MP3 Player)

os.system("start spc.mp3")

 
