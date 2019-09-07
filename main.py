import csv
import matplotlib.pyplot as plt

dict = {}
with open("home_ownership_data.csv") as f:
    rd = csv.reader(f)
    next(rd)
    for row in rd:
        dict[row[0]] = [row[1]]
with open("loan_data.csv") as f:
    rd = csv.reader(f)
    next(rd)
    for row in rd:
        dict[row[0]].append(row[1])

count_m = 0
count_r = 0
count_o = 0
for item in dict.items():
    ownership = item[1][0]
    if ownership == 'MORTGAGE':
        count_m += int(item[1][1])
    if ownership == 'RENT':
        count_r += int(item[1][1])
    if ownership == 'OWN':
        count_o += int(item[1][1])

fig, axes1 = plt.subplots()
fig2, axes2 = plt.subplots()
axes2.bar(['MORTGAGE', 'OWN', 'RENT'], [count_m, count_o, count_r])

axes2.set_title('Average loan amounts per ownership')
axes2.set_xlabel('Home onwnership')
axes2.set_ylabel('Average loan amounts($)')

axes1.table(rowLabels=[0, 1, 2], colLabels=['home_onwnership', 'loan_amnts'], cellText=[['MORTGAGE', count_m], ['OWN', count_o], ['RENT',count_r]], loc='center')
axes1.set_xticks([])
axes1.set_yticks([])
plt.show()