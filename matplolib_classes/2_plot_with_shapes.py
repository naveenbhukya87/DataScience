import matplotlib.pyplot as plt  # type: ignore
import numpy as np  # type: ignore
t = np.arange(0., 5., 0.2)
'''[0.  0.2 0.4 0.6 0.8 1.  1.2 1.4 1.6 1.8 2.  2.2 2.4 2.6 2.8 3.  3.2 3.4
 3.6 3.8 4.  4.2 4.4 4.6 4.8]
 '''
plt.plot(t, t**2, 'b--', label="^2")
plt.plot(t, t**2.2, 'rs', label="^2.2")
plt.plot(t, t**2.5, 'g^', label="^2.5")
plt.grid()
plt.legend()
plt.show()
