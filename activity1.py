class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def introduce(self):
        return f"I am {self.name} from the {self.universe} universe! 💥"

    def use_power(self):
        return f"{self.name} uses {self.power}! 🔥"

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, universe, flight_speed):
        super().__init__(name, power, universe)
        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self.name} flies at {self.flight_speed} km/h and uses {self.power}! 🕊️"


hero1 = Superhero("ShadowBlade", "Invisibility", "Darkverse")
hero2 = FlyingSuperhero("SkyStorm", "Thunder Strike", "Skyworld", 500)

print(hero1.introduce())
print(hero1.use_power())
print(hero2.introduce())
print(hero2.use_power())
