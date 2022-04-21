from posixpath import split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns







if __name__ == '__main__':
  
    """
        Main method
    """
    x_df = pd.read_csv('sample_data.csv')
    chromosomes = 20
    genes = 12
    generations = 2000
    population = np.random.uniform(-1,1,(chromosomes,genes))
    population = np.around(population,4)
    fitness = []
    
    population_reshaped = []
    for i in range(chromosomes):
        splitted = np.hsplit(population[i],2)
        for j in range(2):
            if j == 0:
                splitted[j] = np.reshape(splitted[j],(3,2))
            else:
                splitted[j] = np.reshape(splitted[j],(2,3))

            
            population_reshaped.append(splitted[j])

    population_reshaped = np.asarray(population_reshaped,dtype='object')
    population_reshaped = np.reshape(population_reshaped,(20,2))
    
    predict = []
    for j in range(chromosomes):
        for i in range(len(x_df)):
            x = x_df.loc[i,['X1','X2','X3']].to_numpy()
            x = np.reshape(x,(1,3))
            H = np.dot(x,population_reshaped[j][0])
            F = np.dot(H,population_reshaped[j][1])

            y_predict = np.sum(F,axis=-1)
            predict.append(abs(y_predict[0]-x_df.loc[i,['Y']][0]))
    
        x_df['Fitness'] = predict
        predict = []
        fitness.append(x_df['Fitness'].sum())
        x_df.drop(['Fitness'],inplace=True,axis=1)
    
    print(x_df.head())
    fitness = [round(i,3) for i in fitness] 
    print(fitness)
  
    """ for generation in range(generations):
        if generation % 200 == 0:
            print(("Generation:", generation)) """
    
  
    

