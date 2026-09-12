k=198
u=1.08
d=0.92
s0=200
r=0.04
su=s0*u
sd=20*d
pu=max(0,k-su)
pd=max(0,k-sd)
delta = (pu-pd)/(su-sd)
delta
b=(pd-sd*delta)/(1+r)
b
delta*s0+b
