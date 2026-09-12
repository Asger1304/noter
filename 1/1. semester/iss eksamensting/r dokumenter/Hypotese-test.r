#Opstiller test for theta, givet stikprøven.
s = 21 #antal succes
n = 225 #antal forsøg
x = c(3.93,3.41,3.08,4.72,3.37,4.03,4.82)
#eller indsæt data her som vektor
my_0 = 0.1 #indsæt my fra nulhypotesen

#Find sigma HUSK sqrt
sigma = sqrt(0.1*(0.9)) #hvis kendt
# eller
sigma = sd(x)

sqrt(225)

#find gennemsnit (my)=E(X_i)
x_bar = s/n
#eller
x_bar = mean(x)


#find teststatestikken W
W = ((x_bar)-my_0)/(sigma/sqrt(n))
alfa = 0.05 #signifikansniveau

#tosidet
#for sigma kendt, stor n eller normal H_0:my=my_0, H_1: my ikke lig my_0 Accept 
qnorm(1-(alfa/2)) #nurmerisk(W)=< z_alfa = accept

#for sigma ukendt, normal H_0:my=my_0, H_1: my ikke lig my_0 Accept
qt(1-alfa/2,n-1) #nurmerisk(W)=< t_alfa = accept
W

#for sigma known, stor n eller normal H_0:my=<my_0, H_1: my>my_0 Accept 
qnorm(1-alfa) #W<=z_alfa = accept

#for sigma ukendt, normal H_0:my=<my_0, H_1: my>my_0 Accept
qt(1-alfa,n-1) #W<=t_alfa = accept

#for sigma known, stor n eller normal H_0:my=>my_0, H_1: my<my_0 Accept 
-qnorm(1-alfa) #W>=z_alfa = accept


#for sigma ukendt, normal H_0:my=<my_0, H_1: my>my_0 Accept
-qt(1-alfa,n-1) #W>=t_alfa = accept

#for ukendt parameter med kendt ikke normalfordeling???

#Find p-værdi for test(ikke styrken for test)
#step 1: beregn W
#brug samme fordeling som ved hypotesetesten, men ikke fraktilen(uden q)
#indsæt w på x's plads -> der hvor der står 1-alfa eller lign


dnorm(-0.34)

Bestem 
X_S=sqrt(34)/20
n=225
X_mean-qnorm(1-0.05)*X_S/sqrt(n)
#Accepterer H_0 hvis tetha_0 ligger i intervallet [0.06136313;1]
(X_mean-0.1)/(X_S/sqrt(n))
-qnorm(1-0.05)
#W>=z_alfa, H_0 accepteres
#Udregner den tilhørerende p-værdi
p = 1-pnorm(W)
-qnorm(p)
X_mean-qnorm(1-p)*X_S/sqrt(n)