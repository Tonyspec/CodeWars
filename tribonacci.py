def tribonacci(signature, n):
    if n == 0:
        signature = []
    elif n == 1:
        signature = signature[0]
    elif n==2:
        signature = [signature[0], signature[1]]
    else:
        for i in range(n - 3):
            signature.append(signature[i] + signature[i + 1] + signature[i + 2])
    return signature

result = tribonacci( [106, 71, 53], 1)
print(result)