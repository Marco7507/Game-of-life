from life_game_controller import LifeGameController

def main():
    game = LifeGameController(64, 64, cell_size=10)
    game.start()

if __name__ == "__main__":
    main()
