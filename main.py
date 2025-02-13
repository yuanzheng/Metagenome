from PySide6.QtWidgets import QApplication, QWidget
from logging_config import setup_logger
from mainwindow import MainWindow
import sys

# Call the log configuration at program startup
setup_logger()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow(app)
    MainWindow.show()
    sys.exit(app.exec())



