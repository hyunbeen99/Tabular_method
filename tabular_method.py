# change decimal to 4bit binary
def decTobin(num):
    x = num
    y = ""
    while x > 0:
        y = str(x % 2) + y
        x /= 2
    return y

# to get HD
def hammingDistance(a, b):
    first = []
    second = []
    first.append(decTobin(a))
    second.append(decTobin(b))

    for i in range 4:
        if (first[i] != second[i]):
            count += 1
