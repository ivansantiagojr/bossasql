import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel('Hello, World!', alignment=Qt.AlignmentFlag.AlignCenter)
label.show()
sys.exit(app.exec())
