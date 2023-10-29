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
        windowIcon = QIcon("Qt Application\imgs\windowIcon.png")
        self.setWindowIcon(windowIcon)
        self.setWindowTitle("WinkWatch With Wazowski")

        
        self.openEyeImage="Qt Application\imgs\mikeOpen.png"
        self.closeEyeImage="Qt Application\imgs\mikeClose.png"
      
        self.unfilteredSignalWidget = pg.PlotWidget() 
        self.filteredSignalWidget = pg.PlotWidget()
        self.verticalLayout1.addWidget(self.unfilteredSignalWidget)
        self.verticalLayout2.addWidget(self.filteredSignalWidget)

        self.unfilteredSignalWidget.getViewBox().setMouseEnabled(x=False, y=False)
        self.filteredSignalWidget.getViewBox().setMouseEnabled(x=False, y=False)
 

        self.openEyeButton.clicked.connect(self.showOpenEye)
        self.closeEyeButton.clicked.connect(self.showCloseEye)
        self.addUnfilteredEEG.clicked.connect(self.openUnfilteredFile)
        self.addFilteredEEG.clicked.connect(self.openFilteredFile)

    
    def openUnfilteredFile(self):
        options = QFileDialog.Option.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Files", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if file_name:
            file_data = pd.read_csv(file_name)  
        
        if file_data is not None:
            self.plotUnfiltered(file_data)
            
    def openFilteredFile(self):
        options = QFileDialog.Option.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Files", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if file_name:
            file_data = pd.read_csv(file_name)
        
        if file_data is not None:
            self.plotFiltered(file_data)
            

    def plotUnfiltered(self, data):
        self.unfilteredSignalWidget.clear()  
        num_channels = min(data.shape[1], 16) 

        vertical_offset = 0
        spacing = 5
        
        for i in range(num_channels):
            channel_data = data.iloc[:, i].values + vertical_offset
            self.unfilteredSignalWidget.plot(channel_data, pen='#E9950C')  
            vertical_offset += np.max(channel_data) - np.min(channel_data) + spacing 

            # Add label for channel name
            channel_name = data.columns[i]  # Get the name from the DataFrame column
            label = pg.TextItem(text=channel_name,anchor=(0, 0))
            label.setPos(0, vertical_offset)
            self.unfilteredSignalWidget.addItem(label)

    def plotFiltered(self, data):
        self.filteredSignalWidget.clear()  
        num_channels = min(data.shape[1], 16)  

        vertical_offset = 0
        spacing = 5  
        
        for i in range(num_channels):
            channel_data = data.iloc[:, i].values + vertical_offset
            self.filteredSignalWidget.plot(channel_data, pen='#E9950C')  
            vertical_offset += np.max(channel_data) - np.min(channel_data) + spacing  

            # Add label for channel name
            channel_name = data.columns[i]  # Get the name from the DataFrame column
            label = pg.TextItem(text=channel_name,anchor=(0, 0))
            label.setPos(0, vertical_offset)
            self.filteredSignalWidget.addItem(label)

        
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
