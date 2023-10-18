n=int(input("entrer le nombre de note : "))
notes={}
s=0
for i in range(0,n):
    notes[i]=int(input("entrer la note :"))
    s=s+notes[i]
m=s/n
print("les notes qui sont au dessus de la moyenne ",m)
for i in range(1,n):
    if notes[i]>=m:
        print(notes[i])