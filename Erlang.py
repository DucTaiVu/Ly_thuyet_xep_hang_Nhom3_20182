import numpy as np
import math

def nhap_he_thong():
    print("Nhập các thông số của hệ thống Erlang")
    print("Số kênh phục vụ: n= ")
    n = np.int(input())
    print("Cường độ dòng yêu cầu: λ= ")
    λ = np.float(input())
    print("Cường độ dòng phục vụ: μ= ")
    μ = np.float(input())
    anpha = λ/μ
    return n,anpha,λ

def nhap_chi_phi():
    # print("Thời gian hoạt động của hệ thống: T= ")
    # T = np.float(input())
    print("Giá trị tổn thất khi 1 yêu cầu bị từ chối($): Ctc= ")
    Ctc = np.float(input())
    print("Chi phí 1 kênh phục vụ($/đơn vị tgian): Ckb= ")
    Ckb = np.float(input())
    print("Tổn thất khi 1 kênh rỗi($/đơn vị tgian): Ckr= ")
    Ckr = np.float(input())
    print("Số tiền thu về khi phục vụ 1 y/c($)3: Cpv= ")
    Cpv = np.float(input())
    return Ctc,Ckb,Ckr,Cpv

def tinh_P0(n, anpha):
    tong = 0
    for k in range(n+1):
        tong = tong + math.pow(anpha,k)/math.factorial(k)
    P0 = 1/tong
    return P0

def tinh_Ptc_Ppv(n, anpha, P0):
    Ptc = P0*math.pow(anpha,n)/math.factorial(n)
    return Ptc, 1-Ptc

def kenh_ban_TB(anpha, Ppv):
    N_ban = anpha*Ppv
    return N_ban

def tonthat_hieuqua(n,λ):
    Ctc,Ckb,Ckr,Cpv = nhap_chi_phi()
    G = (λ*Ptc*Ctc + N_ban*Ckb + (n-N_ban)*Ckr)
    E = λ* Ppv*Cpv - G
    return G,E

def toi_uu(anpha):
    print("Xác suất từ chối tối đa: Ptc_max= ")
    Ptc_max = np.float(input())
    n0=1
    sum = 0
    Ptc1 = 1
    while Ptc1>Ptc_max:
        p0 = tinh_P0(n0,anpha)
        Ptc1 = (math.pow(anpha,n0)/math.factorial(n0))*p0
        if Ptc1 > Ptc_max:
            n0 = n0 +1
        else:
            return n0,Ptc1,Ptc_max

n,anpha,λ = nhap_he_thong()
P0 = tinh_P0(n,anpha)
Ptc,Ppv = tinh_Ptc_Ppv(n,anpha,P0)
N_ban = kenh_ban_TB(anpha,Ppv)
print("1,Xác suất các kênh đều rỗi: P0=",P0)
print("2,Xác suất yêu cầu bị từ chối: Ptc=",Ptc)
print("3,Số kênh bận trung bình: N_ban=",N_ban)

G,E = tonthat_hieuqua(n,λ)
print("4,Chi phí tổn thất của hệ thống: G={}($/đvt/gian)".format(G))
print("5,Hiệu quả kinh tế của mô hình E = {}($/đvtg)".format(E))

n0,Ptc1,Ptcmax = toi_uu(anpha)
print("6,Để Ptc < {} hệ thống có tối thiểu {}(kênh) với Ptc ={}.".format(Ptcmax,n0,Ptc1))