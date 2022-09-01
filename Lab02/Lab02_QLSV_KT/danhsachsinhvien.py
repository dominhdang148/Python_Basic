from sv_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiChinhQuy
from sinhvien import SinhVien
from datetime import datetime


class DanhSachSinhVien:
    def __init__(self) -> None:
        self.dssv = []

    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def ReadFile(self, path: str) -> None:
        line = "123"
        with open(path, "r", encoding="utf8") as fileReader:
            while (line := fileReader.readline()) != "":
                sv = ""
                s = line.split("*")
                if s[0] == "CQ":
                    sv = SinhVienChinhQuy(int(s[1]), s[2], datetime.strptime(
                        s[3], "%d/%m/%Y"), int(s[4]))
                else:
                    sv = SinhVienPhiChinhQuy(int(s[1]), s[2], datetime.strptime(
                        s[3], "%d/%m/%Y"), s[4], float(s[5]))
                self.themSV(sv)
        fileReader.close()

    def __str__(self):
        s = f"{'MSSV':<16}{'HỌ VÀ TÊN':<24}{'NGÀY SINH':<20}{'TRÌNH ĐỘ (PCQ)':<20}{'RL (CQ)'}{'TGĐT (PCQ)':>15}\n" + \
            "========================================================================================================\n"
        for sv in self.dssv:
            s += "{}\n".format(sv)
        return s

    def TimSVTheoMa(self, ms: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == ms:
                return i
        else:
            return -1

    def TimSVTheoLoai(self, loai: str):
        result = DanhSachSinhVien()
        if loai == "chinhquy":
            for sv in self.dssv:
                if type(sv) is SinhVienChinhQuy:
                    result.themSV(sv)
        else:
            for sv in self.dssv:
                if type(sv) is SinhVienPhiChinhQuy:
                    result.themSV(sv)
        return result

    # 1. Tìm sinh viên có điểm rèn luyện trên 80 (Truyền điểm sàn vào phương thức)
    def TimSinhVienCoDiemRenLuyenTren(self, diem: int):
        result = DanhSachSinhVien()
        for sv in self.dssv:
            if type(sv) is SinhVienChinhQuy and sv.diemRL >= diem:
                result.themSV(sv)
        return result
    # 2. Tìm sinh viên có trình độ cao đẳng sinh trước 15/8/1999 (Truyền trình độ và ngày sinh vào phương thức)

    def TimSinhVienTrinhDoSinhTruoc(self, trinhdo: str, ngay: str):
        result = DanhSachSinhVien()
        for sv in self.dssv:
            if type(sv) is SinhVienPhiChinhQuy and sv.trinhDo == trinhdo and sv.ngaySinh<=datetime.strptime(ngay, '%d/%m/%Y'):
                result.themSV(sv)
        return result
