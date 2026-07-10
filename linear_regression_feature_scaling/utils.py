import numpy as np
import matplotlib.pyplot as plt

def load_data():
    data=np.loadtxt("houses.txt",delimiter=',')
    X=data[:,:-1]
    y=data[:,-1]
    return X,y

def derivative(X,y,w,b):
    m=X.shape[0]
    n=X.shape[1]
    error=X @ w + b - y
    list_wb=[]
    for j in range(n):
        dj_dwj=np.dot(error,X[:,j])/m
        list_wb.append(dj_dwj)
    dj_db = np.sum(error) / m
    list_wb.append(dj_db)
    return np.array(list_wb)

def iteration(X,y,original_wb,alpha,times):
    original_wb = original_wb.copy()
    hist={}
    hist["cost"] = []; hist["params"] = []; hist["grads"]=[]; hist["iter"]=[];
    for i in range(times):
        gradient=derivative(X,y,original_wb[:-1],original_wb[-1])
        original_wb-=alpha*gradient
    return original_wb,hist

def zscore(X):
    mu=np.mean(X,axis=0)
    sigma=np.std(X,axis=0)
    X_norm=(X-mu)/sigma
    return X_norm

def plot_cost_i_w(X,y,hist):
    ws = np.array([ p[0] for p in hist["params"]])
    rng = max(abs(ws[:,0].min()),abs(ws[:,0].max()))
    wr = np.linspace(-rng+0.27,rng+0.27,20)
    cst = [compute_cost(X,y,np.array([wr[i],-32, -67, -1.46]), 221) for i in range(len(wr))]

    fig,ax = plt.subplots(1,2,figsize=(12,3))
    ax[0].plot(hist["iter"], (hist["cost"]));  ax[0].set_title("Cost vs Iteration")
    ax[0].set_xlabel("iteration"); ax[0].set_ylabel("Cost")
    ax[1].plot(wr, cst); ax[1].set_title("Cost vs w[0]")
    ax[1].set_xlabel("w[0]"); ax[1].set_ylabel("Cost")
    ax[1].plot(ws[:,0],hist["cost"])
    plt.show()

def compute_cost(X, y, w, b):
    """
    compute cost
    Args:
      X (ndarray (m,n)): Data, m examples with n features
      y (ndarray (m,)) : target values
      w (ndarray (n,)) : model parameters  
      b (scalar)       : model parameter
    Returns
      cost (scalar)    : cost
    """
    m = X.shape[0]
    cost = 0.0
    for i in range(m):
        f_wb_i = np.dot(X[i],w) + b           #(n,)(n,)=scalar
        cost = cost + (f_wb_i - y[i])**2
    cost = cost/(2*m)
    return cost 
