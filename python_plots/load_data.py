'''

'''
import sys
import argparse
import datadotworld as dw

## parser argument
# parser = argparse.ArgumentParser(description='Get the url to load dataset.');
# parser.add_argument("-url", action='store', dest='url_path', help="path to dataset", required=True);
# args = parser.parse_args(sys.argv[1:]);
# # get all the variable
# url_path = args.url_path;

def load(url_path):
    # load dataset
    print (url_path);
    dw_intro = dw.load_dataset(url_path);
    return dw_intro;

def select_data(dataframes):
    # display list of dataset in this filepath
    i = 1;
    keys = [];
    print ("[List of dataset]");
    for key in dataframes.keys():
        keys.append(key);
        print ("{}. {}".format(i,key));
        i+=1;
    while True:
        try:
            choice = int(input("Choose dataset: "));
        except ValueError:
            print ("[Error] Please enter integer choice");
            continue;
        if choice < 1 or choice > len(keys):
            print ("[Error] Please enter integer from 1 to {}".format(len(keys)));
        else:
            break;
    print ("Dataset chosen: {}".format(keys[choice-1]));
    return dataframes[keys[choice-1]];

''' 
[function usage command]

data = load(url_path);
dataset = select_data(data.dataframes);

'''