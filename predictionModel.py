import numpy as np

class PredictionModel():
    
    def __init__(self):

        # generating the seed for the random number
        np.random.seed(1)       
        
        # coverting the weights, based on a 3 integer array representing information
        # about the train route, and a 1 integer array based on whether the train is 
        # late or not
        self.weights = 2 * np.random.random((3, 1)) - 1 

    # applies the sigmoid function
    def sigmoid(self, x):
        
        return 1 / (1 + np.exp(-x))


    # calculates the derivative to the sigmoid function above  
    def sigmoidDerivative(self, x):
        
        return x * (1 - x)
    

    # trains the prediction model to understand and learn the outcomes of the train
    # routes based on the information given by the 2 arrays mentioned above   
    def train(self, routeInformation, routeLate, trainingIterations):
        
        for iteration in range(trainingIterations):
            
            # iterates through each instance of a train route information
            output = self.think(routeInformation)

            # computes the back propogation outcome
            error = routeLate - output
            
            # adjusts weights using sigmoid derivative to enhance accuracy
            adjustments = np.dot(routeInformation.T, error * self.sigmoidDerivative(output))

            self.weights += adjustments
            
            
    # passes new data through the instances in the model to receive accurate
    # prediction based on the weights calculated earlier  
    def think(self, inputs):
        
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.weights))
        return output    
    
    def timeMean(self, times):
        
        mean = 0
        count = 0
        
        for number in times:
            mean = (mean + number) 
            count += 1
    
        mean = mean / count
        
        mean = int(round(mean))
        
        return mean
            
