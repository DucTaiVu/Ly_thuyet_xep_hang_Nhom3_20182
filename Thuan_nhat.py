import numpy as np
import math

def nhap_he_thong():
    print("Nhập các thông số của hệ thống thuần nhất(LƯU Ý: λ<nμ)")
    print("Số kênh phục vụ: n= ")
    n = np.int(input())
    print("Cường độ dòng yêu cầu: λ= ")
    λ = np.float(input())
    print("Cường độ dòng phục vụ: μ= ")
    μ = np.float(input())
    anpha = λ/μ
    return n,anpha,λ

def nhap_chi_phi():
    print("Giá trị tổn thất khi 1 yêu cầu chờ($/đơn vị tgian): Cc= ")
    Cc = np.float(input())
    print("Chi phí 1 kênh phục vụ($/đơn vị tgian): Ckb= ")
    Ckb = np.float(input())
    print("Tổn thất khi 1 kênh rỗi($/đơn vị tgian): Ckr= ")
    Ckr = np.float(input())
    print("Số tiền thu về khi phục vụ 1 y/c($)3: Cpv= ")
    Cpv = np.float(input())
    return Cc,Ckb,Ckr,Cpv

def tinh_P0(n, anpha):
    tong = 0
    for k in range(n+1):
        tong = tong + math.pow(anpha,k)/math.factorial(k)
    P0 = 1/(tong + math.pow(anpha,n+1)/(math.factorial(n)*(n-anpha)))
    return P0

def tinh_Pc(n,anpha,P0):
    Pc = P0*(math.pow(anpha,n)/math.factorial(n))*(n/(n-anpha))     #2.20
    return Pc

def hangcho_tgiancho_TB(n,anpha,P0,λ):
    Mc = P0*math.pow(anpha,n+1)/(math.factorial(n-1)*math.pow(n-anpha,2))
    Tc = Mc/λ
    return Mc,Tc

def kenh_roi_TB(n,anpha,P0):
    sum=0
    for k in range(n+1):
        sum=sum+(n-k)*math.pow(anpha,k)/math.factorial(k)
    Nr = P0* sum
    return  Nr

def tonthat_hieuqua(n,anpha,λ,Mc,Nr):
    Cc,Ckb,Ckr,Cpv = nhap_chi_phi()
    G = (Mc*Cc + (n-Nr)*Ckb + Nr*Ckr)
    E = (λ*n/anpha)*Cpv - G
    return G,E

def main():
    n,anpha, λ = nhap_he_thong()
    P0 = tinh_P0(n, anpha)
    print("1,Xác suất hệ thống rỗi: Pr= ",P0)
    Pc = tinh_Pc(n,anpha,P0)
    print("2,Xác suất một yêu cầu phải chờ: Pc= ",Pc)
    print("3,Xác suất một yêu cầu được phục vụ ngay: Ppvn= ",1-Pc)
    Mc,Tc = hangcho_tgiancho_TB(n,anpha,P0,λ)
    print("4,Độ dài hàng chờ trung bình: Mc= ",Mc)
    print("5, Thời gian chờ trung bình của 1 yêu cầu: Tc= ", Tc)
    Nr = kenh_roi_TB(n,anpha,P0)
    print("6,Số kênh rỗi trung bình: Nr= ",Nr)
    print("7,Số kênh bận trung bình: Nb= ", n-Nr)
    G,E = tonthat_hieuqua(n,anpha,λ,Mc,Nr)
    print("8,Chi phí tổn thất của hệ thống: G={}($/đvt/gian)".format(G))
    print("9,Hiệu quả kinh tế của mô hình E = {}($/đvtg)".format(E))
main()