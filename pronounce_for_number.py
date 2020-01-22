#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author   : MuyunLi
Date     : 2019/11/22 18:07
FileName : pronounce_for_number.py
"""

import pyttsx3
from time import sleep
import random
total = 3


def supplementDate(number):
    if number<10:
        return str(u"0%s" % number)
    return str(number)

def supplementSpeechDate(number):
    return  str(u"%sth" % number)


def generateDate(total):
    dateList = []
    for i in range(total):
        year = random.randint(1000,2100)
        month = random.randint(1,12)
        date = random.randint(1,31)

        d = u"%s-%s-%s" %(str(year),supplementDate(month),supplementDate(date))
        dateList.append(d)
    return dateList

def generateDateSpeech(total):
    date_list = [u"January",u"February",u"March",u"April",u"May",u"June",u"July",
                 u"August",u"September",u"October",u"November",u"December"]
    dateList = []
    for i in range(total):
        year = random.randint(1000, 2100)
        monthNumber = random.randint(0, 11)
        month = date_list[monthNumber]
        date = random.randint(1, 31)

        d = u"%s %s, %s" % (str(month), supplementSpeechDate(date),year)
        dateList.append(d)
    return dateList

def generateNumber(total,digit):
    returnList = []
    for i in range(total):
        random_number = random.randint(0,digit)
        returnList.append(str(random_number))

    return returnList


def generatePrice(total):
    priceList = []
    for i in range(total):
        temp = random.randint(0,10)
        if temp < 5:
            priceFloat = round(random.random()*100,2)
            price = u"$%s" % priceFloat
        else:
            priceFloat = round(random.random()*10,2)
            price = u"$%s" % priceFloat
        priceList.append(price)

    return priceList


def pronounce(pronounce_list):
    for i in pronounce_list:
        print i

    for i in pronounce_list:
        engine.say(i)
        engine.runAndWait()
        sleep(0.05)

if __name__ == '__main__':

    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 200)

    engine.say(u"Now, Let's begin a dictation under 100")
    engine.runAndWait()
    numberHundredList = generateNumber(total, 100)
    pronounce(numberHundredList)

    engine.say(u"Now, Let's begin a dictation under 10000")
    engine.runAndWait()

    numberTenThousandList = generateNumber(total, 10000)
    pronounce(numberTenThousandList)

    engine.say(u"Now, Let's begin a dictation of the price")
    engine.runAndWait()
    priceList = generatePrice(total)
    pronounce(priceList)

    engine.say(u"Now, Let's begin a dictation of the date")
    engine.runAndWait()
    dateList = generateDate(total)
    pronounce(dateList)

    dateSpeechList = generateDateSpeech(total)
    pronounce(dateSpeechList)





