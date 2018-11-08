# Machine Learning Classifiers:
In this project we will implement different Machine Learning Classifiers on a small training data set and predict the output based on different classification algorithms.
The classification technique is a systematic approach to build classification models from an input dat set. For example, decision tree classifiers, rule-based classifiers, neural networks, support vector machines, and naive Bayes classifiers are different technique to solve a classification problem. Each technique adopts a learning algorithm to identify a model that best fits the relationshio between the attribute set and class label of the input data. Therefore, a key objective of the learning algorithm is to build predictive model that accurately predict the class labels of previously unkonw records.

# Decision Tree Classifier:
Decision Tree Classifier is a simple and widely used classification technique. It applies a straitforward idea to solve the classification problem. Decision Tree Classifier poses a series of carefully crafted questions about the attributes of the test record. Each time time it receive an answer, a follow-up question is asked until a conclusion about the calss label of the record is reached.

The algorithm of Decision Tree Classifier in simple words is as follows:
1.Place the best attribute of our dataset at the root of the tree.
2.Split the training set into subsets. Subsets should be made in such a way that each subset contains data with the same value for an attribute.
3.Repeat step 1 and step 2 on each subset until you find leaf nodes in all the branches of the tree.

While building our decision tree classifier, we can improve its accuracy by tuning it with different parameters. But this tuning should be done carefully since by doing this our algorithm can overfit on our training data & ultimately it will build bad generalization model.
The code for Decision Tree Classifier implemented using ScikitLearn is attached with in this repository & a sample dataset of Fruits is used for training purpose.

For understanding Decision Tree Classifiers in details refer to the following link of documentation:
http://kudoflow.com/3x6g

# Naive Bayes Classifier:
The Naive Bayesian classifier is based on Bayes’ theorem with the independence assumptions between predictors. A Naive Bayesian model is easy to build, with no complicated iterative parameter estimation which makes it particularly useful for very large datasets. Despite its simplicity, the Naive Bayesian classifier often does surprisingly well and is widely used because it often outperforms more sophisticated classification methods. It is actually based on Bayes rule that is based on conditional probabilities. For understanding it in detail refer to the following link:
http://kudoflow.com/3w8j

The Fruit data set is tested with Naive Bayes Classifer based on Gaussian normalization as it is suitable for our simple data set, and python file is attached with this repository.

For Learning more about different Naive Bayes Classifiers kindly refer the following link:
http://kudoflow.com/3wX0u 

# Support Vector Machines:
A Support Vector Machine (SVM) is a discriminative classifier formally defined by a separating hyperplane. In other words, given labeled training data (supervised learning), the algorithm outputs an optimal hyperplane which categorizes new examples. In two dimentional space this hyperplane is a line dividing a plane in two parts where in each class lay in either side.
For more detailed understanding you can refer following links:
http://kudoflow.com/4Eo4
http://kudoflow.com/4ErD

# Conclusion:
All classifeirs have there own specifications and advantages but for this fruit dataset that is a very simple dataset, DTC can be used. But for more comlpex and detailed dataset other two algorithms can be used.
With given testing value the Decision tree classifier and Naive Bayes Classifier predict more rightly the fruit as an apple, whereas Support Vector Machine predicts it wrong as an orange. This shows that it is very important to have a prior knowledge about the classifier that one is going to use for particular dataset.








