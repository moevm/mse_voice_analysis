# Инструмент анализа голосов на аудиозаписи

### Задача
Создать приложение командной строки, которое будет принимать на вход аудиофайлы (mp3), со следующей функциональностью:

* Идентификация диктора по набору контрольных образцов,
* Идентификация наличия нескольких дикторов на аудио,
* Вычисление и вывод фрагментов аудиозаписи для каждого из дикторов в файлы,
* Распознавание речи для каждого диктора (с указанием меток времени) с выводом в файл,
* Docker-контейнер для работы приложения.

Исследовательская составляющая - применение методов обработки аудио.


### Ссылка на таск трекер
https://github.com/moevm/mse_voice_analysis/projects/1


### Инструкция
Для корректной работы приложения необходимо его использовать на Ubuntu 18.04. Необходимо наличие установленного пакета python3 и make.
1. Скачать репозиторий:
```
git clone https://github.com/moevm/mse_voice_analysis.git
```
2. Перейти в скачанную папку:
```
cd mse_voice_analysis
```
3. Произвести установку: 
```
make install
```
4. Запустить программу:
```
mse_voice_analysis --help
```

Для удаления из папки артефактов сборки можно использовать команду `make clearbuild`

Для удаления приложения из терминала можно использовать команду `make uninstall`

Для работы с файлами формата mp3 будет необходимо скачать библиотеку ffmpeg.
1. Для Linux команды.
```
sudo add-apt-repository universe
sudo apt update
sudo apt install ffmpeg
```
2. Для Windows
Скачать биюлиотеку по ссылке https://www.ffmpeg.org/download.html и добавить для нее зависимость в переменные среды.
