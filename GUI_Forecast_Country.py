
# ::::::::::: import package ::::::::::::::::::::::::::::::

from GUI_package import*
import ressource_rc
import GUI_forecast 
import Common
# :::::::::::functions dependances ::::::::::::::::::::::::::::::
  

class UI(QMainWindow):       
    def __init__(self): 
        super(UI, self).__init__()
        uic.loadUi("ui_files/country_forecast.ui", self)     
        
        self.saudi_btn=self.findChild(QPushButton,"saudi_btn")
        self.qatar_btn=self.findChild(QPushButton,"qatar_btn")
        self.tunisia_btn=self.findChild(QPushButton,"tunisia_btn")
        self.sudan_btn=self.findChild(QPushButton,"sudan_btn")
        self.morocco_btn=self.findChild(QPushButton,"morocco_btn")
        self.mauritan_btn=self.findChild(QPushButton,"mauritania_btn")
        self.mali_btn=self.findChild(QPushButton,"mali_btn")
        self.madagas_btn=self.findChild(QPushButton,"mada_btn")
        self.lybia_btn=self.findChild(QPushButton,"lybia_btn")
        self.guinea_btn=self.findChild(QPushButton,"guinea_btn")
        self.ghana_btn=self.findChild(QPushButton,"ghana_btn")
        self.egypt_btn=self.findChild(QPushButton,"egypt_btn")
        self.cameroon_btn=self.findChild(QPushButton,"cameroon_btn")
        self.burkina_btn=self.findChild(QPushButton,"burkina_btn")
        self.algeria_btn=self.findChild(QPushButton,"algeria_btn")

        self.algeria_btn.clicked.connect(self.algeria_win)
        self.burkina_btn.clicked.connect(self.burkina_win)
        self.cameroon_btn.clicked.connect(self.cameroon_win)
        self.egypt_btn.clicked.connect(self.egypt_win)
        self.ghana_btn.clicked.connect(self.ghana_win)
        self.guinea_btn.clicked.connect(self.guinea_win)
        self.lybia_btn.clicked.connect(self.lybia_win)
        self.madagas_btn.clicked.connect(self.madagascar_win)
        self.mali_btn.clicked.connect(self.mali_win)
        self.mauritan_btn.clicked.connect(self.mauritania_win)
        self.morocco_btn.clicked.connect(self.morocco_win)
        self.tunisia_btn.clicked.connect(self.tunisia_win)
        self.qatar_btn.clicked.connect(self.qatar_win)
        self.saudi_btn.clicked.connect(self.saudi_win)

        

    def algeria_win(self):
        self.win=ALgeria()
        Common.current_country="Algeria"
        self.win.label.setText(str("Algeria"))
        self.win.show()
    def burkina_win(self):
        self.win=Burkina()
        Common.current_country="Burkina"
        self.win.label.setText(str("Burkina Faso"))
        self.win.show()
    def cameroon_win(self):
        self.win=Cameroon()
        Common.current_country="Cameroon"
        self.win.label.setText(str("Cameroon"))
        self.win.show()
    def egypt_win(self):
        self.win=Egypt()
        Common.current_country="Egypt"
        self.win.label.setText(str("Egypt"))
        self.win.show()
    def ghana_win(self):
        self.win=Ghana()
        Common.current_country="Ghana"
        self.win.label.setText(str("Ghana"))
        self.win.show()
    def guinea_win(self):
        self.win=Guinea()
        Common.current_country="Guinea"
        self.win.label.setText(str("Guinea"))
        self.win.show()
    def lybia_win(self):
        self.win=Lybia()
        Common.current_country="Lybia"
        self.win.label.setText(str("Lybia"))
        self.win.show()
    def madagascar_win(self):
        self.win=Madagascar()
        Common.current_country="Madagascar"
        self.win.label.setText(str("Madagascar"))
        self.win.show()
    def mali_win(self):
        self.win=Mali()
        Common.current_country="Mali"
        self.win.label.setText(str("Mali"))
        self.win.show()
    def mauritania_win(self):
        self.win=Mauritania()
        Common.current_country="Mauritania"
        self.win.label.setText(str("Mauritania"))
        self.win.show()
    def morocco_win(self):
        self.win=Morocco()
        Common.current_country="Morocco"
        self.win.label.setText(str("Morocco"))
        self.win.show()
    def tunisia_win(self):
        self.win=Tunisia()
        Common.current_country="Tunisia"
        self.win.label.setText(str("Tunisia"))
        self.win.show()
    def qatar_win(self):
        self.win=Qatar()
        Common.current_country="Qatar"
        self.win.label.setText(str("Qatar"))
        self.win.show()
    def saudi_win(self):
        self.win=Saudi()
        Common.current_country="Saudi"
        self.win.label.setText(str("Saudi Arabia"))
        self.win.show()



         
