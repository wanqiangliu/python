import json
a = [1,2,3,4,5,6]
file_name = "test.json"
with open(file_name,"w") as file_object:
	json.dump(a,file_object)

b = [2,2,4,6,2,7,8]
print(b)
print(set(b))

print("中文")