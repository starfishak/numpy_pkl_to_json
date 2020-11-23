import sys
import os
import pickle as pickle
import json
import numpy as np

def convert_dict_to_json(file_path, data):
    with open('%s.json' % file_path, 'w') as fjson:
        print(data)
        print(type(data))
        for npval in data:
            print(npval)
            for keyval in data[npval]:
                if isinstance(data[npval][keyval],(np.ndarray)):
                    print("\n!ARRAY!\n")
                    print(data[npval][keyval])
                    data[npval][keyval] = data[npval][keyval].tolist()
        json.dump(data, fjson, ensure_ascii=False, sort_keys=True, indent=4)


def main():
    # pickle_path = '/Users/brice/Desktop/Classes/CSCI387/Project/Raw Datasets/Test_subset.pkl'
    pickle_path = '/Users/brice/Desktop/Classes/CSCI387/Project/Raw Datasets/Project_1_Kyle/CASP10/T0705/Zhang-Server_TS1.pkl'
    with open(pickle_path, 'rb') as pik:
        file_paths = '/Users/brice/Desktop/Classes/CSCI387/Project/Raw Datasets/Zhang-Server_TS1_a'
        data = pickle.load(pik)
        convert_dict_to_json(file_paths, data)
    
    # pickle_path = '/Users/brice/Desktop/Classes/CSCI387/Project/Raw Datasets/Project_1_Kyle/CASP10/T0705/Zhang-Server_TS1.pkl'
    # with open(pickle_path, 'rb') as pik:
    #     file_paths = ['/Users/brice/Desktop/Classes/CSCI387/Project/Raw Datasets/Zhang-Server_TS1_a','/Users/brice/Desktop/Classes/CSCI387/Project/Raw Datasets/Zhang-Server_TS1_b']
    #     data = pickle.load(pik)
    #     for i in [0,1]:
    #         val = data[i] 
    #         print(type(val))
    #         convert_dict_to_json(file_paths[i], val)

if __name__ == '__main__':
    main()