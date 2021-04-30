from qgis.PyQt.QtWidgets import * 
from .Tabla_impactos_dialog import Ui_dlg_impactos 

#creareos nuestra clase para la tabla de impactos a partir de la importancia de la clase de tabla impactos dialog 
class tabla_dialog(QDialog,Ui_dlg_impactos):
    def __init__(self):
        super(tabla_dialog,self).__init__()   
        #cambiar el tamano del campo Tipo paara darle mas amplitud
        self.setupUi(self)  
        


