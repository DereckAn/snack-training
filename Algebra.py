
import math
import numpy as np
import sympy as sym
from IPython.display import display, Math
from sympy.abc import w,x,y,z


rangemat = range(1,11)
mat1 = np.zeros((len(rangemat),len(rangemat)), dtype = int)

for i in rangemat:
    for j in rangemat:
        mat1[i-1,j-1] = i*j
        
display(Math(sym.latex(sym.sympify(mat1)))) #Nota solo usamos el display para que aparescan todos los resultados. Por Ejemplo: si ponermos muchos "Math()" solo aparecera el ultimo mientras que si ponemos todos con diplaey se mostraran todos los "Math()"
print(mat1)

#------------------------------------------------- propiedades   --> Propiedad Asosiativa, Propiedad Conmutativa, Propiedad Distributiva. 
# -- Propiedad asosiativa. --> regla de los parentesis

# 2(3x4) = (2x3)4
# 2(12) = (6)4
# 24 = 24

# -- Commutative rule 
# a x b = b x a

# -- Distrivute rule 
# x(y+z) = xy + xz


# Associative 
ex1 = x*(4*y)
ex2 = (x*4)*y
print(ex1 - ex2) # esto es para demostrar que es verdad --> tiene que salir 0

# Commutative 
e1 = 4*x*y
e2 = x*4*y
e3 = y*x*4
print(e1.subs({x:3, y:2}))
print(e2.subs({x:3, y:2}))
print(e3.subs({x:3, y:2})) # Si todas las ecuaciones tienen el mismo resultado entonces la propiedad se cumple. 

# Distrivutive 
a,b,c,d = sym.symbols("a,d,c,b")
exp = (a+b)*(c+d)
sym.expand(exp) # Esta funcion nos da la propiedad distrivutiva --> ab + ac + bd + cd


#--------------------------------------------------------------------------------------------> exercise. 
f1 = x*(y+z)
f2 = 3/x + x**2

x1 = w*(4-w) + (1/w**2)*(1+w)

f1.subs(x,x1)
f2.subs(x,x1)
display(Math(sym.latex(sym.expand(f1)))) # Quitar la propiedad distributiva. --> Quitar parentesis. 
display(Math(sym.latex(sym.expand(f2)))) # Quitar la propiedad distributiva. --> Quitar parentesis.
display(Math(sym.latex(sym.simplify(f1)))) # Agrupoar todo en un solo termino --> todavia con parentesis.
display(Math(sym.latex(sym.simplify(f2)))) # Agrupar todo en un solo termino --> todavia tiene parentesis. 

# -------------------------------------------------------------------------------------------------------------- List 

lista = [1,2,3,4,5]
lista[3]   # usamos Corchetes para crear y para seleccionar el valor de la lista. 

# Slicing 
lista[:2] # para saber los valres del 0 al 1
lista[-2:] # Para ver los dos ultimos valores de la lista. 

words = ["hola", "mi", "nombre", "es", "Dereck"]
for i in words:
    print(i)

alist = [1,2,"cookies", [6,4]]

alist[-1][0]  # Esto es para entrar a una lista dentro de una lista.     --> 6

# -------------------------------- exercise

listex = [e1,e2,e3]

e1 = 2*x + x*(4-6*x) + x
e2 = -x*(2/x + 4/x**2) + ((4+x)/(4*x))
e3 = (x+3)*(x-3)*x*(1/(9*x))

for i in listex:
    #display(Math(sym.latex(sym.expand(i))))
    display(Math("%s \\quad \\Longleftrightarrow \\quad %s" % (sym.latex(i), sym.latex(sym.expand(i)))))  # Ten cuidado con los "%s" hay varios y funcionan para diferentes tipod de datos. 
    

# --------------------------------------------------- Slicing.  




vec = list(range(10,21))      # Ten muhco cuidado de no poner un nombre como "list"
           

