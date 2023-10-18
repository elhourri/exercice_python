n=int(input("entrer un entier n:"))
print("Les nombres entiers premiers inferieurs a ",n," sont  ")
for i in range(1,n):
    np=0
    j=2
    while j<i :
        if i%j==0:
            np=1
        j=j+1
    if np==0:
      print(i)
