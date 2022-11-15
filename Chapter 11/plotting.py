from bakery_salary import industries
import matplotlib.pyplot as plt


mean_salaries = []
median_salaries = []
members = []
for industry in industries:
    mean_salaries.append(industry.mean_salary)
    median_salaries.append(industry.median_salary)
    members.append(industry.members)


plt.scatter(mean_salaries, median_salaries)
plt.scatter(mean_salaries, members)
plt.title("Mean Salaries")
plt.xlabel("Salary")
plt.ylabel("Median Salary")

plt.show()
