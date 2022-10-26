from PyQt5.QtWidgets import QMessageBox

def StaffCheckFormat(self,UserName,Password,FullName,PersonalId,Address,Phone):
    if not (UserName and UserName.strip()) :
            QMessageBox.about(self, 'Warning', 'Username is empty')
    else:
        if not (Password and Password.strip()) :
            QMessageBox.about(self, 'Warning', 'Password is empty')
        else:
            if not (FullName and FullName.strip()) :
                QMessageBox.about(self, 'Warning', 'Full name is empty')
            else:
                if not (PersonalId and PersonalId.strip()) :
                    QMessageBox.about(self, 'Warning', 'Personal Id is empty')
                else:
                    if not (Address and Address.strip()) :
                        QMessageBox.about(self, 'Warning', 'Address is empty')
                    else:   
                        if not (Phone and Phone.strip()) :
                            QMessageBox.about(self, 'Warning', 'Phone is empty')
                        else:
                            if not PersonalId.isnumeric() :
                                QMessageBox.about(self, 'Warning', 'Personal Id must be number')
                            else:
                                if not Phone.isnumeric() :
                                    QMessageBox.about(self, 'Warning', 'Phone must be number')
                                else:
                                    if len(UserName) > 50 :
                                        QMessageBox.about(self, 'Warning', 'Username must be less than 50 characters')
                                    else:
                                        if len(Password) > 50:
                                            QMessageBox.about(self, 'Warning', 'Password must be less than 50 characters')
                                        else:
                                            if len(FullName) > 150:
                                                QMessageBox.about(self, 'Warning', 'Full name must be less than 150 characters')
                                            else:
                                                if len(PersonalId) > 12:
                                                    QMessageBox.about(self, 'Warning', 'Personal Id must be Less than 12 characters')
                                                else:
                                                    if len(Address) >250:
                                                        QMessageBox.about(self, 'Warning', 'Address must be less than 250 characters')
                                                    else:
                                                        if len(Phone) > 11:
                                                            QMessageBox.about(self, 'Warning', 'Phone must be less than 11 character')
                                                        else:
                                                            return True

    return False
