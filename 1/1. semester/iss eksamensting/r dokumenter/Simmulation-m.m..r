#Plotter PDF for x~poisson(500)
plot(dpois(400:600,500))
ppois(510,500)-ppois(489,500) #ss mellem 490 og 510 hændelser
1-ppois(3049,3000)

#Simmulerer middelværdien. Udfører 10000 trails. 
mean(rpois(1000000,1))
X=rpois(100000,1)# Simuler 100000 stok. variable med poisson(1) fordeling
Y=(exp(X))
mean(Y)

k=c(1:10000)          # vektor med stigende tal 
Y=cumsum(X)           # kumulativ sum
Z=Y/k                 # vektor med gennemsnit
plot(Z)
mean(sqrt(X))         #E(sqrt(x))
var(x)                #varians
sd(X)                 #standardafvigelse

     












