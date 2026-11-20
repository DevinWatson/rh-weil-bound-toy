from sympy import symbols, interpolate
x=symbols('x')
pts={11:372,13:901,17:2502,19:3762,23:7432,29:16540}
for sel in ([17,19,23,29],[13,17,19,23],[11,13,17,19],[13,19,23,29]):
    P=interpolate([(a,pts[a]) for a in sel],x)
    print(sel,P,"P(1)=",P.subs(x,1),[ (a,P.subs(x,a)-pts[a]) for a in pts])
# integer-coefficient monic test: q^3+a q^2+b q+c
import itertools
sols=[]
for a in range(-30,1):
    for b in range(0,200):
        for c in range(-400,100):
            if all(a_*a_*a_+a*a_*a_+b*a_+c==v for a_,v in [(19,3762),(23,7432),(29,16540)]):
                sols.append((a,b,c))
print(sols)
