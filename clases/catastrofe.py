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


