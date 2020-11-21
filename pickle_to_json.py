import sys
import os
import pickle as pickle
import json
import numpy as np

def convert_dict_to_json(file_path):
    with open(file_path, 'rb') as pickle, open('%s.json' % file_path, 'w') as fjson:
        data = pickle.load(pickle)
        for val in data:
            for i,npval in enumerate(val):
                print(type(npval))
                if isinstance(npval,(np.ndarray)):
                    val[i] = npval.tolist()
                    print(type(val[i]))
        json.dump(data, fjson, ensure_ascii=False, sort_keys=True, indent=4)


def main():
    file_path = '/Users/brice/Desktop/Classes/CSCI387/Project/567ebca0f59c612eb977065008aad867/Test_subset.pkl'
    convert_dict_to_json(file_path)

if __name__ == '__main__':
    main()
