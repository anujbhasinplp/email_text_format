__author__ = 'Anuj'

import ui_fetch_mails, imaplib, datetime, email, re, os, platform
from PyQt4 import QtCore, QtGui
from location_treeview import location_treeview_form
from calender_form import calender_form
from util import create_dir_path


class fetch_mails_form(QtGui.QWidget, ui_fetch_mails.Ui_Form_fetch_mails):
    def __init__(self):
        super(fetch_mails_form, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.move(QtGui.QApplication.desktop().screen().rect().center() - self.rect().center())
        self.pushButton_select_location.clicked.connect(self.location_treeview)
        self.pushButton_select_date.clicked.connect(self.calender_date)
        self.cal_obj = calender_form()
        self.cal_obj.calendarWidget.clicked.connect(self.date_selected)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_fetch_mails.clicked.connect(self.fetch_mails)
        self.email = ""
        self.password = ""
        self.mail_label = ""
        self.date_selected = ""
        self.folder_name = ""

    def calender_date(self):
        self.cal_obj.show()

    def date_selected(self):
        date_set = self.cal_obj.calendarWidget.selectedDate()
        self.lineEdit_date.setText(date_set.toString('dd-MMM-yyyy'))
        self.date_selected = date_set.toString('dd-MMM-yyyy')

    def location_path(self, folder_path):
        self.folder_name = str(folder_path)
        self.lineEdit_location.setText(self.folder_name)

    def location_treeview(self):
        self.location_tr = location_treeview_form()
        self.location_tr.label.setText("Select location of the folder ")
        self.location_tr.update_location.connect(self.location_path)
        self.location_tr.show()

    def fetch_mails(self):
        self.email = self.lineEdit_email.text()
        self.password = self.lineEdit_password.text()
        self.mail_label = self.lineEdit_mail_label.text()

        if platform.system() == "Windows":
            folder_path = self.folder_name
        else:
            folder_path = self.folder_name + '/'
        folder_name_str = str(datetime.datetime.now().day) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().year)
        folder_name = os.path.join(folder_path, folder_name_str)
        todays_date = datetime.date.today()
        # t_date = datetime.date.strftime(todays_date, "%d-%b-%Y") 08-Jun-2016
        t_date = self.date_selected
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(self.email, self.password)
        mail.list()
        # mail.select('inbox')
        mail.select(self.mail_label)
        # result, data = mail.uid('search', None, '(SENTSINCE {date} HEADER Subject "Storage cleanup request")'.format(date= t_date))  # search and return uids instead
        # SINCE "01-Jan-2012" BEFORE "02-Jan-2012"
        result, data = mail.uid('search', None, '(SINCE "05-Oct-2016" BEFORE "06-Oct-2016" HEADER Subject "Storage cleanup request")')  # search and return uids instead
        print result, data, "result", "data"
        i = len(data[0].split())  # data[0] is a space separate string
        for x in range(i):
            latest_email_uid = data[0].split()[x]  # unique ids wrt label selected
            result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            # fetch the email body (RFC822) for the given id
            raw_email = email_data[0][1]  # raw_email is not a string but a byte literal
            raw_email_string = raw_email.decode('utf-8')  # converts byte-literal to string  removing b''
            email_message = email.message_from_string(raw_email_string)
            sub = email_message['Subject']
            server_number = re.search(r'\d+\b', sub)
            print server_number.group()
            for part in email_message.walk():  # this will loop through all the available multiparts in the mail
                try:
                    if part.get_content_type() == "text/plain":  # ignore attachments/html
                        body = part.get_payload(decode=True)
                        create_dir_path(folder_name)
                        save_string = str(folder_name + '/' + server_number.group() + ".txt")
                        myfile = open(save_string, "a")
                        myfile.write(body)
                        myfile.close()
                except Exception as e:
                    print "Exception raised in if part", e
                else:
                    continue


    def mousePressEvent(self, event):
        self.mouseDown = event.button() == QtCore.Qt.LeftButton
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)

    def mouseReleaseEvent(self,event):
        self.mouseDown = False

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = fetch_mails_form()
    ui.show()
    sys.exit(app.exec_())
