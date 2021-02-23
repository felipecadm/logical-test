

# 1) Implemente um método que crie um novo array baseado nos valores passados.
# Entradas do método (3,a), Resultado do método: ['a', 'a', 'a']

# def multiply(xTimes, item):
#     newArray = []
#     for i in range(xTimes):
#         newArray.append(item)
#     return newArray

# print(multiply(3,'a'))

# 2) Implemente um método que inverta um array, não utilize métodos nativos do array.
# Entrada do método ([1,2,3,4]), Resultado do método: [4,3,2,1]

#  def revert(arr):
#      newArray = []
#      for x in range(len(arr), 0, -1):
#          newArray.append(x)
#      return newArray
    
#  print(revert([1,2,3, 4]))

# 3) Implemente um método que limpe os itens desnecessários de um array (false, undefined, strings vazias, zero, null).
# Entrada do método ([1,2,'', undefined]), Resultado do método: [1,2]

#  def filter(arr):
#      newArray = []
#      for x in arr:
#          if isinstance(x, int):
#              newArray.append(x)
#      return newArray

#  undefined = None
#  print(filter([1,2,'', undefined]))

# 4) Implemente um método que a partir de um array de arrays, converta em um objeto com chave e valor.
# Entrada do método ([["c",2],["d",4]]), Resultado do métdodo: {c:2, d:4}

#  def array2Key(arr):
#      newObject = {}
#      for arrays in  arr:
#          newObject[arrays[0]]=arrays[1]
#      return newObject

#  print(array2Key([["c",2],["d",4]]))

# 5) Implemente um método que retorne um array, sem os itens passados por parâmetro depois do array de entrada. Entrada do método ([5,4,3,2,5], 5,3), Resultado do método: [4,2]

#  def noItems(arr, one, two):
#      newArray = []
#      for itens in arr:
#          if itens!=one and itens!=two:
#              newArray.append(itens)
#      return newArray

#  print(noItems([5,4,3,2,5], 5,3))

# 6) Implemente um método que retorne um array, sem valores duplicados.
# Entrada do método ([1,2,3,3,2,4,5,4,7,3]), Resultado do método: [1,2,3,4,5,7]

#  def noRepeat(arr):
#      newArray = []
#      for item in arr:
#          if item not in newArray:
#              newArray.append(item)
#      return newArray

#  print(noRepeat([1,2,3,3,2,4,5,4,7,3]))

# 7) Implemente um método que compare a igualdade de dois arrays e retorne um valor booleano.
# Entrada do método ([1,2,3,4],[1,2,3,4]), Resultado do método: true

#  def similar(arr1, arr2):
#      if arr1==arr2:
#          return True
#      else:
#          return False

#  print(similar([1,2,3,4],[1,2,3,4]))

# 8) Implemente um método que remova os aninhamentos de um array de arrays para um array unico.
# Entrada do método ([1, 2, [3], [4, 5]]), Resultado do método: [1, 2, 3, 4, 5]

#  def removeItens(arr):
#      newArray = []
#      for item in arr:
#          if isinstance(item, list):
#              for x in item:
#                  newArray.append(x)
#          else:
#              newArray.append(item)
#      return newArray

#  print(removeItens([1, 2, [3], [4, 5]]))

# 9) Implemente um método divida um array por uma quantidade passada por parâmetro.
# Entrada do método ([1, 2, 3, 4, 5], 2), Resultado do método: [[1, 2], [3, 4], [5]]

# def splitArray(arr, xTimes):
#      newArray = []
#      aux = []
#      for item in arr:
#          if len(aux)<xTimes:
#              aux.append(item)
#          else:
#              newArray.append(aux[:]) #python refers as a pointer, so a copy is needed
#                
#      return newArray

# print(splitArray([1, 2, 3, 4, 5], 2))
        
# 10) Implemente um método que encontre os valores comuns entre dois arrays.
# Entrada do método ([6, 8], [8, 9]), Resultado do método: [8]

#  def common(arr1, arr2):
#      newArray = []
#      for item in arr1:
#         for this in arr2:
#             if item==this:
#                 newArray.append(item)
#      return newArray

#  print(common([6, 8], [8, 9]))