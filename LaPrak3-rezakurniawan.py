belanjaan = int(input("Masukkan total harga belanjaan Anda: "))
uang = int(input("Masukkan jumlah uang Anda: "))

kembalian = uang - belanjaan
print(f"\nKembalian Anda sejumlah {kembalian}\nPecahan uang yang dibutuhkan: ")

#cek 100k
if kembalian//100000 != 0:
	jumlah = kembalian//100000
	print(f"Uang kertas 100000 sebanyak {jumlah} lembar")
	kembalian = kembalian%100000
if kembalian//50000 != 0:
	jumlah = kembalian//50000
	print(f"Uang kertas 50000 sebanyak {jumlah} lembar")
	kembalian = kembalian%50000
if kembalian//20000 != 0:
	jumlah = kembalian//20000
	print(f"Uang kertas 20000 sebanyak {jumlah} lembar")
	kembalian = kembalian%20000
if kembalian//10000 != 0:
	jumlah = kembalian//10000
	print(f"Uang kertas 10000 sebanyak {jumlah} lembar")
	kembalian = kembalian%10000
if kembalian//5000 != 0:
	jumlah = kembalian//5000
	print(f"Uang kertas 5000 sebanyak {jumlah} lembar")
	kembalian = kembalian%5000
if kembalian//2000 != 0:
	jumlah = kembalian//2000
	print(f"Uang kertas 2000 sebanyak {jumlah} lembar")
	kembalian = kembalian%2000
if kembalian//1000 != 0:
	jumlah = kembalian//1000
	print(f"Uang kertas 1000 sebanyak {jumlah} lembar")
	kembalian = kembalian%1000
if kembalian//500 != 0:
	jumlah = kembalian//500
	print(f"Uang logam 500 sebanyak {jumlah} keping")
	kembalian = kembalian%500
if kembalian//200 != 0:
	jumlah = kembalian//200
	print(f"Uang logam 200 sebanyak {jumlah} keping")
	kembalian = kembalian%200
if kembalian//100 != 0:
	jumlah = kembalian//100
	print(f"Uang logam 100 sebanyak {jumlah} keping")
	kembalian = kembalian%100