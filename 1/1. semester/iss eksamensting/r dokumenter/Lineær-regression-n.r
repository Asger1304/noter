x = c(1.1,0,5.3,3.8,9.2,6.9,0.7,9.2)
y = c(4.5,-0.1,11.6,5.9,16.4,16.1,1.8,20.6)

# Simpel lineær regression, afsnit 8.5.2
sxx = sum((x-mean(x))^2)
sxy = (sum((x-mean(x))*(y-mean(y))))

cov(x,y)/var(x)
beta_1 = sxy/sxx
beta_0 = mean(y) - beta_1*mean(x)

0.5/sxx #varians for estimat for beta_1, når fejlled har standardafvigelse 0.5.

#Ekstraspørgsmål - prædiktion for y når x = 0.4
n = length(x)
y_hat = beta_0 + beta_1*x

# Konfidensinterval for middelværdi af y når x = 0.4
s02 = 1/(n-2) * sum((y - y_hat)^2)

a = sqrt(s02*(1/n + (0.4 - mean(x))^2/(sum((x - mean(x))^2))))

y_hat_0.4 = beta_0 + beta_1*0.4

y_hat_0.4 + c(-1,1)* qt(1-0.05/2,n  - 2) * a

