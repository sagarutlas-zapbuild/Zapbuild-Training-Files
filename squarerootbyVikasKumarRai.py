def sqrt(num):
    for i in range(1,num+1):
        if i*i == num:
            return i
        elif i*i > num:
            i = i-1
            v = 0.01
            for j in range(1,100):
                if (i+v)**2 >= num:
                    return  i+v
                else:
                    v += 0.01
n = int(input("Enter the number:"))
print(round(sqrt(n),3))