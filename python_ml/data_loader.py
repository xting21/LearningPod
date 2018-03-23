'''
python 3.5

'''
import numpy as np

def load_data(filepath,label_col=-1,test_size=10):
    # file path to data
    #filepath = '../data/glass.dat' # file format within file
    raw_data = np.loadtxt(filepath, dtype=np.float32, comments="@",delimiter=",");
    # separate out the label for each row
    train_data = raw_data[:-test_size,:label_col];
    train_label = raw_data[:-test_size,label_col];
    test_data = raw_data[-test_size,:label_col];
    test_label = raw_data[-test_size,label_col];
    return train_data,train_label,test_data,test_label;
    
load_data("../data/glass.dat",True,23)