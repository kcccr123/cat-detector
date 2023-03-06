import numpy
import os
import pickle
# preparing data
from skimage.io import imread
from skimage.transform import resize
dataset = 'C:/Users/MSI/PycharmProjects/breedDetector/catdata'

classification = ["cats", "not_cats"]

data = []
labels = []
for idx, i in enumerate(classification):
    for file in os.listdir(os.path.join(dataset, i)):
        path = os.path.join(dataset, i, file)
        image = imread(path)
        image = resize(image, (90, 90))
        data.append(image.flatten())
        labels.append(idx)

data = numpy.asarray(data)
labels = numpy.asarray(labels)

# split data
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# classifier
from sklearn.svm import SVC
classifier = SVC()

params = [{'gamma':['scale'], 'C':[0.01, 1, 10, 100, 1000], 'cache_size':[1000]}]

grid_search = GridSearchCV(classifier, params)

grid_search.fit(x_train, y_train)

#performance
from sklearn.metrics import accuracy_score
estimator = grid_search.best_estimator_

predicy = estimator.predict(x_test)
score = accuracy_score(predicy, y_test) * 100
print(score)

pickle.dump(estimator, open('catClass.p', 'wb'))



