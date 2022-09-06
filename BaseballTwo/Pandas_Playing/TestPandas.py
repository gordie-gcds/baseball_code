'''
Created on Oct 18, 2021

@author: gordie.campbell
'''

import pandas as pd
from os import path

def main():
    
    DATA_DIR='C:\\Users\gordie.campbell\eclipse-workspace\gcds\python\BaseballTwo\ltcwbb-files-0.5.0\data'

    #DATA_DIR="/BaseballTwo/Pandas_Playing/TestPandas.py"
    players = pd.read_csv(path.join(DATA_DIR, '2018-season', 'players.csv'))
    
    print(players)
    
    type(players)
    
    print('wingrove')



if __name__ == '__main__':
    main()