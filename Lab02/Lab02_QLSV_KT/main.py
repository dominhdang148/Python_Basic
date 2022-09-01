from datetime import datetime

from os import system
from sv_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiChinhQuy
from danhsachsinhvien import DanhSachSinhVien

system('cls')
danhsach = DanhSachSinhVien()
danhsach.ReadFile("dssv.txt")
print(danhsach)
result=danhsach.TimSinhVienTrinhDoSinhTruoc("Cao đẳng", '15/8/1999')
print(result)