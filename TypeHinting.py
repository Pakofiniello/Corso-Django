# # 1.Scrivi una funzione somma che prende due numeri interi e restituisce
# # la loro somma, specificando i type hints.
# # def somma(a: int, b: int) -> int:
# #     return a + b
# # print(somma(9,10))

# # 2. Scrivi una funzione greeting che prende come parametro una
# # stringa nome opzionale. Se il nome è fornito, restituisci “Ciao, !”,
# # altrimenti restituisci “Ciao, ospite!”. Usa Optional.
# # from typing import Optional
# # def greeting(nome: Optional[str]) -> str:
# #     if nome:
# #         return f"Ciao, {nome}!"
# #     else:
# #         return "Ciao, ospite!"
    
# # print(greeting("Pasquale"))

# # 3. Union
# # Scrivi una funzione to_string che accetta un int o un float e
# # restituisce una stringa con scritto “Il valore è ”. Usa Union.
# # from typing import Union
# # def to_string(val: Union[int,float]) -> str:
# #     return f"Il valore è {val}"
# # print(to_string(5))

# # # 4. Scrivi una funzione applica_due_volte che accetta un numero
# # # intero e una funzione come parametri. La funzione deve applicare
# # # due volte la funzione passata e restituire il risultato. Usa Callable.
# # from typing import Callable
# # def somma(x: int, y: int) -> int:
# #     return x + y
# # def applica_due_volte(n: int, n2: int, f: Callable[[int,int],int]) -> int:
# #     return f(f(n,n2),f(n,n2))
# # print("Risultato: ",applica_due_volte(2,3,somma))


# # # 5. Crea una funzione scambia che prende in input due valori dello
# # # stesso tipo e restituisce i valori scambiati. Usa TypeVar.
# # from typing import List, TypeVar
# # T = TypeVar('T')
# # def scambia(a: T, b: T) -> List[T]:
# #     return [b,a]
# # print(scambia(5,10))
# # print(scambia("Django","Corso"))


# # # 6. Type con classi
# # # Definisci una funzione crea_animale che accetta una classe
# # # Animale o sottoclasse e restituisce un’istanza di essa. Usa Type.
# # from typing import Type
# # class Animale:
# #     def verso(self) -> str:
# #         return "Verso generico"
# # class Azir(Animale):
# #     def verso(self) -> str:
# #         return "Shurima! Your emperor has returned!"
# # def crea_animale(cls: Type[Animale]) -> Animale:
# #     return cls()
# # animale = crea_animale(Azir)
# # print(animale.verso())


# 7.Classe generica
# Crea una classe Box generica che può contenere un valore di
# qualsiasi tipo, con un metodo get_valore che lo restituisce. Usa
# Generic e TypeVar
# from typing import Generic, TypeVar
# T = TypeVar('T')
# class Box(Generic[T]):
#     def __init__(self, valore: T) -> None:
#         self.valore = valore

#     def get_valore(self) -> T:
#         return self.valore
# box_int = Box[int](123)
# box_str = Box[str]("Ciao mondo")
# print(box_int.get_valore())  # Output: 123
# print(box_str.get_valore())  # Output: Ciao mondo

# Challenge
# Scrivi una funzione media che accetta una lista di numeri (int o
# float) e restituisce la media aritmetica. Usa Union o un TypeVar
# vincolato a int e float.

from typing import List, Union
def media(L: List[Union[int,float]]) -> float:
    return sum(L) /len(L)

print(media([1,2,3,4,5]))
print(media([1.5,2.5,3.5]))

