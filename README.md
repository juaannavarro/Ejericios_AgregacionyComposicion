# Ejericios_AgregacionyComposicion

## Repositorio:
Este es el link de mi repositorio: https://github.com/juaannavarro/Ejericios_AgregacionyComposicion


## Tarea:

Esta tarea individual ha constado de 3 ejercicios. En el primero y tercero tenías que seguir las pautas del enunciado y en el 2 corregir el fallo que te pedían.

## Ejercicio 1:

```

class catastrofe():
  def __init__(self, edificio, empleado, ciudad):
    self.edificio = edificio
    self.empleado = empleado
    self.ciudad = ciudad






class AlDiaSiguiente():
      def ciudades(new_york, los_angeles):
          

            while True:
                  print("CREA TU PELÍCULA: ")
                  print("1.  Quieres destruir Nueva York ")
                  print("2.  Quieres destruir Los Ángeles ")
                  print("3. No quieres destruir nada")
                  print()
                  eleccion=int(input("Elige una opción: "))
                  break
            if eleccion == 1:
                  print("-Se ha destruido Nueva York ")
                  print("-Se han destruido los edificios A y B ")
                  print("-Se ha destruido la empresa YooHoo! ")
                  print("-Fin ")
            elif eleccion == 2:
              print("-Se ha destruido Los Ángeles ")
              print("-Se ha destruido el edificio C ")
              print("-Se ha destruido la empresa YooHoo! ")
              print("-Fin ")
            else:
                  print("Vuelve a elegir")
                  return
        
        
        
          

print(AlDiaSiguiente.ciudades("new_york " , "los_angeles"))


```

UML:

<img width="259" alt="Captura de pantalla 2022-03-22 a las 17 41 19" src="https://user-images.githubusercontent.com/91721668/159532439-b6d8abaf-26a8-4d40-b601-21bc8401b0ec.png">




## Ejercicio 2:

```

class Yin: pass 
class Yang: 
        def __del__(self): 
            print("Yang destruido") 
 
yin = Yin() 
yang = Yang() 
yin.yang = yang 
 
print(yang) 
print(yang is yin.yang) 
Yang.__del__(yang) 
print("?") 

#Solución: El del hace que el print al que está asociado tenga mayor importancia. Eso hacía que el (yang)que tenia detrás pertenezca a la clase Yang directamente. Poniendo la clase Yang delante hacemos que la interrogación se introduzca en la clase y no se ponga como opción principal.

``` 

UML:


<img width="418" alt="Captura de pantalla 2022-03-22 a las 17 42 59" src="https://user-images.githubusercontent.com/91721668/159532488-7352784e-b74e-4037-9370-49d587e227be.png">




## Ejercicio 3:

``` 

class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        self.ventanas = []

class Ventana:
    def __init__(self, pared, superficie, proteccion):
        self.pared = pared
        self.superficie = superficie
        self.pared.ventanas.append(self)
        if proteccion is None:
            raise Exception("Protección obligatoria")
        self.proteccion = proteccion

class Casa:
    def __init__(self, paredes):
        self.paredes = paredes

    def superficie_cristal(self):
        superficie = 0
        for pared in self.paredes:
            for ventana in pared.ventanas:
                superficie += ventana.superficie
        return superficie

pared_norte = Pared("NORTE")
pared_oeste = Pared("OESTEE")
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")
ventana_norte = Ventana(pared_norte, 0.5, "persiana")
ventana_oeste = Ventana(pared_oeste, 1, "persiana")
ventana_sur = Ventana(pared_sur, 2, "store vénitien")
ventana_este = Ventana(pared_este, 1, "persiana")
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
print(casa.superficie_cristal())

class ParedCortina(Pared, Ventana):
    def __init__(self, orientacion, superficie):
        Pared.__init__(self, orientacion)
        Ventana.__init__(self, self, superficie, "Ninguna")

pared_cortina = ParedCortina("SUR", 10)
casa.paredes[2] = pared_cortina
print(casa.superficie_cristal())

```
  
UML:


<img width="495" alt="Captura de pantalla 2022-03-22 a las 17 48 30" src="https://user-images.githubusercontent.com/91721668/159532289-d67949a4-ecb0-4d0c-b0c3-a7440ea53f16.png">
