import os
from PySide6 import QtWidgets

from package.python.api.statistiques import Statistique, Statistique_double
from package.python.api.constant import STYLEDIR

class StatWindow(QtWidgets.QWidget) :
    def __init__(self,length : int,stat : list[dict[str,int]] = [] , stat_type : int = 1):
        super().__init__()
        self.length = length
        self.stat = stat
        self.stat_type = stat_type
        self.setWindowTitle("Calcul-statistique")
        self.setup_ui()
        with open(os.path.join(STYLEDIR,"mainWindow.css")) as f:
            self.setStyleSheet(f.read())

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.add_widgets_to_layout()
        self.setup_connections()

    def create_widgets(self):
        #le main Layout
        self.main_layout = QtWidgets.QHBoxLayout(self)
        
        #les widgets
        self.tv_stat_table = QtWidgets.QTableWidget(self.length,2)
        self.line_edit = QtWidgets.QTextEdit()

    def modify_widgets(self):
        
        #------------------------------
        #configuration du  Tablwwidget
        #------------------------------
            #----------ajout-de-valeur
        self.tv_stat_table.setHorizontalHeaderLabels(["xi","yi" if self.stat_type == 2 else "ni"])
        # self.tv_stat_table.setItem(0,0,QtWidgets.QTableWidgetItem("test"))
        # self.tv_stat_table.setItem(0,1,QtWidgets.QTableWidgetItem("hi"))
        # self.tv_stat_table.setItem(0,2,QtWidgets.QTableWidgetItem("test"))
        # self.tv_stat_table.setItem(1,0,QtWidgets.QTableWidgetItem("test"))
        # self.tv_stat_table.setItem(1,1,QtWidgets.QTableWidgetItem("test"))
        # self.tv_stat_table.setItem(1,2,QtWidgets.QTableWidgetItem("test"))
        for i in range(self.length):
            this_dict = self.stat[i]
            self.tv_stat_table.setItem(i,0,QtWidgets.QTableWidgetItem(str(this_dict["xi"])))
            self.tv_stat_table.setItem(i,1,QtWidgets.QTableWidgetItem(str(this_dict["yi" if self.stat_type == 2 else "ni"])))
            #------------corrections de la forme des widgets
        self.tv_stat_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tv_stat_table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.tv_stat_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tv_stat_table.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed,QtWidgets.QSizePolicy.Policy.Fixed)
        
        
        #------------------------------
        #configuration du QtextEdit
        #------------------------------
        self.line_edit.setReadOnly(True)
        
        if self.stat_type == 1:
            stat = Statistique(self.stat)
            self.line_edit.setText(f"""
somme effectif : {stat.get_somme_effectif()}
moyenne : {stat.get_moyenne()}
mode : {stat.get_mode()}
xini : {stat.get_xini()}
variance : {stat.get_variance()}
ecart type : {stat.get_ecart_type()}""")
            
        else:
            stat = Statistique_double(self.stat)
            self.line_edit.setText(f"""
somme effectif : {stat.get_sum_n()}
covariance : {stat.get_cov_xy()}
a : {stat.get_a()}
b : {stat.get_b()}
coefficient corellation : {stat.get_coefficient_corellation()}
""")
        
        #------------------------------
        #configuration du mainLayout
        #-----------------------------
        self.main_layout.setContentsMargins(10,20,10,10)
        

    def add_widgets_to_layout(self):
        #------------------------------
        #configuration du premier widget
        #------------------------------
        self.main_layout.addWidget(self.tv_stat_table)
        self.main_layout.addWidget(self.line_edit)

    def setup_connections(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = StatWindow(stat=[
        {
            "xi" : 5,
            "yi" : 25
        },
        {
            "xi" : 6,
            "yi" : 30
        },
        {
            "xi" : 9,
            "yi" : 35
        },
        {
            "xi" : 12,
            "yi" : 45
        },
        {
            "xi" : 18,
            "yi" : 65
        }
    ],length=5,stat_type=2)
    window.show()
    app.exec()