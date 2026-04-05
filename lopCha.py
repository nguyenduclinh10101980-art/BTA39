# class xe: hang, mauSac, giaTien
#method: str, khoiDong()-> "xe {hang} dang khoi dong", run() - override
class Xe:
    def __init__(self, hang="", mauSac="", giaTien=""):
        self.__hang = hang
        self.__mauSac = mauSac
        self.__giaTien = giaTien

    def __str__(self):
        return f"Xe {self.__hang}, {self.__mauSac}, {self.__giaTien}"
    def khoiDong(self):
        return f" Xe {self.__hang} dang khoi dong"
    # override: ham se ghi de cho lop con
    def run(self):...


