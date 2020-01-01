import matplotlib.pyplot as plt

input_values=list(range(1,5001))
output_values=[x**3 for x in input_values]

plt.scatter(input_values,output_values,c=output_values,cmap=plt.cm.winter)
plt.show()