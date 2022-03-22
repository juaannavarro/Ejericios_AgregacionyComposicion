class catastrofe():
  def __init__(self, empresa, empleado, ciudad):
    self.empresa = empresa
    self.empleado = empleado
    self.ciudad = ciudad
  def catastrofe_ocurrida(self):
        catastrofes = ("{1}, {2}, {3}")
        return catastrofes.format(self.empresa,self.empleado, self.ciudad)
    