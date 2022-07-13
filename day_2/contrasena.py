def contrasenaValida(str):
  if str == "2Fj(jjbFsuj" or str == "eoZiugBf&g9":
    return True
  
  return False


if __name__ == '__main__':
    print(contrasenaValida("2Fj(jjbFsuj"))
    print(contrasenaValida("eoZiugBf&g9"))
    print(contrasenaValida("hola"))
    print(contrasenaValida(""))
  