#Interval estimation
s = 515 #antal succes
n = 1000 #antal forsøg
x = c(3.93,3.41,3.08,4.72,3.37,4.03,4.82) #eller indsæt data her som vektor

#Find sigma
sigma = 0.5 #hvis kendt (sigma= standard deviation)
  # eller
sigma = sd(x)

#find gennemsnit (my)=E(X_i)
x_bar=s/n
#eller
x_bar = mean(x)
x_bar = 0.54


#signifikansniveau
alfa = 0.01

#Interval for my ved kendt varians
x_bar-qnorm(1-(alfa/2))*sigma/sqrt(n)
x_bar+qnorm(1-(alfa/2))*sigma/sqrt(n)

#Interval for my ved ukendt varians, stor n, asymptotisk
x_bar-qnorm(1-(alfa/2))*sigma/sqrt(n)
x_bar+qnorm(1-(alfa/2))*sigma/sqrt(n)

#Interval for my ved ukendt varians, normalfordelt, eksakt
x_bar-qt(1-(alfa/2),n-1)*sigma/sqrt(n)
x_bar+qt(1-(alfa/2),n-1)*sigma/sqrt(n)

#Interval for varians ved ukendt middelværdi og varians (my^2), normalfordelt
((n-1)*(sigma^2))/qchisq(1-(alfa/2),(n-1))
((n-1)*(sigma^2))/qchisq(alfa/2,(n-1))

2/(3*pi)

#Bestem n X_bar højest 0,4 fra my med 0,95 konfidens
qnorm(1-(alfa/2))*sigma/sqrt(n)<0.4
  
qexp(0.95)
