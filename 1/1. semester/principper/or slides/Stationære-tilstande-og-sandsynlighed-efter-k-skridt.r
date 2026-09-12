n = 4 #sætter antal tilstande

P = matrix(c(0.2,0.8,0,0,0,0.3,0.7,0,0,0,0.5,0.5,0.8,0,0,0.2),nrow = n,byrow=TRUE) 

rowSums(P) #tjekker om rækkerne summer til 1
P #tjekker hvordan matricen jeg har defineret ser ud.

#Beregn stationære tilstande: Husk at det ikke gør en forskel hvilket stadie man starter i når man finder grænseværdier 
#Argumenter: 
#aperiodisk jf. s.641(selvløkke = p_ii>0 for et i) eller se s.641
#og irreducibel(alle stadier kommunikerer med hinanden)



A = t(P) - diag(n) #matricen er irreducibel og aperiodisk så der findes en grænsefordeling. Jeg finder den:
A[n, ] = 1
A

b = rep(0,n)
b[n] = 1
b

solve(A,b)
pi_i=solve(A,b)
#Middelventetid:1/n'te indgang af stationærfordeling lige under ex. 11.14 i IPSR
r_i=1/pi_i #når den grænsefordelingen findes
r_i

#Beregn sandsynligheder efter k skridt
k = 7 #antal skridt
P%^%(k) #opløfter overgangsfordeling i k
pi_0 = c(1,0,0,0)#skriver 1 ved givne tilstand hvis vi ved hvor den starter, ellers skriver vi C(P(X_0=tilstand1,P(X_0=tilstand2,....)))
pi_0%*%(P%^%k)



