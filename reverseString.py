def stringReversal(string):
    Li=0
    Ri = len(string)-1
    while Li<Ri:
        # Perform swapping of chars
        string[Li], string[Ri]=string[Ri], string[Li]

        Li+=1
        Ri-=1
    return string

reversed = stringReversal(['o','m','k','a','r'])
print(''.join(reversed))
# stringReversal('kulkarni')