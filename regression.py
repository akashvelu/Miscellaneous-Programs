#Regression algorithms using least squares method
import numpy as np 


#linear regression through origin (in the form y = ax)
def lin_reg_origin(points):
    xs = []
    ys = []
    for point in points:
        xs.append(point[0])
        ys.append(point[1])
    xs = np.array(xs)
    ys = np.array(ys)
    xTx = np.dot(xs.T, xs)
    xTy = np.dot(xs.T, ys)
    print(xTx)
    print(xTy)
    a = (1.0/xTx) * xTy 
    print(a)

    return "y = " + str(a) + "x"

#linear regression with offset (in the form y = ax + b)

def lin_reg(points):
    xs = []
    ys = []
    for point in points:
        xs.append(point[0])
        ys.append(point[1])
    ones = np.ndarray.tolist(np.zeros(len(xs)) + 1)
    X = np.matrix([xs, ones]).T 
    xTx = np.dot(X.T, X)
    xTy = np.dot(X.T, ys)

    ab = np.dot(np.linalg.inv(xTx), xTy.T)
    

   
    return "y = " + str(ab[0,0]) + "x + " + str(ab[1,0])

    


