# Support vector machine leaning
# using library sklearn
from sklearn import datasets
from sklearn import svm
import numpy as np

if __name__ == '__main__':

    # official example
    ## load data
    iris = datasets.load_iris()
    for i in range(len(iris.data)):
        print(iris.data[i], iris.target[i])
    print()

    ## learn
    clf_iris = svm.LinearSVC()

    clf_iris.fit(iris.data, iris.target)
    print(clf_iris)
    print()

    ## predict
    sample_1 = [5.0,  3.6,  1.3,  0.25]
    sample_2 = [5.9, 3., 5.1, 1.8]
    print(clf_iris.predict([sample_1, sample_2]))

    # my example
    print("my_")
    ## load data
    my_data = np.array([[1, 0], [1, 1]])
    my_target = np.array([-1, 1])

    ## learn
    my_clf = svm.LinearSVC()
    my_clf.fit(my_data, my_target)
    print(my_clf.coef_)
