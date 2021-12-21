from math import factorial as fac
#************************************Probabilidades 

#*************************p0
def expr1P0(lambd,mu,k,M):
    acc = 0
    for i in range(0,k):
        expr1 = fac(M)/(fac(M-i)*fac(i))
        expr2 = (lambd/mu)**i
        acc+=expr1*expr2
    return acc

def expr2P0(lambd,mu,k,M):
    loops = M+1
    acc =0
    for i in range(k,loops):
        expr1 = fac(M-i)*fac(k)*(k**(i-k))
        expr1 = fac(M)/expr1
        expr2 = (lambd/mu)**i
        acc += expr1*expr2
    return acc

def p0(lambd,mu,k,M):
    return 1/(expr1P0(lambd,mu,k,M)+expr2P0(lambd,mu,k,M))

def pn(lambd,mu,k,M,n):
    if(n<k):
        expr1 = fac(M)/(fac(M-n)*fac(n))
        expr2 = (lambd/mu)**n
    else:
        expr1 = fac(M)/(fac(M-n)*fac(k)*k**(n-k))
        expr2 = (lambd/mu)**n

    return p0(lambd,mu,k,M)*expr1*expr2    

#ini: inicio de la sumatoria
def sumatoriaPn(lambd,mu,k,M,ini,n):
    loops = n+1
    acc = 0
    for i in range(ini,loops):
        acc+=pn(lambd,mu,k,M,i)

    return acc

def pE(lambd,mu,k,M):
    acc=0
    for i in range(0,k):
        acc+=pn(lambd,mu,k,M,i)
    return (1-acc)

def pNE(lambd,mu,k,M):
    return 1 - pE(lambd,mu,k,M)


#************************************Numero esperado de clientes
#**************************L
def expr1L(lambd,mu,k,M):
    acc =0
    for i in range(0,k):
        acc+= i*pn(lambd,mu,k,M,i)

    return acc

def expr2L(lambd,mu,k,M):
    loops = M+1
    acc =0
    for i in range(k,loops):
        acc+= (i-k)*pn(lambd,mu,k,M,i)
    return acc


def expr3L(lambd,mu,k,M):
    acc = sumatoriaPn(lambd,mu,k,M,0,k-1)
    return k*(1-acc)


def L(lambd,mu,k,M):
    return expr2L(lambd,mu,k,M)+expr1L(lambd,mu,k,M)+expr3L(lambd,mu,k,M)


def Lq(lambd,mu,k,M):
    loops = M+1
    acc =0
    for i in range(k,loops):
        acc+= (i-k)*pn(lambd,mu,k,M,i)
    return acc

def Ln(lambd,mu,k,M):
    return Lq(lambd,mu,k,M)/pE(lambd,mu,k,M)



#************************************Tiempo esperado
def Wq(lambd,mu,k,M):
    return Lq(lambd,mu,k,M)/((M-L(lambd,mu,k,M))*lambd)

def W(lambd,mu,k,M):
    return Wq(lambd,mu,k,M)+(1/mu)

def Wn(lambd,mu,k,M):
    return Wq(lambd,mu,k,M)/pE(lambd,mu,k,M)
