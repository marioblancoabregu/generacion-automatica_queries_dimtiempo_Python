from datetime import datetime, timedelta
import calendar


#======================================================= VALORES MANUALES CAMBIO MENSUAL ======================================================
daniosemana = 14
nsemanaEMPRESA = 14
ndiaAnio = 91 #(+1 según BD)
ndiaSeman = 1 #(+1 según BD)
inicioSemana_Rt = datetime(2026, 3, 30)
finSemana_Rt = inicioSemana_Rt + timedelta(days=6)
n = 3  # daniosemana (+1 según BD)
m = 3  # nsemEMPRESA (+1 según BD)
#======================================================== VALORES MANUALES CAMBIO ANUAL =======================================================
dia_reinicio_EMPRESA = 365  # Día a partir del cual reinicia anioEMPRESA (Revisar Calendario EMPRESA)
anioEMPRESA = 2026  # Año inicial EMPRESA
anioid = 15 # Aumenta 1 cada año
#==============================================================================================================================================


#CAMBIAR IDIOMA daniomes
meses_en = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
meses_es = ["Ene.", "Feb.", "Mar.", "Abr.", "May.", "Jun.",
            "Jul.", "Ago.", "Sep.", "Oct.", "Nov.", "Dic."]

#PARÁMETROS DINÁMICOS
hoy = datetime.today() + timedelta(days=7) #Genera el mes siguiente 7 dias despues del dia actual
anio = hoy.year
mes = hoy.month
fechafin = calendar.monthrange(anio, mes)[1] #toma el rango del mes por generar
daniomes = hoy.strftime("%m.%b.") #Crea un formato juntando los meses en números y letras
abreviado = daniomes[3:6] #Delimita los meses en 2 partes de 3 caracteres
nmesEMPRESA = mes #toma los valores de mes para usarlo como nmesEMPRESA y reiniciarlo a fin de año (como todo el calendario EMPRESA)

if abreviado in meses_en:
    idx = meses_en.index(abreviado) #Toma el índice de los meses en inglés como referencia
    daniomes = f"{mes:02d}.{meses_es[idx]}" #Convierte en texto el mes tomando el índice en español

#TRIMESTRE Y SEMANA ACTUAL
trimestres = {1: "I", 2: "I", 3: "I", 4: "II", 5: "II", 6: "II",
              7: "III", 8: "III", 9: "III", 10: "IV", 11: "IV", 12: "IV"}
trim = trimestres[mes]

x = {1: "1", 2: "1", 3: "1", 4: "2", 5: "2", 6: "2",
              7: "3", 8: "3", 9: "3", 10: "4", 11: "4", 12: "4"}
nsemanatrimestre = x[mes]

dtrimestreEMPRESA = trim #Lo mismo que nmesEMPRESA
#CALCULO AUTOMÁTICO
aniomesid = (anio - 2025) * 12 + mes + 155 #155=aniomesid(enero2025)

gl_reiniciado = False  # para controlar cuándo ocurre el reinicio EMPRESA

#GENERADOR DE QUERIES
for i in range(1, fechafin + 1): #Buclé para generar los días del mes
    fecha_actual = datetime(anio, mes, i) #Crea los días
    fecha_str = fecha_actual.strftime("%Y-%m-%d") #Crea el formato de la fecha

    #CONTROL DE REINICIO EMPRESA
    if not EMPRESA_reiniciado and ndiaAnio == dia_reinicio_EMPRESA: #Compara los dias ndiaAnio con los actuales para poder reiniciar el año
        anioEMPRESA += 1 #Si la fecha actual y ndiaAnio coinciden que cambien los sgtes datos EMPRESA:
        nsemanaEMPRESA = '1'
        dtrimestreEMPRESA = 'I'
        nmesEMPRESA = '1'
        EMPRESA_reiniciado = True  # no volver a reiniciar dentro del mismo ciclo

    insert_sql = (
        f"INSERT INTO date_dimension VALUES('{fecha_str}','{anio}-{daniosemana}','{anioEMPRESA}','{nsemanaEMPRESA}',"
        f"'{anio}','{mes}','{daniomes} {anio}','{trim}','{i}','{ndiaAnio}','{ndiaSeman}','{mes}',"
        f"'{nsemanatrimestre}','{anio}-{mes:02d}-01','{anio}-{mes:02d}-{fechafin}','{anio}-{mes:02d}',"
        f"'{aniomesid}','425','{anioid}','{inicioSemana_Rt.strftime('%Y-%m-%d')}',"
        f"'{finSemana_Rt.strftime('%Y-%m-%d')}','{nmesEMPRESA}','{dtrimestreEMPRESA}','1')"
    )

    print(insert_sql)


    #AVANCES DE CONTADORES
    n += 1 #Se genera el mismo número 7 veces y reinicia conteo al 8vo conteo
    if n == 8:
        daniosemana += 1
        n = 1

    m += 1 #Lo mismo que daniosemana
    if m == 8:
        if isinstance(nsemanaEMPRESA, int):
            nsemanaEMPRESA += 1
        inicioSemana_Rt = finSemana_Rt + timedelta(days=1)
        finSemana_Rt = inicioSemana_Rt + timedelta(days=6)
        m = 1

    ndiaSeman += 1 #Se generan números del 1 al 7 y reinicia al 8vo conteo
    if ndiaSeman == 8:
        ndiaSeman = 1

    ndiaAnio += 1 #Para reiniciar el día para el sgte año
    if ndiaAnio == 365:  # ===========Año bisiesto; cambia a 366 si no lo es============
        ndiaAnio = 1
