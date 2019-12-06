#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Alex Colombari (http://github.com/alexcolombari)
Date: 2019-08-19
Usage: python youtube.py
Return: Play the song that you've searched
"""

import os
import requests
import webbrowser

try:
    from bs4 import BeautifulSoup
except:
    os.system("pip install bs4")


    input_func = None
try:
    input_func = raw_input('Enter the song to be played: ')
except NameError:
    input_func = input('Enter the song to be played: ')

query = input_func.replace(' ', '+')

# search for the best similar matching video
url = 'https://www.youtube.com/results?search_query=' + query
source_code = requests.get(url,timeout=15)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

# fetches the url of the video
songs = soup.findAll('div', {'class': 'yt-lockup-video'})
song = songs[0].contents[0].contents[0].contents[0]

try:
    link = song['href']
    webbrowser.open('https://www.youtube.com' + link)
except KeyError:
    print("Can't find any song, check your network or try a new word")
