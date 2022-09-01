from z3 import *

# test case 1
x = Int('x')
y = Int('y')
solve(x > 2, y < 10, x + 2*y == 7)

# test case 2
p = Bool('p')
q = Bool('q')
print (And(p, q, True))
print (simplify(And(p, q, True)))
print (simplify(And(p, False)))

# test case 3
x = Int('x')
y = Int('y')

s = Solver()
print (s)

s.add(x > 10, y == x + 2)
print (s)
print ("Solving constraints in the solver s ...")
print (s.check())

print ("Create a new scope...")
s.push()
s.add(y < 11)
print (s)
print ("Solving updated set of constraints...")
print (s.check())

print ("Restoring state...")
s.pop()
print (s)
print ("Solving restored set of constraints...")
print (s.check())

# test case 4
print ("test case 4")
x = Real('x')
y = Real('y')
s = Solver()
s.add(x > 1, y > 1, Or(x + y > 3, x - y < 2))
print ("asserted constraints...")
for c in s.assertions():
    print (c)

print (s.check())
print ("statistics for the last check method...")
print (s.statistics())
# Traversing statistics
for k, v in s.statistics():
    print ("%s : %s" % (k, v))

# test case 5
print ("test case 5")
x, y = Reals('x y')
solve(x + 10000000000000000000000 == y, y > 20000000000000000)

print (Sqrt(2) + Sqrt(3))
print (simplify(Sqrt(2) + Sqrt(3)))
print (simplify(Sqrt(2) + Sqrt(3)).sexpr())
# The sexpr() method is available for any Z3 expression
print ((x + Sqrt(y) * 2).sexpr())

# test case 6
print ("test case 6")
x = BitVec('x', 16)
y = BitVec('y', 16)
print (x + 2)
# Internal representation
print ((x + 2).sexpr())

# -1 is equal to 65535 for 16-bit integers
print (simplify(x + y - 1))

# Creating bit-vector constants
a = BitVecVal(-1, 16)
b = BitVecVal(65535, 16)
print (simplify(a == b))

a = BitVecVal(-1, 32)
b = BitVecVal(65535, 32)
# -1 is not equal to 65535 for 32-bit integers
print (simplify(a == b))

# test case 7
print ("test case 7")
x = Int('x')
y = Int('y')
f = Function('f', IntSort(), IntSort())
s = Solver()
s.add(f(f(x)) == x, f(x) == y, x != y)
print (s.check())
m = s.model()
print ("f(f(x)) =", m.evaluate(f(f(x))))
print ("f(x)    =", m.evaluate(f(x)))