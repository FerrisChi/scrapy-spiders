import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
import pandas as pd
 
#hypothesis function
def hypothesis_func(w, x):
    w1,w0 = w
    return w1*x + w0
        
#error function
def error_func(w, train_x, train_y, msg):
    print(msg)
    return hypothesis_func(w, train_x) - train_y
 
def dump_fit_func(w_fit):
    w1,w0=w_fit
    print("fitting line=",str(w1)+"*x + "+str(w0))
    return
    
#square error平方差函数
def dump_fit_cost(w_fit, train_x, train_y):
    error = error_func(w_fit, train_x, train_y, "")
    square_error = sum(e*e for e in error)
    print('fitting cost:',str(square_error))
    return square_error
    
#main function
if __name__=="__main__":

    df1 = pd.read_csv('1confirmed_cases.csv', encoding='utf-8')
    df1 = df1[df1['country']=='World']
    print(df1)
    x=[i for i in range(9,24)]
    y=[]
    for id, row in df1.iterrows():
        y.append(row['confirmedcases'])

    # print(x)
    # print(y)
    train_x = np.array(x[:10])
    train_y = np.array(y[:10])

    #train set
    # train_x = np.array([8.19,2.72,6.39,8.71,4.7,2.66,3.78])
    # train_y = np.array([7.01,2.78,6.47,6.71,4.1,4.23,4.05])
 
    #linear regression by leastsq
    msg = "invoke scipy leastsq"
    w_init = [20, 1]#weight factor init
    fit_ret = leastsq(error_func, w_init, args=(train_x, train_y, msg))
    w_fit = fit_ret[0]
 
    #dump fit result
    dump_fit_func(w_fit)
    fit_cost = dump_fit_cost(w_fit, train_x, train_y)
    
    #test set
    test_x = np.array(x)
    test_y = np.array(y)
    # test_x = np.array(np.arange(train_x.min(), train_x.max(), 1.0))
    # test_y = hypothesis_func(w_fit, test_x)
 
    #show result by figure
    plt.figure(1)
    plt.figure(figsize=(8,6))#指定图像比例： 8：6
    plt.xlabel('Day(December, 2021)')
    plt.ylabel('Confirmed cases')
    plt.title('Linear regression for COVID-19 prediction')
    plt.scatter(train_x, train_y, color='b', label='train set')
    plt.scatter(test_x, test_y, color='r', marker = '^', label='test set', linewidth=2)
    plt.plot(test_x, test_y, color='r', label='fitting line')
    plt.legend(loc='lower right')#label面板放到figure的右下角
    
    plt.show()