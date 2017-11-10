from sklearn import datasets
from sklearn import svm
import numpy as np

segment_length = 50   # length of a segment, each segment's amount of peaks is a selected feature
sample_length = 1000  # the number of points in a sample
feature_amount = int(sample_length/segment_length)  # amount of features


class Filter:
    def __init__(self, data, noised=[0], normal=[0]):

        a = []
        infile = open(data, "r")
        for i in infile:
            a.append(i)
        infile.close()
        a = a[2:]
        for i in range(len(a)):
            a[i] = eval(a[i][:-1])
        self.data = a  # self.data is the list of all numbers

        self.noised = noised
        for i in range(len(self.noised)):
            self.noised[i] -= 1

        self.normal = normal
        for i in range(len(self.normal)):
            self.normal[i] -= 1

        self.sample_amount = int(len(self.data)/sample_length)

        mat = []
        for j in range(self.sample_amount):
            mi = []
            for i in range(feature_amount):
                left = j * sample_length + i * segment_length + 1
                right = j * sample_length + (i + 1) * segment_length
                peak_num = Filter.count_peaks(self.data[left:right])
                mi.append(peak_num)

            mat.append(mi)

        my_data = np.array(mat)
        self.features = my_data  # an array containing each sample's features

    def learn(self):  # train with the targets(noised and normal), result in self.clf, which is a linear classifier

        target = []  # array of targets
        for i in range(self.sample_amount):
            if i in self.noised:
                target.append(-1)   # -1 denoting noised
            if i in self.normal:
                target.append(1)    # 1  denoting normal
        my_target = np.array(target)
        print(self.features)

        # train, using linear model
        my_clf = svm.LinearSVC()
        my_clf.fit(self.features, my_target)
        self.clf = my_clf

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

    x = Filter("my_data.txt", [5,6,19,20,21,22,35,36,37], [1,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,23,24,25,26,
                                                           27,28,29,30,31,32,33,34,38,39,40])
    # train
    x.learn()
    print(x.clf.coef_)

    # predict
    y = Filter("B090615010.txt")
    result = x.clf.predict(y.features)
    for i in range(len(result)):
        if result[i] == -1:
            print(i+1, end=" ")