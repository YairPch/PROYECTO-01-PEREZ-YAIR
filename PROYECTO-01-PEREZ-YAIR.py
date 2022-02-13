from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#Declaramos variables para el acceso al programa
acceso = False
total_intentos = 0

#El usuario es: yairp
#La contraseña es: emtech
while not acceso: #Preguntamos usuario y contraseña
  usuario = input("Ingresa tu usuario: ")
  contrasena = input("Ingresa tu contrasena: ")
  total_intentos += 1

  #Validar que los datos sean correctos
  if usuario == "yairp" and contrasena == "emtech": 
    acceso = True
    print()
    print("Bienvenido " + usuario)
  else:
    print("Te quedan ", 5 - total_intentos, " intentos restantes")
    if usuario == "yairp":
      print("La contraseña es incorrecta")
    else:
      print("El usuario es incorrecto")
  
  #Para cerrar el programa si los datos se ingresaron mal 5 veces
  if total_intentos == 5: 
    exit()

print()
print("¡Comencemos a programar!")
print()
print()
##Productos más vendidos y productos rezagados

# En este caso creamos la lista de id's de producto quitando los que fueron regresados
producto_vendido = []

for venta in lifestore_sales:
  if venta[4] == 0:
    producto_vendido.append(venta[1])
  else:
    continue

#print(producto_vendido)    
 
# Numero de veces que se vende cada producto por id_producto

frecuencia = {}
for producto in producto_vendido:
  if producto in frecuencia:
    frecuencia[producto] += 1
  else:
    frecuencia[producto] = 1

#print(frecuencia)
#Para imprimir cuántas veces se vendio cada uno por id
#for key in frecuencia.keys():
  #print("El producto con id:", key, "se vendio ", frecuencia[key], "vez/veces")

#Para hacer un sort con las 5 ventas más altas
sort_ventas = sorted(frecuencia.items(), key=lambda x:x[1],reverse=True)
#print(sort_ventas[:5])

#Lista con id_producto y nombres
nombre_product = [i[1][:30] for i in lifestore_products]
nombre_product_id = [[i[0],i[1][:30]] for i in lifestore_products]
#for producto in nombre_product:
  #print(producto)
print("Los 5 productos mas comprados fueron los siguientes")
for producto in sort_ventas[:5]:
  print("El producto:", nombre_product[producto[0]-1], " fue comprado ", producto[1], " veces")
print()
print()
print()
###########################################################################

busquedas = []
for buscado in lifestore_searches:
  busquedas.append(buscado[1])
#print(busquedas)  

#Para calcular la frecuencia de busqueda de cada producto
frecuencia2 = {}
for busqueda in busquedas:
  if busqueda in frecuencia2:
    frecuencia2[busqueda] += 1
  else:
    frecuencia2[busqueda] = 1
#print(frecuencia2)

#Para ordenarlas de mayor a menor cantidad de busquedas
sort_searches = sorted(frecuencia2.items(), key=lambda x:x[1],reverse=True)
#print(sort_searches)

#Imprimir el nombre de los 10 más buscados
print("Los 10 productos más buscados son los siguientes:")
for busqueda in sort_searches[:10]:
  print("El producto: ",nombre_product[busqueda[0]-1], " fue buscado: ",busqueda[1], " veces")
print()

#Productos menos buscados
sort_searches = sorted(frecuencia2.items(), key=lambda x:x[1],reverse=False)
print("Los 10 productos menos buscados son los siguientes:")
for busqueda in sort_searches[:15]:
  print("El producto: ",nombre_product[busqueda[0]-1], " fue buscado: ",busqueda[1], " veces")

print()
print()
print()
##########################################################################
#Por categoria, listado de los 50 productos con menores ventas

categorias = {}
for producto in lifestore_products:
  id_producto = producto[0]
  categ = producto[3]
  if categ not in categorias.keys():
    categorias[categ] = []
  categorias[categ].append(id_producto)

#Calculamos las ventas
lista_a = []
for key in categorias.keys():
  ids_categorias = categorias[key]
  ventas_tots = 0
  for id in ids_categorias:
    sale = lifestore_sales[id-1]
    ids = sale[1]
    precio = lifestore_products[ids-1][2]
    ventas_tots += precio
  lista_a.append(key)
  lista_a.append(ventas_tots)
  lista_a.append(len(ids_categorias))
  
print("Las 5 categorias con menor cantidad de ventas son las siguientes: ")
lista_a_limpia = [lista_a[i:i + 3] for i in range(0, len(lista_a), 3)]
sort_lista_a = sorted(lista_a_limpia, key=lambda x:x[2], reverse=False)
for k in sort_lista_a[:5]:
  print("Categoria: ", k[0], " con ", k[2], " ventas, con un valor de MXN: ", k[1])


print()
print()
print()



#########################################################################

#Mostrar dos listados de 5 productos, un listado para productos con las mejores reseñas y otro para las peores, considerando los productos con devolución, sin considerar los productos sin reseña

#Creamos un diccionario con los id
product_reviews = {}
for venta in lifestore_sales:
  id_prod = venta[1]
  review = venta[2]
  if id_prod not in product_reviews.keys():
    product_reviews[id_prod] = []
  product_reviews[id_prod].append(review)

