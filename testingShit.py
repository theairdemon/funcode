# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 20:04:19 2020

@author: hgall
"""

def testfunc(x):
    print(x)
    

testdict = { 'func': testfunc}

testdict['func'](123)