from numpy import zeros

def bbs(key, nr):
    key = int(key[0])
    n = 23746643 * 66190997
    numbers = list(zeros((int(nr) * 8,), dtype=int))
    numbers[0] = (key ** 2) % n
    for i in range(1, int(nr) * 8):
        numbers[i] = (numbers[i-1] ** 2) % n
    bit_numbers = []
    for number in numbers:
        bit_numbers.append(number % 2)
    numbers = [numbers[n:n+8] for n in range(0, len(numbers), 8)]
    bytes = []
    for byte in numbers:
        bytes.append(''.join(byte))
    return list(bytearray([ int(i,2) for i in bytes]))