#Creamos otros diccionario para agregar los reviews promedio
id_rev_prom = {}
for id, rev in product_reviews.items():
  #print(id,rev)
  rev_prom = sum(rev)/len(rev)
  rev_prom = int(rev_prom*100)/100
  id_rev_prom[id] = rev_prom

#Ordenada 
lista_ordenada = []
for id, rev_prom in id_rev_prom.items():
  sub=[id,rev_prom]
  lista_ordenada.append(sub)

sort_reviews = sorted(lista_ordenada, key=lambda x:x[1],reverse=True)

#Mejores resenas
print("Los productos con mejores reviews son los siguientes: ")
for sub in sort_reviews:
  if sub[1]==5:
    print(nombre_product[sub[0]-1], "con un review de: ", sub[1])  

#Peores resenas
sort_reviews2 = sorted(lista_ordenada, key=lambda x:x[1],reverse=False)

print()
print()
print()
print("Los productos con peores reviews son los siguientes: ")
for sub in sort_reviews2[:15]:
  print(nombre_product[sub[0]-1], "con un review de: ", sub[1]) 
print()
print()
print()
  #########################################################

  #Total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año

  #Separamos las ventas por mes
fecha = [[venta[0],venta[3]] for venta in lifestore_sales if venta[4] == 0]

meses = {}
for i in fecha:
  id = i[0]
  dia,mes,ano = i[1].split("/")
  if mes not in meses.keys():
    meses[mes] = []
  meses[mes].append(id)
lista1 = []
vtas_anuales = 0
print("El total de ingresos y ventas se comporto de la siguiente manera:")
for key in meses.keys():
  calendario = meses[key]
  total_vtas = 0 
  for id in calendario:
    venta = lifestore_sales[id-1]
    id_product = venta[1]
    price = lifestore_products[id_product-1][2]
    total_vtas += price
    vtas_anuales += price
  lista1.append(key)
  lista1.append(total_vtas)
  lista1.append(len(calendario))
  if key == "07":
    print("En julio las ventas fueron de: ", total_vtas, " con un total de: ", len(calendario), " ventas")
  elif key == "02":
    print("En febrero las ventas fueron de: ", total_vtas, " con un total de: ", len(calendario), " ventas")
  elif key == "05":
    print("En mayo las ventas fueron de: ", total_vtas, " con un total de: ", len(calendario), " ventas")
  elif key == "01":
    print("En enero las ventas fueron de: ", total_vtas, " con un total de: ", len(calendario), " ventas")
  elif key == "04":
    print("En abril las ventas fueron de: ", total_vtas, " con un total de: ", len(calendario), " ventas")
  elif key == "03":
    print("En marzo las ventas fueron de: ", total_vtas, " con un total de: ", len(calendario), " ventas")
  elif key == "06":
    print("En junio las ventas fueron de: ", total_vtas, " con un total de: ", len(calendario), " ventas")
  elif key == "08":
    print("En agosto las ventas fueron de: ", total_vtas, " con un total de: ", len(calendario), " ventas")


print()
print()
print("El total de ventas anuales fue igual a: ", vtas_anuales)
print()
print()

#print(lista1)
n = 3
lista_limpia = [lista1[i:i + n] for i in range(0, len(lista1), n)]

print("Los 5 meses con mayores ventas son los siguientes: ")
print()
sort_vtas = sorted(lista_limpia, key=lambda x:x[2],reverse=True)
for i in sort_vtas[:5]:
  if i[0] == "01":
    print("Enero generó ", i[2], " ventas, lo que monetariamente represento: ", i[1], " pesos")
  elif i[0] == "02":
    print("Febrero generó ", i[2], " ventas, lo que monetariamente represento: ", i[1], " pesos")
  elif i[0] == "03":
    print("Marzo generó ", i[2], " ventas, lo que monetariamente represento: ", i[1], " pesos")
  elif i[0] == "04":
    print("Abril generó ", i[2], " ventas, lo que monetariamente represento: ", i[1], " pesos")
  elif i[0] == "05":
    print("Mayo generó ", i[2], " ventas, lo que monetariamente represento: ", i[1], " pesos")
  elif i[0] == "06":
    print("Junio generó ", i[2], " ventas, lo que monetariamente represento: ", i[1], " pesos")
  elif i[0] == "07":
    print("Julio generó ", i[2], " ventas, lo que monetariamente represento: ", i[1], " pesos") 
  elif i[0] == "08":
    print("Agosto generó ", i[2], " ventas, lo que monetariamente represento: ", i[1], " pesos")
  elif i[0] == "09":
    print("Septiembre generó ", i[2], " ventas, lo que monetariamente represento: ", i[1], " pesos")
  elif i[0] == "10":
    print("Octubre generó ", i[2], " ventas, lo que monetariamente represento: ", i[1], " pesos")
  elif i[0] == "11":
    print("Noviembre generó ", i[2], " ventas, lo que monetariamente represento: ", i[1], " pesos")
  elif i[0] == "12":
    print("Diciembre generó ", i[2], " ventas, lo que monetariamente represento: ", i[1], " pesos")