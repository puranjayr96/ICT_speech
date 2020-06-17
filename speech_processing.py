from pydub import AudioSegment,silence
import speech_recognition as sr
from collections import defaultdict
import os
class Speech:
    """
    Speech processing class
    """
    def __init__(self,audio_file_name,noise = False,silence_duration = 100,silence_threshold = -16):
        """

        :param audio_file_name: (String) location of the audio file
        :param noise: (Bool) if the file contains noises apart from speech
        :param silence_duration: (int) minimum silence duration in ms
        :param silence_threshold: (int) maximum silence threshold in db
        """
        if audio_file_name == None:
            raise Exception("Audio file name not provided")
        self.supported = {"wav"}
        self.audio_file = audio_file_name
        self.silence_duration = silence_duration
        self.silence_threshold = silence_threshold
        self.audio_length = len(AudioSegment.from_wav(self.audio_file))
        self.words = None
        self.wpm = None
        self.wf = defaultdict(int)
        self.noise = noise
        if not os.path.exists('output'):
            os.makedirs('output')
        with open('output/{}_output.txt'.format(self.audio_file.replace('.','_')),'w') as f:
            f.write("For audio file: {}\n".format(self.audio_file))
        audio_file_name = audio_file_name.split('.')
        if audio_file_name[-1] not in self.supported:
            raise  Exception("Audio file not supported")
    def silenceDetection(self):
        """
        Detects number of silences which are below a certain threshold and last for atleast a  certain duration
        """
        audio = AudioSegment.from_wav(self.audio_file)
        silent = silence.detect_silence(audio,min_silence_len=self.silence_duration,silence_thresh=self.silence_threshold)
        with open('output/{}_output.txt'.format(self.audio_file.replace('.','_')),'a+') as f:
            f.write("Silence Detection:\n")
            f.write("\tThe number of silences of atleast {}ms duration and threshold of {}db is : {}\n".format(self.silence_duration,self.silence_threshold,len(silent)))
    def wordsPerMinute(self):
        """
        Detects the number of words spoken per minute using google translate
        """
        with open('output/{}_output.txt'.format(self.audio_file.replace('.', '_')), 'a+') as f:
            f.write("Words per minute:\n")
        audio_source = sr.AudioFile(self.audio_file)
        r = sr.Recognizer()
        with audio_source as source:
            if self.noise:
                r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.record(source)
        try:
            words = r.recognize_google(audio)
        except Exception as e:
            with open('output/{}_output.txt'.format(self.audio_file.replace('.', '_')), 'a+') as f:
                f.write("\tNo words or No internet connection\n")
            return
        self.words = words.split(' ') if words else []
        self.wpm = len(self.words)/(self.audio_length/60000)
        with open('output/{}_output.txt'.format(self.audio_file.replace('.', '_')), 'a+') as f:
            f.write("\twpm: {}\n".format(self.wpm))
    def wordFrequency(self):
        """
         Detects the frequency of each word spoken using Google translate
        """
        with open('output/{}_output.txt'.format(self.audio_file.replace('.', '_')), 'a+') as f:
            f.write("Word frequency:\n")
        audio_source = sr.AudioFile(self.audio_file)
        r = sr.Recognizer()
        with audio_source as source:
            if self.noise:
                r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.record(source)
        try:
            words = r.recognize_google(audio)
        except Exception as e:
            with open('output/{}_output.txt'.format(self.audio_file.replace('.', '_')), 'a+') as f:
                f.write("\tNo words or No internet connection\n")
            return
        self.words = words.split(' ') if words else []
        for word in self.words:
            self.wf[word]+=1
        with open('output/{}_output.txt'.format(self.audio_file.replace('.', '_')), 'a+') as f:
            f.write("\tThe word frequency is:{}\n".format(self.wf))


if __name__ == "__main__":
    speech = Speech("Output 1-3.wav",noise=True,silence_duration=100,silence_threshold=-16)
    speech.silenceDetection()
    speech.wordsPerMinute()
    speech.wordFrequency()