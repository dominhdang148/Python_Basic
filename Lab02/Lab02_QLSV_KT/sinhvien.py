from datetime import datetime


class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self._maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    @property
    def maSo(self):
        return self._maSo

    @property
    def hoTen(self):
        return self.__hoTen

    @property
    def ngaySinh(self):
        return self.__ngaySinh

    @maSo.setter
    def maSo(self, maSo):
        if self.laMaSoHopLe(maSo):
            self._maSo = maSo

    @hoTen.setter
    def hoTen(self, hoTen):
        self.__hoTen = hoTen

    @ngaySinh.setter
    def ngaySinh(self, ngaySinh):
        self.__ngaySinh = ngaySinh

    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7

    @classmethod
    def doiTenTruong(self, tenMoi):
        self.truong = tenMoi

    def __str__(self) -> str:
        return f"{self._maSo:<10}\t{self.__hoTen:<20}\t{self.__ngaySinh.strftime('%d/%m/%Y'):<20}"

    def xuat(self):
        print(f"{self._maSo:<10}\t{self.__hoTen:<20}\t{self.__ngaySinh:<50}")
