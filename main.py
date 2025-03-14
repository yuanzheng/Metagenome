import sys

from PySide6.QtWidgets import QApplication

from gui.mainwindow import MainWindow
from utils.logging.logging_config import setup_logger

# Call the log configuration at program startup
setup_logger()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