if __name__ == "__main__":
    
    trainPredictions = PredictionModel()
    trainDeparture = str(input("What station are you departing from?: "))
    trainDeparture = trainDeparture.lower()
     
    trainDestination = str(input("What station is your destination?: "))
    trainDestination = trainDestination.lower()
    
    trainRoute = trainDeparture + " to " + trainDestination
    
    print("Your route is", trainRoute)
    
    dayOfTravel = str(input("What day are you travelling?: "))
    dayOfTravel = dayOfTravel.lower()
    if dayOfTravel == 'sunday' or 'saturday':
        
        day = 1
        
    else:
      
        day = 0
             
    numberOfStops = int(input("How many stops are on your journey?: "))
    if numberOfStops > 1:
        
        stops = 1
        
    else:
        
        stops = 0
    
    timeOfDay = str(input("Are you travelling in the morning, afternoon or evening?: "))
    timeOfDay = timeOfDay.lower()
    if timeOfDay == 'morning' or 'evening':
        
        time = 1
        
    else:
        
        time = 0
    
    if trainDeparture == 'london':
        
        routeInformation = np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
                                     [0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],
                                     [0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],
                                     [0,1,1],[0,1,1],[0,1,1],[0,1,1],[0,1,1],
                                     [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                                     [1,0,1],[1,0,1],[1,0,1],[1,0,1],[1,0,1],
                                     [1,1,0],[1,1,0],[1,1,0],[1,1,0],[1,1,0],
                                     [1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]])
        routeLate        = np.array([[0     , 0     , 0     , 1     , 0   , 
                                      0     , 1     , 0     , 1     , 1   ,
                                      1     , 1     , 1     , 0     , 0   ,
                                      1     , 0     , 0     , 1     , 0   ,
                                      0     , 0     , 0     , 0     , 0   ,
                                      0     , 0     , 1     , 1     , 0   ,
                                      0     , 1     , 0     , 0     , 1   ,
                                      1     , 0     , 1     , 0     , 0]]).T
    
        delayTimes = {5, 12, 7, 1, 27, 11, 29, 34, 16, 18, 28, 4, 16, 34, 22, 
                      6, 3, 29, 6, 19, 22, 48, 17, 53, 2, 54, 13, 17, 3, 6, 4,
                      8, 12, 67, 17, 42, 12, 53, 36, 31, 5, 8, 16, 14, 5, 6, 2}
        
    elif trainDeparture == 'norwich':
            
        routeInformation = np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],    
                                     [0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],
                                     [0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],
                                     [0,1,1],[0,1,1],[0,1,1],[0,1,1],[0,1,1],
                                     [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                                     [1,0,1],[1,0,1],[1,0,1],[1,0,1],[1,0,1],
                                     [1,1,0],[1,1,0],[1,1,0],[1,1,0],[1,1,0],
                                     [1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]])
        routeLate        = np.array([[0     , 0     , 0     , 0     , 0   , 
                                      0     , 1     , 0     , 0     , 1   ,
                                      0     , 1     , 0     , 0     , 0   ,
                                      1     , 0     , 0     , 1     , 0   ,
                                      0     , 0     , 0     , 0     , 0   ,
                                      0     , 0     , 0     , 1     , 0   ,
                                      0     , 1     , 0     , 0     , 0   ,
                                      1     , 0     , 1     , 0     , 0]]).T
    
        delayTimes = {10, 2, 5, 8, 3, 12, 4, 5, 2, 2, 15, 35, 15, 3, 17, 31, 26,
                      4, 16, 4, 21, 4, 1, 41, 24, 6, 3, 7, 16, 14, 4, 7, 11, 5,
                      7, 2, 9, 4, 16, 21, 20, 10, 4, 20, 5}
    
    elif trainDeparture == 'cambridge':
            
        routeInformation = np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],    
                                     [0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],
                                     [0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],
                                     [0,1,1],[0,1,1],[0,1,1],[0,1,1],[0,1,1],
                                     [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                                     [1,0,1],[1,0,1],[1,0,1],[1,0,1],[1,0,1],
                                     [1,1,0],[1,1,0],[1,1,0],[1,1,0],[1,1,0],
                                     [1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]])
        routeLate        = np.array([[0     , 0     , 0     , 0     , 0   , 
                                      0     , 0     , 0     , 0     , 0   ,
                                      0     , 1     , 0     , 0     , 0   ,
                                      1     , 0     , 0     , 0     , 0   ,
                                      0     , 0     , 0     , 0     , 0   ,
                                      0     , 0     , 0     , 0     , 0   ,
                                      0     , 0     , 0     , 1     , 0   ,
                                      1     , 0     , 0     , 0     , 0]]).T
    
        delayTimes = {1, 3, 3, 6, 2, 3, 4, 8, 1, 3, 6, 3, 9, 12, 3, 8, 10, 3, 1,
                      6, 18, 4, 8, 23, 36, 4, 7, 14, 20, 17, 5, 3, 9, 10, 3, 9,
                      4, 6, 13, 36, 5, 4, 8, 8, 5, 7, 14, 4, 2, 5, 6, 6, 2}
        
    elif trainDeparture == 'manchester':
            
        routeInformation = np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],    
                                     [0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],
                                     [0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],
                                     [0,1,1],[0,1,1],[0,1,1],[0,1,1],[0,1,1],
                                     [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                                     [1,0,1],[1,0,1],[1,0,1],[1,0,1],[1,0,1],
                                     [1,1,0],[1,1,0],[1,1,0],[1,1,0],[1,1,0],
                                     [1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]])
        routeLate        = np.array([[0     , 1     , 1     , 0     , 0   , 
                                      1     , 1     , 1     , 0     , 0   ,
                                      0     , 1     , 1     , 1     , 0   ,
                                      1     , 1     , 1     , 0     , 1   ,
                                      0     , 1     , 0     , 0     , 1   ,
                                      1     , 0     , 0     , 1     , 0   ,
                                      0     , 1     , 0     , 0     , 0   ,
                                      0     , 0     , 0     , 1     , 1]]).T
    
        delayTimes = {12, 4, 16, 2, 5, 18, 27, 43, 16, 25, 32, 4, 14, 10, 35, 9,
                      26, 20, 8, 14, 6, 12, 10, 18, 25, 30, 26, 13, 8, 16, 35,
                      8, 4, 24, 10, 34, 16, 5, 8, 9, 16, 2, 6, 3, 26, 3, 8, 10}
    
    elif trainDeparture == 'newcastle':
            
        routeInformation = np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],    
                                     [0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],
                                     [0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],
                                     [0,1,1],[0,1,1],[0,1,1],[0,1,1],[0,1,1],
                                     [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                                     [1,0,1],[1,0,1],[1,0,1],[1,0,1],[1,0,1],
                                     [1,1,0],[1,1,0],[1,1,0],[1,1,0],[1,1,0],
                                     [1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]])
        routeLate        = np.array([[1     , 1     , 0     , 0     , 0   , 
                                      0     , 1     , 1     , 1     , 0   ,
                                      0     , 1     , 0     , 1     , 1   ,
                                      1     , 0     , 0     , 0     , 1   ,
                                      0     , 0     , 0     , 0     , 1   ,
                                      1     , 1     , 0     , 0     , 0   ,
                                      0     , 0     , 0     , 1     , 1   ,
                                      0     , 1     , 0     , 0     , 0]]).T
    
        delayTimes = {9, 24, 18, 7, 29, 21, 7, 18, 35, 19, 23, 22, 10, 4, 6, 4,
                      18, 22, 20, 13, 4, 8, 2, 19, 6, 7, 3, 5, 12, 6, 5, 4, 9,
                      4, 9, 19, 24, 43, 1, 4, 15, 7, 38, 47, 12, 30, 3, 6, 1, 3}
    
    elif trainDeparture == 'bristol':
            
        routeInformation = np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],    
                                     [0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],
                                     [0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],
                                     [0,1,1],[0,1,1],[0,1,1],[0,1,1],[0,1,1],
                                     [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                                     [1,0,1],[1,0,1],[1,0,1],[1,0,1],[1,0,1],
                                     [1,1,0],[1,1,0],[1,1,0],[1,1,0],[1,1,0],
                                     [1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]])
        routeLate        = np.array([[0     , 1     , 0     , 0     , 0   , 
                                      0     , 1     , 1     , 0     , 0   ,
                                      0     , 1     , 0     , 1     , 0   ,
                                      0     , 0     , 1     , 0     , 1   ,
                                      0     , 0     , 0     , 0     , 0   ,
                                      0     , 1     , 0     , 0     , 0   ,
                                      0     , 0     , 0     , 1     , 0   ,
                                      0     , 1     , 0     , 1     , 0]]).T
    
        delayTimes = {4, 16, 2, 8, 25, 12, 8, 4, 26, 31, 10, 5, 25, 4, 8, 2, 7, 
                      4, 8, 1, 21, 18, 10, 34, 6, 9, 3, 10, 4, 8, 22, 13, 10, 
                      4, 19, 10, 36, 2, 7, 4, 9, 15, 5}
    
    elif trainDeparture == 'leeds':
            
        routeInformation = np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],    
                                     [0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],
                                     [0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],
                                     [0,1,1],[0,1,1],[0,1,1],[0,1,1],[0,1,1],
                                     [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                                     [1,0,1],[1,0,1],[1,0,1],[1,0,1],[1,0,1],
                                     [1,1,0],[1,1,0],[1,1,0],[1,1,0],[1,1,0],
                                     [1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]])
        routeLate        = np.array([[0     , 1     , 1     , 1     , 0   , 
                                      0     , 0     , 1     , 1     , 0   ,
                                      0     , 1     , 0     , 1     , 0   ,
                                      1     , 0     , 1     , 0     , 1   ,
                                      0     , 1     , 0     , 0     , 0   ,
                                      0     , 0     , 1     , 1     , 0   ,
                                      1     , 1     , 0     , 0     , 1   ,
                                      1     , 1     , 0     , 1     , 0]]).T
    
        delayTimes = {3, 8, 5, 17, 13, 5, 29, 5, 18, 10, 25, 20, 24, 3, 2, 6, 
                      4, 9, 10, 34, 21, 3, 8, 10, 3, 6, 8, 8, 6, 5, 7, 3, 12,
                      10, 5, 23, 22, 20, 18, 4, 7, 2, 9, 5, 14, 19, 23, 12, 10}
    
    elif trainDeparture == 'birmingham':
            
        routeInformation = np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],    
                                     [0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],
                                     [0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],
                                     [0,1,1],[0,1,1],[0,1,1],[0,1,1],[0,1,1],
                                     [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                                     [1,0,1],[1,0,1],[1,0,1],[1,0,1],[1,0,1],
                                     [1,1,0],[1,1,0],[1,1,0],[1,1,0],[1,1,0],
                                     [1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]])
        routeLate        = np.array([[0     , 1     , 1     , 1     , 0   , 
                                      0     , 0     , 1     , 1     , 0   ,
                                      1     , 1     , 0     , 1     , 0   ,
                                      1     , 1     , 1     , 0     , 1   ,
                                      0     , 1     , 0     , 0     , 1   ,
                                      0     , 0     , 0     , 1     , 0   ,
                                      0     , 1     , 0     , 0     , 1   ,
                                      1     , 0     , 1     , 1     , 0]]).T
    
        delayTimes = {6, 2, 9, 14, 10, 4, 8, 19, 4, 6, 21, 10, 7, 3, 20, 9, 15,
                      8, 14, 9, 10, 4, 16, 28, 35, 2, 6, 9, 13, 15, 20, 16, 4,
                      9, 25, 16, 4, 19, 24, 31, 19, 6, 34, 5, 1, 7, 4, 12, 6}

    
    trainPredictions.train(routeInformation, routeLate, 15000)
        
    prediction = trainPredictions.think(np.array([day, stops, time]))
    percentage = prediction * 100
    print("There is a " , percentage , "% chance that your train will be delayed")
    
    predictedDelay = trainPredictions.timeMean(delayTimes)
    print("Your predicted train delay is " , predictedDelay , " minutes, should one occur.")
    
    
    
    
    
    
    
    
    
    
    
    
