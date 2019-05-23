# cat << EOF | tee - a / script_asterisk / converter.py
#!/usr/bin/python

import os
import pydub
import glob
import timeit
import subprocess
import sys

wav_dir = glob.glob('/records/*.wav')             # ищем файлы с разрешением *.wav (входящая директория)

output_mp3 = "/mp3_rec/"                              # имя выходящей директори                  
input_wav = "/records/" 

for wav_dir in wav_dir:                           # генерация строки  из  waw файлов = Имя файла без расширения и пути 
    name =os.path.split(wav_dir)[1]               # для записи в новый путь и с новым именем. 
    wav_names = os.path.splitext(name)[0]
    mp3_names = os.path.splitext(name)[0]+'.mp3'
    mp3_path = output_mp3 + mp3_names
    wav_path = input_wav + name
    if os.path.exists(mp3_path):                                                            # проверяем массив array_mp3 на имена  ( из папки mp3_dir)
        print("Файл существует = "+wav_names)
    elif os.path.getsize(wav_path) > 44:
        print("Новый файл = "+wav_names)
        #subprocess.call(['ffmpeg', '-i', wav_dir, mp3_path])                             # конвертируем ffmpeg вызовом subprocess
        os.system("ffmpeg"+" "+"-i"+" "+ wav_dir +" "+ mp3_path)
        #sound = pydub.AudioSegment.from_wav(wav_dir)
        #sound.export(mp3_path, format="mp3")
        
#subprocess.call('find /records/ -type f -mtime +14 -exec rm -rf {} \;', shell=True)     # удаление файлов из wav_dir, старше 30 дней вызовом subprocess
os.system("find /records/ -type f -mtime +14 -exec rm -rf {} \;")                       # тоже самое только  вызовом os.system

#time_in = timeit.default_timer()- time
#time_out = time_in/60
#print('Время выполнения=', time_out, 'минут')
#sys.exit()

# EOF
