class Parking:

    def __init__(self):
        self.niv = 1
        self.place_niv1 = {}
        self.place_niv2 = {}
        self.place_niv3 = {}
        self.place_niv4 = {}
        self.place_niv5 = {}
        self.abonnes = []

    def place(self):
        for i in range(80):
            self.place_niv1[i] = False
            self.place_niv2[i] = False
            self.place_niv3[i] = False
            self.place_niv4[i] = False
            self.place_niv5[i] = False
    
    def abonnement(self, voiture):
        if voiture.ab == False:
            a = str(input("voulez-vous vous abonnez : "))
            if a == "oui" or a == "Oui":
                voiture.ab = True
                self.abonnes.append(voiture)
        else:
            print("vous êtes déjà abonné")
    
    def desabonner(self, voiture):
        if voiture.ab == True:
                a = str(input("voulez-vous vous désabonner ? : "))
                if a == "oui" or a == "Oui":
                    voiture.ab = False
                    if voiture in self.abonnes:
                        self.abonnes.remove(voiture)

    def si_voiture(self, niv, place):
        if niv == 1:
            if place in self.place_niv1:
                if self.place_niv1[place] != False:
                    print("place non libre")
                    a = str(input("Voulez-vous savoir quelle voiture est dessus ? : "))
                    if a == "oui" or a == "Oui":
                        print(self.place_niv1[place])
                    return False
                else:
                    print("place libre")
                    return True
        if niv == 2:
            if place in self.place_niv2:
                if self.place_niv2[place] != False:
                    print("place non libre")
                    return False
                else:
                    print("place libre")
                    return True
        if niv == 3:
            if place in self.place_niv3:
                if self.place_niv3[place] != False:
                    print("place non libre")
                    return False
                else:
                    print("place libre")
                    return True
        if niv == 4:
            if place in self.place_niv4:
                if self.place_niv4[place] != False:
                    print("place non libre")
                    return False
                else:
                    print("place libre")
                    return True
        if niv == 5:
            if place in self.place_niv5:
                if self.place_niv5[place] != False:
                    print("place non libre")
                    return False
                else:
                    print("place libre")
                    return True
        
    def ajout_place(self, niv, place, voiture):
        if parking.si_voiture(niv, place) == True:
            print("vous avez pris la place")
            if niv == 1:
                self.place_niv1[place] = voiture.information()
            if niv == 2:
                self.place_niv2[place] = voiture.information()
            if niv == 3:
                self.place_niv3[place] = voiture.information()
            if niv == 4:
                self.place_niv4[place] = voiture.information()
            if niv == 5:
                self.place_niv5[place] = voiture.information()
        else:
            print("vous pouvez pas prendre la place")

    def places_abonnes_occupees(self):
        liste_places = []
        for voiture in self.abonnes:
            if voiture.num_place != None:
                niv = voiture.num_place // 100
                place = voiture.num_place % 100
                if niv == 1:
                    if place in self.place_niv1:
                        if self.place_niv1[place] != False:
                            if self.place_niv1[place] != voiture.information():
                                liste_places.append(voiture.num_place)
                if niv == 2:
                    if place in self.place_niv2:
                        if self.place_niv2[place] != False:
                            if self.place_niv2[place] != voiture.information():
                                liste_places.append(voiture.num_place)
                if niv == 3:
                    if place in self.place_niv3:
                        if self.place_niv3[place] != False:
                            if self.place_niv3[place] != voiture.information():
                                liste_places.append(voiture.num_place)
                if niv == 4:
                    if place in self.place_niv4:
                        if self.place_niv4[place] != False:
                            if self.place_niv4[place] != voiture.information():
                                liste_places.append(voiture.num_place)
                if niv == 5:
                    if place in self.place_niv5:
                        if self.place_niv5[place] != False:
                            if self.place_niv5[place] != voiture.information():
                                liste_places.append(voiture.num_place)
        return liste_places

    def nombre_places_libres(self):
        nb = 0
        places_abonnes = []
        for voiture in self.abonnes:
            if voiture.num_place != None:
                places_abonnes.append(voiture.num_place)
        
        for i in range(80):
            if self.place_niv1[i] == False:
                if (0 + i) not in places_abonnes:
                    nb = nb + 1
            if self.place_niv2[i] == False:
                if (100 + i) not in places_abonnes:
                    nb = nb + 1
            if self.place_niv3[i] == False:
                if (200 + i) not in places_abonnes:
                    nb = nb + 1
            if self.place_niv4[i] == False:
                if (300 + i) not in places_abonnes:
                    nb = nb + 1
            if self.place_niv5[i] == False:
                if (400 + i) not in places_abonnes:
                    nb = nb + 1
        return nb

    def afficher_niveau(self, niv):
        if niv == 1:
            print(f"Niveau {niv}:")
            for i in range(80):
                if self.place_niv1[i] == False:
                    print(f"Place {0+i}: libre")
                else:
                    print(f"Place {0+i}: {self.place_niv1[i]}")
        if niv == 2:
            print(f"Niveau {niv}:")
            for i in range(80):
                if self.place_niv2[i] == False:
                    print(f"Place {100+i}: libre")
                else:
                    print(f"Place {100+i}: {self.place_niv2[i]}")
        if niv == 3:
            print(f"Niveau {niv}:")
            for i in range(80):
                if self.place_niv3[i] == False:
                    print(f"Place {200+i}: libre")
                else:
                    print(f"Place {200+i}: {self.place_niv3[i]}")
        if niv == 4:
            print(f"Niveau {niv}:")
            for i in range(80):
                if self.place_niv4[i] == False:
                    print(f"Place {300+i}: libre")
                else:
                    print(f"Place {300+i}: {self.place_niv4[i]}")
        if niv == 5:
            print(f"Niveau {niv}:")
            for i in range(80):
                if self.place_niv5[i] == False:
                    print(f"Place {400+i}: libre")
                else:
                    print(f"Place {400+i}: {self.place_niv5[i]}")

    def __str__(self):
        return (f"{self.place_niv1}"
                f"{self.place_niv2}"
                f"{self.place_niv3}"
                f"{self.place_niv4}"
                f"{self.place_niv5}")

