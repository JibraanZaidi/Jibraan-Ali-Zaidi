string=str(input("ENTER A STRING :"))

alphab=[alpha.lower()for alpha in string.split()]
for k in range(len(alphab)):
    for i in range(len(alphab)-1):
        if alphab[i]>alphab[i+1]:
            alphab[i],alphab[i+1]=alphab[i+1],alphab[i]
print("sorted word:")
for alpha in alphab:
    print(alpha)