class ALgeria(QMainWindow):
    def __init__(self): 
        super(ALgeria, self).__init__()
        uic.loadUi("ui_files/algeria_forecast.ui", self)

        self.label=self.findChild(QLabel,"label")
        self.wheat_btn=self.findChild(QPushButton,"wheat_btn")
        self.tomatoes_btn=self.findChild(QPushButton,"tomatoes_btn")
        self.rice_btn=self.findChild(QPushButton,"rice_btn")
        self.potatoes_btn=self.findChild(QPushButton,"potatoes_btn")
        self.orange_btn=self.findChild(QPushButton,"orange_btn")
        self.maize_btn=self.findChild(QPushButton,"maize_btn")
        self.lentils_btn=self.findChild(QPushButton,"lentils_btn")
        self.dates_btn=self.findChild(QPushButton,"dates_btn")
        self.carrots_btn=self.findChild(QPushButton,"carrots_btn")
        self.beans_btn=self.findChild(QPushButton,"beans_btn")
        self.barley_btn=self.findChild(QPushButton,"barley_btn")
        self.apples_btn=self.findChild(QPushButton,"apples_btn")
        


        self.wheat_btn.clicked.connect(self.open_forecast_1)
        self.tomatoes_btn.clicked.connect(self.open_forecast_2)
        self.rice_btn.clicked.connect(self.open_forecast_3)
        self.potatoes_btn.clicked.connect(self.open_forecast_4)
        self.orange_btn.clicked.connect(self.open_forecast_5)
        self.maize_btn.clicked.connect(self.open_forecast_7)
        self.lentils_btn.clicked.connect(self.open_forecast_8)
        self.dates_btn.clicked.connect(self.open_forecast_10)
        self.carrots_btn.clicked.connect(self.open_forecast_12)
        self.beans_btn.clicked.connect(self.open_forecast_13)
        self.barley_btn.clicked.connect(self.open_forecast_14)
        self.apples_btn.clicked.connect(self.open_forecast_16)
        
    
    
    def open_forecast_1(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/wheat.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_2(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/tomatoes.jpg'
       # Common.current_country="Algeria"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_3(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/rice.jpg'
       # Common.current_country="Algeria"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_4(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/potatoes.jpg'
       # Common.current_country="Algeria"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_5(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/orange.jpg'
      #  Common.current_country="Algeria"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_7(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/maize.jpg'
       # Common.current_country="Algeria"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_8(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/lentils.jpg'
       # Common.current_country="Algeria"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_10(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/dates.jpg'
       # Common.current_country="Algeria"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_12(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/carrot.jpg'
       # Common.current_country="Algeria"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_13(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/beans.jpg'
       # Common.current_country="Algeria"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_14(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/barley.jpg'
       # Common.current_country="Algeria"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_16(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/apple.jpg'
       # Common.current_country="Algeria"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()


 

 
class Egypt(QMainWindow):
    def __init__(self): 
        super(Egypt, self).__init__()
        uic.loadUi("ui_files/egypt_forecast .ui", self)

        self.label=self.findChild(QLabel,"label")
        self.wheat_btn=self.findChild(QPushButton,"wheat_btn")
        self.tomatoes_btn=self.findChild(QPushButton,"tomatoes_btn")
        self.rice_btn=self.findChild(QPushButton,"rice_btn")
        self.potatoes_btn=self.findChild(QPushButton,"potatoes_btn")
        self.orange_btn=self.findChild(QPushButton,"orange_btn")
        self.maize_btn=self.findChild(QPushButton,"maize_btn")
        self.lentils_btn=self.findChild(QPushButton,"lentils_btn")
        self.dates_btn=self.findChild(QPushButton,"dates_btn")
        self.carrots_btn=self.findChild(QPushButton,"carrots_btn")
        self.beans_btn=self.findChild(QPushButton,"beans_btn")
        self.barley_btn=self.findChild(QPushButton,"barley_btn")
        self.apples_btn=self.findChild(QPushButton,"apples_btn")
        


        self.wheat_btn.clicked.connect(self.open_forecast_1)
        self.tomatoes_btn.clicked.connect(self.open_forecast_2)
        self.rice_btn.clicked.connect(self.open_forecast_3)
        self.potatoes_btn.clicked.connect(self.open_forecast_4)
        self.orange_btn.clicked.connect(self.open_forecast_5)
        self.maize_btn.clicked.connect(self.open_forecast_7)
        self.lentils_btn.clicked.connect(self.open_forecast_8)
        self.dates_btn.clicked.connect(self.open_forecast_10)
        self.carrots_btn.clicked.connect(self.open_forecast_12)
        self.beans_btn.clicked.connect(self.open_forecast_13)
        self.barley_btn.clicked.connect(self.open_forecast_14)
        self.apples_btn.clicked.connect(self.open_forecast_16)
        
    
    
    def open_forecast_1(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/wheat.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_2(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/tomatoes.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_3(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/rice.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_4(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/potatoes.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_5(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/orange.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_7(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/maize.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_8(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/lentils.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_10(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/dates.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_12(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/carrot.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_13(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/beans.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_14(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/barley.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_16(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/apple.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()

    
         
         
class Burkina(QMainWindow):
    def __init__(self): 
        super(Burkina, self).__init__()
        uic.loadUi("ui_files/burkina_forecast .ui", self)

        
        self.label=self.findChild(QLabel,"label")
        self.tomatoes_btn=self.findChild(QPushButton,"tomatoes_btn")
        self.rice_btn=self.findChild(QPushButton,"rice_btn")
        self.maize_btn=self.findChild(QPushButton,"maize_btn")
         

        self.tomatoes_btn.clicked.connect(self.open_forecast_2)
        self.rice_btn.clicked.connect(self.open_forecast_3)
        self.maize_btn.clicked.connect(self.open_forecast_7)
         
    
  
    def open_forecast_2(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/tomatoes.jpg'
        Common.current_country="Burkina"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_3(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/rice.jpg'
        Common.current_country="Burkina"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_7(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/maize.jpg'
        Common.current_country="Burkina"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    
         
         
class Lybia(QMainWindow):
    def __init__(self): 
        super(Lybia, self).__init__()
        uic.loadUi("ui_files/lybia_forecast.ui", self)

        
        self.label=self.findChild(QLabel,"label")
        self.orange_btn=self.findChild(QPushButton,"orange_btn")
        self.onions_btn=self.findChild(QPushButton,"onions_btn")
        self.maize_btn=self.findChild(QPushButton,"maize_btn")
        self.dates_btn=self.findChild(QPushButton,"dates_btn")
        self.carrots_btn=self.findChild(QPushButton,"carrots_btn")
        self.beans_btn=self.findChild(QPushButton,"beans_btn")
        self.barley_btn=self.findChild(QPushButton,"barley_btn")
        self.appricot_btn=self.findChild(QPushButton,"appricot_btn")
        self.apples_btn=self.findChild(QPushButton,"apples_btn")
        

        self.orange_btn.clicked.connect(self.open_forecast_2)
        self.onions_btn.clicked.connect(self.open_forecast_3)
        self.maize_btn.clicked.connect(self.open_forecast_4)
        self.dates_btn.clicked.connect(self.open_forecast_5)
        self.carrots_btn.clicked.connect(self.open_forecast_6)
        self.beans_btn.clicked.connect(self.open_forecast_7)
        self.barley_btn.clicked.connect(self.open_forecast_8)
        self.appricot_btn.clicked.connect(self.open_forecast_9)
        self.apples_btn.clicked.connect(self.open_forecast_13)
        
    
  
    def open_forecast_2(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/orange.jpg'
        Common.current_country="Lybia"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_3(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/onions.jpg'
        Common.current_country="Lybia"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_4(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/maize.jpg'
        Common.current_country="Lybia"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_5(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/dates.jpg'
        Common.current_country="Lybia"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_6(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/carrot.jpg'
        Common.current_country="Lybia"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_7(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/beans.jpg'
        Common.current_country="Lybia"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_8(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/barley.jpg'
        Common.current_country="Lybia"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_9(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/apricot.jpg'
        Common.current_country="Lybia" 
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close() 
        self.win.show()
    def open_forecast_13(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/apple.jpg'
        Common.current_country="Lybia"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
  
        
class Cameroon(QMainWindow):
    def __init__(self): 
        super(Cameroon, self).__init__()
        uic.loadUi("ui_files/cameroon_forecast.ui", self)

        
        self.label=self.findChild(QLabel,"label")
        self.tomatoes_btn=self.findChild(QPushButton,"tomatoes_btn")
        self.rice_btn=self.findChild(QPushButton,"rice_btn")
        self.maize_btn=self.findChild(QPushButton,"maize_btn")
         

        self.tomatoes_btn.clicked.connect(self.open_forecast_2)
        self.rice_btn.clicked.connect(self.open_forecast_3)
        self.maize_btn.clicked.connect(self.open_forecast_7)
         
    
  
    def open_forecast_2(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/tomatoes.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_3(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/rice.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_7(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/maize.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    
     


class Ghana(QMainWindow):
    def __init__(self): 
        super(Ghana, self).__init__()
        uic.loadUi("ui_files/ghana_forecast.ui", self)

        
        self.label=self.findChild(QLabel,"label")
        self.tomatoes_btn=self.findChild(QPushButton,"tomatoes_btn")
        self.rice_btn=self.findChild(QPushButton,"rice_btn")
        self.maize_btn=self.findChild(QPushButton,"maize_btn")
         

        self.tomatoes_btn.clicked.connect(self.open_forecast_2)
        self.rice_btn.clicked.connect(self.open_forecast_3)
        self.maize_btn.clicked.connect(self.open_forecast_7)
         
    
  
    def open_forecast_2(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/tomatoes.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_3(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/rice.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_7(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/maize.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    

      
class Guinea(QMainWindow):
    def __init__(self): 
        super(Guinea, self).__init__()
        uic.loadUi("ui_files/guinea_forecast.ui", self)

        
        self.label=self.findChild(QLabel,"label")
        self.tomatoes_btn=self.findChild(QPushButton,"tomatoes_btn")
        self.rice_btn=self.findChild(QPushButton,"rice_btn")
        self.maize_btn=self.findChild(QPushButton,"maize_btn")
         

        self.tomatoes_btn.clicked.connect(self.open_forecast_2)
        self.rice_btn.clicked.connect(self.open_forecast_3)
        self.maize_btn.clicked.connect(self.open_forecast_7)
         
    
  
    def open_forecast_2(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/tomatoes.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_3(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/rice.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_7(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/maize.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    
     
class Lybia(QMainWindow):
    def __init__(self): 
        super(Lybia, self).__init__()
        uic.loadUi("ui_files/lybia_forecast.ui", self)

        
        self.label=self.findChild(QLabel,"label")
        self.tomatoes_btn=self.findChild(QPushButton,"tomatoes_btn")
        self.rice_btn=self.findChild(QPushButton,"rice_btn")
        self.maize_btn=self.findChild(QPushButton,"maize_btn")
         

        self.tomatoes_btn.clicked.connect(self.open_forecast_2)
        self.rice_btn.clicked.connect(self.open_forecast_3)
        self.maize_btn.clicked.connect(self.open_forecast_7)
         
    
  
    def open_forecast_2(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/tomatoes.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_3(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/rice.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_7(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/maize.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    
       
  

class Madagascar(QMainWindow):
    def __init__(self): 
        super(Madagascar, self).__init__()
        uic.loadUi("ui_files/Madagascar_forecast.ui", self)

        
        self.label=self.findChild(QLabel,"label")
        self.tomatoes_btn=self.findChild(QPushButton,"tomatoes_btn")
        self.rice_btn=self.findChild(QPushButton,"rice_btn")
        self.maize_btn=self.findChild(QPushButton,"maize_btn")
         

        self.tomatoes_btn.clicked.connect(self.open_forecast_2)
        self.rice_btn.clicked.connect(self.open_forecast_3)
        self.maize_btn.clicked.connect(self.open_forecast_7)
         
    
  
    def open_forecast_2(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/tomatoes.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_3(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/rice.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_7(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/maize.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    
       
class Mali(QMainWindow):
    def __init__(self): 
        super(Mali, self).__init__()
        uic.loadUi("ui_files/Mali_forecast.ui", self)

        
        self.label=self.findChild(QLabel,"label")
        self.tomatoes_btn=self.findChild(QPushButton,"tomatoes_btn")
        self.rice_btn=self.findChild(QPushButton,"rice_btn")
        self.maize_btn=self.findChild(QPushButton,"maize_btn")
         

        self.tomatoes_btn.clicked.connect(self.open_forecast_2)
        self.rice_btn.clicked.connect(self.open_forecast_3)
        self.maize_btn.clicked.connect(self.open_forecast_7)
         
    
  
    def open_forecast_2(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/tomatoes.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_3(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/rice.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_7(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/maize.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
  

class Mauritania(QMainWindow):
    def __init__(self): 
        super(Mauritania, self).__init__()
        uic.loadUi("ui_files/mauritania_forecast.ui", self)

        
        self.label=self.findChild(QLabel,"label")
        self.tomatoes_btn=self.findChild(QPushButton,"tomatoes_btn")
        self.rice_btn=self.findChild(QPushButton,"rice_btn")
        self.maize_btn=self.findChild(QPushButton,"maize_btn")
         

        self.tomatoes_btn.clicked.connect(self.open_forecast_2)
        self.rice_btn.clicked.connect(self.open_forecast_3)
        self.maize_btn.clicked.connect(self.open_forecast_7)
         
    
  
    def open_forecast_2(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/tomatoes.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_3(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/rice.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_7(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/maize.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
  

class Morocco(QMainWindow):
    def __init__(self): 
        super(Morocco, self).__init__()
        uic.loadUi("ui_files/morocco_forecast .ui", self)

        self.label=self.findChild(QLabel,"label")
        self.wheat_btn=self.findChild(QPushButton,"wheat_btn")
        self.tomatoes_btn=self.findChild(QPushButton,"tomatoes_btn")
        self.rice_btn=self.findChild(QPushButton,"rice_btn")
        self.potatoes_btn=self.findChild(QPushButton,"potatoes_btn")
        self.orange_btn=self.findChild(QPushButton,"orange_btn")
        self.maize_btn=self.findChild(QPushButton,"maize_btn")
        self.lentils_btn=self.findChild(QPushButton,"lentils_btn")
        self.dates_btn=self.findChild(QPushButton,"dates_btn")
        self.carrots_btn=self.findChild(QPushButton,"carrots_btn")
        self.avocado_btn=self.findChild(QPushButton,"avocado_btn")
        self.barley_btn=self.findChild(QPushButton,"barley_btn")
        self.apples_btn=self.findChild(QPushButton,"apples_btn")
        


        self.wheat_btn.clicked.connect(self.open_forecast_1)
        self.tomatoes_btn.clicked.connect(self.open_forecast_2)
        self.rice_btn.clicked.connect(self.open_forecast_3)
        self.potatoes_btn.clicked.connect(self.open_forecast_4)
        self.orange_btn.clicked.connect(self.open_forecast_5)
        self.maize_btn.clicked.connect(self.open_forecast_7)
        self.lentils_btn.clicked.connect(self.open_forecast_8)
        self.dates_btn.clicked.connect(self.open_forecast_10)
        self.carrots_btn.clicked.connect(self.open_forecast_12)
        self.avocado_btn.clicked.connect(self.open_forecast_13)
        self.barley_btn.clicked.connect(self.open_forecast_14)
        self.apples_btn.clicked.connect(self.open_forecast_16)
        
    
    
    def open_forecast_1(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/wheat.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_2(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/tomatoes.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_3(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/rice.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_4(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/potatoes.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_5(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/orange.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_7(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/maize.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_8(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/lentils.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_10(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/dates.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_12(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/carrot.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_13(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/avocat.png'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_14(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/barley.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_16(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/apple.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()



class Sudan(QMainWindow):
    def __init__(self): 
        super(Sudan, self).__init__()
        uic.loadUi("ui_files/sudan_forecast.ui", self)

        
        self.label=self.findChild(QLabel,"label")
        self.tomatoes_btn=self.findChild(QPushButton,"tomatoes_btn")
        self.potatoes_btn=self.findChild(QPushButton,"potatoes_btn")
        
        self.onions_btn=self.findChild(QPushButton,"onions_btn")
        self.carrots_btn=self.findChild(QPushButton,"carrots_btn")
        self.orange_btn=self.findChild(QPushButton,"orange_btn")
        self.barley_btn=self.findChild(QPushButton,"barley_btn")
        
        self.tomatoes_btn.clicked.connect(self.open_forecast_2)
        self.potatoes_btn.clicked.connect(self.open_forecast_3)
        
        self.onions_btn.clicked.connect(self.open_forecast_6)
        self.carrots_btn.clicked.connect(self.open_forecast_7)
        self.orange_btn.clicked.connect(self.open_forecast_8)
        self.barley_btn.clicked.connect(self.open_forecast_9)
        
    
  
    def open_forecast_2(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/tomatoes.jpg'
        Common.current_country="Sudan"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_3(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/potatoes.jpg'
        Common.current_country="Sudan"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
     
    def open_forecast_6(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/onions.jpg'
        Common.current_country="Sudan"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_7(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/carrot.jpg'
        Common.current_country="Sudan"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_8(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/orange.jpg'
        Common.current_country="Sudan"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_9(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/barley.jpg'
        Common.current_country="Sudan" 
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close() 
        self.win.show()
   
class Tunisia(QMainWindow):
    def __init__(self): 
        super(Tunisia, self).__init__()
        uic.loadUi("ui_files/tunisia_forecast.ui", self)

        
        self.label=self.findChild(QLabel,"label")
        self.tomatoes_btn=self.findChild(QPushButton,"tomatoes_btn")
        self.lentils_btn=self.findChild(QPushButton,"lentils_btn")
        
        self.date_btn=self.findChild(QPushButton,"date_btn")
        self.barley_btn=self.findChild(QPushButton,"barley_btn")
        self.apricot_btn=self.findChild(QPushButton,"apricot_btn")
        self.apple_btn=self.findChild(QPushButton,"apple_btn")
        
        self.tomatoes_btn.clicked.connect(self.open_forecast_2)
        self.lentils_btn.clicked.connect(self.open_forecast_3)
        
        self.date_btn.clicked.connect(self.open_forecast_6)
        self.apricot_btn.clicked.connect(self.open_forecast_7)
        self.apple_btn.clicked.connect(self.open_forecast_8)
        self.barley_btn.clicked.connect(self.open_forecast_9)
        
    
  
    def open_forecast_2(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/tomatoes.jpg'
        Common.current_country="Tunisia"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_3(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/lentils.jpg'
        Common.current_country="Tunisia"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
     
    def open_forecast_6(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/dates.jpg'
        Common.current_country="Tunisia"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_7(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/Apricot.jpg'
        Common.current_country="Tunisia"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_8(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/apple.jpg'
        Common.current_country="Tunisia"
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
    def open_forecast_9(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/barley.jpg'
        Common.current_country="Tunisia" 
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close() 
        self.win.show()
        
class Qatar(QMainWindow):
    def __init__(self): 
        super(Qatar, self).__init__()
        uic.loadUi("ui_files/qatar_forecast.ui", self)
        
        self.label=self.findChild(QLabel,"label")
        self.tomatoes_btn=self.findChild(QPushButton,"tomatoes_btn")
        self.dates_btn=self.findChild(QPushButton,"date_btn")
        self.barley_btn=self.findChild(QPushButton,"barley_btn")
         
        self.tomatoes_btn.clicked.connect(self.open_forecast_2)
        self.dates_btn.clicked.connect(self.open_forecast_6)
        self.barley_btn.clicked.connect(self.open_forecast_9)
        
    
  
    def open_forecast_2(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/tomatoes.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()

     
    def open_forecast_6(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/dates.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close()
        self.win.show()
  
    def open_forecast_9(self):
        self.win=GUI_forecast.UI()
        Common.current_item='images/barley.jpg'
        pixmap = QPixmap(Common.current_item)
        self.win.label_img.setPixmap(pixmap)
        self.win.label_img.resize(pixmap.width(),pixmap.height())
        self.close() 
        self.win.show()
  