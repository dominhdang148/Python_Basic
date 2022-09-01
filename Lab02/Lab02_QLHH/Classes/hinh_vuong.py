from Classes.hinh_chu_nhat import HinhChuNhat


class HinhVuong(HinhChuNhat):
    def __init__(self, edge):
        self._canh = edge
        self._chieurong = edge

    def __str__(self):
        return "Hình vuông cạnh {} có diện tích {}".format(self._canh, self.TinhDienTich())
    def xuat(self):
        print("Hình vuông cạnh {} có diện tích {}".format(self._canh, self.TinhDienTich()))