class Voiture:

    def __init__(self, immatriculation , marque , proprietaire , abonnement):
        self.im = immatriculation
        self.ma = marque
        self.pr = proprietaire
        self.ab = abonnement
        self.num_place = None

    def get_immatriculation(self):
        return self.im
    
    def get_marque(self):
        return self.ma
    
    def get_proprietaire(self):
        return self.pr
    
    def get_abonnement(self):
        return self.ab

    def information(self):
        return (f"(immatriculation : {self.im})",
               f"(marque : {self.ma})",
               f"(proprietaire : {self.pr})",
               f"(abonnement : {self.ab})")

#initialisation du parking
parking = Parking()
parking.place()

#création de voiture 
voiture1 = Voiture("AA-123-BB", "BMW", "Jean", False)
voiture2 = Voiture("CC-456-DD", "Renault", "Marie", False)
voiture3 = Voiture("EE-789-FF", "Peugeot", "Paul", False)
voiture4 = Voiture("GG-012-HH", "Audi", "Sophie", False)

#test les informations d'une voiture
print(voiture1.information())

#ajout des abonnés et ajout des places d'abonnées manuelement
parking.abonnement(voiture1)
voiture1.num_place = 150
parking.abonnement(voiture2)
voiture2.num_place = 250

#Cela montre si il y a une voiture. Si oui = True, si non = False
parking.si_voiture(1, 50)
parking.si_voiture(1, 10)

#Ajout des voiture dans le parking
parking.ajout_place(1, 50, voiture1)
parking.ajout_place(2, 50, voiture3)
parking.ajout_place(1, 10, voiture4)
parking.ajout_place(1, 10, voiture2)

#Montre le nombre de place
print(parking.nombre_places_libres())

#affiche le niveau choisi
parking.afficher_niveau(1)

#montre les places d'abonnés occupées
print(parking.places_abonnes_occupees())