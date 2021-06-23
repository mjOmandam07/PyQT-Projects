from main import *
from home_functions import *


class backend_functions(MainWindow):
    def homeFunctions(self):
        self.ui.home_treeWidget.itemClicked['QTreeWidgetItem*', 'int'].connect(
            lambda: home_functions.selected(self))
    
        self.ui.home_lineEdit_firstName.textChanged['QString'].connect(lambda: home_functions.setButtons(self))
        self.ui.home_lineEdit_LastName.textChanged['QString'].connect(lambda: home_functions.setButtons(self))
        self.ui.home_lineEdit_birthday.textChanged['QString'].connect(lambda: home_functions.setButtons(self))
        self.ui.home_lineEdit_phoneNumber.textChanged['QString'].connect(lambda: home_functions.setButtons(self))

        home_functions.viewList(self)
        home_functions.selected(self)
        home_functions.dataCheck(self)


