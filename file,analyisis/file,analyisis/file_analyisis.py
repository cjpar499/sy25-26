import glob



files = glob.glob("server_dump/*.txt") 

type_1 = 0
type_2= 0
type_3= 0

type=input("enter a file type 1.OK 2.Warn 3.Error ")



if type=="1":
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                if "OK" in line:S
                   type_1 += 1
    print("OK: ", type_1)

if type=="2":
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                if "WARN" in line:
                   type_2 += 1
    print("WARN: ", type_2)

if type=="3":
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                if "ERROR" in line:
                   type_3 += 1
    print("ERROR: ", type_3)