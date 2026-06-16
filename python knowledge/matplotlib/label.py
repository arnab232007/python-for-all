import matplotlib.pyplot as plt
data = [1, 2, 3, 4, 5]
subdata = [1, 4, 9, 16, 25]
sub2 = [1, 8, 27, 64, 125]
plt.plot(data, subdata, label='subdata')
plt.plot(data, sub2, label='sub2')
plt.legend()
plt.show()