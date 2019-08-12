#Vérification des numéros ISBN présent dans le tabNum
def verification(tabNum):
    for element in tabNum:#On parcourt le tableau et on traite chaque élément.
        elementMin = element[0:12]#Je retire le dernier chiffre qui est la clef de contrôle
        elementPair = elementMin[1:12:2]#je ne sélectionne que les chiffres ayant un emplacement pair hors du chiffre sans la clef
        elementImpair = elementMin[0:12:2]#je ne sélectionne que les chiffres ayant un emplacement impair hors du chiffre sans la clef
        clef = element[-1:]#je définis la clef comme étant le dernier chiffre du nombre.

        sommePair = 0 #initialisation des différentes variables me servant à faire les opérations
        sommeImpair = 0

        for j in(elementPair):#Je parcours le nb avec les chiffres "pairs" que je * par 3
            multi = int(j)*3
            sommePair = multi + sommePair #je fais la somme des résultats au fur et à mesure.
                                            #En fin de boucle j'ai la somme des chiffres pairs qui ont été * par 3

        for k in(elementImpair):#Je parcours le nb avec les chiffres "pairs"(*1 mais inutile)
            sommeImpair = int(k) + sommeImpair#je fais la somme des résultats au fur et à mesure.
                                                #En fin de boucle j'ai la somme des chiffres impairs

        sommeTotale = sommePair + sommeImpair#J'additionne les 2 sommes pour avoir la somme totale.

        reste = sommeTotale%10# je calcule le modulo de la somme totale que j'appelle "reste"

        if (10-reste) == int(clef):#je vérifie si 10 diminué du reste est égal à la clef
            tabNumBon.append(element) #Si oui, j'ajoute le nb de départ à un nouveau tableau
                                        #ce tableau ne contient que les nombres qui sont ok


    return(tabNumBon)


def triPays(tabNumBon):#Trie et affichage en fonction du pays

    print("Liste par pays:")

    print("     France")
    for element in tabNumBon:#Je parcours le tableau avec les numéros OK
        pays = element[2]#j'extrait le 3ème chiffre qui correspond au pays
        if pays == "1":#je teste, si le chiffre correspond à 1 donc à la France
            print("         ", element[6:12])#je printe les 6 chiffres demandés hors du nb de départ


    print("     Belgique")#Les commentaires sont les mêmes pour les 3 pays
    for data in tabNumBon:
        bel = data[2]
        if bel == "2":
            print("         ", data[6:12])


    print("     Nouvelle-Zelande")#Les commentaires sont les mêmes pour les 3 pays
    for donnee in tabNumBon:
        nz = donnee[2]
        if nz == "3":
            print("         ", donnee[6:12])
    return



def triEdition(tabNumBon):#Je trie et j'affiche en fonction de la maison d'édition

    print("Liste par maison d'édition:")


    print("       Hachette")
    for element in tabNumBon:#parcours du tableau avec nb ok
        hachette = element[4]#extraction du chiffre définissant la maison d'édition
        if hachette == "1":#test si c'est 1
            print("         ", element[6:12])#print des 6 chiffres demandés hors du nb de départ

    print("     Eyrolles")#les commentaires sont les mêmes pour les 3 maisons d'édition
    for data in tabNumBon:
        eyr = data[4]
        if eyr == "2":
            print("         ", data[6:12])

    print("     Casterman")#les commentaires sont les mêmes pour les 3 maisons d'édition
    for donnee in tabNumBon:
        cas = donnee[2]
        if cas == "3":
            print("         ", donnee[6:12])
    return


def triGenre(tabNumBon):#Je trie et j'affiche en fonction de la maison d'édition

    print("Liste par genre:")

    print("     Policier")
    for element in tabNumBon:#parcours du tableau avec nb ok
        pol = element[5]#extraction du chiffre définissant le genre
        if pol == "1":#test si c'est 1
            print("         ", element[6:12])#print des 6 chiffres demandés hors du nb de départ

    print("     Fiction")#les commentaires sont les mêmes pour les 3 genres.
    for data in tabNumBon:
        fic = data[5]
        if fic == "2":
            print("         ", data[6:12])

    print("     Historique")#les commentaires sont les mêmes pour les 3 genres.
    for donnee in tabNumBon:
        his = donnee[2]
        if his == "3":
            print("         ", donnee[6:12])
    return

















#----------------------------------------------------------------------------------------------------------



tabNum = ["0010115478946","0020227517426","0020339481967", "0030331494278","0010115817349","0030224951314","0020338475967","0020327127679","0010111582851","0010123857689","0030231839179","0030216751328","0010128463243","0010133985681","0020214713237","0030329257632","0010118544112"]
tabNumBon = []

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

tabNumBon = verification(tabNum)
triPays(tabNumBon)
triEdition(tabNumBon)
triGenre(tabNumBon)
