s=1 #antal servere
EX=1/0.9 #arrival rate
EY=1 #service rate
lampda=1/EX #Antal ankomster pr. TEmy=s/EY  
my=s/EY #Antal jobs der kan forarbejdes
rho=lampda/my #udnyttelsesgrad
rho
Wq=lampda/(my*(my-lampda)) #forventet køtid
Wq

n=c(0,1,2,3)
K=3
R=10
c=6
f=3

P=(1-rho)/(1-rho^(K+1))*rho^n
P

Omkostning=lampda*R*0.2119802+c*(1-0.2907822)+f*0.2907822 #lampda*R*P_K + c(1-P_0) + f*P_0
Omkostning
