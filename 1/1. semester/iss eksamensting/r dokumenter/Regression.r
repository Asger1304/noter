#Lineær Regression bestem konstanter i y_i=B_0 + B_1 * x_i + epsilon_i
x=c(0.93,0.47,0.26,0.16,0.97,0.74,0.93,0.36,0.48,0.49,0.84,0.77)
y=c(8.56,5.98,6.83,5.26,9.78,7.51,8.41,6.72,6.82,5.14,7.56,6.64)
B_1 = cov(x,y)/var(x) #Bestem B_1 ud fra data (s. 501)
B_1
B_0 = mean(y)-B_1*mean(x) #bestem b_0 ud fra data (s. 501)
B_0

y_hat = B_0+B_1*2 #bestem y når x_i antager givet værdi
y_hat

#find MSE(B_1) kap 8 opg 23 E(B_1^hat)=B_1 Var(B)



e_i = y_hat-y_i #hvor y_i er en værdi af y fra datasættet 
e 
r_2=cov(x,y)^2/(var(x)*var(y)) #koefficient of determination (s.505)
r_2


21/225
21/225-(qnorm(1-0.05)*sqrt(34)/(20)/sqrt(225))
(21/225-0.1)/(sqrt(34)/(20))/sqrt(225)
x_bar=21/225
x_bar-qnorm(1-0.05)*(sqrt(34)/20)/15