vec[0] # para acceder a los elementos de la lista. Este caso es el primero. 
vec[1:4] # Esto es para acceder a una parte especifica de la lista. 
vec[-1] # Para obetjer el ultimo numero. 
vec[::-1] # Esto es para ir de atras para delante en la lista. 
vec[::2] # para mostrar llos numeros en saltos de dos en doe. 
vec[0:5:2] # Esto es para mostrar los numeros del 10 al 14  pero  de dos en dos. 




# ----------------------------------------------------------------------------------------------> Greatest common denominator. 
# The largest integer that divides into two numbers with no remainder. 

# gcd(2,4) = 2
# gcd(6,15) = 3
# gcd(6,17) = 1

math.gcd(95,100)    # Solo para integers. 

a = 16
b = 88

fact = math.gcd(a,b)
print(fact)
display(Math(f"\\frac{{{a}}}{{{b}}} =  \\frac{{{a/fact} \\times {fact}}}{{{b/fact} \\times {fact}}}"))

#---------------------------------------------------------------------------------------------------> exercise 
a,b,c = sym.symbols("a b c")
print(sym.gcd(a*c, b*c))
print(c*sym.gcd(a,b))

a = 5
b = 6
c = 7

print(math.gcd(a*c, b*c))
print(c*math.gcd(a,b))

display(Math("\\text{gcd(ca,cb) = c * gcd(a,b)}"))


#----------------------------> exercise 2
pepa = 10
pepe = 15
matris = np.zeros(([pepa,pepe]), dtype = int)+99  # estos ultimos numeros son para que cada valor de la matris sea "99"

for i in range(0,pepa):
    for j in range(0,pepe):
        matris[i, j] = math.gcd(i+1,j+1)
        
display(Math(sym.latex(sym.sympify(matris))))  # ParseError: KaTeX parse error: Unknown column alignment: 1 at position 34: …t[\begin{array}1̲ & 1 & 1 & 1 & …  Solo pasa cuando pongo el "sym.sympify()"




# ----------------------------------------------------------------------------> Dictionaries. 
# Los diccionaios usan llaves. {}

d = dict(fruit = ["banana" , "apple"], numbers = [1,2,3,4,5])

d.keys()   # dict_keys(['fruit', 'numbers']).
d["fruit"]  # ['banana', 'apple']  Regresa los valores de una llave especifica. 
d["fruit"][1]  # Esto es para escoger un valor especifico de una llave especifica.   --->  'apple'
len(d)  # Esto indica cuantas llaves (keys) tiene el disccionario. 
d.get("fruit")[1] # Esto es para obtener el valor especifico de una llave especifica.  --->  "apple"

for itmer in d:
    print(d[itmer])  # Esto es para regresar todos los valores del diccionario. -->['banana', 'apple'] [1, 2, 3, 4, 5]





#------------------------------------------------------------------------------> Exercises 

ecuation1 = 4*x - 6
ecuation2 = sym.sin(y) == 0
ecuation3 = x**2 - 9

display(Math(f"{{{sym.latex(sym.sympify(ecuation1))}}} \\quad \\RightArrow \\quad X = {{{sym.latex(sym.solve(ecuation1))}}}"))

#---- Version del profesor con un pocpo de version mia. 

D = dict(eqsWithX = [4*x - 6, x**2 - 9], eqsWithY = [sym.sin(y)])

for keyi in D:
    print("Solutions for equations involving " + keyi[-1] + ":") #Solutions for equations involving X:  \n  Solutions for equations involving Y:
    
    for eqi in D[keyi]:
        display(Math(f" {{{sym.latex(sym.sympify(eqi))}}} = 0 \\quad \\Rightarrow \\quad {{{keyi[-1]}}} = {{{sym.latex(sym.solve(eqi))}}}"))
    
    
    
# Version toalmete del profesor.    
D = dict(eqsWithX = [4*x - 6, x**2 - 9], eqsWithY = [sym.sin(y)])

