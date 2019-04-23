import sys # Library needed to use sys.exit(1) from line 14 
import time # Library needed to use time.sleep(0.1) from line 72 
import pygame # Library needed to play the piano sounds through the speaker 
import Adafruit_MPR121.MPR121 as MPR121 # Library needed to use the functions necessary to interact with Touch Hat 


print 'Adafruit MPR121 Capacitive Touch Audio Player Test' 

cap = MPR121.MPR121() 

print 'Error initializing MPR121. Check your wiring!' sys.exit(1) 

pygame.mixer.pre_init(44100, -16, 12, 512) 
pygame.init() # initialize the mixer for sound loading and playback 

sounds = [pygame.mixer.Sound('/home/pi/A.wav'), 
  pygame.mixer.Sound('/home/pi/B.wav'), pygame.mixer.Sound('/home/pi/D.wav'), 
  pygame.mixer.Sound('/home/pi/E.wav'), pygame.mixer.Sound('/home/pi/F.wav'), 
  pygame.mixer.Sound('/home/pi/G.wav')] 

for i in range(6):
  sounds[i].set_volume(1) 

try:
  while True:
    if cap.is_touched(0): 
      print 'Pin 0 is being touched!' 
      sounds[0].play() 
    if cap.is_touched(1): 
      print 'Pin 1 is being touched!' 
       sounds[1].play() 
    if cap.is_touched(2): 
      print 'Pin 2 is being touched!' 
      sounds[2].play() 
    if cap.is_touched(3): 
      print 'Pin 3 is being touched!' 
      sounds[3].play() 
    if cap.is_touched(4): 
      print 'Pin 4 is being touched!' 
      sounds[4].play() 
    if cap.is_touched(5): 
      print 'Pin 5 is being touched!' 
      sounds[5].play() 

except: 
  print 
