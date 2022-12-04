from solitaire import solitaire
from BlumBlumShub import bbs

def en_de_crypt(input, generator_type, key):
    output = []
    match generator_type:
        case 's':
            for byte in input:
                number, key = solitaire(key)
                output.append(byte ^ number)
        case 'b':
            keys = bbs(key, len(input))
            for i in range(len(input)):
                output.append(keys[i] ^ input[i])
    output = bytes(bytearray(output))
    return output

def folyamtitkosito(input):
    with open('./crypto/Lab2/config_file.txt') as f:
        file_in = f.readlines()
    generator_type = file_in[0].strip('\n')
    key = file_in[1].strip('\n')
    if generator_type == "s":
        key = key.split(' ')
    key = list(map(lambda x: int(x), key ))
    coded_bytes = en_de_crypt(input, generator_type, key)
    return coded_bytes
