from sinhvien import SinhVien
import datetime


class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []

    def ReadFile(self, fileName):
        line = "123"
        with open(fileName, "r", encoding='utf8') as fileReader:
            while ((line := fileReader.readline()) != ""):
                str = line.split("*")
                dateString = str[2].split('/')
                ngaySinh = datetime.date(int(dateString[-1]), int(
                    dateString[-2]), int(dateString[-3]))
                sv = SinhVien(int(str[0]), str[1], ngaySinh)
                self.ThemSinhVien(sv)
        fileReader.close()

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

    def TimSVSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]

    def TimTen(self, sv: SinhVien):
        return sv.hoTen

    # Condition=True --> Sắp xếp theo chiều tăng
    # Condition=False hoặc không có tham số truyền vào --> Sắp xếp theo chiều giảm
    def SapXepDSSVTheoTen(self, condition=False):
        self.dssv.sort(key=self.TimTen, reverse=condition)
