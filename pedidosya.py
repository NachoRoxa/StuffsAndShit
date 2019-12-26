#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import traceback
import time
import json
import sys
import os
import datetime
from PIL import Image
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from splinter import Browser

with Browser('firefox', headless=True) as browser:
    driver = browser.driver
    driver.set_window_size(1280, 1200)
    accounts = [
    ['nica.par@mailinator.com', '123456'],
    ['alfred.gonzalez@mailinator.com', '123456'],
    ['any.sky@mailinator.com', '123456'],
    ['alf.manriquez.z@gmail.com', '123456'],
    ['alf.fernandez@mailinator.com','123456'],
    ['ar.gomez@mailinator.com', '123456'],
    ['carm.rocha@mailinator.com', '123456'],
    ['esteban.gonzalez@mailinator.com', '123qwe'],
    ['esteban.quito@mailinator.com', '123456'],
    ['ig.quevedo@mailinator.com', '123456'],
    ['ig.rayen@mailinator.com', '123456'],
    ['ig.rocha@alumnos.duoc.cl', 'Cyn040212'],
    ['ig.toro@mailinator.com','123456'],
    ['nvapibvkdfvn@mailinator.com', '123456'],
    ['pete.anguila@mailinator.com', '123456'],
    ['qwerty@mailinator.com', '123456'],
    ['su.schultz@mailinator.com', '123456'],
    ['vale.quevedo@mailinator.com', '123456'],
    ['vale.ming@mailinator.com', '123456'],
    ['vale.rocha@mailinator.com', '123456'],
    ['wilsouls@gmail.com', 'Cyn040212']
    ]
    urlcupon = "https://www.pedidosya.cl/login?returnUrl=myVoucherWallet"
    url = "https://www.pedidosya.cl/login?returnUrl=myOrders"
    datetime = datetime.datetime.now()
    os.mkdir('/home/rocha/pedidosya/'+datetime.strftime("%H:%M:%S"))
    browser.visit(urlcupon)
    for account in accounts:
        time.sleep(1)
        browser.fill('email', account[0])
        browser.fill('password', account[1])
        browser.find_by_id('login').click()
        time.sleep(3)
        browser.driver.get_screenshot_as_file('/home/rocha/pedidosya/'+datetime.strftime("%H:%M:%S")+'/'+account[0]+'.png')
        time.sleep(2)
        driver.delete_all_cookies()
        time.sleep(2)
        browser.visit(urlcupon)
    sys.exit(0)
