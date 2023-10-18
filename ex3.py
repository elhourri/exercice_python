def somme_Diviseurs(n):
   s=0
   for i in range(2,n):
    if n%i==0:
     s=s+i
   return s

N=int(input("entrer un nombre :"))
M=int(input("entrer un nombre :"))
print("la somme des diviseur de  :",N," est",somme_Diviseurs(N))
print("la somme des diviseur de  :",M," est",somme_Diviseurs(M))
if somme_Diviseurs(N)==M and somme_Diviseurs(M)==N :
 print(M," et ",N," sont des amis")
else :
  print(M," et ",N," ne sont pas des amis")