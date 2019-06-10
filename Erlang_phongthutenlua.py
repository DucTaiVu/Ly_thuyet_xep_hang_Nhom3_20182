import numpy as np
import math

def nhap_he_thong():
    print("Nhập các thông số của hệ thống Erlang")
    print("Cường độ tên lửa bắn phá(chiếc/phút): λ1= ")
    λ1 = np.float(input())
    print("Cường độ tiêu diệt của tầng 1: μ1= ")
    μ1 = np.float(input())
    print("Cường độ tiêu diệt của tầng 2: μ2= ")
    μ2 = np.float(input())
    anpha1 = λ1/μ1
    return anpha1,λ1,μ2
def tinh_P0(n, anpha):
    tong = 0
    for k in range(n+1):
        tong = tong + math.pow(anpha,k)/math.factorial(k)
    P0 = 1/tong
    return P0

def tinh_Ptc_Ppv(n, anpha, P0):
    Ptc = P0*math.pow(anpha,n)/math.factorial(n)
    return Ptc

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

n=1
anpha1,λ1,μ2 = nhap_he_thong()
P01 = tinh_P0(n,anpha1)
#print(P01)
Ptc1 = tinh_Ptc_Ppv(n,anpha1,P01)
print("Xác suất để lọt qua của tầng 1: Ptc1=",Ptc1)
λ2 = Ptc1*λ1
print("Cường độ bắn phá tầng 2 là: λ2=",λ2)
P02 = tinh_P0(n,λ2/μ2)
Ptc2 = tinh_Ptc_Ppv(n,λ2/μ2,P02)
print("Xác suất để lọt qua của tầng 2: Ptc2=",Ptc2)
Ptc = Ptc1*Ptc2
print("Xác suất để lọt qua của cả hệ thống: Ptc=",Ptc)