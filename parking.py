class Parking:

    def __init__(self):
        pass

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
    
voiture1 = Voiture(12, "BMW", "Jean", True)
voiture1.information()