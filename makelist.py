#make yolo images list

import sys, os
import time
from os import listdir

link = "./"

def FindImage(dir_list):
    
    result_list = list()
    search1 = ".jpg"
    search2 = ".jpeg"

    for i in dir_list:      
        if search1 in i:
            result_list.append(i)
            print("Filename: " + i)
        
        elif search2 in i:
            result_list.append(i)
            print("Filename: " + i)
            
    return result_list

def MakeTextFile(result_list):
    
    final_list = list()

    with open(link + "train.txt", "w") as file:
        for i in result_list:
            final_list.append( 'data/img/' + i )
        list2string = '\n'.join(final_list)
        file.write(list2string)

if __name__ == "__main__":

    dir_list = listdir(link)
    MakeTextFile(FindImage(dir_list))
    print("Done!")