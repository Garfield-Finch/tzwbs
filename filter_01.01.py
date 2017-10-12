class Filter:
    def __init__(self, data_source, noised, normal):
        a = []
        infile = open(data_source, "r")
        for i in infile:
            a.append(i)
        infile.close()

        a = a[2:]
        for i in range(len(a)):
            a[i] = eval(a[i][:-1])
        self.data = a
        self.noised = noised
        self.normal = normal

    def __learn__(self):
        """tell the filter which one are noised"""

        return domains, keys


    def __process__(self, domain):
        ct = []  # a list containing all the counters
        begin = domain[0]
        end = domain[1]
        for i in range(20):
            counter = 0
            peak = False
            for j in range(i * 1000 + begin + 1, i * 1000 + end):
                if self.data[j] >= self.data[j - 1]:
                    peak = True
                elif peak:
                    counter += 1
                    peak = False
            ct.append(counter)
        return ct

    def __cluster__(self):
        flt = []
        domains, keys = self.__learn__()
        if domains == 1:
            ct = self.__process__(domains[0])
            for i in range(20):
                if ct[i] >= keys[i]:
                    flt.append(False)
                else:
                    flt.append(True)

        ans = []
        for i in range(len(flt)):
            if not flt[i]:
                ans.append(i + 1)

print("the noised data are", ans)

if __name__ == "__main__":

