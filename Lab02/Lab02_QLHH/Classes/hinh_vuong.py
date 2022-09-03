from Classes.hinh_chu_nhat import HinhChuNhat


class HinhVuong(HinhChuNhat):
    def __init__(self, edge):
        self._canh = edge
        self._chieurong = edge

    def __str__(self):
        return "Hình vuông cạnh {} có diện tích {}".format(self._canh, self.TinhDienTich())

    @property
    def Canh(self):
        return self._canh

    @Canh.setter
    def Canh(self, edge):
        self._canh = edge

    def xuat(self):
        print("Hình vuông cạnh {} có diện tích {}".format(
            self._canh, self.TinhDienTich()))

    def __eq__(self, o):
        if type(o) is not HinhVuong:
            return False
        return self._canh == o.Canh
