from random import *
inimesed = ['A', 'B', 'C', 'D','E']
palk = [1200,2500,750,395,1200]
n=len(inimesed)
def sisesta_andmed(i,p):
    N = int(input('Введите количество людей: '))
    for n in range(N):
        inimene = input("Введите имя: ")
        i.append(inimene)
        palk = randint(100,10000)
        p.append(palk)
    return i,p

def andmed_ekranile(i,p):
    N=len(i)
    for n in range(N):
        print(f"{i[n]} - {p[n]}")

def kustutamine(i,p):
    nimi=input("Введите имя человека, которого нужно удалить: ")
    n=i.count(nimi)
    abi_list=[]
    if n > 0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e))
                print(f"{t}.{i[e]} - {p[e]}")
        j=int(input("Порядковый номер человека: "))
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekranile(i,p)
    return i,p

def sorteerimine(i,p,v):
    N = len(p)
    if v == 1:
        for n in range (0, N):
            for m in range (n, N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    else:
        for n in range (0, N):
            for m in range (n, N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi

    andmed_ekranile(i ,p)

def Sort_nimi_jargi(palk,inimesed,n):
    abi_p = 0
    abi_i = ""
    for i in range(0,n-1):
        for j in range(i+1,n):
            if inimesed[i]>inimesed[j]:
                abi_i=inimesed[i]
                inimesed[i]=inimesed[j]
                inimesed[j]=abi_i
                abi_p=palk[i]
                palk[i]=palk[j]
                palk[j]=abi_p

def vordsed_palgad(palk, inimesed,n):
    odin_p =[palk[i] for i in range(n) if palk.count(palk[i])>1]   
    odin_p_i =[inimesed[i] for i in range(n) if palk.count(palk[i])>1] 
    odin_p_s, odin_p_i_s = sorteerimine(odin_p,odin_p_i,len(odin_p))   
    for i in range(len(odin_p_s)):
        print(odin_p_i_s[i],'получает',str(odin_p_s[i])+'€',) 

def maximum(palk,inimesed):
    max_palk=palk[0]       
    kellel=inimesed[0]      
    for p in palk:          
        if p > max_palk:      
            max_palk=p       
            nr=palk.index(max_palk)   
            kellel=inimesed[nr]      
    return max_palk, kellel,nr+1  

def minimum(palk,inimesed):
    min_palk=palk[0]
    kellel=inimesed[0]
    for p in palk:
        if p < min_palk:
            min_palk=p
            nr=palk.index(min_palk)
            kellel=inimesed[nr]
    return min_palk, kellel,nr+1 

def nimi(i, p):
    otsi_nimi = []
    otsi_palk = []
    palk_keda = 0
    keda = input("Введите имя: ")
    n = len(inimesed)
    for j in range(n):
        if inimesed[j] == keda:
            palk_keda = palk[j]
            otsi_nimi.append(inimesed[j])
            otsi_palk.append(palk_keda)
        else:pass
    for i in range(len(otsi_nimi)):
        print(f'{otsi_nimi[i]} - {otsi_palk[i]}')

def keskmine(palk,n):
    summa=0
    for p in palk:
        summa+=p
    kesk=round(summa/n,2)
    print(f"Средняя зарплата {kesk}")

def erinev_palk(i, p):
    number = int(input('Введите зарплату: '))
    tin = int(input('Больше или меньше зарплаты(1 - > / 2 - <?'))
    for i in palk:
        if tin == 1:
            if i > number:
                ind = palk.index(i)
                nimi = inimesed[ind]
                print(f'{nimi} - {i}')
        else:
            if i < number:
                ind = palk.index(i)
                nimi = inimesed[ind]
                print(f'{nimi} - {i}')

def top(i, p):
    N = len(p)
    v = int(input('Богатые(1)/бедные(2): '))
    if v == 1:
        for n in range (0, N):
            for m in range (n, N):
                if p[n] < p[m]:
                    abi = p[n]
                    p[n] = p[m]
                    p[m] = abi
                    abi = i[n]
                    i[n] = i[m]
                    i[m] = abi
        k = 3
        print('Топ 3 богатых')
        for i in range(0, k, 1):
            print(f'{inimesed[i]} - {palk[i]}')
    else:
        for n in range (0, N):
            for m in range (n, N):
                if p[n] > p[m]:
                    abi = p[n]
                    p[n] = p[m]
                    p[m] = abi
                    abi = i[n]
                    i[n] = i[m]
                    i[m] = abi
        k = 3
        print('Топ 3 бедных')
        for i in range(0, k, 1):
            print(f'{inimesed[i]} - {palk[i]}')

def tulumaks(i, p):
    z = int(input('Введите зарплату: '))
    k = 0
    if z < 1200:
        t = (z-500)*0.2
        k = z - t
    elif z > 1200 <= 2100:
        t = 500-(500/850)*(z-1200)
        k = z - t
    else:
        k = z*0.2
    print(f'Нетто зарплата - {round(k,2)}')

def Kustutamine(palk,inimesed,n):
    uus_palk = []; uus_inimesed = []
    kesk = keskmine(palk,n)
    for p in palk:
        if p > kesk:
            nr = palk.index(p)
            uus_palk.append(p)
            uus_inimesed.append(inimesed[nr])
    palk.clear();inimesed.clear()
    for i in range(len(uus_palk)):
        palk.append(uus_palk[i])
        inimesed.append(uus_inimesed[i])
    return uus_palk, uus_inimesed


while 1:
    print("Добавить человека и зарплату - add")
    print("Удалить человека и зарплату - del")
    print("Удаление данных тех, чья зарплата ниже средней - delk")
    print('Сортировка зарплат по возрастанию/убыванию - sort')
    print("Кто получает одинаковые зарплаты? - same")
    print('Максимальная зарплата и кто её получает - max')
    print('Минимальная зарплата и кто её получает - min')
    print('Поиск зарплаты по имени человека - nimi')
    print("Средняя зарплата - kesk")
    print("У кого зарплата больше/меньше заданной? - erinev")
    print("Top3 (3 самых богатых и 3 самых бедных) - top")
    print("Зарплата после подоходного налога - tulumaks")
    print("Сортировка по имени - sort_n")

    valik=input("Ваш выбор? ")

    if valik.lower() == "add":
        inimesed,palgad=sisesta_andmed(inimesed,palk)
    elif valik.lower() == "del":
        inimesed,palgad=kustutamine(inimesed,palk)
    elif valik.lower() == 'delk':
        Kustutamine(inimesed, palk, n)
    elif valik.lower() == "sort":
        sorteerimine(inimesed, palk, int(input("Сортировка: 1 - по возрастанию, 2 - по убыванию")))
    elif valik.lower() == "same":
        vordsed_palgad(inimesed, palk,n)
    elif valik=="max":
        max_palk,kellel,nr=maximum(palk,inimesed)
        print("Максимальную зарплату", str(max_palk), "получает",kellel)
    elif valik=="min":
        min_palk,kellel,nr=minimum(palk,inimesed)
        print("Минимальную зарплату", str(min_palk), "получает",kellel)
    elif valik.lower() == 'nimi':
        nimi(inimesed, palk)
    elif valik.lower() == 'kesk':
        keskmine(palk,n)
    elif valik.lower() == 'erinev':
        erinev_palk(inimesed, palk)
    elif valik.lower() == 'top':
        top(inimesed, palk)
    elif valik.lower() == 'tulumaks':
        tulumaks(inimesed, palk)
    elif valik.lower() == 'sort_n':
        Sort_nimi_jargi(inimesed, palk,n)
    else:
        break