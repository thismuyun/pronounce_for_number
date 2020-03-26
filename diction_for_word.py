#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author   : MuyunLi
Date     : 1/22/20 1:13 PM
FileName : diction_for word.py
"""

import pyttsx3
from time import sleep
import pandas as pd

sleep_time = 1
loop_time = 3

dictation_word_path = '/Users/muyunli/Limuyun/diction/dictation.xlsx'


def getElement(fileName, columName):
    pd_csv = pd.read_excel(fileName)
    unknowWords_lis = pd_csv[columName].tolist()
    return unknowWords_lis


def getNewWordList():
    newWordList = getElement(dictation_word_path, 'word')
    return newWordList


def pronounce(pronounce_list):
    for i in pronounce_list:
        print i

    for i in pronounce_list:

        for j in range(0, loop_time):
            engine.say(i)
            engine.runAndWait()
            sleep(sleep_time)


def pronounce_chinese(pronounce_dict):
    for k, v in pronounce_dict.items():
        engine.say(k)
        engine.say(v)
        engine.runAndWait()
        sleep(3)


def generateWordList(newWordList):
    word_list = []
    for idx, corpus in enumerate(newWordList):
        zh_en = corpus.split('*')
        word_list.append(zh_en[0].strip().lower())
    return word_list


def generterChineseAndEnglishDict(newWordList):
    word_dict = {}
    for idx, corpus in enumerate(newWordList):
        zh_en = corpus.split('*')
        word = zh_en[0].strip().lower()
        explain = zh_en[1]
        word_dict[word] = explain

    return word_dict


if __name__ == '__main__':
    newWordList = getNewWordList()
    print newWordList

    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 200)

    engine.say(u"Now, Let's begin a dictation ")
    engine.runAndWait()

    numberHundredList = generateWordList(newWordList)
    pronounce(numberHundredList)

    # chineseAndEnglishDict = generterChineseAndEnglishDict(newWordList)
    #
    # pronounce_chinese(chineseAndEnglishDict)
