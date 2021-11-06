from client import Client
from facade import DietKeto

client = Client()
keto = DietKeto()

client.diet = keto

client.eatBreakfast()

print(client.balance)