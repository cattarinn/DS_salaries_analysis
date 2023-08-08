# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:30:04 2023

@author: Катя
"""

import webscraper as wb
import pandas as pd
path = 'C:/Users/Катя/Documents/DS_salaries_analysis/chromedriver.exe'

df = wb.get_jobs('data scientist', 15, False, path, 15)