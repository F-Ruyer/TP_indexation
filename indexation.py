# Mon TP
# Fred Ruyer
from typing import Iterator

import outils

def loadFile(dossier,filename):# loadfile du module outil modifié pour prendre en compte tout chemin
    """
    Lit un fichier et le renvoie sous forme de chaine unicode (tout en minuscule)
    """
    with open(dossier+filename, encoding='utf-8') as f:
        result = f.read()
    return result.lower()




def doc2listeRacines(dossier,fichier):
    """
    :param chemin: chemin du document
    :return: liste des racines
    """
    chaine_de_fichier = loadFile(dossier, fichier) #chargement de la chaine
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

#utilistaires chemins et fichiers
liste_documents_TP = os.listdir(outils.DOSSIERDOCUMENTS)

liste_test = os.listdir("mes_docs/")

liste_test_2 = os.listdir("Docs_Lorraine/")


def dico_liste_racines(dossier, l):
    """
    :param: dossier= dossier où sont les fichiers
    :param: l = liste des fichiers
    :return: retourne le dictionnaire des clés= noms de fichiers et élts = liste des racines
    """
    dict ={}
    for f in l:
        dict[f] = doc2listeRacines(dossier, f)
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


from math import sqrt


def norme_doc(dict):
    """
    :param dict: un dictionnaire de clés des mots et de valeurs le nb d'occ du mot dans un doc
    :return: la norme de ce vecteur
    """
    s= 0
    for mot in dict:
        s=s+dict[mot]**2
    n = sqrt(s)
    return n

def scalaire(u,v):
    """
    calcul du produt scalaire; mettre si possible en premier un vecteur qui a peu de coordonnées!
    Les vecteurs sont des dictionnaires, et on est sûr que toutes les clés de v sont aussi dans u
    :param u: vecteur
    :param v: vecteur
    :return: produit scalaire
    """
    scal = 0
    for mot in u:
        if v.get(mot):
            scal = scal + u[mot]*v[mot]
    return scal



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
        dejavu={} # contient les racines déjà rencontées
        for w in listeracines[doc]:
            if dict.get(w): # a été rencontré dans un doc précédent
                if  (not dejavu.get(w)): # n'a pas été comptabilisé dans ce document
                    dict[w]=dict[w]+1
                    dejavu[w]=1
            else:
                dict[w] = 1
                dejavu[w] = 1
    return dict



from math import log

def creationIndex(dicoTF,dicoDF):
    """
    :param dicoTF: contient les TF de chaque doc
    :param dicoDF: contient les df de chaque racine
    :return: dico qui contient pour chaque doc  un dico qui contient pour chaque racine son tfidf = tf/idf puis divisé par la norme
    """
    taille_corpus = len(dicoTF)
    for doc in dicoTF:
        for rac in dicoTF[doc]:
            dicoTF[doc][rac] = dicoTF[doc][rac]*log(taille_corpus/ dicoDF[rac])  #On calcule les tfidf
        norme = norme_doc(dicoTF[doc])  #on calcule les normes
        for rac in dicoTF[doc]:
            dicoTF[doc][rac] = dicoTF[doc][rac]/norme #on calcule les tfidf normalisés
    return dicoTF


def inverseindex(index):
    """
    :param index: index doc:recine:tfidf
    :return: renvoie l'inverse racine:doc:tfidf
    """
    inverse = {}
    for doc in index:
        for rac in index[doc]:
            if inverse.get(rac):
                inverse[rac][doc]=index[doc][rac]
            else:
                inverse[rac]={}
                inverse[rac][doc] = index[doc][rac]
    return inverse












