
# ::::::::::: import package ::::::::::::::::::::::::::::::

from GUI_package import*
import GUI_Forecast_Country
import Common
# :::::::::::functions dependances ::::::::::::::::::::::::::::::
  

class UI(QMainWindow):       
    def __init__(self): 
        super(UI, self).__init__()
        uic.loadUi("ui_files/forecast_fen.ui", self)     
        
        self.setinput_btn=self.findChild(QPushButton,"input_btn")
        self.helps_btn=self.findChild(QPushButton,"help_btn")
        self.predict_btn=self.findChild(QPushButton,"predict_btn")

        self.precision=self.findChild(QLabel,"precision_yield")
        self.yields=self.findChild(QLabel,"predict_yield")
        self.year=self.findChild(QLabel,"year")
        self.pesticide=self.findChild(QLineEdit,"pesticides")
        self.temp=self.findChild(QComboBox,"predict_temp")
        self.rain=self.findChild(QComboBox,"predict_rain")
        self.label_img=self.findChild(QLabel,"label_img")
        self.groupBox_2=self.findChild(QGroupBox,"groupBox_4")
         
        self.country_name=Common.current_country
        if self.country_name=="Algeria":
            self.rain_lis=  ['2023       67.76231 mm',
                        '2024       72.54032 mm',
                        '2025       68.46716 mm',
                        '2026       78.65246 mm',
                        '2027       70.36176 mm',
                        '2028       65.31108 mm',
                        '2029       83.49974 mm',
                        '2030       72.63327 mm',
                        '2031       62.66137 mm',
                        '2032       78.66774 mm']
            self.temp_lis= ['2023       23.90665 mm',
                            '2024       23.65392 mm',
                            '2025       24.07657 mm',
                            '2026       23.94976 mm',
                            '2027       24.14309 mm',
                            '2028       24.02510 mm',
                            '2029       23.66270 mm',
                            '2030       23.81828 mm',
                            '2031       23.94420 mm',
                            '2032       24.18341 mm']
            self.rain.addItems(self.rain_lis)
            self.temp.addItems(self.temp_lis)
        elif self.country_name=="Morocco":
            self.rain_lis= ['2023       404.60799 mm',
                            '2024       627.05668 mm',
                            '2025       413.26793 mm',
                            '2026       377.24059 mm',
                            '2027       297.54480 mm',
                            '2028       283.90799 mm',
                            '2029       145.29468 mm',
                            '2030       298.38611 mm',
                            '2031       238.40418 mm',
                            '2032       465.86068 mm']
            self.temp_lis= ['2023       18.62308 mm',
                            '2024       18.32078 mm',
                            '2025       18.84323 mm',
                            '2026       18.92365 mm',
                            '2027       19.16826 mm',
                            '2028       19.40114 mm',
                            '2029       17.83196 mm',
                            '2030       18.68554 mm',
                            '2031       19.00754 mm',
                            '2032       19.22354 mm']
            self.rain.addItems(self.rain_lis)
            self.temp.addItems(self.temp_lis)
        elif self.country_name=="Egypt":
            self.rain_lis= ['2023       23.32856 mm',
                            '2024       21.32606 mm',
                            '2025       23.21338 mm',
                            '2026       23.93415 mm',
                            '2027       20.90596 mm',
                            '2028       18.24931 mm',
                            '2029       29.13762 mm',
                            '2030       20.75686 mm',
                            '2031       22.91285 mm',
                            '2032       18.90263 mm']
            self.temp_lis= ['2023       24.20206 mm',
                            '2024       23.85024 mm',
                            '2025       24.12950 mm',
                            '2026       23.92556 mm',
                            '2027       24.36585 mm',
                            '2028       23.80183 mm',
                            '2029       24.83929 mm',
                            '2030       23.82920 mm',
                            '2031       23.44981 mm',
                            '2032       24.45519 mm']
            self.rain.addItems(self.rain_lis)
            self.temp.addItems(self.temp_lis)
        elif self.country_name=="Burkina":
            self.rain_lis= ['2023       890.12112 mm',
                            '2024       843.93951 mm',
                            '2025       836.96075 mm',
                            '2026       968.58089 mm',
                            '2027       910.74851 mm',
                            '2028       880.49103 mm',
                            '2029       994.79913 mm',
                            '2030       951.98630 mm',
                            '2031       949.66862 mm',
                            '2032       918.84483 mm']
            self.temp_lis= ['2023       29.51835 mm',
                            '2024       29.66550 mm',
                            '2025       29.90082 mm',
                            '2026       29.79865 mm',
                            '2027       29.86235 mm',
                            '2028       29.97211 mm',
                            '2029       29.76231 mm',
                            '2030       29.74885 mm',
                            '2031       29.81746 mm',
                            '2032       30.08099 mm']
            self.rain.addItems(self.rain_lis)
            self.temp.addItems(self.temp_lis)
        elif self.country_name=="Cameroon":
            self.rain_lis= ['2023       1618.31333 mm',
                            '2024       1598.04540 mm',
                            '2025       1607.82236 mm',
                            '2026       1538.00676 mm',
                            '2027       1602.03939 mm',
                            '2028       1588.73654 mm',
                            '2029       1581.08517 mm',
                            '2030       1639.30239 mm',
                            '2031       1616.17315 mm',
                            '2032       1603.44793 mm']
            self.temp_lis= ['2023       24.97774 mm',
                            '2024       25.08204 mm',
                            '2025       25.14181 mm',
                            '2026       25.17018 mm',
                            '2027       25.40363 mm',
                            '2028       25.17087 mm',
                            '2029       25.16153 mm',
                            '2030       25.11162 mm',
                            '2031       25.38966 mm',
                            '2032       25.39714 mm']
            self.rain.addItems(self.rain_lis)
            self.temp.addItems(self.temp_lis)
            
        elif self.country_name=="Ghana":
            self.rain_lis= ['2023       1296.19473 mm',
                            '2024       1126.94134 mm',
                            '2025       1272.17693 mm',
                            '2026       1110.80560 mm',
                            '2027       1219.68932 mm',
                            '2028       1157.37658 mm',
                            '2029       1360.31755 mm',
                            '2030       1490.81309 mm',
                            '2031       1239.29871 mm',
                            '2032       1309.82720 mm']
            self.temp_lis= ['2023       27.94250 mm',
                            '2024       28.08647 mm',
                            '2025       28.21811 mm',
                            '2026       28.29368 mm',
                            '2027       28.43413 mm',
                            '2028       28.39615 mm',
                            '2029       28.29950 mm',
                            '2030       28.22561 mm',
                            '2031       28.35218 mm',
                            '2032       28.40918 mm']
            self.rain.addItems(self.rain_lis)
            self.temp.addItems(self.temp_lis)
        elif self.country_name=="Guinea":
            self.rain_lis= ['2023       1842.02338 mm',
                            '2024       1825.64808 mm',
                            '2025       1720.55577 mm',
                            '2026       1879.59232 mm',
                            '2027       1817.63762 mm',
                            '2028       1740.45049 mm',
                            '2029       1864.08241 mm',
                            '2030       1790.93380 mm',
                            '2031       1820.39747 mm',
                            '2032       1787.35037 mm']
            self.temp_lis= ['2023       26.01982 mm',
                            '2024       26.26467 mm',
                            '2025       26.37549 mm',
                            '2026       26.43595 mm',
                            '2027       26.48719 mm',
                            '2028       26.55308 mm',
                            '2029       26.31696 mm',
                            '2030       26.34561 mm',
                            '2031       26.50337 mm',
                            '2032       26.40269 mm']
            self.rain.addItems(self.rain_lis)
            self.temp.addItems(self.temp_lis)
        elif self.country_name=="Lybia":
            self.rain_lis= ['2023       33.93885 mm',
                            '2024       32.13347 mm',
                            '2025       31.65849 mm',
                            '2026       35.57829 mm',
                            '2027       26.62510 mm',
                            '2028       31.59853 mm',
                            '2029       41.84829 mm',
                            '2030       36.85510 mm',
                            '2031       32.49837 mm',
                            '2032       29.16964 mm']
            self.temp_lis= ['2023       22.60996 mm',
                            '2024       22.46602 mm',
                            '2025       22.44620 mm',
                            '2026       21.94116 mm',
                            '2027       22.54042 mm',
                            '2028       22.05869 mm',
                            '2029       22.74887 mm',
                            '2030       22.15877 mm',
                            '2031       22.04019 mm',
                            '2032       22.34139 mm']
            self.rain.addItems(self.rain_lis)
            self.temp.addItems(self.temp_lis)
            
        elif self.country_name=="Madagascar":
            self.rain_lis= ['2023       1305.99862 mm',
                            '2024       1409.38671 mm',
                            '2025       1422.00100 mm',
                            '2026       1273.51493 mm',
                            '2027       1103.74960 mm',
                            '2028       1253.38360 mm',
                            '2029       1435.20603 mm',
                            '2030       1511.02301 mm',
                            '2031       1270.58350 mm',
                            '2032       1350.97142 mm']
            self.temp_lis= ['2023       23.20597 mm',
                            '2024       23.12458 mm',
                            '2025       23.36017 mm',
                            '2026       23.41699 mm',
                            '2027       23.25854 mm',
                            '2028       23.51085 mm',
                            '2029       23.31813 mm',
                            '2030       23.58301 mm',
                            '2031       23.33310 mm',
                            '2032       23.51297 mm']
            self.rain.addItems(self.rain_lis)
            self.temp.addItems(self.temp_lis)
        elif self.country_name=="Mali":
            self.rain_lis= ['2023       359.06327 mm',
                            '2024       347.20326 mm',
                            '2025       322.50195 mm',
                            '2026       377.73397 mm',
                            '2027       352.79463 mm',
                            '2028       343.00154 mm',
                            '2029       388.99562 mm',
                            '2030       359.36138 mm',
                            '2031       374.22718 mm',
                            '2032       361.98604 mm']
            self.temp_lis= ['2023       29.24984 mm',
                            '2024       29.45060 mm',
                            '2025       29.57918 mm',
                            '2026       29.50342 mm',
                            '2027       29.63090 mm',
                            '2028       29.65727 mm',
                            '2029       29.43646 mm',
                            '2030       29.40606 mm',
                            '2031       29.51451 mm',
                            '2032       29.79666 mm']
            self.rain.addItems(self.rain_lis)
            self.temp.addItems(self.temp_lis)
                
        elif self.country_name=="Mauritania":
            self.rain_lis= ['2023       130.03145 mm',
                            '2024       125.15551 mm',
                            '2025       110.23498 mm',
                            '2026       132.66125 mm',
                            '2027       120.24990 mm',
                            '2028       121.21282 mm',
                            '2029       121.94472 mm',
                            '2030       124.05257 mm',
                            '2031       134.51685 mm',
                            '2032       131.67612 mm']
            self.temp_lis= ['2023       28.99335 mm',
                            '2024       29.47300 mm',
                            '2025       29.23658 mm',
                            '2026       29.32435 mm',
                            '2027       29.34184 mm',
                            '2028       29.42255 mm',
                            '2029       29.00845 mm',
                            '2030       29.10437 mm',
                            '2031       29.37731 mm',
                            '2032       29.47550 mm']
            self.rain.addItems(self.rain_lis)
            self.temp.addItems(self.temp_lis)
        elif self.country_name=="Tunisia":
            self.rain_lis= ['2023       199.15683 mm',
                            '2024       246.38709 mm',
                            '2025       270.91725 mm',
                            '2026       310.05743 mm',
                            '2027       271.00431 mm',
                            '2028       234.83440 mm',
                            '2029       275.19261 mm',
                            '2030       302.13048 mm',
                            '2031       240.82823 mm',
                            '2032       309.59829 mm']
            self.temp_lis= ['2023       21.18121 mm',
                            '2024       20.95642 mm',
                            '2025       21.34463 mm',
                            '2026       21.08145 mm',
                            '2027       21.25543 mm',
                            '2028       20.95405 mm',
                            '2029       21.02191 mm',
                            '2030       21.00573 mm',
                            '2031       21.13117 mm',
                            '2032       21.10462 mm']
            self.rain.addItems(self.rain_lis)
            self.temp.addItems(self.temp_lis)
        elif self.country_name=="Qatar":
            self.rain_lis= ['2023       75.68344 mm',
                            '2024       44.48764 mm',
                            '2025       85.94373 mm',
                            '2026       81.54443 mm',
                            '2027       67.02199 mm',
                            '2028       122.8160 mm',
                            '2029       71.70701 mm',
                            '2030       124.1951 mm',
                            '2031       81.26906 mm',
                            '2032       126.7823 mm']
            self.temp_lis= ['2023       28.78702 mm',
                            '2024       28.46277 mm',
                            '2025       28.76021 mm',
                            '2026       29.12581 mm',
                            '2027       29.25853 mm',
                            '2028       29.19174 mm',
                            '2029       29.55903 mm',
                            '2030       29.26228 mm',
                            '2031       29.03165 mm',
                            '2032       29.42269 mm']
            self.rain.addItems(self.rain_lis)
            self.temp.addItems(self.temp_lis)
                    
            
        
        self.predict_btn.clicked.connect(self.con_fore_)



    def con_fore_(self):
        if self.pesticide.text().isdigit():
                
            self.country=Common.current_country
            if self.country=="Algeria":
                self.algeria_yield()
            elif self.country=="Burkina":
                self.burkina_yield()
            elif self.country=="Cameroon":
                self.cameroon_yield()
            elif self.country=="Egypt":
                self.egypt_yield()
            elif self.country=="Ghana":
                self.ghana_yield()
            elif self.country=="Guinea":
                self.guinea_yield()
            elif self.country=="Lybia":
                self.lybia_yield()
            elif self.country=="Madagascar":
                self.madagascar_yield()
            elif self.country=="Mali":
                self.mali_yield()
            elif self.country=="Mauritania":
                self.mauritania_yield()
            elif self.country=="Morocco":
                self.morocco_yield()
            elif self.country=="Tunisia":
                self.tunisia_yield()
            elif self.country=="Qatar":
                self.qatar_yield()
        else:
            QMessageBox.about(self,"info","you must give correct value in Pesticide field")


     
    def algeria_yield(self):
        self.crop_name=Common.current_item
        self.bsname=self.crop_name[7:len(self.crop_name)-4]
         
        if self.bsname=="apple":  
            if self.pesticide.text()=="":
                QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
            else:
                model_filename="models_dir/yield_dir/algeria_yield/Apples_model.pkl"
                self.model=pickle.load(open(model_filename, 'rb'))
               
                self.temp_val=float(self.temp.currentText()[9:20])
                self.rain_val=float(self.rain.currentText()[9:20])
                self.pest_val=float(self.pesticide.text())
                 
                self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                self.pred=self.model.predict(self.input)[0]
                self.accuracy=0.8
                self.absplage=self.pred*(1-self.accuracy)
                self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
                
        elif self.bsname=="barley":
            if self.pesticide.text()=="":
                QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
            else:
                model_filename="models_dir/yield_dir/algeria_yield/Barley_model.pkl"
                self.model=pickle.load(open(model_filename, 'rb'))
               
                self.temp_val=float(self.temp.currentText()[9:20])
                self.rain_val=float(self.rain.currentText()[9:20])
                self.pest_val=float(self.pesticide.text())
                 
                self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                self.pred=self.model.predict(self.input)[0]
                self.accuracy=0.8
                self.absplage=self.pred*(1-self.accuracy)
                self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
        elif self.bsname=="beans":  
            if self.pesticide.text()=="":
                QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
            else:
                model_filename="models_dir/yield_dir/algeria_yield/Beans_model.pkl"
                self.model=pickle.load(open(model_filename, 'rb'))
               
                self.temp_val=float(self.temp.currentText()[9:20])
                self.rain_val=float(self.rain.currentText()[9:20])
                self.pest_val=float(self.pesticide.text())
                 
                self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                self.pred=self.model.predict(self.input)[0]
                self.accuracy=0.8
                self.absplage=self.pred*(1-self.accuracy)
                self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
        elif self.bsname=="carrot":
            if self.pesticide.text()=="":
                QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
            else:
                model_filename="models_dir/yield_dir/algeria_yield/Carrots_model.pkl"
                self.model=pickle.load(open(model_filename, 'rb'))
               
                self.temp_val=float(self.temp.currentText()[9:20])
                self.rain_val=float(self.rain.currentText()[9:20])
                self.pest_val=float(self.pesticide.text())
                 
                self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                self.pred=self.model.predict(self.input)[0]
                self.accuracy=0.8
                self.absplage=self.pred*(1-self.accuracy)
                self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
        elif self.bsname=="dates":
            if self.pesticide.text()=="":
                QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
            else:
                model_filename="models_dir/yield_dir/algeria_yield/Dates_model.pkl"
                self.model=pickle.load(open(model_filename, 'rb'))
               
                self.temp_val=float(self.temp.currentText()[9:20])
                self.rain_val=float(self.rain.currentText()[9:20])
                self.pest_val=float(self.pesticide.text())
                 
                self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                self.pred=self.model.predict(self.input)[0]
                self.accuracy=0.8
                self.absplage=self.pred*(1-self.accuracy)
                self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
        elif self.bsname=="lentils":
            if self.pesticide.text()=="":
                QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
            else:
                model_filename="models_dir/yield_dir/algeria_yield/Lentils_model.pkl"
                self.model=pickle.load(open(model_filename, 'rb'))
               
                self.temp_val=float(self.temp.currentText()[9:20])
                self.rain_val=float(self.rain.currentText()[9:20])
                self.pest_val=float(self.pesticide.text())
                 
                self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                self.pred=self.model.predict(self.input)[0]
                self.accuracy=0.8
                self.absplage=self.pred*(1-self.accuracy)
                self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
        elif self.bsname=="maize":
            if self.pesticide.text()=="":
                QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
            else:
                model_filename="models_dir/yield_dir/algeria_yield/Maize_model.pkl"
                self.model=pickle.load(open(model_filename, 'rb'))
               
                self.temp_val=float(self.temp.currentText()[9:20])
                self.rain_val=float(self.rain.currentText()[9:20])
                self.pest_val=float(self.pesticide.text())
                 
                self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                self.pred=self.model.predict(self.input)[0]
                self.accuracy=0.8
                self.absplage=self.pred*(1-self.accuracy)
                self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            if self.pesticide.text()=="":
                QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
            else:
                model_filename="models_dir/yield_dir/algeria_yield/Oranges_model.pkl"
                self.model=pickle.load(open(model_filename, 'rb'))
               
                self.temp_val=float(self.temp.currentText()[9:20])
                self.rain_val=float(self.rain.currentText()[9:20])
                self.pest_val=float(self.pesticide.text())
                 
                self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                self.pred=self.model.predict(self.input)[0]
                self.accuracy=0.8
                self.absplage=self.pred*(1-self.accuracy)
                self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
        elif self.bsname=="potatoes":
            if self.pesticide.text()=="":
                QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
            else:
                model_filename="models_dir/yield_dir/algeria_yield/Potatoes_model.pkl"
                self.model=pickle.load(open(model_filename, 'rb'))
               
                self.temp_val=float(self.temp.currentText()[9:20])
                self.rain_val=float(self.rain.currentText()[9:20])
                self.pest_val=float(self.pesticide.text())
                 
                self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                self.pred=self.model.predict(self.input)[0]
                self.accuracy=0.8
                self.absplage=self.pred*(1-self.accuracy)
                self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
        elif self.bsname=="rice":
            if self.pesticide.text()=="":
                QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
            else:
                model_filename="models_dir/yield_dir/algeria_yield/Rice_model.pkl"
                self.model=pickle.load(open(model_filename, 'rb'))
               
                self.temp_val=float(self.temp.currentText()[9:20])
                self.rain_val=float(self.rain.currentText()[9:20])
                self.pest_val=float(self.pesticide.text())
                 
                self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                self.pred=self.model.predict(self.input)[0]
                self.accuracy=0.8
                self.absplage=self.pred*(1-self.accuracy)
                self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
        elif self.bsname=="tomatoes":
            if self.pesticide.text()=="":
                QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
            else:
                model_filename="models_dir/yield_dir/algeria_yield/Tomatoes_model.pkl"
                self.model=pickle.load(open(model_filename, 'rb'))
               
                self.temp_val=float(self.temp.currentText()[9:20])
                self.rain_val=float(self.rain.currentText()[9:20])
                self.pest_val=float(self.pesticide.text())
                 
                self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                self.pred=self.model.predict(self.input)[0]
                self.accuracy=0.8
                self.absplage=self.pred*(1-self.accuracy)
                self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
        elif self.bsname=="wheat":
            if self.pesticide.text()=="":
                QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
            else:
                model_filename="models_dir/yield_dir/algeria_yield/Wheat_model.pkl"
                self.model=pickle.load(open(model_filename, 'rb'))
               
                self.temp_val=float(self.temp.currentText()[9:20])
                self.rain_val=float(self.rain.currentText()[9:20])
                self.pest_val=float(self.pesticide.text())
                 
                self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                self.pred=self.model.predict(self.input)[0]
                self.accuracy=0.8
                self.absplage=self.pred*(1-self.accuracy)
                self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
                
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::Morocco::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    def morocco_yield(self):
            self.crop_name=Common.current_item
            self.bsname=self.crop_name[7:len(self.crop_name)-4]
            if self.bsname=="apple":
                QMessageBox.about(self,"info","sorry, not available for apple")
            elif self.bsname=="orange":
                QMessageBox.about(self,"info","sorry, not available for orange")
            elif self.bsname=="barley":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/morocco_yield/Barley_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="avocat":  
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/morocco_yield/Avocados_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="carrot":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/morocco_yield/Carrots_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="dates":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/morocco_yield/Dates_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="lentils":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/morocco_yield/Lentils_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="maize":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/morocco_yield/Maize_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
                
            elif self.bsname=="potatoes":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/morocco_yield/Potatoes_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="rice":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/morocco_yield/Rice_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="tomatoes":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/morocco_yield/Tomatoes_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="wheat":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/algeria_yield/Wheat_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
                
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::Egypt::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    def egypt_yield(self):
            self.crop_name=Common.current_item
            self.bsname=self.crop_name[7:len(self.crop_name)-4]
            if self.bsname=="apple":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/egypt_yield/Apples_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="orange":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/egypt_yield/Oranges_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="barley":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/egypt_yield/Barley_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="beans":  
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/egypt_yield/Beans_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="carrot":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/egypt_yield/Carrots_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="dates":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/egypt_yield/Dates_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="lentils":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/egypt_yield/Lentils_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="maize":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/egypt_yield/Maize_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
                
            elif self.bsname=="potatoes":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/egypt_yield/Potatoes_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="rice":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/egypt_yield/Rice_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="tomatoes":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/egypt_yield/Tomatoes_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="wheat":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/egypt_yield/Wheat_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::Burkina::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    def burkina_yield(self):
            self.crop_name=Common.current_item
            self.bsname=self.crop_name[7:len(self.crop_name)-4]
            if self.bsname=="maize":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/burkina_yield/Maize_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="rice":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/burkina_yield/Rice_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="tomatoes":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/burkina_yield/Tomatoes_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))


