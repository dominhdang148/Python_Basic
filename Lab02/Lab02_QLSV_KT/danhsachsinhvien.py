from sv_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiChinhQuy
from sinhvien import SinhVien


class DanhSachSinhVien:
    def __init__(self) -> None:
        self.dssv = []

    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def TimSVTheoMa(self, ms: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == ms:
                return i
        else:
            return -1
    def TimSVTheoLoai(self, loai:str):
        if loai=="chinhquy":
            return [sv for sv in  self.dssv if isinstance(sv,SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiChinhQuy)]
