import indexation

l= indexation.liste_test
d = indexation.dico_liste_racines("mes_docs/", l)
dicotf = indexation.calculeTF(d)
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
    affiche_leTF()
    affiche_leDF()
    affiche_index_tfidf()
    affiche_index_inverse()







