#Overblik over forskellige fordelinger i R

#Diskrete fordelinger
  #Bernoulli(p) (virker kun med Rlab package)
    #f_X(x)
dbern(x,p)
    #F_X(x)
pbern(x,p)

  #Binomial(n,p)
    #f_X(x)
dbinom(1,20,1/6)
    #F_X(x)
pbinom(1,9,1/6)

  #Geometrisk(p) Husk: vores F_x(5)=pgeom(4)
    #f_X(x)
dgeom(x-1,p)
    #F_X(x)
pgeom(x-1,p)

  #Pascal(m,p) husk vores F_x(forsøg) mens p #######hvordan er det med m?
    #f_X(x)
dnbinom(x,m,p)
    #F_X(x)
pnbinom(x,m,p)

  #Poisson(lambda)
    #f_X(x)
dpois(x,lambda)
    #F_X(x)
ppois(x,lambda)

#Kontinuerte fordelinger
  #Uniform(a,b) 
    #f_X(x)
dunif(x,a,b)
    #F_X(x)
punif(x,a,b)

  #Exponential(lambda)
    #f_X(x)
dexp(x,lambda)
  #F_X(x)
pexp(x,lambda)

  #Gamma(alfa,lambda)
    #f_X(x)
dgamma(x,alfa,lambda)
#F_X(x)
pgamma(x,alfa,lambda)

  #Normalfordeling(my,sigma^2) med m?
    #f_X(x)
dnorm(my,sigma^2)
#F_X(x)
pnorm(my,sigma^2)

  #chi^2 fordeling
#f_X(x)
dchisq(x,frihedsgrader)
#F_X(x)
pchisq(x,frihedsgrader)


