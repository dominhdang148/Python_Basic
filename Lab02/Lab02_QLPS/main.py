from dsps import DanhSachPhanSo
from phanso import PhanSo

import math
danhsach = DanhSachPhanSo()
danhsach.ThemPhanSo(PhanSo(5, 2))
danhsach.ThemPhanSo(PhanSo(1, 2))
danhsach.ThemPhanSo(PhanSo(-2, 4))
danhsach.ThemPhanSo(PhanSo(5, 7))
danhsach.ThemPhanSo(PhanSo(1, 2))
danhsach.ThemPhanSo(PhanSo(1, 9))

print(danhsach)

test = PhanSo(1, 2)

danhsach.SapXepTheoMau(True)
print(danhsach)
