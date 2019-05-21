import numpy as np
import matplotlib.pyplot as plt

A = [5, 3, 9, 7]
I = np.argsort(A)
A.sort()
print(I)
# help(plt.plot)
plt.plot(I, A, 'go')
plt.show()
