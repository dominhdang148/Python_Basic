from ds_hinh_hoc import DanhSachHinhHoc
from os import system
from Classes.hinh_chu_nhat import HinhChuNhat
from Classes.hinh_vuong import HinhVuong
system('cls')
# ds= DanhSachHinhHoc()
# ds.ReadFile()
# print(ds)
# ds.Xuat()
# print("Kết quả là:")
# ds.SapXepGiamTheoDienTich()
# print(result)
# print(ds)
hcn = HinhChuNhat(5, 5)
print(type(hcn) is HinhVuong)
