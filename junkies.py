import _hf
import math

# Simple Linear Regression
# y = a + bx 
class SimpleLinearRegression:
    def __init__(self):
        pass

    def train(self,xknowns,yknowns):
        if len(xknowns) != len(yknowns):
            raise Exception("training data must be of the same length({}:{})".format(len(xknowns),len(yknowns)))
        
        # b = cov(x,y) / var(x)
        b = (_hf.cov(xknowns, yknowns) / _hf.var(xknowns))

        # a = ybar - b*xbar
        a = _hf.meanof(yknowns) - (b * _hf.meanof(xknowns))
        setattr(self,"b",b)
        setattr(self,"a",a)
        setattr(self,"training_set_x",xknowns)
        setattr(self,"training_set_y",yknowns)

    def predict(self,xs):
        if hasattr(self,"a") and hasattr(self,"b"):
            pass
        else:
            raise Error("model needs to be trained")

        if isinstance(xs,list) or isinstance(xs,tuple):
            solutions = []

            for x in xs:
                solved = getattr(self,"a") + (getattr(self,"b") * x)
                solutions.append(solved)
            
            return solutions
        elif isinstance(xs, int) or isinstance(xs, float):
            return (getattr(self,"a")) + (getattr(self,"b") * xs)
        else:
            raise Exception("unsupported data format: {}".format(type(xs)))
            

    def check_accuracy(self,xtests,ytests):
        # Pearson's Product Moment Correlation Coefficient (Pearson r) is used to define the accuracy
        # The result will be between 1 and -1
        # With 1 as very accurate and
        # With -1 as very inacurate
        cov_x_y = _hf.cov(xtests,ytests)
        var_x = _hf.var(xtests)
        var_y = _hf.var(ytests)
        r = cov_x_y / (math.sqrt(var_x) * math.sqrt(var_y))

        return r