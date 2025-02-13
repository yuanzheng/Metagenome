from PySide6.QtWidgets import QApplication, QWidget
from mainwindow import MainWindow
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow(app)
    MainWindow.show()
    sys.exit(app.exec())



