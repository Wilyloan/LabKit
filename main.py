import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox, QTableWidgetItem, QPushButton
from mainwindow import Ui_MainWindow
from generatepassword import Ui_MainWindow as GenerateWindowPs
from setinfo import Ui_MainWindow as ui_setinfo
from deleteinfo import Ui_MainWindow as ui_deleteinfo
from calc import Ui_MainWindow as ui_calc
import buttons
import password
import CreateJson


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.GenerateWindow1 = GenerateWindow(self)
        self.ui.btn_gen_password.clicked.connect(self.openSecond)

        self.ui_setinfo1 = SetInfo(self)
        self.ui.btn_add.clicked.connect(self.openSetInfo)

        self.ui_delete = DBWindow(self)
        self.ui.btn_passwords.clicked.connect(self.openPasswords)

        self.ui_calc1 = CalcWindow(self)
        self.ui.btn_calc.clicked.connect(self.openCalc)

        

    def openSecond(self):
        self.GenerateWindow1.show()
        self.hide()

    def openSetInfo(self):
        self.ui_setinfo1.show()

    def openPasswords(self):
        self.ui_delete.refresh()
        self.ui_delete.show()
        self.hide()

    def openCalc(self):
        self.ui_calc1.show()
        
# Окно добавления информации
class SetInfo(QMainWindow):
    def __init__(self, main_window2):
        super().__init__()
        self.ui = ui_setinfo()
        self.ui.setupUi(self)
        self.main_window2 = main_window2
        self.ui.btn_save.clicked.connect(self.save_and_back)
        self.ui.btn_back.clicked.connect(self.goBack2)

    def goBack2(self):
        self.ui.input_site.clear()
        self.ui.input_login.clear()
        self.ui.input_password.clear()

        self.hide()
        
    def save_and_back(self):
        site = self.ui.input_site.text()
        login = self.ui.input_login.text()
        password = self.ui.input_password.text()

        CreateJson.set_password(site, login, password)
# Сюда добавить сохранение и отправку информации в json
        self.ui.input_site.clear()
        self.ui.input_login.clear()
        self.ui.input_password.clear()

        self.hide()
        self.main_window2.show()
    
# Окно удаления информации
class DBWindow(QMainWindow):
    def __init__(self, mainwindow3):
        super().__init__()
        self.ui = ui_deleteinfo()
        self.ui.setupUi(self)
        self.mainwindow3 = mainwindow3
        self.ui.btn_back.clicked.connect(self.goBack3)
        
        self.ui.btn_delete.clicked.connect(self.delete_selected)
        self.ui.btn_add.clicked.connect(self.add_info)

    def refresh(self) -> None:
        self.loadJson = CreateJson.load_json()
        self.fill_table()

    def fill_table(self) -> None:
        self.ui.tableWidget.setRowCount(0)  # очищаем таблицу

        for service, accounts in self.loadJson.items():
            for acc in accounts:
                row = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row)
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(service))
                self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(acc["login"]))
                self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(acc["password"]))
        
        # Подгонка столбцов
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

    def delete_selected(self):
        secelcted_rows = set(idx.row() for idx in self.ui.tableWidget.selectedIndexes())
        if not secelcted_rows:
            QMessageBox.information(self, "Удаление", "Выберете строку")
            return
        
        for row in sorted(secelcted_rows, reverse=True):
            service = self.ui.tableWidget.item(row, 0).text()
            login = self.ui.tableWidget.item(row, 1).text()

            if service in self.loadJson:
                self.loadJson[service] = [acc for acc in self.loadJson[service] if acc["login"] != login]
                if not self.loadJson[service]:
                    del self.loadJson[service]

            self.ui.tableWidget.removeRow(row)
        
        CreateJson.save_json(self.loadJson)


    def add_info(self) -> None:
        site = self.ui.input_site.text()
        login = self.ui.input_login.text()
        password = self.ui.input_password.text()
        CreateJson.set_password(site, login, password)
        self.ui.input_site.clear()
        self.ui.input_login.clear()
        self.ui.input_password.clear()

        self.refresh()

    def goBack3(self) -> None:
        self.hide()
        self.mainwindow3.show()


