from Portfolio import Portfolio
from Obra import Obra
from Author import Author
from Multimedia import Multimedia
from Exposicion import Exposicion

if __name__ == '__main__':
  portafolio = Portfolio('Mi portafolio')

  obra1 = Obra('Puesta de Sol', 'Pintura', '20/12/2021', '$ 3,500.00')
  obra1.addAuthor(Author('Jhon Doe', '01/10/1999'))
  obra1.addAuthor(Author('Chris Doe', '01/10/2003'))
  obra1.addMultimedia(Multimedia('Video', '25/12/2021'))
  obra1.addMultimedia(Multimedia('Video', '26/12/2021'))

  obra2 = Obra('Naturaleza', 'Video', '11/01/2022', '$ 900.00')
  obra2.addAuthor(Author('Mary Jane', '21/12/1990'))
  obra2.addMultimedia(Multimedia('Foto', '20/01/2022'))

  obra3 = Obra('Cupido', 'Escultura', '10/10/2019', '$ 5,000.00')
  obra3.addAuthor(Author('Carlos D.', '02/09/1995'))
  obra3.addMultimedia(Multimedia('foto', '10/10/2019'))

  obra4 = Obra('Angeles', 'Escultura', '02/11/2020', '$ 5,500.00')
  obra4.addAuthor(Author('Abner Malin', '22/12/1985'))
  obra4.addAuthor(Author('Alejandro López', '19/11/1980'))
  obra4.addAuthor(Author('Anna Vásquez', '01/03/1999'))
  obra4.addMultimedia(Multimedia('Video', '02/11/2020'))
  obra4.addMultimedia(Multimedia('Foto', '02/11/2020'))

  portafolio.agregarObra(obra1)
  portafolio.agregarObra(obra2)
  portafolio.agregarObra(obra3)
  portafolio.agregarObra(obra4)

  portafolio.listInfo()

  expo = Exposicion('16/07/2022', 'Parque Iguazul', 'Exposición de arte')
  expo.agregarObra(portafolio.getItemAt(0))
  expo.agregarObra(portafolio.getItemAt(2))
  expo.agregarObra(portafolio.getItemAt(3))
  expo.info()
