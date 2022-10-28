from pickle import TRUE
from PyQt5.QtWidgets import QMessageBox
import re

def CustomerCheckValidation(self,FullName,PersonalId,Room):
   
    if not (FullName and FullName.strip()) :
        QMessageBox.about(self, 'Warning', 'Full name is empty')
    else:
        if not (PersonalId and PersonalId.strip()) :
            QMessageBox.about(self, 'Warning', 'Personal Id is empty')
        else:
            if not (Room and Room.strip()) :
                QMessageBox.about(self, 'Warning', 'Room is empty')
            else:                  
                if not PersonalId.isnumeric() :
                    QMessageBox.about(self, 'Warning', 'Personal Id must be number')
                else:                
                    if len(FullName) > 150:
                        QMessageBox.about(self, 'Warning', 'Full name must be less than 150 characters')
                    else:
                        if len(PersonalId) > 12:
                            QMessageBox.about(self, 'Warning', 'Personal Id must be Less than 12 characters')
                        else:
                            if len(Room) >250:
                                QMessageBox.about(self, 'Warning', 'Room must be less than 50 characters')
                            else:
                                return True

    return False
def ParkCheckValidation(self,Area,NumberofSlot):
    if not (Area and Area.strip()) :
        QMessageBox.about(self, 'Warning', 'Full name is empty')
    else:
        if not (NumberofSlot and NumberofSlot.strip()) :
            QMessageBox.about(self, 'Warning', 'Number of slot is empty')
        else:
            if len(Area) >50 :
                QMessageBox.about(self, 'Warning', 'Area must be less than 50 character')
            else:
                if not NumberofSlot.isnumeric():
                    QMessageBox.about(self, 'Warning', 'Number of slot must be number')
                else:
                    if len(NumberofSlot)>10:
                        QMessageBox.about(self, 'Warning', 'Number of slot must be less than 10 character')
                    else:
                        return True 
    return False
