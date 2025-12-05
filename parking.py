class Parking:

    def __init__(self):
        self.niv = 1
        self.place_niv1 = {}
        self.place_niv2 = {}
        self.place_niv3 = {}
        self.place_niv4 = {}
        self.place_niv5 = {}

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
        else:
            print("vous êtes déjà abonné")
    
    def desabonner(self, voiture):
        if voiture.ab == True:
                a = str(input("voulez-vous vous désabonner ? : "))
                if a == "oui" or a == "Oui":
                    voiture.ab = False

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

    def information(self):
        return (f"(immatriculation : {self.im})",
               f"(marque : {self.ma})",
               f"(proprietaire : {self.pr})",
               f"(abonnement : {self.ab})")

voiture1 = Voiture(12, "BMW", "Jean", False)
print(voiture1.information())
parking = Parking()
parking.place()
parking.abonnement(voiture1)
parking.ajout_place(1, 50, voiture1)
print(voiture1.information())
parking.si_voiture(1, 50)