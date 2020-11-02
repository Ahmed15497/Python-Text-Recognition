# Python-Text-Recognition
Python text recognition from an image code (Iphone screenshots)

This project aims for text recgnition using [EasyOCR](https://github.com/JaidedAI/EasyOCR) from known places inside the image. It extracts the text then stack them inside a CSV.

The dataset is a bunch of screenshots from Iphone from music sets.

Input: The path of the folder containing the images.
Logic: For each image inside the folder extract the title, artist and the current time.
Output: A csv file contains (file name, date taken, title, artist, current time)

you can run the program from command shell using this command : python screenshots_OCR.py ./put_your_folder_path_here

