#define market

sigma =1/100* matrix(c(2.89,0.646,1.224,
               0.646,3.61,1.824,
               1.224,1.824,5.76),3,3,byrow=TRUE)


RE = c(0.12,0.09,0.16)



one=c(1,1,1)
#ønsket afkast

r_p=0.12


#MARKOWITZ FRAMEWORK
a =t(one)%*%solve(sigma)%*%one
b = t(one)%*%solve(sigma)%*%RE
c = t(RE)%*%solve(sigma)%*%RE
d = a*c-b*b
#optimale vægtninger

w_mark = as.numeric((a*r_p-b)/d)*solve(sigma)%*%RE +as.numeric((c-r_p*b)/d)*solve(sigma)%*%one
#tjek
t(w_mark)%*%RE

V_mark=t(w_mark)%*%sigma%*%w_mark
S_mark=sqrt(V_mark)

#MVP
r_mvp = b/a
v_mvp = 1/a
w_mvp = as.numeric(1/a)*solve(sigma)%*%one

#risikofrit aktiv

r_f=0.04
#alpha
alpha = RE - r_f

#ønsket afkast so ekstra afkast

r_p=0.12
r_p_e = r_p-r_f


#finder optimale vægte efter det risikofrie aktiv træder ind på markedet 
w_rf = as.numeric( r_p_e / (t(alpha)%*%solve(sigma)%*%alpha) ) * solve(sigma)%*%alpha


#finder andel i risiko frit aktiv

w_in_rf = 1-sum(w_rf)



#finder variansen 
var_rf = r_p_e^2/t(alpha)%*%solve(sigma)%*%alpha
sd_rf = sqrt(var_rf)



#sanity check
r_p_e_test = sd_rf*sqrt(t(alpha)%*%solve(sigma)%*%alpha)




#finder tangentporteføljen

r_e_tan = t(alpha)%*%solve(sigma)%*%alpha / ( t(one)%*%solve(sigma)%*%alpha )



#bemærk at r_e_tan er ekstra afkast og det egentlige afkast kan findes + r_f

w_e_tan = ( solve(sigma)%*%alpha ) /as.numeric( ( t(one)%*%solve(sigma)%*%alpha))

var_tan = t(w_e_tan) %*% sigma %*% w_e_tan
r_tan = r_e_tan + r_f
sd_tan = sqrt(var_tan)





pnorm(-r_mvp/sqrt(v_mvp))







