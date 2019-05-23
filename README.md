# converter_wav
Converter wav to mp3 filles
# Инсталяция пайтон скрипта на астериск (конвертер файлов)

Manual all OS
install python3  https://realpython.com/installing-python/


Centos

python --version
pip --version
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python get-pip.py
python -m pip install --upgrade pip setuptools wheel


#Ins

tall Modules python 
python -m pip install pydub
pip install pydub



#Изменение версии пайтона в системе
# which python
# /usr/bin/python
# ls -l /usr/bin/python

ls -l /usr/bin/python
/usr/bin/python -> python2.7
ln -f -s  /usr/bin/python3.5  /usr/bin/python 
python -v;


Debian
# Установка дополнительного софта
# libav
apt-get install libav-tools libavcodec-extra

# ffmpeg
apt-get install ffmpeg libavcodec-extra

CENT OS






# Созание скрипта
mkdir /mp3_rec/
mkdir /script_asterisk/
touch /script_asterisk/converter.py
chmod 755 /script_asterisk/
chmod +x /script_asterisk/converter.py
chown root:root /script_asterisk/converter.py # сли нужно измениеть пользователя

vim /etc/asterisk/extensions.conf

[call-out]
	exten => h,1,System(/script_asterisk/converter.py)

[call-in]
	exten => h,1,System(/script_asterisk/converter.py)
