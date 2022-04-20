from posixpath import split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns







if __name__ == '__main__':
  
    """
        Main method
    """
    
    chromosomes = 20
    genes = 12
    generations = 2000
    population = np.random.uniform(-1,1,(chromosomes,genes))
   
    #arr = np.zeros(shape=(chromosomes,2))
    a = []
    for i in range(chromosomes):
        splitted = np.hsplit(population[i],2)
        for j in range(2):
            if j == 0:
                splitted[j] = np.reshape(splitted[j],(3,2))
            else:
                splitted[j] = np.reshape(splitted[j],(2,3))
    
            b = splitted[j]
            a.append(b)
    a = np.asarray(a)                 
    print(a[1])
    #reshaped = np.reshape(splitted[0],(3,2))
    """ for generation in range(generations):
        if generation % 200 == 0:
            print(("Generation:", generation)) """
    
  
    

