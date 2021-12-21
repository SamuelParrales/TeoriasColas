#************************************Probabilidades 
#M: población
from math import factorial as fac

def p0(lambd,mu,M):
    acc =0
    loops = M+1
    for i in range(0,loops):
        expr1 = fac(M)/fac(M-i)
        expr2 = (lambd/mu)**i
        acc += expr1*expr2
        
    return 1/acc

def pE(lambd,mu,M):
    return 1-p0(lambd,mu,M)


def pN(lambd,mu,M,n):
    expr1= fac(M)/fac(M-n)
    expr2 = ((lambd/mu)**n)*p0(lambd,mu,M)
    return expr1*expr2

def sumatoriaP(lambd,mu,M,ini,n):
    loops = n+1
    acc = 0
    for i in range(ini,loops):
        acc+= round(pN(lambd,mu,M,i),2)
    
    return acc



#************************************Clientes esperados
def L(lambd,mu,M):
    exp1=(mu/lambd)*(1-p0(lambd,mu,M))
    return M - exp1

def Lq(lambd,mu,M):
    exp1=((lambd+mu)/lambd)*(1-p0(lambd,mu,M))
    return M - exp1

def Ln(lambd,mu,M):
    return Lq(lambd,mu,M)/pE(lambd,mu,M)

#************************************Tiempo esperado

def Wq(lambd,mu,M):
    numerador = Lq(lambd,mu,M)
    denominador = (M-L(lambd,mu,M))*lambd 
    return numerador/denominador

def W(lambd,mu,M):
    return Wq(lambd,mu,M) +(1/mu) 

def Wn(lambd,mu,M):
    return Wq(lambd,mu,M)/pE(lambd,mu,M)
