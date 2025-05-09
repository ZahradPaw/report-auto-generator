from PyQt6.QtWidgets import QApplication
import sys
from mainwindow import MainWindow


def main():
    """Основная функция приложения"""
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
