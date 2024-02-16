from dat import EditFile


data1= EditFile("bucketlist.dat")
data = data1.read_from_file()
data["INFO"]={}

for item in data.keys():
    if item!="INFO":
        data["INFO"][item]=""

data1.overwrite_file()

data2 = EditFile("bucketlist.dat")
data = data2.read_from_file()
print(data)