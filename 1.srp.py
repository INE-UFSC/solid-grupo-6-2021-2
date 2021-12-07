"""
Single Responsibility Principle

Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name

class DataBase:
    def __init__(self):
        self.db = []

    def save(self, animal: Animal):
        self.db.append(animal)