# Окно генерации пароля
class GenerateWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.ui = GenerateWindowPs()
        self.ui.setupUi(self)

        self.main_window = main_window
        self.ui.btn_back.clicked.connect(self.goBack)
        self.connect_slider_to_spinbox()
        self.set_password()
        for btn in buttons.GENERATE_PASSWORD:
            getattr(self.ui, btn).clicked.connect(self.set_password)

        self.ui.btn_visibility.clicked.connect(self.change_password_visibility)
        self.ui.btn_copy.clicked.connect(self.copy_to_clipboard)

    def goBack(self) -> None:
            self.hide()
            self.main_window.show()

    def connect_slider_to_spinbox(self) -> None:
        self.ui.slider_lenght.valueChanged.connect(self.ui.spinbox_lenght.setValue)
        self.ui.spinbox_lenght.valueChanged.connect(self.ui.slider_lenght.setValue)
        self.ui.spinbox_lenght.valueChanged.connect(self.set_password)

    def get_characters(self) -> str:
        chars = ''
        for btn in buttons.Characters:
            if getattr(self.ui, btn.name).isChecked():
                chars += btn.value
        return chars
    
    def set_password(self) -> None:
        try:
            self.ui.line_password.setText(
                password.create_new(lenght=self.ui.spinbox_lenght.value(), characters=self.get_characters())
            )
        except IndexError:
            self.ui.line_password.clear()

        self.set_entropy()
        self.set_strenght()

    def get_characters_number(self) -> int:
        num = 0

        for btn in buttons.CHARACTERS_NUMBER.items():
            if getattr(self.ui, btn[0]).isChecked():
                num += btn[1]
        return num
    
    def set_entropy(self) -> None:
        lenght = len(self.ui.line_password.text())
        char_num = self.get_characters_number()
        self.ui.label_entropy.setText(
            f'Entropy: {password.get_entropy(lenght, char_num)} bit'
        )

    def set_strenght(self) -> None:
        lenght = len(self.ui.line_password.text())
        char_num = self.get_characters_number()

        for strenght in password.StrenghtEntropy:
            if password.get_entropy(lenght, char_num) >= strenght.value:
                self.ui.label_strenght.setText(f'Strenght: {strenght.name}')

    def change_password_visibility(self) -> None:
        if self.ui.btn_visibility.isChecked():
            self.ui.line_password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.line_password.setEchoMode(QLineEdit.Password)

    def copy_to_clipboard(self) -> None:
        QApplication.clipboard().setText(self.ui.line_password.text())

# Калькулятор
class CalcWindow(QMainWindow):
    def __init__(self, main_window4):
        super().__init__()
        self.ui = ui_calc()
        self.ui.setupUi(self)

        self.exp = ""

        self.ui.btn_0.clicked.connect(lambda: self.add_symbol("0"))
        self.ui.btn_1.clicked.connect(lambda: self.add_symbol("1"))
        self.ui.btn_2.clicked.connect(lambda: self.add_symbol("2"))
        self.ui.btn_3.clicked.connect(lambda: self.add_symbol("3"))
        self.ui.btn_4.clicked.connect(lambda: self.add_symbol("4"))
        self.ui.btn_5.clicked.connect(lambda: self.add_symbol("5"))
        self.ui.btn_6.clicked.connect(lambda: self.add_symbol("6"))
        self.ui.btn_7.clicked.connect(lambda: self.add_symbol("7"))
        self.ui.btn_8.clicked.connect(lambda: self.add_symbol("8"))
        self.ui.btn_9.clicked.connect(lambda: self.add_symbol("9"))

        self.ui.btn_minus.clicked.connect(lambda: self.add_symbol('-'))
        self.ui.btn_multiplication.clicked.connect(lambda: self.add_symbol('*'))
        self.ui.btn_plus.clicked.connect(lambda: self.add_symbol('+'))
        self.ui.btn_division.clicked.connect(lambda: self.add_symbol('/'))

        self.ui.btn_reslut.clicked.connect(self.calculate)
        self.ui.btn_clear.clicked.connect(self.clear)


    def add_symbol(self, symbol):
        self.exp += symbol
        self.ui.label.setText(self.exp)

    def calculate(self):
        try:
            result = eval(self.exp)
            self.ui.label.setText(str(result))

            self.exp = str(result)
        except Exception:
            self.ui.label.setText('Error')
            self.exp = ""
    
    def clear(self):
        self.exp = ""
        self.ui.label.setText("0")
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
