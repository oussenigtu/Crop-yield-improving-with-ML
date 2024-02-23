
# ::::::::::: import package ::::::::::::::::::::::::::::::

from GUI_package import*
import ressource_rc
import GUI_Forecast_Country
# :::::::::::functions dependances ::::::::::::::::::::::::::::::
  

class UI(QMainWindow):       
    def __init__(self): 
        super(UI, self).__init__()
        uic.loadUi("ui_files/acceuil.ui", self)     
        self.predict_btn=self.findChild(QPushButton,"predict_btn")
        self.recommander_btn=self.findChild(QPushButton,"recommander_btn")
        self.available_crop=self.findChild(QPushButton,"available_crop")
        
         
        self.predict_btn.clicked.connect(self.country_forecast)
        self.available_crop.clicked.connect(self.show_available)
 
 
    def country_forecast(self):
        self.win=GUI_Forecast_Country.UI()
        self.win.show()
        
    def show_available(self):
        self.win=available_country()
        self.res=self.win.get_outputs()
  

"""_summary_:
dialog window to show available country
"""
class available_country(QDialog):
    def __init__(self):
        super(available_country,self).__init__()
        uic.loadUi("ui_files/country.ui", self)
    
    def get_outputs(self):
        if self.exec_()==QDialog.Accepted:
            return 1
        else:
            return 0
        
          
# ::::::::::::::::::::::: run :::::::::::::::::::::::::::::::::::::::::

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        ui = UI()
        ui.show()
        sys.exit(app.exec_())                



  