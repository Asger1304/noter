n = 4 #antal tilstande
P = matrix(c(1,0,0,0,0,1,0,0,0.3,0.4,0.2,0.1,0.2,0.3,0.1,0.4),nrow=n,byrow=TRUE)
rowSums(P) #tjekker om rækkerne summer til 1

b=c(0,0,1)
solve(A,b)

C = matrix(c(1,3,2,0),nrow=2,byrow=TRUE)
D = matrix(c(2,3,4,1),nrow=2,byrow=TRUE)
#matrix produkt
C%*%D
#A^2, aktiver først pakken "expm"
C%^%2

A_8=matrix(c(-1,0.6,0.6,0.6,-1,0.4,1,1,1),nrow=3,byrow=TRUE)
solve(A_8,b)

A_d=matrix(c(-0.2,0.3,1,1),nrow=2,byrow=TRUE)
b_d=c(0,1)
solve(A_d,b_d)

A_e=matrix(c(-p,1-p,p,-1,0,1,1,1),nrow=3,byrow=TRUE)
solve(A_e,b)
