import pickle
import numpy
from skimage.io import imread
from skimage.transform import resize

CATMODEL = pickle.load(open("./classifier/catClass.p", "rb"))

def cat_color(image):
    image = imread(image)
    image_data = [resize(image, (90, 90, 3)).flatten()]
    numpy_data = numpy.array(image_data)
    y_output = CATMODEL.predict(numpy_data)
    if y_output == 0:
        return 'Cat'
    else:
        return 'Not Cat'

