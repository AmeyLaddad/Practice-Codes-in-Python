import numpy as np

x = np.arange(3*2).reshape(3,2)
print(x)

y = x = np.arange(3*2).reshape(3,2)
print(y)
 
# Add `x` and `y`
print("addition = ",np.add(x,y))

# Subtract `x` and `y`
print("subtraction = ",np.subtract(x,y))

# Multiply `x` and `y`
print("multiplication = ",np.multiply(x,y))

# Divide `x` and `y`
print("division = ",np.divide(x,y),float)