for keyi in D:
    print("Solutions for equations involving " + keyi[-1] + ":") #Solutions for equations involving X:  \n  Solutions for equations involving Y:
    
    for eqi in D[keyi]:
        leftpart = sym.latex(eqi) + ' = 0'
        midpart = "\\quad \\Rightarrow \\quad " + keyi[-1] + " = "
        rightpart = sym.latex(sym.solve(eqi))
        
        display(Math("\\quad \\quad " + leftpart + midpart + rightpart))
        

# ------------------------------------------------------------------------------- prime Factorization. 
number = 48

sym.factorint(number) # Esta es la funcion para saber la factorizacion prima. (con solamente numeros primos)  ---> :. {2: 4, 3: 1} this is a dictionary.

#------------ ecxercise 
rango = range(2,51)
for i in rango:
    factprim = sym.factorint(i)
    if list(factprim)[0] == i:
        print(f"{i} is a prime number.")
    else:
        print(f"{i} is a composite number with prime factors: {list(factprim)}")

# Solucion del profesor
nums = range(2,51)

for numi in nums:
    di = sym.factorint(numi)
    ks = list(di.keys())
    
    if len(di) == 1 and di[ks[0]] == 1:
        print("%g is a prime number " % numi)
    else:
        print("%g is a composite number with prime factors: %s" % (numi, list(di.keys())))

# ------------------------------------------------------------------------------------------------- Inequalities. 

ho = (x-1)*(x+3) > 0
sym.solve(ho)     #(−∞<x∧x<−3)∨(1<x∧x<∞)

# ----------- Exercise 
hol1 = (3*x)/2 + (4-5*x)/3 <= 2 - (5*(2-x))/4
display(Math(sym.latex(sym.sympify(hol1))))
sym.solve(hol1)

# --------------------------------------------------------------------------------------------------------- Adding polynomials  

p1 = 2*x**3 + x**2 - x
p2 = x**3 - x**4 - 4*x**2

display(Math(sym.latex(p1)))
display(Math(sym.latex(p2)))
display(Math(f"({{{sym.latex(p1)}}}) + ({{{sym.latex(p2)}}}) \\quad = \\quad {{{sym.latex(p1+p2)}}}"))



p11 = sym.Poly(2*x**3 + x**2 - x)
type(p11)   #---> sympy.polys.polytools.Poly
print(p11)  #  ---> Poly(2*x**3 + x**2 - x, x, domain='ZZ')    indica el polinomio, la variable principal, y el dominio -- 'z' representa que todos los coeficientes son integers 

p11.eval(0) # Sustituye el valor de todas las variables x por 0    ---> Solo regresa el resultado final
p11.coeffs() # Esto regresa una lista de todos los coeficientes  (los numeros que estan adelante de las variables.)


#  ------------------ Exercise
p21 = x**2 + 2*x
p22 = -x**3 +4*x    
p23 =  x**5 - x**4  + 1/4*x + 4

lp = [sym.poly(p21),sym.Poly(p22), sym.Poly(p23)] # Necesitamos transformar tdas las ecuaciones en polinomios. 
for i in lp:
    if i.degree() % 2 == 0:
        print("The degree of (%s) is even, and the coefficients sum to %g" % (i.as_expr(), sum(i.coeffs())))
    else:
        print("THe degree of (%s) is odd, and there are %g coefficients" % (i.as_expr(), len(i.coeffs())))
        
        
# -------------------------------------------------------------- Multiplying polynomials  

pol1 = 4*x**2 - 2*x
pol2 = x**3 - 1

print(pol1*pol2)  # --> (4*x**2 - 2*x)*(x**3 - 1)
sym.expand(pol1*pol2)  # Para expadir los polinomias. Popiedad distributiva. (No parentesis)
display(Math(sym.latex(sym.expand(pol1*pol2))))  

# ----------------Exercise

f = 4*x**4 - 3*x**2 + x*y**2 - 9*y**3
g = -x**3 + 6*x**2*y + 0.8*y**3

