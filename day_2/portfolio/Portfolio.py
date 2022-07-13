class Portfolio:
  def __init__(self, nombre):
    self._name = nombre
    self._pices = []


  def agregarObra(self, obra):
    self._pices.append(obra)


  def getItemAt(self, index):
    return self._pices[index]


  def listInfo(self):
    print('Portafolio: {}'.format(self._name))

    if len(self._pices):
      print('Obras:')
      for idx, obra in enumerate(self._pices):
        print('    Obra No. {}'.format(idx + 1))
        obra.showInfo()
