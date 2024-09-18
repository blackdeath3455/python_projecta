import random
def dikdorgenformul():
    a=int(input("u kenar girin"))
    b=int(input("k kenar girin"))
    print("alan")
    print(a*b)
    print("cevre")
    print((a+b)*2)
def daireformul():
    a=int(input("yaricapi girin"))
    print("alan")
    print(3*a*a)
    print("cevre")
    print(2*3*a)
def ciftmidir(a,b):
    if(a/b%2==0):
        print("cift sayilarin ortalamasi cift")
    else:
        print("cift sayilarin ortalamasi cift degil")
def varmidir(kelime, harf):
    for i in range(len(kelime)):
        if(harf==kelime[i]):
            print("var")
            break
"""
#soru 1
print("merhaban dunya")
#soru 2
isim=input("isiminiz : ")
print("merhaban "+isim)
#soru 3
sayi1=int(input("sayi 1'i giriniz : "))
sayi2=int(input("sayi 2'yi giriniz : "))
print(sayi1+sayi2)
#soru 4
sayi1=int(input("sayi 1'i giriniz : "))
sayi2=int(input("sayi 2'yi giriniz : "))
print((sayi1+sayi2)/2)
#soru 5
sayi1=int(input("vize'yi giriniz : "))
sayi2=int(input("final'i giriniz : "))
print((sayi1+sayi2)/2)"""
#soru 6
sayi1=int(input("not 1'i giriniz : "))
sayi2=int(input("not 2'yi giriniz : "))
sayi3=int(input("not 3'u giriniz : "))
print((sayi1+sayi2+sayi3)/3)
"""#soru 7
sayi1=int(input("ortalama'yi giriniz : "))
if(sayi1>50):
    {
        print("gecti")
    }  
else:{
    print("kaldi")
}
#soru 8
sayi1=int(input("sayi'yi giriniz : "))
if(sayi1%2==0):
    {
        print("cift")
    }  
else:{
    print("tek")
}
#soru 9
sayi1=int(input("sayi'yi giriniz : "))
if(sayi1>0):
    {
        print("pozitif")
    }  
elif(sayi1<0):{
    print("negatif")
}
else:{
    print("sifir")
}
#soru 10
sayi1=int(input("kilonuzu giriniz : "))
sayi2=float(input("boyunuxu giriniz : "))
sayi1=sayi1/sayi2*sayi2
if(sayi1>25):
    {
        print("kilolu")
    }  
elif(sayi1<18):{
    print("zayif")
}
else:{
    print("normal")
}
#soru11
sayi1=int(input("yasinizi giriniz : "))
if(sayi1>18):
    {
        print("ehliyet alabilirsiniz")
    }  
else:{
    print("ehliyet alamazsiniz")
}
#soru12
for i in range(100):{
    print(i+1)
}
#soru13
for i in range(100):
    if(i%2==0):
        {
            print(i)
        }  
#soru14
for i in range(100):
    if(i%2==1):
        {
            print(i)
        }
#soru15
for i in range(100):
    if(i%3==0 and i%5==0):
        {
            print(i)
        }  
#soru 16
sayi1=int(input("sayi'yi giriniz : "))
for i in range(sayi1):
    print(i)
# soru 17
sayi1=int(input("dikdortgen 1'i giriniz : "))
sayi2=int(input("dikdortgen 2'yi giriniz : "))
print("alan")
print(sayi1*sayi2)
print("cevre")
print((sayi1+sayi2)*2)
# soru 18
kelime=input("kelimeyi giriniz : ")
for i in kelime:
    print(i)
# soru 19
sayi1=int(input("baslangic sayisini giriniz : "))
sayi2=int(input("bitis sayisin giriniz : "))

for i in range(sayi2-sayi1):
    sayi3+=i+sayi1
print(sayi3)    
# soru 20
sayi1=input("gitmek istediginiz etkinligi  giriniz : ")
sayi2=input("ogrenci misiniz : ")
if (sayi1=="tiyatro"):sayi3=10
else:sayi3=16
if(sayi2=="evet"):sayi3/=2
print(sayi3)

# soru 21 
sayi1=int(input(" sayiyi giriniz : "))
sayi2=0
for i in range(2,sayi1):
    
    if(sayi1%i==0):
        print("sayiniz asal degil")
        sayi2=1
        break 
           
if(sayi2==0):
    print("sayiniz asal")

#soru  22
sayi1=int(input("sayi'yi giriniz : "))
sayi2=0
sayi3=0
for i in range(sayi1):
    if(i%2==0):
        sayi2+=i
        print(sayi2)     
    else:
        sayi3+=i
        print(sayi3)
print( sayi3  )
print(sayi2) 
# soru 23
sayi1=int(input("maasinizi  giriniz : ")) 
sayi2=int(input("zam oranizi  giriniz : "))
sayi1=sayi1+ sayi1/100*sayi2
print(sayi1)"""
#soru 24 
dikdorgenformul()
#soru 25
daireformul()
#soru 26
sayi1=random.randint(1,100)
for i in range(3):
    sayi2=int(input("tahmininizi girin "))
    if(sayi1==sayi2):
        print("dogru tahmin")
        sayi3=1
    elif(sayi1 <=sayi2):
        print("tahmininiz cok buyuk")
    elif(sayi1 >=sayi2):
        print("tahmininiz cok kucuk")
if(sayi3!=1):
    print("kaybettiniz dogru sayi")
    print(sayi1)
#soru 27
from datetime import datetime


tarih_str = input("Tarihi gir ")



tarih = datetime.strptime(tarih_str, "%d-%m-%Y")
    
gun_numarasi = tarih.timetuple().tm_yday
print(f"{tarih_str} tarihi yılın {gun_numarasi}. günü.")
# soru 28
liste=[1,25,8,69,2,4,3,5,78,2,50,6,57,45,50,95,25,55]
for i in range(len(liste)):
    if(liste[i]%5==0):
        print(liste[i])
# soru 29
kelime="sdalasdasdadjoqwejiqngihrajomklsklgvnbaqhigojpetjh"
sayi1=input("harf giriniz")
varmidir(kelime=kelime,harf=sayi1)
# soru 30 
sayi1=int(input("baslangic sayisini giriniz : "))
sayi2=int(input("bitis sayisin giriniz : "))
sayi3=0
sayi4=0
for i in range(sayi2-sayi1):
    if(i%2==0):
        sayi3+=i+sayi1
        sayi4+=1

print(sayi3)
ciftmidir(sayi3,sayi4)
#soru 31
dikdorgenformul()
#soru 32
gunler=["pazartesi","sali","carsamba","persembe","cuma"]
sayi1=int(input("gunun indeksini giriniz"))
print(gunler[sayi1])
#soru 33
list1020=[11,12,13,14,15,16,17,18,19,20]
list2030=[21,22,23,24,25,26,27,28,29,30]
list1030=[]
for i in range(len(list1020)):
    list1030.append(list1020[i])
    list1030.append(list2030[i])
for i in range(len(list1030)):
    if(list1030[i]%4==0):
        print(list1030[i])
#soru 34 \
sayi1=input("sayi giriniz")
sayi2=int(sayi1[1])+int(sayi1[2])
print(sayi2)
# soru 35
sayi2=0
while True:
    
    sayi1=int(input("sayi giriniz 0 ile islemi bitirebilirsiniz"))
    if(sayi1==0):
        print("islem bitti girdiginiz sayilarin toplami")
        print(sayi2)
    else:
        sayi2+=sayi1    