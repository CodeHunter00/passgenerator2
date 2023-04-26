#Random kütüphanemizi ekliyoruz.
import random
#Kullanýcýdan deðer alýyoruz.
d = int(input("Sifrenizin uzunlugunu giriniz."))
#Alfaponetik alfabeyi listeliyoruz.
ap =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#Alfanumerik alfabeyi listeliyoruz.
an=['1','2','3','4','5','6','7','8','9','0']
#Boþ listeye yukarýdaki alfaponetik ve alfanumerik iki listeden rastgele deðer alýp yazdýracaðýz.
lst=[] 
#For bloðu ile (d) deðiþkeni kadar döngüyü çalýþtýrýyoruz.
for i in range(d):
    #Random kütüphanesini kullanarak alfaponetik (ap) ve alfanumerik (an) listelerinden rastgele aldýðýmýz,
    #deðerleri boþ listemize yazdýrýyoruz.
    lst.append(random.choice(ap))
    lst.append(random.choice(an))
# str manipülasyon yöntemi ile çýktýdaki parantez ve týrnaklarý siliyoruz.
print("Sifreniz : " + "".join(lst)) 