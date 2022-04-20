import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns







if __name__ == '__main__':
  
    """
        Main method
    """
    
    chromosomes = 16
    genes = 12
    generations = 2000
    population = np.random.uniform(-1,1,(chromosomes,genes))
   
    #splitted = np.hsplit(population,2)
    for generation in range(generations):
        if generation % 200 == 0:
            print(("Generation:", generation+1))
    
  
    

