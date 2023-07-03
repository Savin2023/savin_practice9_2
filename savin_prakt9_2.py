print("Введите список №1 через пробел")
m=input().split()
mnvo_m=set(m)

print("Введите список №2 через пробел")
n=input().split()
mnvo_n=set(n)

print(len(mnvo_m.intersection(mnvo_n)))
    
