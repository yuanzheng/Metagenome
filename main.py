from PySide6.QtWidgets import QApplication
from utils.logging_config import setup_logger
from gui.mainwindow import MainWindow
import sys

# Call the log configuration at program startup
setup_logger()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())



