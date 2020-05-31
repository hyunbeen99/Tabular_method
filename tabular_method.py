class TabularMethod:
    
    # change decimal to 4bit binary
    def decTobin(self, num):
        x = num
        y = ""
        while x > 0:
            y = str(x % 2) + y
            x /= 2
        return y

    # to get HD
    def hammingDistance(self, a, b):
        count = 0
        first = []
        second = []
        first.append(decTobin(a))
        second.append(decTobin(b))

        for i in range(0,4):
            if (first[i] != second[i]):
                count += 1

    # count # of 1 for each terms     
    def numOfones(self, num):
        numcount = 0

        for i in num:
            if (int(i) == 1):
                numcount += 1
        return numcount

    def primeImplicants(self, term):
        terms = []      # ['0000', '0101', '0001' ...... '1111']
        orderterms = []
        for i in term:
            terms.append(decTobin(i))

        for j in terms:
            if(numOfones(j) == 0):
                orderterms[0].append(list(i))