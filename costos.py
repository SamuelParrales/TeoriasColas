def CTte(lambd,t,Wq,Cte):
    return lambd*t*Wq*Cte

def CTts(lambd,t,W,Cts):
    return lambd*t*W*Cts

def CTtse (lambd,mu,t,Ctse):
    return lambd*t*(1/mu)*Ctse

#k: numeros de servidores
#Cs: $/d
def CTs (k,Cs):
    return k*Cs