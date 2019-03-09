import matplotlib.pyplot as plt
import math
def NewX(x0,h):
    x2=x0+h #The next X
    return x2
def func(x,y):
    return 1 - 0.25*y + 0.2*x #Please put the function here

def Predictor(x,y,h):
    y_pre=y+h*(func(x,y))
    return y_pre

def corrector(x1,y1,h,xend):
    vectorX=list() #Vector X to display the graph
    vectorY=list() #Vector Y to display the graph
    while(x1<=xend):
        x_next=NewX(x1,h)
        pre = func(x1, y1) #Insert the current X and Y into the current function
        nextOne=func(x_next,Predictor(x1,y1,h))#We'll take the next X, and the Predictor Y
        y_cor= y1+ h/2*(pre+nextOne)#We'll get average and get better accuracy
        vectorX.append(x1)#Enter x into the x vector
        vectorY.append(y1)#Enter y into the y vector
        x1=x_next #We will switch between the current X and the next X
        y1=y_cor #We will switch between the current Y and the next Y
    plt.axis([0,5, 0,20])#Displays the graph
    plt.plot(vectorX,vectorY,'bo-')
    plt.show()
    print("All the points in VectorX",vectorX)
    print("All the points in VectorY",vectorY)


corrector(0,1,0.5,10)
#data entry corrector(x start,y start,jump h,x end)