import indexation
import outils

#----------
# Fonctions
#----------


def requete2listeRacines(req):
    """
    :param req: texte de la requete
    :return: liste des racines
    """
    liste_de_mots_bruts = outils.string2list(req)  #transo de la chaine en liste
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



def liste2dico(l,dicodf):
    """
    calcule le vecteur de clés les racines de la liste et de valeurs leur tfidf
    :param l: racines d'une requete
    :param dicodf: dictionnaire des df des racines
    :return: dictionnaire
    """
    resultat={}
    for rac in l:
        resultat[rac] = dicodf[rac]
    return resultat



def scalaires(vecteur_requete,inverse,index):
    """
    :param vecteur_requete:
    :param inverse: index inverse
    :param index: index
    :return: un dictionnaire de documents avec leurs poids (similarité) calculés avec la requête.
    """
    resultat = {}
    for rac in vecteur_requete:
        for doc in inverse[rac]:
            if not (resultat.get(doc)):
                resultat[doc] = indexation.scalaire(vecteur_requete,index[doc])
    return resultat


def trie_docs(d):
    """
    trie un dictionnaire de clés noms de docs et de valeurs un nombre en une liste triée
    :param l: dico de docs
    :return: liste de docs
    """
    petitversgrand = sorted(d.items(), key=lambda x:x[1])
    l = len(petitversgrand)
    sortie = []
    for i in range(l):
        sortie.append(petitversgrand[l-i-1])
    return sortie



def traite_requete(r):
    """
    :param r:une requete (chaine de caracteres)
    :return: liste de docs triés
    """
    return[]




#----------
# Interaction
#----------

def boucle_interaction():
    """
    boucle principale
    :return: programme principal
    """
    while True:
        print("Votre requête?")