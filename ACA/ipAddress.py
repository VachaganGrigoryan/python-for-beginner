# ipAddress = input().split('.')


def encode(ipAddress):
    code = 0
    for i, num in enumerate(ipAddress.split('.')):
        code |= int(num) << (8*(3-i))
    return code

def decode(code):
    ipAddress = []
    for i in range(4):
        ipAddress.append(code << i*8 >> 24)
        code = code - (ipAddress[i] << (8*(3-i)))
    return '.'.join(map(str, ipAddress))

def main():
    print(encode("192.168.1.23"))
    print(decode(3232235799))

main()
