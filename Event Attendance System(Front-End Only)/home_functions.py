from main import *
from more_itertools import unique_everseen

import sqlite3

conn = sqlite3.connect('upstreamers.db')
my_cursor = conn.cursor()
upstreamers_allData = "SELECT * FROM upstreamers"

searchedData = []

class home_functions(MainWindow):
    def viewList(self):
        try:
            entry = self.ui.home_search_bar.text()
            my_cursor.execute(upstreamers_allData)
            display = my_cursor.fetchall()
            data = []
            searched = []
            for row in display:
                n = (str(row[0]), row[1], row[2])
                data.append(list(n))

            self.ui.home_treeWidget.clear()
            for row in data:
                for field in row:
                    if entry.lower() in field.lower():
                        searched.append(row)
            n = list(unique_everseen(searched))
            for i in n:
                self.ui.home_treeWidgetItem(self.ui.home_treeWidget, [i[0], i[1], i[2]])
        except Exception:
            raise Exception


    def selected(self):
        try:
            getSelected = self.ui.home_treeWidget.selectedItems()
            my_cursor.execute(upstreamers_allData)
            display = my_cursor.fetchall()
            if getSelected:
                baseNode = getSelected[0]
                getChildNode = baseNode.text(0)
                for i in display:
                    if i[0] == int(getChildNode):
                        self.ui.home_lineEdit_firstName.setText(str(i[2]))
                        self.ui.home_lineEdit_LastName.setText(str(i[1]))
                        self.ui.home_lineEdit_birthday.setText(str(i[3]))
                        self.ui.home_lineEdit_phoneNumber.setText(str(i[4]))
                        #self.NumOfAttnd()
                        searchedData.append(i)
                        home_functions.dataCheck(self)
                #print(searchedData)
        except Exception:
            raise Exception


    def dataCheck(self):
        fname = self.ui.home_lineEdit_firstName.text()
        lname = self.ui.home_lineEdit_LastName.text()
        bday = self.ui.home_lineEdit_birthday.text()
        phone = self.ui.home_lineEdit_phoneNumber.text()

        try:
            for row in searchedData:
                if fname == row[2] and lname == row[1] and bday == str(row[3]) and phone == str(row[4]):
                    #print('[ '+fname+', '+lname+', '+bday+', '+phone+' ]')
                    self.ui.home_btn_delete.setDisabled(False)

        except Exception:
            raise Exception


    def setButtons(self):
        fname = self.ui.home_lineEdit_firstName.text()
        lname = self.ui.home_lineEdit_LastName.text()
        bday = self.ui.home_lineEdit_birthday.text()
        phone = self.ui.home_lineEdit_phoneNumber.text()
        my_cursor.execute(upstreamers_allData)
        display = my_cursor.fetchall()
        isSame = False
        for item in searchedData:
            for row in display:
                if row[0] == item[0]:
                    isSame = True
                    for row in searchedData:
                        for field in row[1:]:
                            if str(fname).lower() not in str(field).lower() and str(lname).lower() not in str(field).lower() and str(bday).lower() not in str(field).lower() and str(phone).lower() not in str(field).lower():
                                self.ui.home_btn_updt.setDisabled(False)
                                print("wala")


        '''print(isSame)
        if isSame is not True: 
  
                self.ui.home_btn_add.setDisabled(False)

        else:
            self.ui.home_btn_add.setDisabled(True)'''














