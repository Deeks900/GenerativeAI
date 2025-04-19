from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int


newPerson : Person = {
    'name': 'Deeksha',
    'age' : 24
}

print(newPerson)