#Brandon Bauer
#26-XX /9/2020
#Website loader, works with java script, 

#https://www.youtube.com/watch?v=FSH77vnOGqU
#https://stackoverflow.com/questions/47173791/cannot-use-qurl

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl, pyqtSignal, QEventLoop
from PyQt5.QtWebEngineWidgets import QWebEnginePage

class Client(QWebEnginePage):
    toHtmlFinished = pyqtSignal()
    
    def __init__(self, url):
        self.app = QApplication([])
        QWebEnginePage.__init__(self) #wtf
        self.loadFinished.connect(self.on_page_load)
        self.load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.instance().quit()
        
    def store_html(self, html):
        self.html = html
        self.toHtmlFinished.emit()

    def get_html(self,url):
        self.load(QUrl(url))
        self.toHtml(self.store_html)
        loop = QEventLoop()
        self.toHtmlFinished.connect(loop.quit)
        loop.exec_()
        return self.html



