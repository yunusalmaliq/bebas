def fib (n):
	if num <3 :
		print ("minimal 3 deret")
	else:
		fibs.append(fibs[-2]+fibs[-1])
print ("fungsi untuk menampilkan deret fibonaci sebanyak x buah")
n =int(input("masukan x :"))
for i in range (1,n):
	print (fib(i))