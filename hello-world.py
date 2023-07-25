# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 06:13:39 2023

@author: user
"""

yosh = int(input('yoshingiz nechida? '))
if yosh<=4:
    narx = 0
elif yosh<=12:
    narx = 5000
elif yosh<=18:
    narx = 8000
else: narx = 10000
print(f"Sizga kirish {narx} so'm")
#izoh qo'shdim