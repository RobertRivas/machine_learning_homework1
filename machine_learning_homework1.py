import matplotlib.pyplot as plt


x_data = [45, 36, 37, 43, 38, 49, 39, 43, 44, 38, 42, 40]

y_data = [43, 35, 34, 41, 44, 44, 42, 46, 39, 39, 47, 39]

x_average = sum(x_data)/len(x_data)
y_average = sum(y_data)/len(y_data)


xy = []

for i in range(len(x_data)):

    xy.append(x_data[i] * y_data[i])


xy_average = sum(xy)/len(x_data)

x_squared = []
for j in range(len(x_data)):

    x_squared.append(pow(x_data[j], 2))

x_squared_average = sum(x_squared)/len(x_data)

theta_sub_1 = ((xy_average) - (x_average * y_average))/((x_squared_average)-(pow(x_average, 2)))

theta_sub_0 = y_average - (theta_sub_1 * x_average)



#  best linear function
best_linear_function_values = []

for z in range(len(x_data)):

    best_linear_function_values.append(theta_sub_0 + (theta_sub_1*x_data[z]))
    print(best_linear_function_values[z])



# prediction for x = 27

print()

predicted_value_at_27 = theta_sub_0 + (theta_sub_1 * 27)
print("The predicted value at x = 27 is: ", predicted_value_at_27)

plt.scatter(x_data, y_data)
plt.plot(x_data, best_linear_function_values)
plt.xlabel('Interested in Class')
plt.ylabel('Enrolled in Class')

plt.show()