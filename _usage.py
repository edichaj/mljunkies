from junkies import SimpleLinearRegression as SLR

# Celsius to Fahrenheit conversion using Simple Linear Regression

# in Celsius
cs =   [2, 3, 12, 15, 17, 19, 22, 27, 32, 33, 34, 43, 49, 53]
# in Fahrenheit
fs = [35.6, 37.4, 53.6, 59.0, 62.6, 66.2, 71.6, 80.6, 89.6, 91.4, 93.2, 109.4, 120.2, 127.4]


# data to use and confirm the model's training (testdata in C and expected_outcomes in F)   
testdata = [65, 77, 83, 86, 97]
print("test data in celsius: {}".format(testdata))
expected_outcomes = [149.0, 170.6, 181.4, 186.8, 206.6] # if you run the code, the output is expected to be very close to these values

model = SLR()
model.train(cs,fs)
predictions = model.predict(testdata)
print("outcome in fahrenheit: {}".format(predictions))
print("accuracy: {}".format(model.check_accuracy(testdata,expected_outcomes)))


