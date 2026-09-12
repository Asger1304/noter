k=198
u=1.08
d=0.92
s0=200
r=0.04
su=s0*u
sd=20*d
cu=max(0,su-k)
cd=max(0,sd-k)
delta = (cu-cd)/(su-sd)
beta = (cd-sd*delta)/(1+r)
beta
delta
c0=s0*delta+beta
c0
p0=k/(1+r)+c0-s0

