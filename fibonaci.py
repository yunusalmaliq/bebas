fibs = [1,1]
num = int(input (" masukan jumlah deret fibonaci"))

if num <1 :
	print ("minimal 3 deret")
else:
	for i in range (num-2):
		fibs.append(fibs[-2]+fibs[-1])
		print(fibs)