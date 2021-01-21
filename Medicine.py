import os
from io import open


class Medicine:

    ID = 0;
    Name = "";
    Des = "";

    def GetID(self):

        try:

            File = open("med" + os.sep + "IDCount.txt","r");
            ID = int(File.readline());
            File.close();

        except IOError:
            pass;

        try:

            File = open("med" + os.sep + "IDCount.txt","w");
            File.write(str(ID+1));
            File.close();

        except IOError:
            pass;

        self.ID = ID;

    def GetName(self,Name):
        self.Name = Name;

    def GetDes(self,Des):
        self.Des = Des;

    def Dump(self):

        try:
            File = open("med" + os.sep + "Medicinas.csv","a");
            File.write(str(ID) + "," + str(Name) + "," + str(Des) + "\n");
            File.close()
        except IOError:
            pass;

    def load(self):
       try:

           Data =[];
           File = open("med" + os.sep + "Medicinas.csv", "r");

           for Line in File:
               Data.append(Line.split(","));

            return Data;

       except IOError:
           pass;
