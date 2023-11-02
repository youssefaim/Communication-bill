def com(m):
    t = []
    t.append(m*2)
    a1 = m - 30
    if a1 >= 0 :
        b1 = 20 + a1 * 1.5
        t.append(b1)
    else :
        t.append(20)
    a2 = m - 60
    if a2 >= 0 :
        b2 = 50 + a2 * 1
        t.append(b2)
    else :
        t.append(50)
    a3 = m - 120
    if a3 >= 0 :
        b3 = 100 + a3 * 0.5
        t.append(b3)
    else :
        t.append(100)
    return t
m = float(input("enter the number of hours :"))

m = m * 60
print("Given the time you enter, we have four plans for you :")
t = com(m)
T2 = [0,20,50,100]
for i in range (4):
    print("Plan ",i+1," has an amount of ",t[i],"MAD","if you subscribe by :",T2[i],"MAD")
for i in range(4):
    for j in range(i+1,4):
        if t[j] < t[i]:
            min = t[j]
print("the best for you is the plan when you well pay :",min,"MAD")
print("the last plan that we think is the best for everyone you will pay 200 MAD and you'll get infinity time to speak")