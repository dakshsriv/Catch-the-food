from pygame import mixer

file = 'sample.mp3'
#file = 'file_example_OOG_5MG.ogg'
#file = 'bullet.wav'
#file = '/usr/share/sounds/sound-icons/electric-piano-3.wav'
mixer.init()
mixer.music.load(file)
mixer.music.play(0)
