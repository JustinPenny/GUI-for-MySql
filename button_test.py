# Testing executing code from a button press.
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import mysql.connector

def window():
    app = QApplication(sys.argv)
    win = QDialog()

    # Trying to create a QTextEdit to display the results of mysql searches
    
    # Used a QTextEdit to dump all of the sql results to a box
    # I'm trying to use a QTableView to list them in a table instead
    logOutput = QTableView(win)
    #logOutput.setReadOnly(True)
    #logOutput.setLineWrapMode(QTextEdit.NoWrap)
    logOutput.move(100,100)
    font = logOutput.font()
    font.setFamily("Courier")
    font.setPointSize(10)
    
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="monoman123"
    )

    mycursor = mydb.cursor()

    mycursor.execute("show databases")

    database_list = []
    for x in mycursor:
        database_list.append(x)

    # This will print text to a table 
    for x in mycursor:
        logOutput.insertPlainText(str(x))
    
    b1 = QPushButton(win)
    b1.setText("Button1")
    #b1.setText(str(database_list[0])) -- This will make the results of a query the name of a button, instead i'm going to put the results in a table
    b1.move(50,20)
    click_1 = b1.clicked.connect(b1_clicked)
    
    if click_1 == True:
        b1.setText("CLICKED")

    b2 = QPushButton(win)
    b2.setText("Button2")
    b2.move(50,50)
    QObject.connect(b2,SIGNAL("clicked()"),b2_clicked)

    win.setGeometry(100,100,200,100)
    win.setWindowTitle("PyQt")
    win.show()
    sys.exit(app.exec_())

# Returning SQL results via button press
def b1_clicked(i):
    print "Button 1 clicked"
        

def b2_clicked():
   print "Button 2 clicked"

if __name__ == '__main__':
   window()
