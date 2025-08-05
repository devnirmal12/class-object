a = {
    'Maharashtra':['Mumbai','Pune'],
    "Gujarat":"Surat"
}

class City:
    def __init__(self,a):
        self.a = a

    def search(self, city):
        for state, cities in self.a.items():
            if city in cities:
                return f"{city} is in {state}"
        return "not present"

c = City(a)

while(1):
    city = input("Enter city: ")
    if city.lower() == 'exit':
        break
    print(c.search(city))

