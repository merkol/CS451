import numpy as np
import pandas as pd
def matrix_convertion(population, chromosomes):
    # Convert our [chromosomes * genes] matrice into [chromosome*2] and this matrice will contain [3*2] and [2*3] small matrices in each row

    population_reshaped = []
    for i in range(chromosomes):
        splitted = np.hsplit(population[i],2)
        for j in range(2):
            if j == 0:
                splitted[j] = np.reshape(splitted[j],(3,2))
            else:
                splitted[j] = np.reshape(splitted[j],(2,3))

            population_reshaped.append(splitted[j])
            

    population_reshaped = np.asarray(population_reshaped,dtype='object').reshape((20,2))
    return population_reshaped

def selection_and_crossover(population,fitness_array):
    temp_array = np.copy(fitness_array)
    indice = list()
    marked = set()
    for i in range(temp_array.size):
        value = np.argmin(temp_array)
        temp_array[value] = 5000
        if value not in marked:
            indice.append(value)
        if len(indice) == 2:
            ## Crossover
            rand = np.random.randint(3,8)
            temp = np.copy(population[indice[0],rand:])
            population[indice[0],rand:] = population[indice[1],rand:]
            population[indice[1],rand:] = temp
            marked.add(indice[0])
            marked.add(indice[1])
            
            indice = []
    
    return population

def mutation(population):
    for i in population:
        rand = np.random.randint(0,10)
        for j in i:
            if rand==2:
                j = j*-1






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
    fitness_array = np.zeros(chromosomes)
  
    
    # Gen creation will start from here
    for generation in range(generations+1):
        population_reshaped = matrix_convertion(population,chromosomes)
        #Below loop is fitness calculation
        for i in range(chromosomes):
            x = x_df.loc[:,['X1','X2','X3']].to_numpy()
            x = np.reshape(x,(100,3))
            H = np.dot(x,population_reshaped[i][0])
            F = np.dot(H,population_reshaped[i][1])

            y_predict = np.sum(F,axis=-1)
            y = x_df.loc[:,['Y']].to_numpy()
            y = np.reshape(y,(100,))
            fitness_value = np.sqrt((y-y_predict)**2).sum() 
            fitness_array[i] = fitness_value 
            
        
        fitness_array = np.round(fitness_array,3)
        population = selection_and_crossover(population,fitness_array)
        mutation(population)


        if generation % 200 == 0:
            print(("Generation:", generation))
            print(('Fitness:', fitness_array))

            
            


   
    