# f1 = sym.Poly(f)
# g1 = sym.Poly(g)
# display(Math("The multiplication of %s and %s is: %s" % (f1.as_expr(),g1.as_expr(), sym.latex(sym.expand(f*g)) )))  # Mia

display(Math("(%s) \\times (%s) = %s" % (sym.latex(f), sym.latex(g), sym.latex(sym.expand(f*g)))))  # Profe

xval = 5
yval = -2

ans = (f*g).subs({x:xval, y: yval}) # Esta funcion regresa el resultado total.    SOLO UN NUMERO  
print(ans)

fans = f.subs({x:xval, y: yval})
gans = g.subs({x:xval, y: yval})

print(f"{fans}\n{gans}")


# --------------------------------------------------------------------------------Dividing polynomials.
p1 = 4*x**5 - x 
p2 = 2*x**3 - x

display(Math("\\frac{%s}{%s} = %s" % (sym.latex(p1), sym.latex(p2), sym.latex(p1/p2))))
display(Math("\\frac{%s}{%s} = %s" % (sym.latex(p1), sym.latex(p2), sym.latex(sym.expand(p1/p2)))))
display(Math("\\frac{%s}{%s} = %s" % (sym.latex(p1), sym.latex(p2), sym.latex(sym.simplify(p1/p2)))))

# ------ exercise

ecu1 = x**6 + 2*x**4 +6*x - y
ecu2 = x**3 + 3
rango1 = range(5,16)

for i in rango1:
    ecu11 = ecu1.subs(y,i)
    display(Math("\\frac{%s}{%s} = %s" % (sym.latex(ecu11), sym.latex(ecu2), sym.latex(sym.simplify(ecu11/ecu2)))))
    
    if sym.fraction(sym.simplify(ecu11/ecu2))[1] == 1:
        answer0 = i

print(f"The answer that satisfies our goal is y = {answer0}")


# --------------------------------------------------------------------------------- Factoring polymonials. 

p = x**2 + 4*x + 3
sym.factor(p)  # Este meotodo es para factorizar os polinomios ---> (x + 1)*(x + 3)

expr = 2*x**3*y - 2*x**2 + 2*x**2*y + 6*x**2 - 6*x*y + 6*x
sym.factor(expr)  #  --->  2*x*(x**2*y + x*y + 2*x - 3*y + 3)

# --- exercise

hola1 = [x**2 +4*x +3, 2*y-1, 3*y**2 +12*y]  # Mi solucion 
for i in hola1:
    if sym.factor(i) == i:
        nha = "\\text {Not factorable!}"
    else:
        nha = sym.latex(sym.factor(i))
        
    display(Math("%s \\quad \\Rightarrow \\quad %s" % (sym.latex(i), nha )))



exprs = [x**2 +4*x +3, 2*y-1, 3*y**2 +12*y]  # solucion del profesor. 
for ei in exprs:
    strfact = str(sym.factor(ei))
    
    if strfact.find("(") != -1:
        display(Math("%s \\quad \\Rightarrow \\quad %s" % (sym.latex(ei), sym.latex(sym.factor(ei)))))
    else:
        display(Math("%s \\quad \\Rightarrow \\quad \\text{ Not factorable!}" % (sym.latex(ei))))
        

# -------------------------------------------------------------------------------------------------Bug Hunt

# import math   --> ejercicio con un error. 
# gcd(30,50) 

# ----> solucion --> math.gcd(30,50)


x = sym.symbols("x")
expr = 4*x - 8
sym.solve(expr) # Para encontrar el valor de x



A = np.array([[1,2],[3,4]])  # Ten cuidado con los parentesis y los corchetes
display(Math(sym.latex(sym.sympify(A))))



fact_dict = sym.factorint(44)
for i in fact_dict:
    print("%g was present %g times" % (i, fact_dict[i]))
    
    

expr2 = 4*x -5*y**2
expr2.subs({x:5})







