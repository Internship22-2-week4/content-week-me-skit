from mailbox import NoSuchMailboxError


class Author:

  def __init__(self, nombre, fecha_nacimiento):
    self._name = nombre
    self._birthdate = fecha_nacimiento

  
  def getName(self):
    return self._name