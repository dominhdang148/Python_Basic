from sinhvien import SinhVien
import datetime
from dssv import DanhSachSV

danhsach = DanhSachSV()

danhsach.ThemSinhVien(
    SinhVien(1203213, "Nguyễn Văn A", datetime.date(2000, 5, 5)))
danhsach.ThemSinhVien(SinhVien(1203221, "Nguyễn Văn B",
                      datetime.date(2000, 12, 30)))
danhsach.ThemSinhVien(
    SinhVien(1203543, "Nguyễn Văn C", datetime.date(2000, 3, 6)))
danhsach.ThemSinhVien(
    SinhVien(1204324, "Nguyễn Văn D", datetime.date(2000, 1, 12)))
danhsach.ThemSinhVien(SinhVien(1205721, "Lê Văn D",
                      datetime.date(1992, 12, 1))),

danhsach.XuatSinhVien()
newList = danhsach.TImSVSinhTruocNgay(datetime.date(2000, 4, 30))

for sv in newList:
    print(sv)
