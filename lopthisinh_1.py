from datetime import datetime

class ThiSinh:
    def __init__(self, ho_ten, ngay_sinh, diem1, diem2, diem3):
        self.ho_ten = ho_ten
        self.ngay_sinh = self.dinh_dang_ngay_sinh(ngay_sinh)
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
        self.tong_diem = self.diem1 + self.diem2 + self.diem3

    def dinh_dang_ngay_sinh(self, ngay_sinh):

        ngay_sinh_dinh_dang = datetime.strptime(ngay_sinh, "%d/%m/%Y").strftime("%d/%m/%Y")
        return ngay_sinh_dinh_dang

    def hien_thi(self):

        print(f"{self.ho_ten} {self.ngay_sinh} {self.tong_diem:.1f}")

# Đọc thông tin từ bàn phím
ho_ten = input().strip()
ngay_sinh = input().strip()
diem1 = float(input())
diem2 = float(input())
diem3 = float(input())

thi_sinh = ThiSinh(ho_ten, ngay_sinh, diem1, diem2, diem3)
thi_sinh.hien_thi()
