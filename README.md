# MLJUNKIES

Basic Implementations of Supervised Machine Learning Algorithms
> Please read: 
No standard libraries like numpy or scikitlearn are used, (these implementations are just to get a feel of how those standard libraries work). All the implementations can be simply done using those standard libraries with very few lines of code. The implemented algorithms may not be used on very large datasets as it might be slow or have very low accuracy. always check the accuracy of the prediction after the training to ascertain the effectiveness of the training

## Table of Contents

* [Algorithms](#algorithms)

## ALGORITHMS
> All algorithms are implemented in the junkies module and all test examples can be found in _usage.py file. _hf module holds the functions that helps in the calculation

### 01. Simple Linear Regression

### Usage of API

``` python
model = SimpleLinearRegression()
```
train the model with your training datasets
x_training_set = values of the independent variable
y_training_set = observed values of the dependent or response variable
``` python
model.train(x_training_set, y_training_set)
```
you can check accuracy of the training using your testsets
x_test_set = values of the independent variable
y_test_set = observed values of the dependent or response variable (accuracy is measured between -1 and 1 with 1 as most accurate and -1 as least accurate)
``` python
model.check_accuracy(x_test_set y_test_set)
```
Now you can use the model to predict the observed values for response variables using only the x_test_set (if the accuracy is high), the observed values will be so close to the y_test_set
``` python
model.predict(x_test_set)
```
