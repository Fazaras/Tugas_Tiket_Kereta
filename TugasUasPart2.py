print ("======== PEMESANAN TIKET ========")
print ("")
Nama = input("Masukan Nama :")
Ktp = int(input("Masukan Nomor NIK :"))
St_awal = input("Masukan Stasiun Awal [BKS/BGR/JKT/SBY/DPK] :") #st_awal = stasiun awal
St_ahir = input("Masukan Stasiun Ahir [BKS/BGR/JKT/SBY/DPK] :") #st_ahir = stasiun ahir
Tj_aw = [] #Tj_aw = Tujuan Awal / Stasiun Awal
Tj_ah = [] #Tj_ah = Tujuan Ahir / Stasiun Tujuan
Hg = [] #Hg = Harga
if St_awal == "BKS" :
    Tj_aw = "Bekasi"
elif St_awal == "BGR" :
    Tj_aw = "Bogor"
elif St_awal == "JKT" :
    Tj_aw = "Jakarta"
elif St_awal == "SBY" :
    Tj_aw =  "Surabaya"
elif St_awal == "DPK" :
    Tj_aw = "Depok"
else:
    print("Tujuan Tidak Ada")

if St_ahir == "BKS" :
    Tj_ah = "Bekasi"
    Hg = 25000
elif St_ahir == "BGR" :
    Tj_ah = "Bogor"
    Hg = 30000
elif St_ahir == "JKT" :
    Tj_ah = "Jakarta"
    Hg = 35000
elif St_ahir == "SBY" :
    Tj_ah = "Surabaya"
    Hg = 40000
elif St_ahir == "DPK" :
    Tj_ah = "Depok"
    Hg = 15000
else :
    print("Tujuan Tidak Ada")

Jumlah = int(input("Masukan Jumlah Tiket Dibeli :"))
if Jumlah  >= 3 :
    Potongan = (Jumlah*Hg)*0.10
else :
    Potongan = 0
No = int(input("Masukan Nomor HP :"))
Umur = int(input("Masukan Umur :"))

total = (Jumlah*Hg-Potongan)
pajak = total*0.1
jumlah_Bayar = total+pajak

print ("")
print ("===========Rincian Tiket Anda===========")
print ("")
print ("Nama Pembeli                  :" +str(Nama))
print ("Nomor HP                      :" +str(No))
print ("Nomor NIK KTP                 :" +str(Ktp))
print ("Umur Pembeli                  :" +str(Umur))
print ("Stasiun Awal                  :" +str(Tj_aw))
print ("Stasiun Tujuan                :" +str(Tj_ah))
print ("Harga Tiket                   :" +str(Hg))
print ("Jumlah Tiket Dibeli           :" +str(Jumlah))
print ("Potongan Harga                :" +str(Potongan))
print ("Total Harga                   :" +str(total))
print ("Pajak PPN                     :" +str(pajak))
print ("Jumlah Yang Harus Dibayar     :" +str(jumlah_Bayar))
print ("Pelunasan Tiket Kereta        :")
uang = int(input("Masukan Jumlah Uang :"))
Kembalian = uang-total
print ("Uang Kembalian                :" +str(Kembalian)) 