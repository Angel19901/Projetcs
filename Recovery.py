

#Librerias no estandar
import win32api
#Librerias estandar
import os
import shutil


class Recovery:

    def __init__(self):
        pass

    def GetDevices(self):

        drives = win32api.GetLogicalDriveStrings().split('\x00')[:-1]
        drives.remove("C:\\");

        return drives;

    def CreateBackUp(self,Device):

        Name = os.environ["USERNAME"];

        Ruta = "C:" + os.sep + "Users" + os.sep + Name + os.sep + "Documents" + os.sep + "MiConsultorioVirtual" + os.sep;

        if os.path.exists(Device + "usr"):
            try:
                shutil.rmtree(Device + "usr")
            except:
                pass

        if os.path.exists(Device + "exp"):
            try:
                shutil.rmtree(Device + "exp")
            except:
                pass

        if os.path.exists(Device + "dates"):
            try:
                shutil.rmtree(Device + "dates")
            except:
                pass

        try:

            shutil.copytree((Ruta + "usr"),Device + "usr");
            shutil.copytree((Ruta + "exp"),Device + "exp");
            shutil.copytree((Ruta + "dates"),Device + "dates");

        except:

            return 0;

    def Recovery(self, Device):

