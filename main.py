import sys
import pyodbc
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from functools import partial

from ui_mainSearch import *
from ui_soResult import *
from ui_tenResult import *
from ui_hosoResult import *
from ui_detail import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.soResultWin = QWidget()
        self.soUI = Ui_SoResultWidget()
        self.soUI.setupUi(self.soResultWin)

        self.tenResultWin = QWidget()
        self.tenUI = Ui_tenResultWidget()
        self.tenUI.setupUi(self.tenResultWin)

        self.hosoResultWin = QWidget()
        self.hosoUI = Ui_hosoResultWidget()
        self.hosoUI.setupUi(self.hosoResultWin)

        self.detailWin = QWidget()
        self.detailUI = Ui_DetailWidget()
        self.detailUI.setupUi(self.detailWin)

        self.listServer = ["DESKTOP-2RT3LOI\DUATLE1", "DESKTOP-2RT3LOI\DUATLE2", "DESKTOP-2RT3LOI\DUATLE3"]
        self.getDB()

        self.ui.TimButton.clicked.connect(self.TimKiem)
        
    def connectDB(self, server):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                            'Server='+server+';'
                            'Database=HBDT;'
                            'Trusted_Connection=yes;')

    def getDB(self):
        self.connectDB(self.listServer[0])

        sql = "SELECT MaSo, TenSo FROM SoGiaoDuc"
        result = self.conn.execute(sql)
        self.ui.SogiaoducCombobox.addItem("Chọn Sở giáo dục")
        for row_number, row_data in enumerate(result):
            self.ui.SogiaoducCombobox.addItem(row_data[1])

        self.conn.close()

    def TimKiem(self):
        maso = self.ui.SogiaoducCombobox.currentIndex()
        mahocba = self.ui.MahocbaText.text()
        tenhocsinh = self.ui.TenhocsinhText.text()

        if maso != 0:
            self.TimKiemTheoSo(maso)
        elif mahocba != "":
            self.TimKiemTheoMaHocBa(mahocba)
        else:
            self.TimKiemTheoTenHocSinh(tenhocsinh)
    
    def TimKiemTheoSo(self, maso):
        self.connectDB(self.listServer[0])

        sql = "SELECT HocBa.MaHB, HocSinh.TenHS, HocSinh.DiaChi, SoGiaoDuc.TenSo FROM HocBa JOIN HocSinh ON HocBa.MaHB=HocSinh.MaHB JOIN SoGiaoDuc ON HocBa.MaSo=SoGiaoDuc.MaSo WHERE SoGiaoDuc.MaSo="+str(maso)+""
        result = self.conn.execute(sql)
        self.soUI.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.soUI.SogiaoducLabel.setText(row_data[3])
            self.soUI.tableWidget.insertRow(row_number)
            self.xemhosoButton = QtWidgets.QPushButton("Xem")
            self.xemhosoButton.clicked.connect(partial(self.TimKiemTheoMaHocBa, row_data[0]))
            self.soUI.tableWidget.setCellWidget(row_number, 3, self.xemhosoButton)
            for column_number, data in enumerate(row_data):
                self.soUI.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.soResultWin.show()
        self.conn.close()

    def TimKiemTheoMaHocBa(self, mahocba):
        self.connectDB(self.listServer[0])

        sql = "SELECT HocBa.MaHB, HocSinh.TenHS, HocSinh.NgaySinh, HocSinh.GioiTinh, HocSinh.DiaChi, SoGiaoDuc.TenSo FROM HocBa JOIN HocSinh ON HocBa.MaHB=HocSinh.MaHB JOIN SoGiaoDuc ON HocBa.MaSo=SoGiaoDuc.MaSo WHERE HocBa.MaHB="+str(mahocba)+""
        result = self.conn.execute(sql)
        for row_number, row_data in enumerate(result):
            self.hosoUI.MahocbaLabel.setText(str(row_data[0]))
            self.hosoUI.TenhocsinhLabel.setText(str(row_data[1]))
            self.hosoUI.NgaysinhLabel.setText(str(row_data[2]))
            if row_data[3] == 1:
                self.hosoUI.GioitinhLabel.setText("Nam")
            else:
                self.hosoUI.GioitinhLabel.setText("Nữ")
            self.hosoUI.DiachiLabel.setText(str(row_data[4]))
            self.hosoUI.SogiaoducLabel.setText(str(row_data[5]))

        self.hosoUI.XemhosochitietButton.clicked.connect(lambda:self.XemChiTietHocBa(mahocba))
        self.hosoResultWin.show()
        self.conn.close()

    def TimKiemTheoTenHocSinh(self, tenhocsinh):
        self.connectDB(self.listServer[0])

        sql = "SELECT HocBa.MaHB, HocSinh.TenHS, HocSinh.DiaChi, SoGiaoDuc.TenSo FROM HocBa JOIN HocSinh ON HocBa.MaHB=HocSinh.MaHB JOIN SoGiaoDuc ON HocBa.MaSo=SoGiaoDuc.MaSo WHERE HocSinh.TenHS LIKE '%"+tenhocsinh+"%'"
        result = self.conn.execute(sql)
        self.tenUI.tableWidget.setRowCount(0)
        self.tenUI.TenhocsinhLabel.setText(tenhocsinh)
        for row_number, row_data in enumerate(result):
            self.tenUI.tableWidget.insertRow(row_number)
            self.xemhosoButton = QtWidgets.QPushButton("Xem")
            self.xemhosoButton.clicked.connect(partial(self.TimKiemTheoMaHocBa, row_data[0]))
            self.tenUI.tableWidget.setCellWidget(row_number, 4, self.xemhosoButton)
            for column_number, data in enumerate(row_data):
                self.tenUI.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.tenResultWin.show()
        self.conn.close()

    def XemChiTietHocBa(self, mahocba):
        self.connectDB(self.listServer[0])

        sql1 = "SELECT HocSinh.TenHS, SoGiaoDuc.TenSo FROM HocBa JOIN SoGiaoDuc ON HocBa.MaSo = SoGiaoDuc.MaSo JOIN HocSinh ON HocBa.MaHB = HocSinh.MaHB WHERE HocBa.MaHB = "+str(mahocba)+""
        result1 = self.conn.execute(sql1)
        for row_number, row_data in enumerate(result1):
            self.detailUI.SoGiaoDucLabel.setText(str(row_data[1]))
            self.detailUI.TenHSLabel.setText(str(row_data[0]))

        sql2 = "SELECT MonHoc.TenMH, MonHoc.Khoi, Diem.Diem, Diem.Loai, GiaoVien.TenGV FROM MHLHS JOIN HocSinh ON MHLHS.MaHS = HocSinh.MaHS JOIN MonHoc ON MHLHS.MaMH = MonHoc.MaMH JOIN Diem ON MHLHS.MaMHLHS = Diem.MaMHLHS JOIN GiaoVien ON MonHoc.MaGV = GiaoVien.MaGV WHERE HocSinh.MaHB = "+str(mahocba)+""
        result2 = self.conn.execute(sql2)
        self.detailUI.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result2):
            self.detailUI.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.detailUI.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.detailWin.show()
        self.conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    m = Main()
    m.show()

    sys.exit(app.exec_())