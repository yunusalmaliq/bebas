

#1
dict={"mady":"8","roger":"5","paul":"5","luci":"7"}
print(dict)

#2 
dict={"ken":"8","andre":"7","smith":"6"}
print(dict)

#3 
dict={"mady":"8","roger":"5","paul":"5","luci":"7"}
new_dict={"ken":"8","andre":"7","smith":"6"}
dict.update(new_dict)
print(dict)

#4 
dict["roger"]="8"
dict["paul"]="8"
dict["smith"]="8"
print(dict)

#5
dict={"mady":"8","roger":"8","paul":"8","ken":"8","smith":"8"}
for data in dict:
	print(dict)