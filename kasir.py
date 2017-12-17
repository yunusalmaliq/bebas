print ("1._kasir_")
nama=input("masukan nama barang:")
x=int(input("masukan harga barang:"))
jumlah=int(input("masukan jumlah beli:"))
total=x*jumlah
print ("total harga",nama,"anda adalah Rp.",total)
pem=int(input("masukan pembayaran:"))
hutang=total-pem
if(pem>total):
	print("jumlah kembalian anda adalah Rp .",pem-total)
else:
	print("anda memiliki hutang Rp.",hutang)