#blackscholes calculator


# inputs
s=226
k=226
sigma=0.18
r=0.054
t=0.5


#finder optionspricer under BSM framework
BSCPrice <- function(s,k,sigma,r,t){
  d1=(log(s/k)+(r+sigma^2/2)*t)/(sigma*sqrt(t))
  d2=d1-sigma*sqrt(t)
  c=s*pnorm(d1)-k*exp(-r*t)*pnorm(d2)
  return(c)
}
BSCPrice(s,k,sigma,r,t)

BSPPrice<- function(s,k,sigma,r,t){
  d1=(log(s/k)+(r+sigma^2/2)*t)/(sigma*sqrt(t))
  d2=d1-sigma*sqrt(t)
  p=k*exp(-r*t)*pnorm(-d2)-s*pnorm(-d1)
  return(p)
}
BSPPrice(s,k,sigma,r,t)

BSPrices<-function(s,k,sigma,r,t){
  V=c(BSCPrice(s,k,sigma,r,t),BSPPrice(s,k,sigma,r,t))
  print(V)
}
BSPrices(s,k,sigma,r,t)


#finder og printer option greeks i BSM framework
greeks<-function(s,k,sigma,r,t){
  d1=(log(s/k)+(r+sigma^2/2)*t)/(sigma*sqrt(t))
  d2=d1-sigma*sqrt(t)
  c=s*pnorm(d1)-k*exp(-r*t)*pnorm(d2)
  p=k*exp(-r*t)*pnorm(-d2)-s*pnorm(-d1)
  
  deltaC=pnorm(d1)
  thetaC=-s*dnorm(d1)*sigma/(2*sqrt(t))-r*k*exp(-r*t)*pnorm(d2)
  gammaC=dnorm(d1)/(s*sigma)
  deltaP=deltaC-1
  thetaP=thetaC+r*k*exp(-r*t)
  gammaP=gammaC
  vega=s*sqrt(T)
  cg=c(deltaC,gammaC,thetaC,vega)
  pg=c(deltaP,gammaP,thetaP,vega)
  print("callgreeks")
  print("delta gamma theta vega")
  print(cg)
  print("putgreeks")
  print("delta gamma theta vega")
  print(pg)
}
greeks(s,k,sigma,r,t)

#hjælpefunktion
cvol <- function(v){
  BSCPrice(s,k,v,r,t)
}
cvol(0.17)



#implied vol estimator
#udfyld tail i toppen hvor sigma selvfølgelig er ligemeget
#giver implied volatility nedrundet til nærmeste promille OBS på at den ikke kan finde vol over 200%
volestimator <- function(c){
  iv=0
  i=0:2000
  b=i/1000
  for (x in b) {
   if (cvol(x)<=c){
    iv=x}
    if (cvol(x)>c){break
      }
  }
  return(iv)
  }




cvol(0)
volestimator(3)
cvol(0.05)








