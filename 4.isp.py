"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC, abstractmethod

class IJanela(ABC):
        
    @abstractmethod
    def fechar(self):
        raise NotImplementedError

class IJanelaTamanhoFixo(IJanela):
    
    @abstractmethod
    def mostrar_menu(self):
        raise NotImplementedError

class IJanelaSemMenu(IJanela):

    @abstractmethod
    def maximizar(self):
        raise NotImplementedError
    
    @abstractmethod
    def minimizar(self):
        raise NotImplementedError

class JanelaTamanhoFixo(IJanelaTamanhoFixo):
    
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass

class JanelaSemMenu(IJanelaSemMenu):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def fechar(self):
        pass
