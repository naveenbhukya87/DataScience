import matplotlib.pyplot as plt  # type: ignore
x1 = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
x2 = [1, 2, 3, 4]
y2 = [2, 4, 6, 8]

lines = plt.plot(x1, y1, x2, y2)

# use keyword args
plt.setp(lines[0], color='r', linewidth=2.0)
# MATLAB style string value pairs
plt.setp(lines[1], "color", 'g', "linewidth", 2.0)
plt.grid()
plt.show()