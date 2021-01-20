
import os
from io import open


def CreateDirAndFile(ID, Data):
       if os.path.exists(str("exp" + os.sep + str(ID))):
               try:
                       File = open(str("exp" + os.sep + str(ID) + os.sep + str(ID) + ".expe"),"a+");
                       File.write(Data);
                       File.close();
               except IOError:
                       return False;
       else:
               try:
                        os.mkdir(str("exp" + os.sep+ str(ID)))
               except OSError:
                       return False;

        return True;

def SClean(String):

        Aux = str();

        for i in String:
                Aux += i if i != "\n" else " ";


        Res = (len(Aux) + 1 % 3)

        Res = 3 - Res;

        if Res > 0:
                for i in range(Res):
                        Aux += " ";
        return Aux;

class HISCG: 

        # 0 Datos de Unidad
        UNIDAD_MEDICA = ""
        EXPEDIENTE = ""
        FECHA_DE_ELABORACION = ""
        HORA_DE_ELABORACION = ""
        TIPO_DE_INTERROGATORIO = ""

        # I. FICHA DE  IDENTIFICACION
        NOMBRE_DEL_PACIENTE = "" #(APELLIDO PATERNO, APELLIDO MATERNO Y NOMBRE (S))
        EDAD = ""
        FECHA_DE_NACIMIENTO = ""
        OCUPACION_DEL_PACIENTE = ""
        DOMICILIO = ""
        TELEFONO = ""
        NOMBRE_DEL_PADRE_O_TUTOR = ""
        PARENTESCO_CON_EL_PACIENTE = ""

        # II. ANTECEDENTES HEREDOFAMILIARES
        AntHer = ""

        # III. ANTECEDENTES PERSONALES  NO PATOLOGICOS
        AntPerNoPat = ""

        # IV. ANTECENTES PERSONALES PATOLOGICOS
        AntPerPat = ""

        # V. ANTECEDENTES GINECOLOGICOS
        AntGin = ""

        # VI. PADECIMIENTO ACTUAL
        PadAct = ""

        # VII. INTERROGATORIO POR APARATOS  Y SISTEMAS
        CARDIOVASCULAR = ""
        RESPIRATORIO = ""
        GASTROINTESTINAL = ""
        HEMATICO_Y_LINFATICO = ""
        ENDOCRINO = ""

        #VII. INTERROGATORIO POR APARATOS Y SISTEMAS
        NERVIOSO = ""
        MUSCULOESQUELETICO  = ""
        PIEL_MUCOSAS_Y_ANEXOS = ""

        # VIII. SIGNOS VITALES
        TENSION_ARTERIAL  = ""
        TEMPERATURA  = ""
        FRECUENCIA_CARDIACA = ""
        FRECUENCIA_RESPIRATORIA = ""
        PESO = ""
        TALLA = ""

        # IX EXPLORACION FISICA
        HABITUS_EXTERIOR = ""
        CABEZA = ""
        CUELLO = ""
        TORAX = ""
        ABDOMEN = ""

        GENITALES = ""
        EXTREMIDADES = ""
        PIEL = ""
        # X. RESULTADOS PREVIOS  Y ACTUALES DE LABORATORIO, GABINETE Y OTROS:
        ResPreActLabGabOtr = ""

        # XI. DIAGNOSTICOS O PROBLEMAS  CLINICOS:
        DiaProCli = ""

        # XII. TRATAMIENTO FARMACOLOGICO\
        TraFar = ""
        TERAPEUTICA_EMPLEADA_Y_RESULTADOS_PREVIOS = ""
        TERAPEUTICA_ACTUAL = ""

        # XIII. PRONOSTICO
        Pro = ""


        #Metodos para establcer Valores

        #Seccion 0

        def SetUNIDAD_MEDICA(self,UnidadMedica):
                self.UNIDAD_MEDICA = UnidadMedica;

        def SetEXPEDIENTE(self, Expediente):
                self.EXPEDIENTE = Expediente;

        def SetFECHA_DE_ELABORACION(self,FechaDeElaboracion):
                self.FECHA_DE_ELABORACION = FechaDeElaboracion;

        def SetHORA_DE_ELABORACION(self,HoraDeElaboracion):
                self.HORA_DE_ELABORACION = HoraDeElaboracion;

        def SetTIPO_DE_INTERROGATORIO(self,TipoDeInterrogatorio):
                self.TIPO_DE_INTERROGATORIO = TipoDeInterrogatorio;

        #Seccion  I

        def SetNOMBRE_DEL_PACIENTE(self,NombreDelPaciente): #(APELLIDO PATERNO, APELLIDO MATERNO Y NOMBRE (S))
                self.NONBRE_DEL_PACIENTE = NombreDelPaciente;

        def SetEDAD(self,Edad):
                self.EDAD = Edad;

        def SetFECHA_DE_NACIMIENTO(self,FechaDeNacimiento):
                self.FECHA_DE_NACIMIENTO = FechaDeNacimiento

        def SetOCUPACION_DEL_PACIENTE(self,OcupacionDelPaciente):
                self.OCUPACION_DEL_PACIENTE = OcupacionDelPaciente;

        def SetDOMICILIO(self, Domicilio):
                self.DOMICILIO = Domicilio;

        def SetTELEFONO(self,Telefono):
                self.TELEFONO = Telefono;

        def SetNOMBRE_DEL_PADRE_O_TUTOR(self,NombreDelPadreOTutor):
                self.NOMBRE_DEL_PADRE_O_TUTOR = NombreDelPadreOTutor;

        def SetPARENTESCO_CON_EL_PACIENTE(self,ParentescoConELPaciente):
                self.PARENTESCO_CON_EL_PACIENTE = ParentescoConELPaciente;

        # II. ANTECEDENTES HEREDOFAMILIARES

        def SetAntHer(self,Antecedentes):
                self.AntHer = Antecedentes

        # III. ANTECEDENTES PERSONALES  NO PATOLOGICOS
        def SetAntPerNoPat(self,AntPerNoPat):
                self.AntPerNoPat = AntPerNoPat;

        # IV. ANTECENTES PERSONALES PATOLOGICOS
        def SetAntPerPat(self, AntPerPat):
                self.AntPerPat = AntPerPat;

        # V. ANTECEDENTES GINECOLOGICOS
        def SetAntGin(self,AnteGin):
                self.AntGin = AnteGin;

        # VI. PADECIMIENTO ACTUAL
        def SetPadAct(self,PadActual):
                self.PadAct = PadActual

        # VII. INTERROGATORIO POR APARATOS  Y SISTEMAS
        def SetCARDIOVASCULAR(self, CarVas):
                self.CARDIOVASCULAR = CarVas;

        def SetRESPIRATORIO(self,Resp):
                self.RESPIRATORIO = Resp

        def SetGASTROINTESTINAL(self, Gas):
                self.GASTROINTESTINAL = Gas;

        def SetHEMATICO_Y_LINFATICO(self,HemLin):
                self.HEMATICO_Y_LINFATICO = HemLin;

        def SetENDOCRINO(self, Endocrino):
                self.ENDOCRINO = Endocrino;

        #VII. INTERROGATORIO POR APARATOS Y SISTEMAS
        def SetNERVIOSO(self,Ner):
                self.NERVIOSO = Ner;

        def SetMUSCULOESQUELETICO(self,Mus):
                self.MUSCULOESQUELETICO =  Mus;

        def SetPIEL_MUCOSAS_Y_ANEXOS(self,PiMuAne):
                self.PIEL_MUCOSAS_Y_ANEXOS = PiMuAne;

        # VIII. SIGNOS VITALES
        def SetTENSION_ARTERIAL(self,TenArt):
                self.TENSION_ARTERIAL = TenArt;

        def SetTEMPERATURA(self,Tem):
                self.TEMPERATURA = Tem;

        def SetFRECUENCIA_CARDIACA(self,FreCar):
                self.FRECUENCIA_CARDIACA = FreCar;

        def SetFRECUENCIA_RESPIRATORIA(self,FreRes):
                self.FRECUENCIA_RESPIRATORIA = FreRes;

        def SetPESO(self,Peso):
                self.PESO = Peso;

        def SetTALLA(self,Tall):
                self.TALLA = Tall;

        # IX EXPLORACION FISICA
        def SetHABITUS_EXTERIOR(self,HabiExt):
                self.HABITUS_EXTERIOR = HabiExt;

        def SetCABEZA(self,Cab):
                self.CABEZA = Cab;

        def SetCUELLO(self,Cue):
                self.CUELLO = Cue;

        def SetTORAX(self,Tor):
                self.TORAX = Tor;

        def SetABDOMEN(self,Abd):
                self.ABDOMEN = Abd;

        def SetGENITALES(self,Gen):
                self.GENITALES = Gen;

        def SetEXTREMIDADES(self, Ext):
                self.EXTREMIDADES = Ext;

        def SetPIEL(self,Piel):
                self.PIEL = Piel;


        # X. RESULTADOS PREVIOS  Y ACTUALES DE LABORATORIO, GABINETE Y OTROS:

        def SetResPreActLabGabOtr(self,ResPre):
                self.ResPreActLabGabOtr = ResPre;


        # XI. DIAGNOSTICOS O PROBLEMAS  CLINICOS:
        def SetDiaProCli(self, Dia):
                self.DiaProCli = Dia;


        # XII. TRATAMIENTO FARMACOLOGICO\
        def SetTraFar(self,Tra):
                self.TraFar = Tra;

        def SetTERAPEUTICA_EMPLEADA_Y_RESULTADOS_PREVIOS(self,TEYRP):
                self.TERAPEUTICA_EMPLEADA_Y_RESULTADOS_PREVIOS = TEYRP;

        def SetTERAPEUTICA_ACTUAL(self, TA):
                self.TERAPEUTICA_ACTUAL = TA;


        # XIII. PRONOSTICO
        def SetPro(self, Pro):
                self.Pro = Pro;

        #IDP
        def IDP(self):
                try:
                        File = open(str("exp" + os.sep + "IDCount.dat"),"r")
                        ID = int(File.readline());
                        File.close();

                        File = open(str("exp" + os.sep + "IDCount.dat"),"w")
                        File.write(str(ID+1))
                        File.close();

                        return ID;
                except IOError:
                        return -1;

        def Dump(self):

                ID = self.IDP();

                if ID >= 0:

                        # 0 Datos de Unidad
                        self.UNIDAD_MEDICA = SClean(self.UNIDAD_MEDICA) + "\n"
                                CreateDirAndFile(ID, self.UNIDAD_MEDICA);
                        self.EXPEDIENTE = SClean(self.EXPEDIENTE) + "\n"
                        self.FECHA_DE_ELABORACION = SClean(self.FECHA_DE_ELABORACION) + "\n"
                        self.HORA_DE_ELABORACION = SClean(self.HORA_DE_ELABORACION) + "\n"
                        self.TIPO_DE_INTERROGATORIO = SClean(self.TIPO_DE_INTERROGATORIO) + "\n"

                        # I. FICHA DE  IDENTIFICACION
                        self.NOMBRE_DEL_PACIENTE = SClean(self.NOMBRE_DEL_PACIENTE) + "\n" #(APELLIDO PATERNO, APELLIDO MATERNO Y NOMBRE (S))
                        self.EDAD = SClean(self.EDAD) + "\n"
                        self.FECHA_DE_NACIMIENTO = SClean(self.FECHA_DE_NACIMIENTO) + "\n"
                        self.OCUPACION_DEL_PACIENTE = SClean(self.OCUPACION_DEL_PACIENTE) + "\n"
                        self.DOMICILIO = SClean(self.DOMICILIO) + "\n"
                        self.TELEFONO = SClean(self.TELEFONO) + "\n"
                        self.NOMBRE_DEL_PADRE_O_TUTOR = SClean(self.NOMBRE_DEL_PADRE_O_TUTOR) + "\n"
                        self.PARENTESCO_CON_EL_PACIENTE = SClean(self.PARENTESCO_CON_EL_PACIENTE) + "\n"

                        # II. ANTECEDENTES HEREDOFAMILIARES
                        self.AntHer = SClean(self.AntHer) + "\n"

                        # III. ANTECEDENTES PERSONALES  NO PATOLOGICOS
                        self.AntPerNoPat = SClean(self.AntPerNoPat) + "\n"

                        # IV. ANTECENTES PERSONALES PATOLOGICOS
                        self.AntPerPat = SClean(self.AntPerPat) + "\n"

                        # V. ANTECEDENTES GINECOLOGICOS
                        self.AntGin = SClean(self.AntGin) + "\n"

                        # VI. PADECIMIENTO ACTUAL
                        self.PadAct = SClean(self.PadAct) + "\n"

                        # VII. INTERROGATORIO POR APARATOS  Y SISTEMAS
                        self.CARDIOVASCULAR = SClean(self.CARDIOVASCULAR) + "\n"
                        self.RESPIRATORIO = SClean(self.RESPIRATORIO) + "\n"
                        self.GASTROINTESTINAL = SClean(self.GASTROINTESTINAL) + "\n"
                        self.HEMATICO_Y_LINFATICO = SClean(self.HEMATICO_Y_LINFATICO) + "\n"
                        self.ENDOCRINO = SClean(self.ENDOCRINO) + "\n"

                        #VII. INTERROGATORIO POR APARATOS Y SISTEMAS
                        self.NERVIOSO = SClean(self.NERVIOSO) + "\n"
                        self.MUSCULOESQUELETICO  = SClean(self.MUSCULOESQUELETICO) + "\n"
                        self.PIEL_MUCOSAS_Y_ANEXOS = SClean(self.PIEL_MUCOSAS_Y_ANEXOS) + "\n"

                        # VIII. SIGNOS VITALES
                        self.TENSION_ARTERIAL  = SClean(self.TENSION_ARTERIAL) + "\n"
                        self.TEMPERATURA  = SClean(self.TEMPERATURA) + "\n"
                        self.FRECUENCIA_CARDIACA = SClean(self.FRECUENCIA_CARDIACA) + "\n"
                        self.FRECUENCIA_RESPIRATORIA = SClean(self.FRECUENCIA_RESPIRATORIA) + "\n"
                        self.PESO = SClean(self.PESO) + "\n"
                        self.TALLA = SClean(self.TALLA) + "\n"

                        # IX EXPLORACION FISICA
                        self.HABITUS_EXTERIOR = SClean(self.HABITUS_EXTERIOR)
                        self.CABEZA = SClean(self.CABEZA) + "\n"
                        self.CUELLO = SClean(self.CUELLO) + "\n"
                        self.TORAX = SClean(self.TORAX) + "\n"
                        self.ABDOMEN = SClean(self.ABDOMEN) + "\n"

                        self.GENITALES = SClean(self.GENITALES) + "\n"
                        self.EXTREMIDADES = SClean(self.EXTREMIDADES) + "\n"
                        self.PIEL = SClean(self.PIEL) + "\n"
                        # X. RESULTADOS PREVIOS  Y ACTUALES DE LABORATORIO, GABINETE Y OTROS:
                        self.ResPreActLabGabOtr = SClean(self.ResPreActLabGabOtr) + "\n"

                        # XI. DIAGNOSTICOS O PROBLEMAS  CLINICOS:
                        self.DiaProCli = SClean(self.DiaProCli) + "\n"

                        # XII. TRATAMIENTO FARMACOLOGICO\
                        self.TraFar = SClean(self.TraFar) + "\n"
                        self.TERAPEUTICA_EMPLEADA_Y_RESULTADOS_PREVIOS = SClean(self.TERAPEUTICA_EMPLEADA_Y_RESULTADOS_PREVIOS) + "\n"
                        self.TERAPEUTICA_ACTUAL = SClean(self.TERAPEUTICA_ACTUAL) + "\n"

                        # XIII. PRONOSTICO
                        self.Pro = SClean(self.Pro) + "\n"
