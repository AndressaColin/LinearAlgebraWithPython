#set up a proportion: x1/y1 = x2/y2
x1 = 2
x2 = 10
y1 = 
y2 = 9

if x2 == 0:
    answer = x1 * y2 / y1
elif y2 == 0:
    answer = x2 * y1 / x1
else:
    answer = (x1/y1) == (x2/y2)

print(answer)