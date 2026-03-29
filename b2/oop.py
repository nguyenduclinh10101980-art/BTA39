#oop : object - oriented promgraming
#tao lop vat nuoi(giong, mau sac, tuoi, can nang)

class VatNuoi:
    def __init__(self, giong="", mauSac="", tuoi=0,canNang=0):
        self.__giong = giong
        self.__mauSac = mauSac
        self.__tuoi = tuoi
        self.__canNang = canNang

    def __str__(self) -> str: 
        return f"VatNuoi: {self.__giong}, {self.__mauSac}, {self.__tuoi}, {self.__canNang}"

#getter vaf setter(lay va cai dat gia tri thuoc tinh)
#"get"//"set" + ten thuoc tinh
def getGiong (self):
     return self.__giong 

def getmauSac (self):
    return self.__mauSac

def getTuoi (self):
    return self.__tuoi

def getCanNang (self):
    return self.__canNang

def setGiong (self,giongMoi):
    if giongMoi == "": print("gia tri khong duoc de trong")
    else: self.__giong = giongMoi

def setMauSac (self,mauSacMoi):
    if mauSacMoi == "": print("gia tri khong duoc de trong")
    else: self.__mauSac = mauSacMoi

def setTuoi (self, tuoiMoi):
    if tuoiMoi < 0: print("gia tri khong duoc de la so am")
    else: self.__tuoi = tuoiMoi

def setCanNang (self, canNangMoi):
    if canNangMoi < 0: print("gia tri khong duoc la so am")
    else: self.__canNang = canNangMoi



#tao doi tuong
meo1 = VatNuoi("meo", "den")
print(meo1)

# gan gia tri cho thuoc tinh
print(meo1.getTuoi())
meo1,setTuoi(tuoiMoi=2)

meo1,setCanNang(canNangMoi=-1)
print(meo1.getCanNang())

print(meo1)

