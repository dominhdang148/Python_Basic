from sinhvien import SinhVien
from datetime import datetime


class SinhVienPhiChinhQuy(SinhVien):
    def __init__(self, maSo, hoTen, ngaySinh, trinhdo: str, tgdt: int) -> None:
        super().__init__(maSo, hoTen, ngaySinh)
        self.thoiGianDaoTao = tgdt
        self.trinhDo = trinhdo
    def __str__(self)->str:
        return super().__str__()+f"\t{self.trinhDo}\t{self.thoiGianDaoTao}"