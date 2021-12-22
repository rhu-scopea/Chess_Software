from controllers.base import Controller
from views.base_view import View


def main():
    print("Running")

    view = View()

    game = Controller(view)
    game.run()


if __name__ == '__main__':
    main()
