#Random k�t�phanemizi ekliyoruz.
import random
#Kullan�c�dan de�er al�yoruz.
d = int(input("Sifrenizin uzunlugunu giriniz."))
#Alfaponetik alfabeyi listeliyoruz.
ap =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#Alfanumerik alfabeyi listeliyoruz.
an=['1','2','3','4','5','6','7','8','9','0']
#Bo� listeye yukar�daki alfaponetik ve alfanumerik iki listeden rastgele de�er al�p yazd�raca��z.
lst=[] 
#For blo�u ile (d) de�i�keni kadar d�ng�y� �al��t�r�yoruz.
for i in range(d):
    #Random k�t�phanesini kullanarak alfaponetik (ap) ve alfanumerik (an) listelerinden rastgele ald���m�z,
    #de�erleri bo� listemize yazd�r�yoruz.
    lst.append(random.choice(ap))
    lst.append(random.choice(an))
# str manip�lasyon y�ntemi ile ��kt�daki parantez ve t�rnaklar� siliyoruz.
print("Sifreniz : " + "".join(lst)) 