# myfile = open("mytext.txt", "w+")
#
# content = "This content will be insert in file"
#
# myfile.write(content)


import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size !=0:
    old_file = open("./ages.json" , "r+")
    data = json.loads(old_file.read())
    print("current age is: " , data["age"] , "--- adding a year.")
    data["age"] = data["age"] + 1
    print("new age is: ", data["age"])
else:
    old_file = open("./ages.json" , "w+")
    data = {"name" : "zoli" , "age": 25}
    print("no file found, setting default age to : " , data["age"])


old_file.seek(0)
old_file.write(json.dumps(data))
