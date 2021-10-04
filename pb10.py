n=input("Combinari de:")
k=input("Luate cate:")
def get_n_choose_k(n,k):
    nfactorial=kfactorial=nkfactorial=1
    for i in range (1,int(n)+1):
        nfactorial*=i
    for i in range (1,int(k)+1):
        kfactorial*=i
    for i in range (1,int(n)-int(k)+1):
        nkfactorial*=i
    return(nfactorial//kfactorial//nkfactorial)
def test_get_n_choose_k():
    assert get_n_choose_k(8,3)==56
    assert get_n_choose_k(3,2)==3
    assert get_n_choose_k(7,0)==1
test_get_n_choose_k()
print(get_n_choose_k(n,k))