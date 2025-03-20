#Estructura de datos

products_structure = {
  "Computador":{
    "Procesador":{
      "Chip": 150,
      "Refrigeracion": 30
    },
    "Memoria RAM":{
      "Módulo DRAM": 70,
      "PCB": 20
    },
    "Disco Duro":{
      "Platos magnéticos": 100,
      "Cabezal de lectura": 50
    },
    "Carcasa":{
      "Chasis": 50,
      "Fuente de alimentación": 80
    }
  },
  "Celular":{
    "Procesador":{
      "Chip": 50,
      "Refrigeracion": 30
    },
    "Memoria RAM":{
      "Módulo DRAM": 70,
      "PCB": 20
    },
    "Disco Duro":{
      "Platos magnéticos": 100,
      "Cabezal de lectura": 50
    },
    "Carcasa":{
      "Chasis": 50,
      "Fuente de alimentación": 80
    }
  }
}

def calculate_total_cost(product):
  #If it is a number, returns its cost
  if isinstance(product, (int, float)):
    return product
  
  #If it is a dictionary, we sum recursively the cost of its elements
  total_cost = 0  
  for element in product:
    total_cost += calculate_total_cost(product[element])
    
  return total_cost 

computer_cost = calculate_total_cost(products_structure["Computador"])
celphone_cost = calculate_total_cost(products_structure["Celular"])

print(f"El costo total del computador es: {computer_cost}")
print(f"El costo total del celular es: {celphone_cost}")
