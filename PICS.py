
# Calculo de probabilidades
def p(lambd,mu):
    return lambd/mu

def p0(lambd,mu):
    return 1-p(lambd,mu)

def pN(lambd,mu,n):
    proba0=p0(lambd,mu)
    return proba0*(lambd/mu)**n

def sumatoriaP(lambd,mu,ini,n):
    proba0 = p0(lambd,mu)
    acc = 0
    n+=1
    if(ini==0):
        acc+=proba0
        ini=1

    for i in range(ini,n):
        probabilidad = round(proba0*(lambd/mu)**i,2)
     
        acc+= probabilidad
    return acc

#Numero esperado de clientes

def L(lambd,mu):
    return lambd/(mu-lambd)

def Lq(lambd,mu):
    numerador = (lambd**2)
    denominador = (mu*(mu-lambd)) 
    return numerador/denominador

def Ln(lambd,mu):
    return lambd/(mu-lambd)


#Tiempo esperado en el sistema

def W(lambd,mu):
    return 1/(mu-lambd)
    
def Wq(lambd,mu):
    numerador = lambd
    denominador = (mu*(mu-lambd))

    return numerador/denominador

def Wn(lambd,mu):
    return 1/(mu-lambd)

print(p(2,3))    