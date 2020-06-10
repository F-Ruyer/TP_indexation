# Mon TP
# Fred Ruyer

import outils




def essai():
    print("hi")

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
    print(liste_sans_non_mots)
    liste_mots_utiles=[]
    for m in liste_sans_non_mots:
        if not(m in outils.MOTSOUTILS):
            liste_mots_utiles.append(m)
    return liste_mots_utiles


def calculeTF(listeracine):
    """
    :param listeracine: dictionnaire de cles noms desdocs et d'éléments la liste des racines
    :return: dictionnaire de clés nm du doc et d'éléments un dictionnaire de clé la racine et d'élément son tf
    """
    return{}

def calculeDF(listeracines):
    """

    :param listeracines: dico qui contient les listes de racines pour chaque doc
    :return: dico qui contient pour chaque racine le nbre de docs qui la contiennent
    """
    return{}

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












