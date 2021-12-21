import math

#************************************Probabilidades 

#*************************p0

def exp1P0(lambd,mu,k):       #Expresion 1 de P0
    n=k-1
    acc=0
    for i in range(0,n+1):
        exp1 = 1/ math.factorial(i) #Expresion 1
        exp2 = (lambd/mu)**i        #Expesion 2
        acc+= exp1*exp2
    return acc

def exp2P0(lambd,mu,k):            #Expresion 2 de P0
    exp1=1/math.factorial(k)
    exp2 = (lambd/mu)**k
    exp3 = (k*mu)/(k*mu-lambd)
    return exp1*exp2*exp3

def p0(lambd,mu,k):
    return 1/(exp1P0(lambd,mu,k)+exp2P0(lambd,mu,k))




#*************************pk
def condicionEstabilidad(lambd,mu,k):
    if(lambd/(mu*k)<1):
        return True
    return False
def pk(lambd,mu,k):
    
    if(not condicionEstabilidad(lambd,mu,k)):
        return 0

    exp1 = 1/math.factorial(k)
    exp2 = (lambd/mu)**k
    exp3 = ((k*mu)/(k*mu-lambd))*p0(lambd,mu,k)
    return exp1*exp2*exp3

#*************************pNE

def pNE(lambd,mu,k):
    return 1 - pk(lambd,mu,k)


#*************************pn

def pN(lambd,mu,k,n):
    if(n>=k):
        exponente = n-k
        exp1 = 1/(math.factorial(k)*(k**exponente))
        exp2 = ((lambd/mu)**n)*p0(lambd,mu,k)

    else:
        exp1= p0(lambd,mu,k)/math.factorial(n)
        exp2 = (lambd/mu)**n
        
    return exp1*exp2


#*************************Sumatoria de probabilidades
#ini: cant de clientes inicial
#n: cant de clientes final
def sumatoriaP(lambd,mu,k,ini,n):
    acc = 0
    n+=1
    for i in range(ini,n):
        acc += round(pN(lambd,mu,k,i),2)

    return acc

#************************************Número esperado de clientes
def L(lambd,mu,k):
    numerador = (lambd*mu)*((lambd/mu)**k)
    exp1Deno = math.factorial(k-1)
    exp2Deno = (k*mu-lambd)**2
    denominador = exp1Deno*exp2Deno
    exp1 = (numerador/denominador)*p0(lambd,mu,k)
    exp2 = lambd/mu
    return exp1 + exp2

def Lq(lambd,mu,k):
    numerador = (lambd*mu)*((lambd/mu)**k)
    exp1Deno = math.factorial(k-1)
    exp2Deno = (k*mu-lambd)**2
    denominador = exp1Deno*exp2Deno
    return (numerador/denominador)*p0(lambd,mu,k)

def Ln(lambd,mu,k):
    numerador = Lq(lambd,mu,k)
    denominador = pk(lambd,mu,k)
    return numerador/denominador

#************************************Tiempo espero en el sistema
def W(lambd,mu,k):
    return L(lambd,mu,k)/lambd

def Wq(lambd,mu,k):
    return Lq(lambd,mu,k)/lambd


def Wn(lambd,mu,k):

    return Wq(lambd,mu,k)/pk(lambd,mu,k)

