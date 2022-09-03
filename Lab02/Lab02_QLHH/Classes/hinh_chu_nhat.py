from Classes.hinh_hoc import HinhHoc


class HinhChuNhat(HinhHoc):
    def __init__(self, edge, width):
        if (edge > width):
            self._canh = edge
            self._chieurong = width
        else:
            self._canh = width
            self._chieurong = edge

    @property
    def ChieuDai(self):
        return self._canh

    @property
    def ChieuRong(self):
        return self._chieurong

    @ChieuDai.setter
    def ChieuDai(self, cd):
        self._canh = cd

    @ChieuRong.setter
    def ChieuRong(self, cr):
        self.__chieurong = cr

    def TinhDienTich(self):
        return round((self._canh*self._chieurong), 2)

    def __str__(self):
        return "Hình chữ nhật chiều dài {}, chiều rộng {} có diện tích {}".format(self._canh, self._chieurong, self.TinhDienTich())

    def xuat(self):
        print("Hình chữ nhật chiều dài {}, chiều rộng {} có diện tích {}".format(
            self._canh, self._chieurong, self.TinhDienTich()))

    def __eq__(self, o):
        if type(o) is not HinhChuNhat:
            return False
        return self._canh == o.ChieuDai and self._chieurong == o.ChieuRong