### ICT_speech
Takes .wav files and outputs the number of silences, words per minute and word frequency

## Assumptions:
  The audio file is .wav format
  There is a stable internet connection

## Lanuguage and library requirements:
  python 3.7
  SpeechRecognition
  pydub

## Instructions:
  Import the speech_processing.py file
  The following args need to be passed to the Speech class:
    :param audio_file_name: (String) location of the audio file
    :param noise(default = False): (Bool) if the file contains noises apart from speech
    :param silence_duration(default = 100): (int) minimum silence duration in ms
    :param silence_threshold(default = -16): (int) maximum silence threshold in db
  The output text file will be saved in the output directory in the following format:
    ```'output/{}_output.txt'.format(self.audio_file.replace('.', '_')```
    example : harvard.wav will be saved as harvard_wav_output.txt in output directory
  # Sample Code:
      ```from speech_processing.py import Speech
         speech = Speech("Output 1-3.wav",noise=True,silence_duration=100,silence_threshold=-16)
         speech.silenceDetection()
         speech.wordsPerMinute()
         speech.wordFrequency()
      ```
## Code explaination:
  The Speech class uses pydub library to detect the number of silences, the silences are categorised with a minimum duration in ms and a maximum threshold in db.
  It uses SpeechRecognition library to use google translate for recognising speech, this requires an active internet connection.
  Also if the audio contains noise other than speech, we can set ```noise = True```, so that the first 0.5 seconds will be used to adjust the audio file for ambient noise.
  If no Internet connection is available or no words are recognised, then the ouput file will mention that.
  
