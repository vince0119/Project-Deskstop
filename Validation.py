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

def CustomerRegisteredCheckValidation(self,CardID, CustomerID, CarLicense, CarColor, CarModel):
    if not (CardID and CardID.strip()) :
        QMessageBox.about(self, 'Warning', 'Card Id is empty')
    else:
        if not (CustomerID and CustomerID.strip()) :
            QMessageBox.about(self, 'Warning', 'Customer Id is empty')
        else:
            if not (CarLicense and CarLicense.strip()) :
                QMessageBox.about(self, 'Warning', 'Car License is empty')
            else:
                if not (CarColor and CarColor.strip()) :
                    QMessageBox.about(self, 'Warning', 'Car Color is empty')
                else:
                    if not (CarModel and CarModel.strip()) :
                        QMessageBox.about(self, 'Warning', 'Car Model is empty')
                    else:
                        if len(CardID) >10 :
                            QMessageBox.about(self, 'Warning', 'Car Id must be less than 10 characters')
                        else:
                            if not CustomerID.isnumeric() :
                                QMessageBox.about(self, 'Warning', 'Customer Id must be number')
                            else:
                                if len(CarLicense) != 8 :
                                    QMessageBox.about(self, 'Warning', 'Car License must has 8 characters')
                                else:
                                    if len(CarColor) >50 :
                                        QMessageBox.about(self, 'Warning', 'Car Color must be less than 50 characters')
                                    else:
                                        if len(CarModel)>50 :
                                            QMessageBox.about(self, 'Warning', 'Car Model must be less than 50 characters')
                                        else:
                                            return True

