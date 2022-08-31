from phanso import PhanSo


class DanhSachPhanSo:
    def __init__(self):
        self.dsps = []

    def TimGiaTri(self, x: PhanSo):
        return x.GetValue()

    def TimTu(self, x: PhanSo):
        return x.tu

    def TimMau(self, x: PhanSo):
        return x.mau

    def ThemPhanSo(self, ps: PhanSo):
        self.dsps.append(ps)

    def __str__(self):
        s = ""
        for ps in self.dsps:
            s += str(ps)+'\t'
        return s

    # 1. Đếm phân số âm trong mảng
    def DemPhanSoAmTrongMang(self):
        count = 0
        for phanso in self.dsps:
            if phanso.IsNegative():
                count += 1
        return count

    # 2. Tìm phân số dương nhỏ nhất
    def TimPSDuongNhoNhat(self):
        psMin = PhanSo(100)
        for ps in self.dsps:
            if not ps.IsNegative() and ps.GetValue() < psMin.GetValue():
                psMin = ps
        return psMin

    # 3. Tìm tất cả vị trí của phân số x trong mảng
    def TimViTriCuaPhanSo(self, phanso: PhanSo):
        indexList = []
        for i in range(len(self.dsps)):
            if self.dsps[i].IsSimilar(phanso):
                indexList.append(i)
        return indexList

    # 4. Tổng tất cả các phân số âm trong mảng

    def TinhTongPhanSoAmTrongMang(self):
        sum = PhanSo()
        for ps in self.dsps:
            if ps.IsNegative():
                sum += ps
        return sum

    # 5. Xóa pnân số X trong mảng

    def XoaPhanSo_X(self, phanso: PhanSo):
        self.dsps = [
            value for value in self.dsps if not value.IsSimilar(phanso)]

    # 6. Xóa tát cả phân số có tử X
    def XoaPhanSoCoTu(self, tu: int):
        self.dsps = [
            value for value in self.dsps if value.tu != tu
        ]
    # 7. Sắp xếp danh sách phân số

    def SapXepTheoGiaTri(self, condition=False):
        self.dsps.sort(key=self.TimGiaTri, reverse=condition)
    def SapXepTheoTu(self, condition=False):
        self.dsps.sort(key=self.TimTu, reverse=condition)
    def SapXepTheoMau(self, condition=False):
        self.dsps.sort(key=self.TimMau, reverse=condition)
