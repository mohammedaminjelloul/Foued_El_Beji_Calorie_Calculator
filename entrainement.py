from pickle import load ,dump
from numpy import array
F1=open("nutrition.dat","wb")
F2=open("nutrition.txt","w")


def saisir():
    N=input("saisir le Nombre de repas : ")
    if N.isdigit():
        return int(N)
    else:
        return saisir()


def remplir(T,N):
    for i in range(N):
        T[i]["Nom_repas"]=str(input("nom de repas: "))
        T[i]["Poids_repas"]=float(input("le poids de repas: "))
        T[i]["P"]=float(input("saisir le quantite de protein/100(g-ml) dans "+T[i]["Nom_repas"]+" : "))
        T[i]["C"]=float(input("saisir le quantite de carbs/100(g-ml) dans "+T[i]["Nom_repas"]+" : "))
        T[i]["F"]=float(input("saisir le quantite de fats/100(g-ml) dans "+T[i]["Nom_repas"]+" : "))
        T[i]["Total_P"]=((T[i]["Poids_repas"]*T[i]["P"])/100)
        T[i]["Total_C"]=((T[i]["Poids_repas"]*T[i]["C"])/100)
        T[i]["Total_F"]=((T[i]["Poids_repas"]*T[i]["F"])/100)

        #2 nombre apres la virgule
        str1=str(T[i]["Total_P"])
        str1=float(str1[0:str1.find(".")+3])
        str2=str(T[i]["Total_C"])
        str2=float(str2[0:str2.find(".")+3])
        str3=str(T[i]["Total_F"])
        str3=float(str3[0:str3.find(".")+3])

        T[i]["Total_cals"]=(T[i]["Total_P"])*4+(T[i]["Total_C"])*4+(T[i]["Total_F"])*9
        #2 nombre apres la virgule
        str4=str(T[i]["Total_cals"])
        str4=float(str4[0:str4.find(".")+3])
        #
        resultat=T[i]["Nom_repas"]+" : "+"P: "+str(str1)+" C: "+str(str2)+" F: "+str(str3)+" Calories : "+str(str4)
        F2.write(resultat+"\n")
        dump(T[i],F1)
    F1.close()
    F2.close()
N=saisir()
T=array([{}]*N)
remplir(T,N)
