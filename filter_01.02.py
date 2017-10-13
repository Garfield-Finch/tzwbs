class Filter:
    def __init__(self, data, noised, normal):

        a = []
        infile = open(data, "r")
        for i in infile:
            a.append(i)
        infile.close()
        a = a[2:]
        for i in range(len(a)):
            a[i] = eval(a[i][:-1])

        self.data = a

        self.noised = noised
        for i in range(len(self.noised)):
            self.noised[i] -= 1

        self.normal = normal
        for i in range(len(self.normal)):
            self.normal[i] -= 1



    def learn(self):
        # 10 intervals with length 100, could be modified
        mat = []
        for i in range(10):
            mi = []
            for j in range(20):
                left = j*1000 + i*100+1
                right = j*1000 + i*100+100
                peak_num = Filter.count_peaks(self.data[left:right])
                mi.append(peak_num)

            mat.append(mi)

        diff = []
        for i in range(len(mat)):
            noised_sum = 0
            normal_sum = 0
            for j in self.noised:
                noised_sum += mat[i][j]
            for j in self.normal:
                normal_sum += mat[i][j]

            noised_average = noised_sum / len(self.noised)
            normal_average = normal_sum / len(self.normal)

            dif = noised_average - normal_average
            diff.append([i, dif, noised_average, normal_average])

        # sort by the difference of the noised and normal, maximum to minimum
        for i in range(len(diff) - 1):
            for j in range(len(diff) - 1 - i):
                if diff[j][1] < diff[j + 1][1]:
                    diff[j], diff[j + 1] = diff[j + 1], diff[j]

        print("diff: ", diff)

        print("training outcome:", diff[:2])
        return diff[:2]

    def count_peaks(data):

        counter = 0
        peak = False
        for j in range(len(data)):
            if data[j] >= data[j - 1]:
                peak = True
            elif peak:
                counter += 1
                peak = False

        return counter

if __name__ == '__main__':
    x = Filter("B090512020.txt", [5,6,19,20], [1,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18])
    # train
    x.learn()
    # next use the data
    # tbd
