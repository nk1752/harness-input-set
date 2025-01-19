def basic():

  person: dict = {}
  person = {"name": "Alice", "age": 25}
  print(person) # {'name': 'Alice', 'age': 25}
  
  new_person = {"name": "Nadeem", "age": 58}
  person.update(new_person)  # Adds 'city' and updates 'age'
  print(person)  # {'name': 'Nadeem', 'age': 58}
 

if __name__ == "__main__":
    basic()