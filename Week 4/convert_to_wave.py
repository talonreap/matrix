import sound
import stereosound as myfile
# ??? should be replaced with the name of
#the file which has your functions.

#Read the statements and comments below.
#You will need to make appropriate changes to the statements
#to work with different wav files and test various functions
#you have written.

#Converts the sound in love.wav file to a Sound object.
love = sound.Sound(filename='love.wav')


#The function rem_vocals written in the stereosound module is called
#and the Sound object it returns is assigned to remvocals.
remvocals = myfile.rem_vocals(love)

#The Sound object remvocals is converted to sound in
#a wav file called lovenovocals.wav.
#This wav file did not exist before but is newly created.
remvocals.save_as('lovenovocals.wav')


#Prompts the user to chose a fade length they want
#fade_length = raw_input("Please enter fade length: ")
#Converts the sound in water.wav file to a Sound object.
#wave = sound.Sound(filename='water.wav')


#The function fade_in written in the stereosound module is called
#and the Sound object it returns is assigned to fadein.
#fadein = myfile.fade_in(wave,fade_length)

#The Sound object fadein is converted to sound in
#a wav file called fadeinwave.wav.
#This wav file did not exist before but is newly created.
#fadein.save_as('fadeinwave.wav')


#Converts the sound in rain.wav file to a Sound object.
#raindrops = sound.Sound(filename='rain.wav')


#The function fade_in written in the stereosound module is called
#and the Sound object it returns is assigned to fadein.
#fadeout = myfile.fade_out(raindrops,fade_length)

#The Sound object fadein is converted to sound in
#a wav file called fadeinwave.wav.
#This wav file did not exist before but is newly created.
#fadeout.save_as('fadeoutwave.wav')


#Converts the sound in grace.wav file to a Sound object.
#gracewave = sound.Sound(filename='grace.wav')


#The function fade written in the stereosound module is called
#and the Sound object it returns is assigned to fade.
#fade = myfile.fade(gracewave,fade_length)

#The Sound object fade is converted to sound in
#a wav file called gracefade.wav.
#This wav file did not exist before but is newly created.
#fade.save_as('gracefade.wav')
