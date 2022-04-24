import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





def matrix_convertion(population, chromosomes):
    # Convert our [chromosomes * genes] matrice into [chromosome * 2] and this matrice will contain [3*2] and [2*3] small matrices in each row for calculating our fitness

    population_reshaped = []
    for i in range(chromosomes):
        splitted = np.hsplit(population[i],2)
        for j in range(2):
            if j == 0:
                splitted[j] = np.reshape(splitted[j],(3,2))
            else:
                splitted[j] = np.reshape(splitted[j],(2,3))

            population_reshaped.append(splitted[j])
            

    population_reshaped = np.asarray(population_reshaped,dtype='object').reshape((chromosomes,2))
    return population_reshaped




if __name__ == '__main__':
  
    """
        Main method
    """
    x_df = pd.read_csv('sample_data.csv')
    chromosomes = 20
    genes = 12
    generations = 2000
    mattingSize = 12 # Parent size
    offSpringSize = chromosomes - mattingSize # children size
    population = np.random.uniform(-1,1,(chromosomes,genes))
    population = np.around(population,4)
    fitness = np.zeros(chromosomes)
    fitness_visualization = np.zeros((generations,chromosomes))
    # Gen creation will start from here
    for generation in range(generations):
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
            fitness_value = np.sqrt((y-y_predict)**2).sum() # Fitness Value Calculation
            fitness[i] = fitness_value 
        
        fitness = np.round(fitness,3)
        fitness_visualization[generation,:] = fitness
        parents = np.empty((mattingSize, genes))
        offspring = np.empty((offSpringSize, genes))


        if generation % 200 == 0:
            print(("Generation:", generation))
            print(('Fitness:', fitness))

            

        
        for i in range(mattingSize):    # Parent Selection
            minIndex = np.argmin(fitness)
            parents[i,:] = population[minIndex,:]
            fitness[minIndex] = 99999  # defining it to a very high value to not select it again
        
        
        for i in range(offSpringSize): #Crossover
            crossoverPoint = np.random.randint(0,genes) 
            parent1Index = i % mattingSize    # Mod operation to not go over array out of bounds
            parent2Index = (i+1)% mattingSize 
            offspring[i, 0: crossoverPoint] = parents[parent1Index, 0: crossoverPoint] # First Half
            offspring[i, crossoverPoint:] = parents[parent2Index, crossoverPoint:] # Second Half
       
        for i in range(offSpringSize): # Mutation
            randomIndex = np.random.randint(1,genes)
            randomValue = np.random.uniform(-1, 1, 1)
            randomValue= np.round(randomValue,4)
            offspring [i, randomIndex] = randomValue  # Assigning the random value generated to our offsprings some random gene
        
        
        population[0:mattingSize,:] = parents   # Repopulate our new generation
        population[mattingSize:,:] = offspring

   
    x = range(generations)
    y = fitness_visualization

    for xe, ye in zip(x, y):
        plt.scatter([xe] * len(ye), ye, s = 5)
    plt.title('100 row inputs 20 chromosomes matting size of 12, each color represent a chromosome')    
    plt.xlabel('# of generations')
    plt.ylabel('Fitness scores')
    plt.xticks([0,200,400,600,800,1000,1200,1400,1600,1800,2000])
    plt.ylim(0,30)
    plt.show()
    
    

