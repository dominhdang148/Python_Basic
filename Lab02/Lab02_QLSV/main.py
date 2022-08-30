from sinhvien import SinhVien
import datetime
from dssv import DanhSachSV

danhsach = DanhSachSV()

danhsach.ReadFile("sv.txt")
print("Danh sách sinh viên mặc định: ")
danhsach.XuatSinhVien()
print("Danh sách sinh viên sau khi sắp xếp")
danhsach.SapXepDSSVTheoTen()
danhsach.XuatSinhVien()
