


class HISCG: 

        # 0 Datos de Unidad
        UNIDAD_MEDICA = ""
        EXPEDIENTE = ""
        FECHA_DE_ELABORACION = ""
        HORA_DE_ELABORACION = ""
        TIPO_DE_INTERROGATORIO = ""

        # I. FICHA DE  IDENTIFICACION
        NONBRE_DEL_PACIENTE = "" #(APELLIDO PATERNO, APELLIDO MATERNO Y NOMBRE (S))
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

        #Seccion 0;

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
