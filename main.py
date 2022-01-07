from controllers.base_controller import Controller
from views.base_view import View


def main():
    print("Running")

    game = Controller()
    game.run()

    print("Finished")

if __name__ == '__main__':
    main()
