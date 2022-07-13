def likes(n_likes):
  if n_likes >= 1000000:
    return str(n_likes // 1000000) + "M"
  elif n_likes >= 1000:
    return str(n_likes // 1000) + "K"
  
  return n_likes


if __name__ == '__main__':
  print(likes(983)) # "983"
  print(likes(1900)) # "1K"
  print(likes(54000)) # "54K"
  print(likes(120800)) # "120K"
  print(likes(25222444)) # "25M"