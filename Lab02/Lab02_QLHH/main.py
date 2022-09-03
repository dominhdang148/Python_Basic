from ds_hinh_hoc import DanhSachHinhHoc
from os import system
from Classes.hinh_chu_nhat import HinhChuNhat
from Classes.hinh_vuong import HinhVuong
system('cls')
ds= DanhSachHinhHoc()
ds.ReadFile()
print(ds)
print("Kết quả là:")
ds.XoaHinhTheoLoai(HinhChuNhat)
print(ds)




