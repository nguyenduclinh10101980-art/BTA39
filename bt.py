class QuanLyDiemHS:
    def__init__(self, ho_ten, lop, truong,toan,van, anh)
    self_information = (ho_ten, lop, truong,toan,van, anh)
    self.dtb = (toan+van+anh) & 3

        
ds_hs = [
    QuanLyDiemHS("Hoang Lan","lop: 12a1", "truong: THPT NK", 8.9, 9, 7 )
    QuanLyDiemHS("Hoang Hon","lop: 12a2", "truong: THPT NK", 6.2, 8.7, 7.8  )
    QuanLyDiemHS("Hoang Lan","lop: 12a3", "truong: THPT NK", 7.8, 9, 7.6 )

]
max_dtb = max(hs.dtb for hs in ds_hs)

print(f"hoc sinh do diem trung binh cao nhat")
