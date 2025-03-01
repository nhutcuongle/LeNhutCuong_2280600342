sogiolam = float(input(" nhap so gio lam moi ngay : "))
luonggio = float(input("nhap thu lao moi gio lam tieu chuan : "))
giotieuchuan = 44
giovuotchuan = max(0, sogiolam- giotieuchuan)
thuclinh= giotieuchuan*luonggio+giovuotchuan*luonggio*1.5
print(f"so tien thuc linh cua nhan vien : {thuclinh}")