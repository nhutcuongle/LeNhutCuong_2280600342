def chiacho5(sonhiphan):
    sothapphan = int (sonhiphan, 2)
    if(sothapphan %5==0):
        return True
    else:
        return False
chuoi_sonhiphan = input("nhap chuoi so nhi phan ( phan tach boi dau phay): ")
sonhiphan_list = chuoi_sonhiphan.split(',')
sochiacho5 = [so for so in sonhiphan_list if chiacho5(so)]
if(len(sochiacho5)>0):
    ketqua=','.join(sochiacho5)
    print("cac so nhi phan chia cho 5 la: ",ketqua)      
else:
    printf("khong cos so nhi phan chia het cho 5 torng chuoi da nhap .")