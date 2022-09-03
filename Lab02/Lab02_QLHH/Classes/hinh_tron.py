from Classes.hinh_hoc import HinhHoc
import math


class HinhTron(HinhHoc):
    @property
    def banKinh(self):
        return self._canh

    @banKinh.setter
    def banKinh(self, radius):
        self._canh = radius

    def TinhDienTich(self):
        return round(math.pi * self._canh**2,2)
    def __eq__(self, o):
        if type(o) is not HinhTron:
            return False
        return self._canh == o.banKinh

    def __str__(self):
        return "Hình tròn bán kính {} có diện tích {}".format(self._canh, self.TinhDienTich())
    def xuat(self):
        print("Hình tròn bán kính {} có diện tích {}".format(self._canh, self.TinhDienTich()))