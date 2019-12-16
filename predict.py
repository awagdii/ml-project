import pandas as pd
import numpy as np # linear algebra
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import to_categorical
import keras    
RANDOM_SEED = 13
N_TIME_STEPS = 50
N_FEATURES = 3
step = 10
segments = []
labels = []
DATA_PATH ="testing.txt"
COLUMN_NAMES = [
    'user',
    'activity',
    'timestamp',
    'x-axis',
    'y-axis',
    'z-axis'
]

LABELS = [
    'Downstairs',
    'Jogging',
    'Sitting',
    'Standing',
    'Upstairs',
    'Walking'
]
def readData(DATA_PATH,COLUMN_NAMES=COLUMN_NAMES,LABELS=LABELS):
    data = pd.read_csv(DATA_PATH, header=None, names=COLUMN_NAMES)
    data['z-axis'].replace({';': ''}, regex=True, inplace=True)
    data['z-axis']=pd.to_numeric(data['z-axis'],errors='coerce')
    data = data.dropna() 
    return data
#projectData=readData(DATA_PATH,COLUMN_NAMES,LABELS)
def predict(projectData):
    segments=[]
    keras.backend.clear_session()
    for i in range(0, len(projectData) - N_TIME_STEPS, step):
        xs = projectData['x-axis'].values[i: i + N_TIME_STEPS]
        ys = projectData['y-axis'].values[i: i + N_TIME_STEPS]
        zs = projectData['z-axis'].values[i: i + N_TIME_STEPS]
        segments.append([xs, ys, zs])
        #reshape the segments which is (list of arrays) to one list
        reshaped_segments = np.asarray(segments, dtype= np.float32).reshape(-1, N_TIME_STEPS, N_FEATURES)
        from keras.models import model_from_json
        # Model reconstruction from JSON file
        with open('static/model_architecture.json', 'r') as f:
            model = model_from_json(f.read())

        # Load weights into the new model
        model.load_weights('static/harmodel.h5')
        probas = model.predict_proba(reshaped_segments)[0]
        res = {LABELS[i]: probas[i] for i in range(len(LABELS))} 
        final_class= LABELS[int(model.predict_classes(reshaped_segments)[0])]
        return final_class
        #return LABELS[int(model.predict_classes(reshaped_segments)[0])]

keras.backend.clear_session()
