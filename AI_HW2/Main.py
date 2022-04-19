import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def return_random_population(population_size, chromosome_size, gene_set):
    '''Returns a random initialised population

    This funtion initialise a matrix of integers using numpy randint.
    @param chromosome_size 
    @param population_size
    @param gene_set list or array containing the gene values
    @return matrix of integers size:
         population_size x chromosome_size
    '''
    return np.random.choice(gene_set, size=(population_size,chromosome_size))



if __name__ == '__main__':
  
    """
        Main method
    """
    population_size = 16
    chromosome_size = 12
    gene_set = np.arange(-1,1,0.0001).tolist()
    population = return_random_population(population_size,chromosome_size,gene_set)
    

