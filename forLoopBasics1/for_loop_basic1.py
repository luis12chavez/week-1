# 1 
for i in range(151):
    print(i)

# 2
for i in range(5, 1001, 5):
    print(i)

# 3 
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# 4
total = 0
for i in range(0, 500001):
    if i % 2 != 0:
        total += i
print(total)   

#5
for i in range(2018, 0 , -4):
    print(i)

#6
lowNum = 4
highNum = 20
mult = 5
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)