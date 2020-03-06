import sys, os
import time
import shutil
from os import listdir

#These global variables are the object numbers for the 2017 coco dataset.
PERSON = "0"
BICYCLE = "1"
CAR = "2"
MOTORBIKE = "3"
AEROPLANE = "4"
BUS = "5"
TRAIN = "6"
TRUCK = "7"
BOAT = "8"
TRAFFIC LIGHT = "9"
FIRE HYDRANT = "10"
STOP SIGN = "11"
PARKING METER = "12"
BENCH = "13"
BIRD = "14"
CAT = "15"
DOG = "16"
HORSE = "17"
SHEEP = "18"
COW = "19"
ELEPHANT = "20"
BEAR = "21"
ZEBRA = "22"
GIRAFFE = "23"
BACKPACK = "24"
UMBRELLA = "25"
HANDBAG = "26"
TIE = "27"
SUITCASE = "28"
FRISBEE = "29"
SKIS = "30"
SNOWBOARD = "31"
SPORTS BALL = "32"
KITE = "33"
BASEBALL BAT = "34"
BASEBALL GLOVE = "35"
SKATEBOARD = "36"
SURFBOARD = "37"
TENNIS RACKET = "38"
BOTTLE = "39"
WINE GLASS = "40"
CUP = "41"
FORK = "42"
KNIFE = "43"
SPOON = "44"
BOWL = "45"
BANANA = "46"
APPLE = "47"
SANDWICH = "48"
ORANGE = "49"
BROCCOLI = "50"
CARROT = "51"
HOT DOG = "52"
PIZZA = "53"
DONUT = "54"
CAKE = "55"
CHAIR = "56"
SOFA = "57"
POTTEDPLANT = "58"
BED = "59"
DININGTABLE = "60"
TOILET = "61"
TVMONITOR = "62"
LAPTOP = "63"
MOUSE = "64"
REMOTE = "65"
KEYBOARD = "66"
CELL PHONE = "67"
MICROWAVE = "68"
OVEN = "69"
TOASTER = "70"
SINK = "71"
REFRIGERATOR = "72"
BOOK = "73"
CLOCK = "74"
VASE = "75"
SCISSORS = "76"
TEDDY BEAR = "77"
HAIR DRIER = "78"
TOOTHBRUSH = "79"
FRIENDLY = "80"

class TextFileError(Exception):

	def FindYoloText(textfile):
		
		result_list = []
		search = ".txt"

		for i in textfile:
			if search in i:
				result_list.append(i)	# find .txt filename and append list

		return result_list

def CreateFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    except OSError:
        print("Error: Createing directory" + directory)

def FileCopy(filepath, dstpath):
    shutil.copy(filepath, dstpath)

def ChangeClassNum(constant): #This function can be changed from the object number used in the coco dataset to the object number you want to use. You can modify it as needed.

    if constant == PERSON:
        return "1"
    
    elif constant == TRUCK:
        return "3"
                            #ex) This code changes the object number and combines truck and car into one object.
    elif constant == CAR:
        return "3"
    
    elif constant == DOG:
        return "4"
    
    elif constant == CAT:
        return "5"

def CheckFileData(f, file): #This function finds the desired object number. You can modify it as needed.

    return_string = ""
    count = 0

    while(True):
        line_list = file.readline().split()
        newdata_list = list()
        
        if line_list:
            if line_list[0] == PERSON:
                line_list[0] = ChangeClassNum(PERSON)
                newdata_list += line_list
                return_string += ' '.join(newdata_list)
                return_string += "\n"
                                               
            elif line_list[0] == CAR:
                line_list[0] = ChangeClassNum(CAR)
                newdata_list += line_list
                return_string += ' '.join(newdata_list)
                return_string += "\n"
                                   
            elif line_list[0] == TRUCK:
                line_list[0] = ChangeClassNum(TRUCK)
                newdata_list += line_list
                return_string += ' '.join(newdata_list)
                return_string += "\n"
                                      
            elif line_list[0] == CAT:
                line_list[0] = ChangeClassNum(CAT)
                newdata_list += line_list
                return_string += ' '.join(newdata_list)
                return_string += "\n"
                                   
            elif line_list[0] == DOG:
                line_list[0] = ChangeClassNum(DOG)
                newdata_list += line_list
                return_string += ' '.join(newdata_list)
                return_string += "\n"
                           
            else:
                pass
         
        if not line_list:
            break

    if return_string:
        with open("./data/" + f, "w") as write_file:
            write_file.write(return_string)
        
        return 1

def SplitFileExtension(file):
    file_name = os.path.splitext(file)
    result = file_name[0] + ".jpg"
    return result

def menu(): #수정해야하는 기능
    print("="*100)
    print("coco dataset ")
    print("="*100)

if __name__ == "__main__":

    start_time = time.time()

    CreateFolder('./data')
    dir_list = listdir('.')

    try:
        file_list = TextFileError.FindYoloText(dir_list)

    except TextFileError:
        print("Error: check ./*.txt file")
    
    for f in file_list:
        print("!working!:" + f)
        with open(f, "r") as file:
            if CheckFileData( f, file):
                FileCopy(SplitFileExtension(f), "./data")

    print("\nwaiting time: {}s ".format((time.time() - start_time)))
    print("Done!")