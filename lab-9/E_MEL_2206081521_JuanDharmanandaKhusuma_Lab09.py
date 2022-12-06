from random import randint


class Entity:
    # TODO: Lengkapi constructor
    #       Perhatikan access modifiernya!
    def __init__(self, name, hp, atk):
        self.__name = name
        self.__hp = hp
        self.__atk = atk

    # TODO Lengkapi getter dan setter
    def get_name(self):
        return self.__name

    def get_atk(self):
        return self.__atk

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_hp):
        self.__hp = new_hp

    # TODO: Lengkapi method-method dibawah ini
    def attack(self, other):
        other.take_damage(self.get_atk())

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage)

    def is_alive(self):
        return self.get_hp() > 0

    def __str__(self):
        # Akan digunakan untuk print nama
        return f"{self.__name}"


class Player(Entity):
    # TODO: Lengkapi constructor
    #       Perhatikan access modifiernya!
    def __init__(self, name, hp, atk, defense):
        self.__defense = defense
        super().__init__(name, hp, atk)

    # TODO: Lengkapi getter
    def get_defense(self):
        return self.__defense

    # TODO: Lengkapi agar damage yang diterima dikurangi oleh DEF
    def take_damage(self, damage):
        if damage - self.get_defense() > 0:
            self.set_hp(self.get_hp() - damage + self.get_defense())


class Boss(Entity):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)

    # TODO: Lengkapi agar damage yang diterima Depram tidak dipengaruhi
    #       oleh DEF
    def attack(self, other):
        other.take_damage(self.get_atk())


def main():
    # TODO: Meminta ATK dan DEF Depram
    atk = int(input("Masukkan ATK Depram: "))
    defense = int(input("Masukkan DEF Depram: "))

    # Inisialisasi Depram dan musuh-musuh
    depram = Player("Depram", 100, atk, defense)
    enemies = [
        Entity(f"Enemy {i}", randint(20, 100), randint(10, 30))
        for i in range(randint(0, 1))
    ]
    enemies.append(Boss("Ohio Final Boss", randint(20, 100), randint(10, 30)))

    print(f"Terdapat {len(enemies)} yang menghadang Depram!")
    print("------------")

    for enemy in enemies:
        print(f"{enemy} muncul!")
        print()
        print("---Status---")
        print(f"{enemy.get_name():20} HP: {enemy.get_hp()}")
        print(f"{depram.get_name():20} HP: {depram.get_hp()}")
        print("------------")
        while enemy.is_alive() and depram.is_alive():
            # TODO: Depram dan musuh melakukan attack dan print:
            #       Depram menyerang: "Depram menyerang {enemy} dengan {damage} ATK!"
            #       Musuh  menyerang: "{enemy} menyerang Depram dengan {damage} ATK!"
            print(
                f"{depram} menyerang: {enemy} dengan damage {depram.get_atk()} ATK!")
            depram.attack(enemy)
            if not enemy.is_alive():
                break
            print(
                f"{enemy} menyerang: {depram} dengan {enemy.get_atk()} ATK")
            enemy.attack(depram)

        if not depram.is_alive():
            print("------------")
            print()
            print("Tidak! Depram telah dikalahkan oleh musuhnya :(")
            return
        else:
            print(f"{enemy} telah kalah!")

        print("------------")
        print()

    print("Selamat! Semua musuh Depram telah kalah!")


if __name__ == "__main__":
    main()
