class Parking:

    def __init__(self):
        self.niv = 1
        self.place_niv1 = []
        self.place_niv2 = []
        self.place_niv3 = []
        self.place_niv4 = []
        self.place_niv5 = []

    def place(self):
        for i in range(80):
            self.place_niv1.append(False)
            self.place_niv2.append(False)
            self.place_niv3.append(False)
            self.place_niv4.append(False)
            self.place_niv5.append(False)
    
    def abonnement(self, voiture):
        if voiture.ab == False:
            a = str(input("voulez-vous vous abonnez : "))
            if a == "oui" or a == "Oui":
                voiture.ab = True
        else:
            print("vous êtes déjà abonné")
            if voiture.ab == True:
                a = str(input("voulez-vous vous désabonner ? : "))
                if a == "oui" or a == "Oui":
                    voiture.ab = False

    def si_voiture(self, niv, place):
        if niv == 1:
            for i in range(len(self.place_niv1)):
                if i + 1 == place:
                    if self.place_niv1[i] == True:
                        print("place non libre")
                        return False
                    else:
                        print("place libre")
                        return True
        if niv == 2:
            for i in range(len(self.place_niv2)):
                if i + 1 == place:
                    if self.place_niv2[i] == True:
                        print("place non libre")
                        return False
                    else:
                        print("place libre")
                        return True
        if niv == 3:
            for i in range(len(self.place_niv3)):
                if i + 1 == place:
                    if self.place_niv3[i] == True:
                        print("place non libre")
                        return False
                    else:
                        print("place libre")
                        return True
        if niv == 4:
            for i in range(len(self.place_niv4)):
                if i + 1 == place:
                    if self.place_niv4[i] == True:
                        print("place non libre")
                        return False
                    else:
                        print("place libre")
                        return True
        if niv == 5:
            for i in range(len(self.place_niv5)):
                if i + 1 == place:
                    if self.place_niv5[i] == True:
                        print("place non libre")
                        return False
                    else:
                        print("place libre")
                        return True
        
    def ajout_place(self, niv, place, voiture):
        if parking.si_voiture(niv, place) == True:
            print("vous avez pris la place")
            if niv == 1:
                self.place_niv1[place-1] = True
            if niv == 2:
                self.place_niv2[place-1] = True
            if niv == 3:
                self.place_niv3[place-1] = True
            if niv == 4:
                self.place_niv4[place-1] = True
            if niv == 5:
                self.place_niv5[place-1] = True
        else:
            print("vous pouvez pas prendre la place")

    def __str__(self):
        print(f"{self.place_niv1}"+
              f"{self.place_niv2}"+
              f"{self.place_niv3}"+
              f"{self.place_niv4}"+
              f"{self.place_niv5}")

class Voiture:

    def __init__(self, immatriculation , marque , proprietaire , abonnement):
        self.im = immatriculation
        self.ma = marque
        self.pr = proprietaire
        self.ab = abonnement

    def information(self):
        print (f"(immatriculation : {self.im})",
               f"(marque : {self.ma})",
               f"(proprietaire : {self.pr})",
               f"(abonnement : {self.ab})")

voiture1 = Voiture(12, "BMW", "Jean", False)
voiture1.information()
parking = Parking()
parking.place()
parking.ajout_place(5, 80, voiture1)
parking.abonnement(voiture1)
voiture1.information()