class Exposicion:
  def __init__(self, fecha, lugar, descripcion):
    self._date = fecha
    self._place = lugar
    self._description = descripcion
    self._pices = []


  def agregarObra(self, obra):
    self._pices.append(obra)


  def info(self):
    print('EXPOSICIÓN')
    print('==========')
    print('Fecha: {}\nLugar: {}\nDescripcion: {}'.format(self._date, self._place, self._description))

    if len(self._pices):
      print('Obras:')
      for obra in self._pices:
        obra.showInfo()
