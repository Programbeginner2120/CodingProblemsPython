# https://www.codewars.com/kata/526989a41034285187000de4


def ips_between(start, end):
    start = start.split('.')
    end = end.split('.')

    numIpBetween = 0

    for i in range(0 ,4): # note length start equals length end
        diff = int(end[3 - i]) - int(start[3 - i])
        numIpBetween += pow(256, i) * diff

    return numIpBetween


print(ips_between("10.0.0.0", "10.0.0.50"))  # 50
print(ips_between("10.0.0.0", "10.0.1.0"))  # 256
print(ips_between("20.0.0.10", "20.0.1.0"))  # 246


