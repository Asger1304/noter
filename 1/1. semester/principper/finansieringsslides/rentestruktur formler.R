#rentestruktur
#kuponrente
r=0.12
#hovedstol
h=100
#resterende antal betalinger#
n=3
#annuitetsfaktor#

#normal#
a=(1-(1+r)^-n)/r
a

#n liste#

nl=1:n
ab=n-nl+1

#tidspunktsrettet#

aj1=(1+r)^(-(ab))
aj=(1-aj)/r




#annuitets#

nb=n-nl+1
ya=h*a^-1
za = ya*(1+r)^-(nb)
ia = h*r*a^-1*aj



#stående #
n0=nl/nl
is=r*h*n0
ys=is
ys[n]=is[n]+h
zs=ys-is
ys

#serie
zse=h/n
n3=nl-1
n4=(1-(n3))/n
yse=h*(1/n+r*n4)
ise=h*r*n4
yse

#vedhængende rente
#dage ud af terminsperioden ved valørdato
d=260
#antal årlige terminer
m=1
v=h*r*d/365
v
#kurs
#rissikofri rente
r0=0.06
dt=(1+r0)^-nl

#pris af ønsket
sum(yse*dt)
yse*dt




###Varighed

#Serie
y=0.04
R=0.06
n=5
Vse=(1+y)/y*(1-(R*(1-(1+y)^(-n))/y+n*(y-R)*(1+y)^(-n-1))/(R*n+(y-R)*(1-(1+y)^(-n))/y))
Vse

#Stående
y=0.04
R=0.06
n=5
Vst=(1+y)/y-(1+y-n*(y-R))/(R*((1+y)^n-1)+y)
Vst

#Annuitet
y=0.04
R=0.06
n=5
Van=(1+y)/y-n/((1+y)^n-1)
Van