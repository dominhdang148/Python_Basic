from sinhvien import SinhVien
from datetime import datetime


class SinhVienChinhQuy(SinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, diemRL: int):
        super().__init__(maSo, hoTen, ngaySinh)
        self.diemRL = diemRL
    def __str__(self)->str:
        return super().__str__()+f"\t{self.diemRL:>18}"