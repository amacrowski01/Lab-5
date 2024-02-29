#the authors' names are Allison Macrowski and Therese Burns
def perfect():
    total=0
    x=int(input("number:\n"))
    for n in range(1,x):
        if x%n==0:
            total+=n
    if total==x:
        return(True)
    else:
        return(False)
print(perfect())



