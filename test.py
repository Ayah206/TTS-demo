from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS

# tts = gTTS('hello')
# tts.save('hello.mp3')



texts = ['e', 'm', 'a']
sounds = './Ahh.mp3'
sound3 = AudioSegment.from_file('Ahh.mp3')
sound2 = AudioSegment.from_file('ehh.mp3')
sound1 = AudioSegment.from_file('MMm.mp3')
aa = AudioSegment.from_file('steve/01.wav')
bb = AudioSegment.from_file('steve/20.wav')
cc = AudioSegment.from_file('steve/09.wav')
dd = AudioSegment.from_file('steve/21.wav')


concatenated_sound = bb + aa + bb +aa

play(concatenated_sound)
# playsound('Ahh.mp3')
# playsound('output.wav')

sound = bb.append(aa, crossfade = 200).append(bb, crossfade = 50).append(aa, crossfade = 200)

play(sound)
