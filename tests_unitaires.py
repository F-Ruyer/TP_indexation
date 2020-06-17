import indexation

l= indexation.liste_test
d = indexation.dico_liste_racines("mes_docs/", l)
dicotf = indexation.calculeTF(d)
#norme1 = indexation.norme_doc(dicotf["mondoc1.txt"])
dicodf = indexation.calculeDF(d)
index = indexation.creationIndex(dicotf,dicodf)
inv = indexation.inverseindex(index)


def teste_liste():
    print("liste des docs de tests:")
    print (l)

def affiche_le_dico():
    print(" ")
    print("Affichage du dico des docs:")
    print(d)

def calcule_norme():
    print(" ")
    print("Norm e du vecteur de tf de mondoc1")
    print(norme1)


def affiche_leTF():

    print(" Affichage des TF:")
    print(dicotf)

def affiche_leDF():
    print(" Affichage des DF:")
    print(dicodf)

def affiche_index_tfidf():
    # index = indexation.creationIndex(dicotf,dicodf)
    print(" Affichage de l'index:")
    print(index)

def affiche_index_inverse():
    print(" Affichage de l'index inverse:")
    print(inv)

def teste_tout():
    teste_liste()
    affiche_le_dico()
    #calcule_norme()
    affiche_leTF()
    affiche_leDF()
    affiche_index_tfidf()
    affiche_index_inverse()

import requete



def teste_liste_racine(r):
    print("Liste de racines:")
    return requete.requete2listeRacines(r)


def teste_liste2dico(l):
    print("vecteur requete pondere")
    return  requete.liste2dico(l,dicodf)



def teste_scalaires(vecteur_requete, inverse, index):
    print("produits scalaires:")
    return requete.scalaires(vecteur_requete, inverse,index)




def teste_tout_requetes():
    ma_requete = "chat et chien"
    l = teste_liste_racine(ma_requete)
    print(l)
    d= teste_liste2dico(l)
    print(d)
    produits = teste_scalaires(d, inv, index)
    print(produits)


