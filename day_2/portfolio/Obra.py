class Obra:

  def __init__(self, nombre, tipo, fecha, valor_estimado):
    self._name = nombre
    self._type = tipo
    self._creation_date = fecha
    self._stimated_value = valor_estimado
    self._authors = []
    self._multimedia = []  


  def addAuthor(self, str):
    self._authors.append(str)

  
  def addMultimedia(self, media):
    self._multimedia.append(media)


  def showInfo(self):
    print('    Nombre: {}\n    Tipo: {}\n    Fecha: {}\n    Valor estimado: {}'.format(self._name, self._type, self._creation_date, self._stimated_value))
    self.showAutors()
    self.showMultimedia()
    print('    {}'.format('-' * 30))


  def showAutors(self):

    if len(self._authors):
      autores = []
      for author in self._authors:
        autores.append(author.getName())

      print('    Autore(s): {}'.format(', '.join(autores)))


  def showMultimedia(self):

    if len(self._multimedia):
      print('    Fotos y Vídeos: ')
      for medio in self._multimedia:
        print('\t{}'.format('-' * 22))
        print('\tTipo: {}'.format(medio.type))
        print('\tFecha: {}'.format(medio.date))
