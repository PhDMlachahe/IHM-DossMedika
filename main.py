#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import *
import pandas as pd


df = pd.DataFrame({'Nom': ["Nada","Patrcik","Roero", "Helene"], 'Salaire':[s*500 for s in range(4)]})

df['Enfant'] = [3,4,5,6]

df.drop(0, inplace=True)

print(df)


