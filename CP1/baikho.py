class HocSinh:
    def __init__(self, ho_ten, dia_chi, chieu_cao, can_nang, hoc_luc):
        self.ho_ten = ho_ten
        self.dia_chi = dia_chi
        self.chieu_cao = chieu_cao
        self.can_nang = can_nang
        self.hoc_luc = hoc_luc

    def cap_nhat_dia_chi(self, dia_chi_moi):
        self.dia_chi = dia_chi_moi
        print(f"--- Đã cập nhật địa chỉ mới cho {self.ho_ten} ---")

    def kham_suc_khoe(self, chieu_cao_moi, can_nang_moi):
        # Hành động khi đến kỳ khám sức khỏe
        self.chieu_cao = chieu_cao_moi
        self.can_nang = can_nang_moi
        print(f"Đã cập nhật chỉ số sức khỏe cho {self.ho_ten} ---")

    def xuat_thong_tin(self):
        print("---------- THÔNG TIN HỌC SINH ----------")
        print(f"Họ và tên: {self.ho_ten}")
        print(f"Địa chỉ: {self.dia_chi}")
        print(f"Chiều cao: {self.chieu_cao} cm")
        print(f"Cân nặng: {self.can_nang} kg")
        print(f"Học lực: {self.hoc_luc}")
        print("----------------------------------------")


        