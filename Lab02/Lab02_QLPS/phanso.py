import math


class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau

    def __str__(self):
        return "{}/{}".format(self.tu, self.mau)

    @staticmethod
    def __TimUCLN(a: int, b: int):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def RutGon(self):
        # number = self.__TimUCLN(self.tu, self.mau)
        # self.tu = int(self.tu/number)
        # self.mau = int(self.mau/number)
        number = math.gcd(self.tu, self.mau)
        self.tu //= number
        self.mau //= number

    def __add__(self, other):
        kq = PhanSo()
        kq.tu = self.tu*other.mau+self.mau*other.tu
        kq.mau = self.mau*other.mau
        kq.RutGon()
        return kq

    def __sub__(self, other):
        kq = PhanSo()
        kq.tu = self.tu*other.mau-self.mau*other.tu
        kq.mau = self.mau*other.mau
        # kq.RutGon()
        return kq

    def __mul__(self, other):
        kq = PhanSo()
        kq.tu = self.tu*other.tu
        kq.mau = self.mau*other.mau
        # kq.RutGon()
        return kq

    def __truediv__(self, other):
        kq = PhanSo()
        kq.tu = self.tu*other.mau
        # kq.mau = self.mau*other.tu
        kq.RutGon()
        return kq

    def GetValue(self):
        return self.tu/self.mau

    def IsSimilar(self, other):
        return self.tu == other.tu and self.mau == other.mau

    def IsNegative(self):
        return self.tu/self.mau < 0

    def IsEqual(self, other):
        return self.GetValue() == other.GetValue()
