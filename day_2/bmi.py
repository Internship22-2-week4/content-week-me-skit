def bmi(peso, altura):
  indice = peso / altura**2

  if indice >= 30:
    return "Obeso"
  elif 25 <= indice <= 29.9:
    return "Sobrepeso"
  elif 18.5 <= indice <= 24.9:
    return "Normal"
  else:
    return "Bajo de peso"


if __name__ == '__main__':
    print(bmi(65, 1.8)) # "Normal"
    print(bmi(72, 1.6)) # "Sobrepeso"
    print(bmi(52, 1.75)) #  "Bajo de peso"
    print(bmi(135, 1.7)) # "Obeso"