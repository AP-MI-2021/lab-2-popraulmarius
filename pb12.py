import math
n=input("Primul numar:")
m=input("Al doilea numar:")
def get_perfect_squares(n,m):
    numereprime =''
    if (math.sqrt(n)==math.isqrt(n) and n!=0):
        numereprime+=str(n)+' '
    for i in range(math.isqrt(n)+1,math.isqrt(m)+1):
        if i!=0:
            numereprime+=str(i*i)+" "
    return(numereprime)
def test_get_perfect_squares():
    assert get_perfect_squares(9,16)=="9 16 "
    assert get_perfect_squares(5, 10) == "9 "
    assert get_perfect_squares(4,10) =="4 9 "
    assert get_perfect_squares(100, 121)=="100 121 "
    assert get_perfect_squares(0,10)=="1 4 9 "
test_get_perfect_squares()
print(get_perfect_squares(int(n),int(m)))



