# Making a Naive Bayes Classifier for predicting the output based on the input training data

# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB

# Now making a data set, we can also import data set using csv files, but for that you need to install pandas and then import it
# Making a data set based on the characteristics of Apple, Oranges and Lemons

# [Mass, Width, Height]
training_data = [[192, 8.4, 7.3],[190, 8.1, 6.9],[181, 7.4, 7.2],[342, 9.0, 9.4],[356, 9.2, 9.1],[362, 9.6, 9.2],[162, 7.5, 7.1],
      [194, 7.2, 10.3],[180, 7.6, 8.2],[200, 7.3, 10.5],[210, 7.8, 8.0],[172, 7.1, 7.6],[116, 5.9, 8.1],[168, 7.5, 7.6],
      [190, 7.5, 8.1],[172, 7.1, 7.6],[216, 7.3, 10.2],[117, 5.9, 8.1],[180, 7.6, 8.2],[170, 7.0, 7.6]]

labels = ['apple', 'apple', 'apple', 'oranges', 'oranges', 'oranges', 'apple', 'lemon', 'oranges', 'lemon', 'oranges', 'apple', 'lemon', 'apple', 'oranges', 'apple', 'oranges', 'lemon', 'oranges', 'apple'] 

label = [1, 1, 1, 2, 2, 2, 1, 3, 2, 3, 2, 1, 3, 1, 2, 1, 2, 3, 2, 1]

#Creating a Naive Bayes Classifier for applying on our dataset
gnb = GaussianNB()

# Training the Classfier on our data set using fit method and updating it
gnb = gnb.fit(training_data, labels)
print('Training of classifier completed')

# Making prediction using predict method and then printing the result
# A sample testing value generated, you can change it to test for different values
testing_data = [[196, 8.0, 7.1]]
prediction = gnb.predict(testing_data)
print("The Predicted Fruit is:")
print(prediction)
