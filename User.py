from io import open;

class User:

    def __init__(self, Password, Name, TypeOfUser):
        self.__Password = Password;
        self.__Name = Name;
        self.__TypeOfUser = TypeOfUser;

    def __FirstTime(self, TypeOfUser):

        if TypeOfUser == "root":
            File = Open("usr/root/root.dat", "r");
        else:
            if TypeOfUser == "admin"":
                File = open("usr/admin/admin.dat", "r");
            else:
                if TypeOfUser == "assistant":
                    File = open("usr/assistant/assistant.dat", "r");
                else:
                    return 3;  # Error: Usuario no encontrado.

        Line = File.readline();

        if Line[0] == TypeOfUser and Line[1] == TypeOfUser:
            File.close();
            return True;
        else:
            File.close();
            return False;

    def __CreateUser(self,Name,Password,TypeOfUser):
        if TypeOfUser == "assistant":
            File = open("usr/assistant/assistant.dat","ab");
            File.write(str(Name + " " + Password + "\n"));
            File.close();
        else:
            if TypeOfUser == "root":
                File = open("usr/root/root.bin","wb");
                File.write(str(Name + " " + Password + "\n"));
                File.close();
            else:
                if TypeOfUser = "admin":
                    File = open("usr/admin/admin.bin","wb");
                    File.write(str(Name + " " + Password + "\n"));
                    File.close();



    def SetNewPassword(self, Name, OldPassword, NewPassword):


    def Check(self,Name,Password,TypeOfUser):
        First = self.__FirstTime(self.__TypeOfUser)

        if First == True:
            self.__CreateUser(Name,Password,TypeOfUser);
        else:
            if First = False:
                if TypeOfUser == "root":
                    File = open("usr/root/root.bin","rb");
                else:
                    if TypeOfUser == "admin":
                        File = open("usr/admin/admin.bim","rb");
                    else:
                        if TypeOfUser == "assistant":
                            File = open("usr/assistant/assistant.bin","rb");




class root(User):

    def __init__(self, Name, Password):
        self.__Password = Password;
        self.__Name = Name;
        self.__TypeOfUser = "root";

    def SetPassword(self, Password):


class admin(User):
    pass

class Assistant(User):
    pass

