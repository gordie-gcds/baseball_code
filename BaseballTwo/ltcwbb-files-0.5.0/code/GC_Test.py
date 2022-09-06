'''
Created on Nov 16, 2021

@author: gordie.campbell
'''
import sqlite3
import pandas as pd
from os import path

def main():
    print("Testing...")
    
    # handle directories
    DATA_DIR = '/Users/nathan/baseball-book/data'
    HUNDRED_DIR = path.join(DATA_DIR, '100-game-sample')
    
    # create connection
    conn = sqlite3.connect(path.join(HUNDRED_DIR, 'baseball.sqlite'))


if __name__ == '__main__':
    main()