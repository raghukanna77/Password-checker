import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QProgressBar
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

def get_strength_score(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    return score

class PasswordStrengthChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Strength Checker - PyQt5")
        self.setGeometry(200, 200, 400, 200)
        
        layout = QVBoxLayout()

        self.label = QLabel("Enter Password:")
        self.label.setFont(QFont("Arial", 12))
        layout.addWidget(self.label)

        self.entry = QLineEdit()
        self.entry.setEchoMode(QLineEdit.Password)
        self.entry.textChanged.connect(self.update_strength)
        layout.addWidget(self.entry)

        self.progress = QProgressBar()
        self.progress.setRange(0, 5)
        layout.addWidget(self.progress)

        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Arial", 12))
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def update_strength(self):
        password = self.entry.text()
        score = get_strength_score(password)
        self.progress.setValue(score)

        if score == 0:
            self.result_label.setText("❗ Please enter a password")
            self.result_label.setStyleSheet("color: orange;")
        elif score <= 2:
            self.result_label.setText("❌ Weak Password")
            self.result_label.setStyleSheet("color: red;")
        elif score <= 4:
            self.result_label.setText("⚠️ Medium Password")
            self.result_label.setStyleSheet("color: blue;")
        else:
            self.result_label.setText("✅ Strong Password 💪")
            self.result_label.setStyleSheet("color: green;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordStrengthChecker()
    window.show()
    sys.exit(app.exec_())
