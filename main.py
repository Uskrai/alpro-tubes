from gui.controller import ControllerGUI
import modulfactory


def main():
    controller = ControllerGUI()
    controller.start( modulfactory.get_all_modul() )

    exit()

main()
