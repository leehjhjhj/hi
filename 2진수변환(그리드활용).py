n = int(input(" ***이진수 변환기*** \n256 미만 숫자를 넣어봐: "))
output = [0, 0, 0, 0, 0, 0, 0, 0]
while n > 0:
    if n >= 128:
        output[0] = 1
        n -= 128
    elif n >= 64:
        output[1] = 1
        n -= 64
    elif n >= 32:
        output[2] = 1
        n -= 32
    elif n >= 16:
        output[3] = 1
        n -= 16
    elif n >= 8:
        output[4] = 1
        n -= 8
    elif n >= 4:
        output[5] = 1
        n -= 4
    elif n >= 2:
        output[6] = 1
        n -= 2
    elif n >= 1:
        output[7] = 1
        n -= 1
        
while True:
    if output[0] == 0:
        output.pop(0)
    else:
        break

for i in output:
    print(i, end="")