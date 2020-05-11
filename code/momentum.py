#******************************************Rolling Funcs ******************************************
def exp_2_avg(x): 
    x = x[::-1]
    weights = np.array([2**(len(x) - 1 - y) /(2**(len(x))-1) for y in range(len(x))])
    average = np.array(x)*weights
    return average.sum()

def exp_e_avg(x): 
    x = x[::-1]
    weights = np.array([np.e**(len(x) - 1 - y) /(np.e**(len(x))-1) for y in range(len(x))])
    average = np.array(x)*weights
    return average.sum()

def exp_x_avg(x,constant=10):
    x = x[::-1]
    weights = np.array([constant**(len(x) - 1 - y) /(constant**(len(x))-1) for y in range(len(x))])
    average = np.array(x)*weights
    return average.sum()

def pond_avg(x): 
    x = x[::-1]
    weights = np.array([((len(x)-y))/(int(((len(x))*((len(x)+1))))/2) for y in range(len(x))])
    average = np.array(x)*weights
    return average.sum()

def relu(x):
    return max(0,x)

def RSI(x, agg=exp_e_avg):
    x = np.array(x)
    today = x[1:]
    yesterday = x[:-1]
    up = today - yesterday
    down = up*(-1)
    up = [relu(x) for x in up]
    down = [relu(x) for x in down]
    rsi =  ( agg(up)/ (agg(up)+agg(down)) ) 
    return rsi

def RS(x, agg=exp_e_avg):
     x = np.array(x)
    today = x[1:]
    yesterday = x[:-1]
    up = today - yesterday
    down = up*(-1)
    up = [relu(x) for x in up]
    down = [relu(x) for x in down]
    rs = agg(up)/agg(down)
    return rs

def K_line(x)
    "Stochastic Momentum Oscillator formula, sell above 80, buy under 20"

    closing = x[-1]
    l_n = min(x)
    h_n = max(x)
    k = (closing-l_n)/(h_n-l_n)
    return k 

def D_line(x):
    l_n = min(x)
    h_n = max(x)    
    return h_n/l_n
