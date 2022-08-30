from sinhvien import SinhVien
import datetime


class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []

    def ReadFile(self, fileName):
        

    def ThemSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def XuatSinhVien(self):
        for sv in self.dssv:
            print(sv)

    def TimSVTheoMaSo(self, mssv: int):
        return [sv for sv in self.dssv if sv.maSo == mssv]

    def TimVTSVTheoMSSV(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
        return -1

    def XoaSVTheoMSSV(self, mssv: int) -> bool:
        vt = self.TimVTSVTheoMSSV(mssv)
        if vt != -1:
            # del self.dssv[vt]
            self.dssv.remove(self.dssv[vt])
            return True
        else:
            return False

    def TimSinhVienTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen.split(' ')[-1].lower() == ten.lower()]

    def TImSVSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]
