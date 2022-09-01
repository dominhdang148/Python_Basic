from datetime import datetime

from os import system
from sv_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiChinhQuy
from danhsachsinhvien import DanhSachSinhVien

system('cls')
danhsach = DanhSachSinhVien()
danhsach.ReadFile("dssv.txt")
print(danhsach)


result=danhsach.TimSinhVienCoDiemRenLuyenTren(80)
print("Danh sách sinh viên có điểm rèn luyện trên 80 là:")
print(result)


result=danhsach.TimSinhVienTrinhDoSinhTruoc("Cao đẳng", '15/8/1999')
print("Danh sách sinh viên phi chính quy có trình độ Cao đằng sinh trước 15/8/1999 là: ")
print(result)