library(pracma)

fun <- function(x,y) (y * x * 15 * x * (y^2)) #skriv funktion
#hvis grænserne er en funktion af x eller y skriv; function(x eller y) funktionsforskrift
#hvis uendelig så skriv inf eller -inf
xmin <- 0; xmax <- function(y) sqrt(1-(y^2)) #græænserne for x
ymin <- 0; ymax <- 1 #grænserne for y
integral2(fun, ymin, ymax, xmin, xmax) #de første grænser er for yderste integrale

#integration
f = integral(exp(2*x) ~ x)
f(from=1,to=4)
#eller
fun <- function(x) (sin(x)*x) #skriv funktion
xmin <- 0; xmax <- pi/2
integral(fun, xmin, xmax)
