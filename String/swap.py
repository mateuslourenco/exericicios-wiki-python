def swap_case(s):
    swap = ''
    for letra in s:
        if letra.islower():
            swap += ''.join(letra.upper())
        else:
            swap += ''.join(letra.lower())
    return swap


if __name__ == '__main__':
    s = 'Teste'
    result = swap_case(s)
    print(result)
