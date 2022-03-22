class catastrofe():

  def __init__(self, edificio, empleado, ciudad):
    self.edificio = edificio
    self.empleado = empleado
    self.ciudad = ciudad
  def catastrofe_ocurrida(self):
        catastrofes = ("{1}, {2}, {3}")
        return catastrofes.format(self.edificio, self.empleado, self.ciudad)

class AlDiaSiguiente():
      def ciudades(new_york, los_angeles):
            while True:
                  print("Menú")
                  print("1. Qué edificio quieres destruir")
                  print("2. Qué empleado quieres destruir")
                  print("3. Qué ciudad quieres destruir")
                  print()
                  eleccion=int(input("Elige una opción: "))
                  break
            if eleccion == 1:
                      print("Destruir A, B o C")


          
print(AlDiaSiguiente.ciudades("new_york " , "los_angeles"))
            

      

