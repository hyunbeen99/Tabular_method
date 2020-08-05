# change decimal to 4bit binary
def decTobin(n):
    if (n == 1):
        return '1'
    ans = ''
    while True:
        if n % 2 == 0:
            ans+='0'
        else:
            ans+='1'
        n = n / 2

        if n==1:
            ans+='1'
            return ans[::-1]

# to get HD
def hammingDistance(a, b):
    count = 0
    first = []
    second = []
    first.append(decTobin(a))
    second.append(decTobin(b))

    for i in range(0,4):
        if (first[i] != second[i]):
            count += 1

# count # of 1 for each terms     
def numOfones(num):
    numcount = 0

    for i in num:
        if (int(i) == 1):
            numcount += 1
    return numcount

def primeImplicants(term):
    terms = []      # ['0000', '0101', '0001' ...... '1111']
    orderterms = []
    for i in term:
        terms.append(decTobin(i))

    for j in terms:
        if(numOfones(j) == 0):
            orderterms[0].append(list(i))


def main():
    #input to strings
    minterms = raw_input("(ex, 0 1 2 3 4 5 6) >>> ")
    minterms = minterms.split(" ")
    for minterm in minterms:
        print(decTobin(int(minterm)))

if __name__ == "__main__":
    main()