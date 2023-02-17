from pydub import AudioSegment
from pydub.playback import play

#Load an audio file
myAudioFile = "tone.wav"
sound1 = AudioSegment.from_file(myAudioFile, format="wav")

#Invert phase of audio file
sound2 = sound1.invert_phase()

#Merge two audio files
combined = sound1.overlay(sound2)

#Export merged audio file
sound2.export("outAudio.wav", format="wav")

#Play audio file :
#should play nothing since two files with inverse phase cancel each other
# mergedAudio = AudioSegment.from_wav("outAudio.wav")
# play(sound2)