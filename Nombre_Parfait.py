def est_premiers(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i== 0:
            return False
    return True
def affichage_premiers(n):
    N=[i for i in range(2, n+1) if est_premiers(i)]
    print(f"nombres premiers <={n} : {N}")
n=int(input("entrez un nombre: "))
affichage_premiers(n)