#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::Cameroon::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    def cameroon_yield(self):
            self.crop_name=Common.current_item
            self.bsname=self.crop_name[7:len(self.crop_name)-4]
            if self.bsname=="maize":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/cameroon_yield/Maize_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="rice":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/cameroon_yield/Rice_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="tomatoes":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/cameroon_yield/Tomatoes_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::Ghana:::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    def ghana_yield(self):
            self.crop_name=Common.current_item
            self.bsname=self.crop_name[7:len(self.crop_name)-4]
            if self.bsname=="maize":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/ghana_yield/Maize_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="rice":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/ghana_yield/Rice_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="tomatoes":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/ghana_yield/Tomatoes_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::Guinea:::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    def guinea_yield(self):
            self.crop_name=Common.current_item
            self.bsname=self.crop_name[7:len(self.crop_name)-4]
            if self.bsname=="maize":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/guinea_yield/Maize_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="rice":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/guinea_yield/Rice_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="tomatoes":
                    QMessageBox.about(self,"info","not available")
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::Lybia:::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    def lybia_yield(self):
            self.crop_name=Common.current_item
            self.bsname=self.crop_name[7:len(self.crop_name)-4]
            if self.bsname=="maize":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/lybia_yield/Maize_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="tomatoes":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/lybia_yield/Tomatoes_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="rice":
                    QMessageBox.about(self,"info","not available")

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::Madagascar:::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    def madagascar_yield(self):
            self.crop_name=Common.current_item
            self.bsname=self.crop_name[7:len(self.crop_name)-4]
            if self.bsname=="maize":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/mada_yield/Maize_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="rice":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/mada_yield/Rice_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="tomatoes":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/mada_yield/Tomatoes_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::Mali:::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    def mali_yield(self):
            self.crop_name=Common.current_item
            self.bsname=self.crop_name[7:len(self.crop_name)-4]
            if self.bsname=="maize":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/mali_yield/Maize_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="rice":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/mali_yield/Rice_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="tomatoes":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/mali_yield/Tomatoes_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::Mauritania:::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    def mauritania_yield(self):
            self.crop_name=Common.current_item
            self.bsname=self.crop_name[7:len(self.crop_name)-4]
            if self.bsname=="maize":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/mauritania_yield/Maize_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="rice":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/mauritania_yield/Rice_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="tomatoes":
                    QMessageBox.about(self,"info","not available")
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::Tunisia:::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    def tunisia_yield(self):
            self.crop_name=Common.current_item
            self.bsname=self.crop_name[7:len(self.crop_name)-4]
            if self.bsname=="apple":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/tunisia_yield/Apples_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="Apricot":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/tunisia_yield/Apricots_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="barley":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/tunisia_yield/Barley_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="dates":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/tunisia_yield/Dates_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="lentils":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/tunisia_yield/Lentils_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="tomatoes":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/tunisia_yield/Tomatoes_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::Qatar::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    def qatar_yield(self):
            self.crop_name=Common.current_item
            self.bsname=self.crop_name[7:len(self.crop_name)-4]
            if self.bsname=="barley":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/Qatar_yield/Barley_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="dates":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/Qatar_yield/Dates_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))
            elif self.bsname=="tomatoes":
                if self.pesticide.text()=="":
                    QMessageBox.about(self,"Missing Fields","Give value for pesticides use!")
                else:
                    model_filename="models_dir/yield_dir/Qatar_yield/Tomatoes_model.pkl"
                    self.model=pickle.load(open(model_filename, 'rb'))
                
                    self.temp_val=float(self.temp.currentText()[9:20])
                    self.rain_val=float(self.rain.currentText()[9:20])
                    self.pest_val=float(self.pesticide.text())
                    
                    self.input=np.array([[self.temp_val],[self.rain_val],[self.pest_val]]).reshape(1,-1)
                    self.pred=self.model.predict(self.input)[0]
                    self.accuracy=0.8
                    self.absplage=self.pred*(1-self.accuracy)
                    self.yields.setText(str("       "+str(round(self.pred/10000,5))))
                    self.precision.setText(str("       "+"± "+str(round(self.absplage/10000,5))))