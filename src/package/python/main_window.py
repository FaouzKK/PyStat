import os
from PySide6 import QtWidgets , QtCore

from package.python.mwidgets import mspinbox , mbutton
from package.python.statwindow import StatWindow
from package.python.api.constant import STYLEDIR

class MainWindow(QtWidgets.QWidget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStat")
        # self.setMinimumSize(600, 400)
        self.setMaximumSize(800, 600)
        self.value_list_xi : dict[str , mspinbox.MSpinBox] = {}
        self.value_list_ni : dict[str , mspinbox.MSpinBox] = {}
        self.setup_ui()
        with open(os.path.join(STYLEDIR,"mainWindow.css"),"r",encoding="utf-8") as f:
            self.setStyleSheet(f.read())
        
        
    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.add_widgets_to_layout()
        self.setup_connections()
    
    def create_widgets(self):
        #le main Layout
        self.get_stat_widget = QtWidgets.QVBoxLayout(self)
        
        #premier Widget : Recuperer les valeurs statistiques
        self.get_stat_first_layout = QtWidgets.QVBoxLayout()
        self.text_label = QtWidgets.QLabel("Veillez configurer votre serie statistique")
        self.serie_type_select = QtWidgets.QComboBox()
            #Layout pour le choix de taille de la serie
        self.serie_lenght_layout = QtWidgets.QHBoxLayout()
        self.serie_lenght_label = QtWidgets.QLabel("Taille de la serie(le nombre d'effectifs) : Limit-20")
        self.serie_lenght = QtWidgets.QSpinBox()
            #---------------------------------------
        self.confirm_config_button = QtWidgets.QPushButton("Confirmer")
        
        #deuxieme Widget : Afficher les valeurs statistiques
        self.enter_value_widgets = QtWidgets.QVBoxLayout()
        self.ev_text_information = QtWidgets.QLabel("Les valeurs a configurer serons rentree ici")
    
    def modify_widgets(self):
        #------------------------------
        #configuration du premier widget
        #------------------------------
        self.serie_type_select.addItems(["Serie simple", "Serie double"])
        self.serie_lenght.setRange(1,20)
        self.get_stat_first_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.get_stat_first_layout.setContentsMargins(QtCore.QMargins(10, 10, 20, 10))
        self.get_stat_first_layout.addItem(QtWidgets.QSpacerItem(0,0,QtWidgets.QSizePolicy.Policy.MinimumExpanding , QtWidgets.QSizePolicy.Policy.Fixed))
        self.get_stat_first_layout.setSpacing(20) 
        self.text_label.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.serie_type_select.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        self.serie_lenght.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.confirm_config_button.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.serie_lenght.setMinimumWidth(100)
        self.ev_text_information.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        
        #------------------------------
        #confriguration du deuxieme widget
        #------------------------------
        self.enter_value_widgets.setContentsMargins(QtCore.QMargins(10, 30, 10, 10))
        self.enter_value_widgets.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
    
    def add_widgets_to_layout(self):
        #------------------------------
        #configuration du premier widget
        #------------------------------
        self.get_stat_first_layout.addWidget(self.text_label)
        self.get_stat_first_layout.addWidget(self.serie_type_select)
            #------Layout pour le choix de taille de la serie---
        self.serie_lenght_layout.addWidget(self.serie_lenght_label)
        self.serie_lenght_layout.addWidget(self.serie_lenght)
        self.get_stat_first_layout.addLayout(self.serie_lenght_layout)
            #----------------------------------------------------
        self.get_stat_first_layout.addWidget(self.confirm_config_button)
        
        #-------------------------------
        #configuration du deuxieme widget
        #-------------------------------
        self.enter_value_widgets.addWidget(self.ev_text_information)

        #------------------------------
        #add to main-Layout
        #------------------------------
        self.get_stat_widget.addLayout(self.get_stat_first_layout)
        self.get_stat_widget.addLayout(self.enter_value_widgets)
    
    def setup_connections(self):
        self.confirm_config_button.clicked.connect(self.add_grid_set_value_widget)
    
    
    def add_grid_set_value_widget(self) :
        serie_type = 1 if self.serie_type_select.currentText() == "Serie simple" else 2
        # print(serie_type,
        serie_lenght = self.serie_lenght.value()
        
        print(self.enter_value_widgets.count() > 1 )
        if self.enter_value_widgets.count() > 1:
            for i in range(self.enter_value_widgets.count()) :
                if i != 0 :
                    item = self.enter_value_widgets.itemAt(i)
                    if item :
                        self.enter_value_widgets.removeItem(item)

        
        self.grid_value_layout = QtWidgets.QGridLayout()
        self.grid_value_layout.setHorizontalSpacing(20)
        self.grid_value_layout.setVerticalSpacing(20)
        # self.grid_value_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        xi = QtWidgets.QLabel("xi :")
        ni = QtWidgets.QLabel("yi :" if serie_type == 2 else "ni :")
        self.grid_value_layout.addWidget(xi, 0, 0,1,1)
        self.grid_value_layout.addWidget(ni, 1, 0,1,1)
        
        self.value_list_ni.clear()
        self.value_list_xi.clear()
        
        for i in range(serie_lenght):
            spn_xi = mspinbox.MSpinBox()
            spn_ni = mspinbox.MSpinBox()
            if serie_type == 1 :
                spn_ni.setMinimum(1)
            self.grid_value_layout.addWidget(spn_xi, 0, i+1,1,1)
            self.grid_value_layout.addWidget(spn_ni,1,i+1,1,1)
            
            self.value_list_xi[f"x{i+1}"] = spn_xi
            self.value_list_ni[f"n{i+1}"] = spn_ni
            
        self.confirm_value_button = mbutton.MPushButton("Confirmer")
        
        self.confirm_value_button.clicked.connect(self.open_stat_window)
        
        self.enter_value_widgets.addLayout(self.grid_value_layout)
        self.enter_value_widgets.addWidget(self.confirm_value_button)
    
    def open_stat_window(self) :
        serie_type = 1 if self.serie_type_select.currentText() == "Serie simple" else 2
        rang = self.value_list_ni.__len__()
        stat : list[dict[str,int]] = []
        for i in range(rang) :
            stat.append({'xi': 0, 'ni': 0}) 
            stat[i]['xi'] = self.value_list_xi[f"x{i+1}"].value()
            stat[i]['ni' if serie_type == 1 else 'xi'] = self.value_list_ni[f"n{i+1}"].value()
            
        self.win = StatWindow(length = rang, stat = stat, stat_type = serie_type)
        self.win.show()
            
            
            