import math
def get_base_16_from_2(n):
    #problema 9
    if len(n) % 4 != 0:
        extra = 4 - len(n) % 4
        for i in range(extra):
            n = '0' + n
    baza16 = ''
    baza16cif = "0123456789ABCDEF"
    i = 0
    while i < len(n):
        baza10 = int(n[i]) * 2 * 2 * 2 + int(n[i + 1]) * 2 * 2 + int(n[i + 2]) * 2 + int(n[i + 3])
        i += 4
        baza16 += baza16cif[baza10]
    return(baza16)
def test_get_base_16_from_2():
    #test problema 9
    assert get_base_16_from_2('1111')=='F'
    assert get_base_16_from_2('0') == '0'
    assert get_base_16_from_2('1') == '1'
    assert get_base_16_from_2('111111') == '3F'
def get_n_choose_k(n,k):
    #problema 10
    nfactorial=kfactorial=nkfactorial=1
    for i in range (1,int(n)+1):
        nfactorial*=i
    for i in range (1,int(k)+1):
        kfactorial*=i
    for i in range (1,int(n)-int(k)+1):
        nkfactorial*=i
    return(nfactorial//kfactorial//nkfactorial)
def test_get_n_choose_k():
    #test problema 10
    assert get_n_choose_k(8,3)==56
    assert get_n_choose_k(3,2)==3
    assert get_n_choose_k(7,0)==1
def get_perfect_squares(n,m):
    #problema 12
    numereprime =''
    if (math.sqrt(n)==math.isqrt(n) and n!=0):
        numereprime+=str(n)+' '
    for i in range(math.isqrt(n)+1,math.isqrt(m)+1):
        if i!=0:
            numereprime+=str(i*i)+" "
    return(numereprime)
def test_get_perfect_squares():
    #test problema 12
    assert get_perfect_squares(9,16)=="9 16 "
    assert get_perfect_squares(5, 10) == "9 "
    assert get_perfect_squares(4,10) =="4 9 "
    assert get_perfect_squares(100, 121)=="100 121 "
    assert get_perfect_squares(0,10)=="1 4 9 "
while True:
    print("1.Transformă un număr dat din baza 2 în baza 16. Numărul se dă în baza 2.")
    print("2.Calculează combinări de n luate câte k (n și k date).")
    print("3.Afișează toate pătratele perfecte dintr-un interval închis dat.")
    print("4.Iesire din program.")
    optiune=input("Alege optiunea:")
    if optiune=='1':
        n = input("Numarul in baza 2:")
        test_get_base_16_from_2()
        print(get_base_16_from_2(n))
    elif optiune=='2':
        n = input("Combinari de:")
        k = input("Luate cate:")
        test_get_n_choose_k()
        print(get_n_choose_k(n, k))
    elif optiune=='3':
        n = input("Primul numar:")
        m = input("Al doilea numar:")
        test_get_perfect_squares()
        print(get_perfect_squares(int(n), int(m)))
    elif optiune=='4':
        break






