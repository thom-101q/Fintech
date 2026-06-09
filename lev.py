def simpleAdder(x,y):
    total = 0;
    total = x + y;
    return total;


print(simpleAdder(5,11));

def complexTotal(x,y):
    newTotal = 0;
    count = 0;  
    while newTotal < 100:
        newTotal += simpleAdder(x,y);
        count += 1;
    return count;
    #counts the number of simpleAdder function needed to run to fullfil the while loop condition;

print(complexTotal(1,4))

