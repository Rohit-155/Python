from numpy import *

# exp = [2200, 2350, 2600, 2130, 2190]
# # print(exp[1]-exp[0])
# # print(exp[0]+exp[1]+exp[2])
# # if 2000 in exp:
# #     print("Yes")
# # else:
# #     print("No")
# # exp.append(1980)
# # print(exp)
# exp[3] = exp[3]-200
# print(exp)


N = [10,25,52,47,30]
max = N[0]
for num in N:
    if num>max:
        max=num
        print(max)
