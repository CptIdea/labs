#!/usr/bin/env python
# encoding: utf-8

import npyscreen
import random
import os
import sys
from functions import allfunctions

# def toConsole(F, lab, num, var):
#     allFunctions[lab][num]
lab = 0
nom = 0

def main(*args):
    F  = npyscreen.ActionForm(name = "Запускатор лаб Mark 1",footer=None)
    
    F._clear_all_widgets()
    ls = F.add(npyscreen.SelectOne,value=[lab], values = ["Лаба 1","Лаба 2","Лаба 3","Лаба 4","Лаба 5"],max_height=6,exit_right=True,exit_left=True)
    ns = F.add(npyscreen.SelectOne,value=[nom], values = ["Номер 1","Номер 2","Номер 3","Номер 4"],max_height=5,rely=2,relx=20,exit_right=True,exit_left=True)
    F.on_cancel = sys.exit
    F.edit()
    return (ls.value[0],ns.value[0])

       

while True:
    lab,nom = npyscreen.wrapper_basic(main)
    os.system('clear')
    print(f'===== Лаба {lab+1} Задание {nom+1} =====')
    allfunctions[lab][nom]()
    input("Enter чтобы продолжить")
