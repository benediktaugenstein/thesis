import os
import speech_recognition as sr
import time

speech_engine = sr.Recognizer()

languages = ['de', 'en', 'es', 'ru', 'it', 'fr']
#languages = ['hi', 'ml', 'mr', 'ur', 'gu', 'bn']

for folder in languages:

    correct = 0
    false = 0
    cnd = 0  # could not detect

    path = 'C:/path/to/audio/' + folder + '/'

    for file_no, file in enumerate(os.listdir(path)[0:50]):
        print(file_no + 1)
        file_path = path + file

        with sr.WavFile(file_path) as source:
            audio = speech_engine.record(source)
            max_conf = 0
            max_conf_adj = 0
            max_ln = ''
            max_ln_adj = ''
            for ln in languages:
                try:
                    result = speech_engine.recognize_google(audio, language=ln)['alternative'][0]
                    conf = result['confidence']
                    transcript = result['transcript']
                    #print(transcript)

                    letters = transcript.replace(' ', '')
                    letter_count = len(letters)
                    word_count = len(transcript.split())
                    conf_adj = conf #+ 0.005 * letter_count + 0.005 * word_count

                except:
                    conf_adj = 0

                if conf_adj > max_conf_adj:
                    max_conf_adj = conf_adj
                    max_ln_adj = ln

        if max_ln_adj == '':
            cnd += 1
        elif max_ln_adj == folder:
            correct += 1
        else:
            false += 1
        
        time.sleep(1)
        
    print(folder)
    print('Correct: ', correct)
    print('False: ', false)
    print('Could not detect: ', cnd, '\n')
    
    time.sleep(120)
    
