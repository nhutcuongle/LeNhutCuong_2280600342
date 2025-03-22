import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)   
        self.ui.btn_Encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_Decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.txt_PlainText.toPlainText(),
            "key": self.ui.txt_Key.text()
        }
        
        try:
            response = requests.post(url, json=payload)
            data = response.json()
            print("API Response:", data)  # Debug response từ API
            
            encrypted_text = data.get("encrypted_message", "Error: No data received")
            self.ui.txt_cipherText.setPlainText(encrypted_text)
            QMessageBox.information(self, "Success", "Encrypted Successfully")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request Error: {str(e)}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipherText.toPlainText(),
            "key": self.ui.txt_Key.text()
        }
        
        try:
            response = requests.post(url, json=payload)
            data = response.json()
            print("API Response:", data)  # Debug response từ API
            
            decrypted_text = data.get("decrypted_message", "Error: No data received")
            self.ui.txt_PlainText.setPlainText(decrypted_text)
            QMessageBox.information(self, "Success", "Decrypted Successfully")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
