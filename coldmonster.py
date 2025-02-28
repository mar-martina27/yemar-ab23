class Monster():
    def __init__(self, name:str,color:str,eye:int,limbs:int):
        self.name = name
        self.color = color
        self.eye = eye
        self.limbs = limbs
    def roar(self):
        print(f"{self.name} lets out a terrifying roar!")

class IceMonster(Monster):
    def __init__(self, name, color, eyes, limbs, ice_power:str):
        super().__init__(name, color, eyes, limbs)
        self.ice_power = ice_power
    def ice_fart(self):
        print(f'{self.name} uses {self.ice_power} to make the land ice')
    def throwing_ice_blocks_from_nose(self):
        print(f'{self.name} throws a  {self.ice_power} and fight')
    def cold_air(self):
        print(f'{self.name} breath {self.ice_power} and bring hurricane!')
    def roar(self):
        print("WOOOOFFFFF!!! I AM COLD MOSTER")


marya=ClodMonster("Antartica Mon", "Light Blue", 2, 6, "Ice blocks")
marya.ice_fart()
