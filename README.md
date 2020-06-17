### ICT_speech
Takes .wav files and outputs the number of silences, words per minute and word frequency

## Assumptions:
  The audio file is .wav format
  There is a stable internet connection

## Language and library requirements:
  - python 3.7
  - SpeechRecognition
  - pydub

## Instructions:
  - run test.py
  - The following args need to be passed to test.py:
    * :param filename: (String) location of the audio file
    * :param noise(default = False): (Bool) if the file contains noises apart from speech
    * :param sd(default = 100): (int) minimum silence duration in ms
    * :param st(default = -16): (int) maximum silence threshold in db
  - The output text file will be saved in the output directory in the following format:
    * ```'output/{}_output.txt'.format(self.audio_file.replace('.', '_')```
    * example : harvard.wav will be saved as harvard_wav_output.txt in output directory
  # Sample:
      ```python test.py 'harvard.wav' --sd 100
      ```
## Code explaination:
  - The Speech class uses pydub library to detect the number of silences, the silences are categorised with a minimum duration in ms and a maximum threshold in db.
  - It uses SpeechRecognition library to use google translate for recognising speech, this requires an active internet connection.
  - Also if the audio contains noise other than speech, we can set ```noise = True```, so that the first 0.5 seconds will be used to adjust the audio file for ambient noise.
  - If no Internet connection is available or no words are recognised, then the ouput file will mention that.
  
