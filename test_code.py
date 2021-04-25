from gtts import gTTS
import pygame
from pygame import mixer
import playsound
from pydub import AudioSegment
from pydub.playback import play

def say(text):
    tts = gTTS(text)
    tts.save('tts_output.mp3')
    pygame.mixer.init(28000)
    pygame.mixer.music.load('tts_output.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    #sound = AudioSegment.from_mp3('tts_output.mp3')
    #sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={'frame_rate': int(sound.frame_rate * 1.2)})
    #faster = sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)
    #play(faster)
    
say('testing audio testing audio')
print('test')
