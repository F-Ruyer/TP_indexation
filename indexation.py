# Mon TP
# Fred Ruyer
from typing import Iterator

import outils



def doc2listeRacines(chemin):
    """
    :param chemin: chemin du document
    :return: liste des racines
    """
    chaine_de_fichier = outils.loadFile(chemin) #chargement de la chaine
    liste_de_mots_bruts = outils.string2list(chaine_de_fichier)  #transo de la chaine en liste
    liste_sans_non_mots=[]
    for m in liste_de_mots_bruts:
        if outils.contientLettres(m):
            liste_sans_non_mots.append(m)  #suppression des nonmots
    liste_mots_utiles=[]  #suppression des mots-outils
    for m in liste_sans_non_mots:
        if not(m in outils.MOTSOUTILS):
            liste_mots_utiles.append(m)
    liste_racines = list(map (outils.mot2racine , liste_mots_utiles))
    return liste_racines

import os

liste_documents = os.listdir(outils.DOSSIERDOCUMENTS)


def dico_liste_racines():
    """
    :return: retourne le dictionnaire des clés= noms de fichiers et élts = liste des racines
    """
    dict ={}
    for f in liste_documents:
        dict[f] =  doc2listeRacines(f)
    return dict


def calcule_tf(liste):
    """
    :param liste: liste de mots
    :return: le dictionnaire de clés les mots et de valeur le nb d'occurence du mot dans la liste
    """
    dict={}
    for w in liste:
        if dict.get(w):  # renvoie 1 si le mot est dans le dict, faux sinon
            dict[w]=dict[w]+1
        else:
            dict[w]=1
    return dict


def calculeTF(listeracine):
    """
    :param listeracine: dictionnaire de cles noms des docs et d'éléments la liste des racines
    :return: dictionnaire de clés nm du doc et d'éléments un dictionnaire de clé la racine et d'élément son tf
    """
    dict={}
    for cle in listeracine:
        dict[cle] = calcule_tf(listeracine[cle])
    return dict



def calculeDF(listeracines):
    """
    :param listeracines: dico qui contient les listes de racines pour chaque doc
    :return: dico qui contient pour chaque racine le nbre de docs qui la contiennent
    """
    dict={}
    for doc in listeracines:
        for w in listeracines[doc]:
            if dict.get(w):
                dict[w]=dict[w]+1
            else:
                dict[w] = 1
    return dict

def creationIndex(dicoTF,dicoDF):
    """
    :param dicoTF: contient les TF de chaque doc
    :param dicoDF: contient les df de chaque racine
    :return: dico qui contient pour chaque doc  un dico qui contient pour chaque racine son tfidf
    """
    return{}


def inverseindex(index):
    """
    :param index: index doc:recine:tfidf
    :return: renvoie l'inverse racine:doc:tfidf
    """
    return{}












