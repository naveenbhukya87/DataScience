import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
data1 = np.arange(0, 10, 2)
squares = [0, 4, 16, 36, 64]
data2 = np.arange(0, 10, 2)
cubes = [0, 8, 64, 216, 512]
plt.figure(1)
plt.subplot(211)
plt.grid()
plt.plot(data1, squares, "b-o")
plt.subplot(212)
plt.grid()
plt.plot(data1, cubes, "r-o")

plt.figure(2)
plt.plot([0,1,2,3,4])

plt.figure(1)
plt.subplot(211)
plt.title("Squares")
plt.figure(2)
plt.grid()
plt.show()