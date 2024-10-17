from PyQt5.QtWidgets import QApplication
import sys

from main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow(app.primaryScreen().size())
    main_window.showMaximized()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
