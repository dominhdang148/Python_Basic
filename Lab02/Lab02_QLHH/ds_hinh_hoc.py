from Classes.hinh_chu_nhat import HinhChuNhat
from Classes.hinh_hoc import HinhHoc
from Classes.hinh_vuong import HinhVuong
from Classes.hinh_tron import HinhTron


class DanhSachHinhHoc:
    def __init__(self) -> None:
        self.dshh = []

    def ReadFile(self):
        line = "123"
        with open("Data\hh.txt", 'r') as fileReader:
            while((line := fileReader.readline()) != ""):
                hh = ""
                s = line.split(" ")
                if s[0] == "HV":
                    hh = HinhVuong(float(s[1]))
                elif s[0] == "HT":
                    hh = HinhTron(float(s[1]))
                elif s[0] == "HCN":
                    hh = HinhChuNhat(float(s[1]), float(s[2]))
                self.ThemHinh(hh)
        fileReader.close()

    # region 1. Thêm hình vào danh sách
    def ThemHinh(self, hh: HinhHoc):
        self.dshh.append(hh)
    # endregion

    # region 2. Xuất danh sách hình
    def Xuat(self):
        print("\n=============================== DANH SÁCH HÌNH HỌC ===============================\n")
        for hh in self.dshh:
            print("{}. {}".format(self.dshh.index(hh), hh))
        print("==================================================================================\n")

    def __str__(self):
        s = "\n=============================== DANH SÁCH HÌNH HỌC ===============================\n"
        for hh in self.dshh:
            s += "{}. {}\n".format(self.dshh.index(hh), hh)
        s += "==================================================================================\n"
        return s
    # endregion

    # region 3. Tìm hình có diện tích lớn nhất -> DanhSachHinhHoc

    def TimHinhCoDienTichLonNhat(self):
        return self.TimHinhCoDienTich(self.TimDienTichHinhLonNhat())
    # endregion

    # region 4. Tìm hình có diện tích nhỏ nhất -> DanhSachHinhHoc

    def TimHinhCoDienTichNhoNhat(self):
        return self.TimHinhCoDienTich(self.TimDienTichHinhNhoNhat())
    # endregion

    # region 5. Tìm hình tròn có diện tích nhỏ nhất -> DanhSachHinhHoc
    def TimHinhTronNhoNhat(self):
        return self.TimHinhCoDienTich(self.TimDienTichHinhNhoNhat(HinhTron), HinhTron)
    # endregion

    # region 6. Sắp xếp tăng giảm theo diện tích
    def SapXepTangGiamTheoDienTich(self, condition=False):
        self.dshh.sort(key=self.GetDT, reverse=condition)
    # endregion

    # region 7. Đếm số lượng hình theo kiểu cho trước
    def DemSoLuongHinhTheoKieu(self, hinh=HinhHoc):
        count = 0
        for hh in self.dshh:
            if isinstance(hh, hinh):
                count += 1
        return count
    # endregion

    # region 8. Tính tổng diện tích các hình
    def TinhTongDienTich(self):
        return self.TinhTongDienTichTheoKieu()
    # endregion

    # region 9. Tìm hình có diện tích lớn nhất theo kiểu
    def TimHinh_X_CoDienTichLonNhat(self, hinh):
        return self.TimHinhCoDienTich(self.TimDienTichHinhLonNhat(hinh), hinh)
    # endregion

    # region 10. Tìm vị trí của hình h trong danh sách
    def TimViTriCuaHinhTrongDanhSach(self, hinh: HinhHoc):
        for i in range(len(self.dshh)):
            if self.dshh[i] == hinh:
                return i
        return -1
    # endregion

    # region 11. Xóa hình tại vị trí:

    def XoaHinhTaiViTri(self, index: int):
        try:
            del self.dshh[index]
            return True
        except:
            return False
    # endregion

    # region 12. Tìm hình theo diện tích
    def TimHinhCoDienTich(self, dientich: float, hinh=HinhHoc):
        result = DanhSachHinhHoc()
        for hh in self.dshh:
            if isinstance(hh, hinh) and hh.TinhDienTich() == dientich:
                result.ThemHinh(hh)
        return result
    # endregion

    # region 13. Xóa hình
    def XoaHinhChoTruoc(self, hinh: HinhHoc):
        return self.XoaHinhTaiViTri(self.TimViTriCuaHinhTrongDanhSach(hinh))
    # endregion

    # region 14. Xóa hình theo loại
    def XoaHinhTheoLoai(self, loai):
        for hh in self.dshh:
            if type(hh) is loai:
                self.dshh.remove(hh)
    # endregion

    # region 15. Xuất hình theo chiều tăng giảm
    def XuatHinhTheoChieuTangGiam(self, loai, condition=True):
        result = self.TimHinhTheoKieu(loai)
        result.SapXepTangGiamTheoDienTich()

        # region Hàm hỗ trợ

    def TimDienTichHinhLonNhat(self, hinh=HinhHoc):
        max = -1
        for hh in self.dshh:
            if isinstance(hh, hinh) and hh.TinhDienTich() > max:
                max = hh.TinhDienTich()
        return max

    def TimDienTichHinhNhoNhat(self, hinh=HinhHoc):
        min = 1000000000
        for hh in self.dshh:
            if isinstance(hh, hinh) and hh.TinhDienTich() < min:
                min = hh.TinhDienTich()
        return min

    def GetDT(self, hh):
        return hh.TinhDienTich()

    def TinhTongDienTichTheoKieu(self, hinh=HinhHoc):
        sum = 0
        for hh in self.dshh:
            if isinstance(hh, hinh):
                sum += hh.TinhDienTich()
        return sum

    def TimHinhTheoKieu(self, hinh):
        result = DanhSachHinhHoc()
        for hh in self.dshh:
            if type(hh) is hinh:
                result.ThemHinh(hh)
        return result
    # endregion
