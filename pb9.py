n = input("Numarul in baza 2:")
def get_base_16_from_2(n):
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
    assert get_base_16_from_2('1111')=='F'
    assert get_base_16_from_2('0') == '0'
    assert get_base_16_from_2('1') == '1'
    assert get_base_16_from_2('111111') == '3F'
test_get_base_16_from_2()
print(get_base_16_from_2(n))