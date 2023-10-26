# Import necessary modules
import sys  
from os import path  
import numpy as np  
import pandas as pd
from PyQt6 import QtWidgets,QtGui
from PyQt6.QtWidgets import *  
from PyQt6.QtCore import *  
from PyQt6.uic import loadUiType
from PyQt6.QtGui import QIcon, QPixmap
import pyqtgraph as pg






FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "design.ui"))

class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        windowIcon = QIcon("imgs/windowIcon.png")
        self.setWindowIcon(windowIcon)
        self.setWindowTitle("WinkWatch With Wazowski")

        
        self.openEyeImage="imgs/mikeOpen.png"
        self.closeEyeImage="imgs/mikeClose.png"
      
        self.unfilteredSignalWidget = pg.PlotWidget() 
        self.filteredSignalWidget = pg.PlotWidget()
        self.verticalLayout1.addWidget(self.unfilteredSignalWidget)
        self.verticalLayout2.addWidget(self.filteredSignalWidget)

        self.unfilteredSignalWidget.getViewBox().setMouseEnabled(x=False, y=False)
        self.filteredSignalWidget.getViewBox().setMouseEnabled(x=False, y=False)
        
        self.x_axis_labels = [(0, '0'), (np.pi / 2, 'π/2'), (np.pi, 'π'), (3 * np.pi / 2, '3π/2'), (2 * np.pi, '2π')]
        self.unfilteredSignalWidget.setXRange(0, 2 * np.pi)
        self.filteredSignalWidget.setXRange(0, 2 * np.pi)
        
        self.unfilteredSignalWidget.getAxis("bottom").setTicks([self.x_axis_labels])
        self.filteredSignalWidget.getAxis("bottom").setTicks([self.x_axis_labels])
        
        
        self.openEyeButton.clicked.connect(self.showOpenEye)
        self.closeEyeButton.clicked.connect(self.showCloseEye)
        
    def showOpenEye(self):
        pixmap = QtGui.QPixmap(self.openEyeImage)
        pixmap = pixmap.scaled(self.imageLabel.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setScaledContents(True)

    def showCloseEye(self):
        pixmap = QtGui.QPixmap(self.closeEyeImage)
        pixmap = pixmap.scaled(self.imageLabel.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setScaledContents(True)
        

def main():
    app = QApplication(sys.argv) 
    window = MainApp() 
    window.show() 
    app.exec()  

if __name__ == "__main__":
    main()
