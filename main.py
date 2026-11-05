
from character import Character

def main():
    hero = Character("Knight", 30, 5)

    enemy1 = Character("Goblin", 20, 3)
    enemy2 = Character("Orc", 25, 4)

    enemies = [enemy1, enemy2]

    print(hero)
    for enemy in enemies:
        print(enemy)
    print()

    while hero.is_alive() and any(enemy.is_alive() for enemy in enemies):

        for enemy in enemies:
            if enemy.is_alive():
                hero.attack(enemy)

                if enemy.is_alive():
                    enemy.attack(hero)

                print(hero)
                print(enemy)
                print()

                if not hero.is_alive():
                    break

    print("Battle over!")

    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print("Enemies win!")

if __name__ == "__main__":
    main()
