#Definimos la clase Animal
class Animal:
   cont = 0

   def __init__(self, especie, edadMedia, enfComunes, pesoMedio, dietaMedia, habitat):
       self.especie = especie
       self.edadMedia = edadMedia
       self.enfComunes = enfComunes
       self.pesoMedio = pesoMedio
       self.dietaMedia = dietaMedia
       self.habitat = habitat


class animalAnfibios(Animal):
   def __init__(self, especie, edadMedia, enfComunes, pesoMedio, dietaMedia, habitat, huevos):
       super().__init__(especie, edadMedia, enfComunes, pesoMedio, dietaMedia, habitat)
       self.numeroHuevos = huevos

#super() trabaja igual que Animal.


class animalReptiles(Animal):
   def __init__(self, especie, edadMedia, enfComunes, pesoMedio, dietaMedia, habitat, escamas):
       super().__init__(especie, edadMedia, enfComunes, pesoMedio, dietaMedia, habitat)
       self.escamas = escamas
