from datetime import datetime

v_desc = 1.07

while True:
    v_mes = int(input("MES ACTUAL (1-12): "))
    if 1 <= v_mes <= 12:
        break

while True:
    v_dia = int(input("DIA ACTUAL (1-31): "))
    if 1 <= v_dia <= 31:
        try:
            # Intenta crear una fecha con el año actual y los valores proporcionados
            today = datetime(datetime.now().year, v_mes, v_dia)
            break
        except ValueError:
            # Maneja el caso de un día inválido para el mes (por ejemplo, 31 de febrero)
            print("Día inválido para el mes especificado. Inténtelo de nuevo.")

v_dsemana = today.strftime("%A").upper()

# Resto del código a partir de aquí...

v_preciodep = 750
v_preciozv = 1100
v_precioesc = 500

print(f"HOY ES: {v_dsemana}\n")

if v_dsemana in ["LUNES", "MARTES", "MIÉRCOLES"]:
    v_preciodep /= v_desc
    v_preciozv /= v_desc
    v_precioesc /= v_desc

while True:
    v_deportivo = 1
    v_escolar = 1
    v_zapato = 1
    print("QUE TIPO DE CALZADO DESEA?")
    print("DEPORTIVO------(3)")
    print("ESCOLAR--------(2)")
    print("ZAPATO VESTIR--(1)")
    print("SALIR--(0)")
    v_tipzapato = int(input())
    if v_tipzapato > 0:
        print("CALZADOS EXISTENTES, SELECCIONE EL DE SU PREFERENCIA...")
    if v_tipzapato == 3:
        print("MULTITACO FÚTBOL SOCCER------(1)")
        print("TACHONES FÚTBOL SOCCER--------(2)")
        print("TENIS PARA CORREDOR-----------(3)")
        print("BOTINES DE BOX----------------(4)")
        print("REGRESAR AL MENU PRINCIPAL....(0)")
        v_deportivo = int(input())
    if v_tipzapato == 2:
        print("ESCOLAR PARA NIÑO--------(1)")
        print("ESCOLAR PARA NIÑA--------(2)")
        print("TENIS ESCOLAR------------(3)")
        print("REGRESAR AL MENU PRINCIPAL....(0)")
        v_escolar = int(input())
    if v_tipzapato == 1:
        print("CALZADO DE VESTIR CABALLERO------(1)")
        print("CALZADO DE VESTIR DAMA SIN TACÓN-(2)")
        print("CALZADO DE VESTIR DAMA CON TACÓN-(3)")
        print("REGRESAR AL MENU PRINCIPAL....(0)")
        v_zapato = int(input())
    if v_tipzapato > 0 and v_zapato > 0 and v_deportivo > 0 and v_escolar > 0:
        v_talla = input("ESCRIBA SU NÚMERO DE TALLA: ")
        v_colorcal = input("ESCRIBA EL COLOR DEL CALZADO DE SU PREFERENCIA: ")
        v_imp = int(input("DESEA IMPRIMIR SU TICKET?\nSI---(2)\nNO---(1)"))
        if v_imp == 2:
            print(f"EL DÍA DE HOY ES: {v_dsemana}")
            print("TIPO DE CALZADO:")
            if v_tipzapato == 3:
                if v_deportivo == 1:
                    print("MULTITACO FÚTBOL SOCCER")
                if v_deportivo == 2:
                    print("TACHONES FÚTBOL SOCCER")
                if v_deportivo == 3:
                    print("TENIS PARA CORREDOR")
                if v_deportivo == 4:
                    print("BOTINES DE BOX")
            if v_tipzapato == 2:
                if v_escolar == 1:
                    print("ESCOLAR PARA NIÑO")
                if v_escolar == 2:
                    print("ESCOLAR PARA NIÑA")
                if v_escolar == 3:
                    print("TENIS ESCOLAR")
            if v_tipzapato == 1:
                if v_zapato == 1:
                    print("CALZADO DE VESTIR CABALLERO")
                if v_zapato == 2:
                    print("CALZADO DE VESTIR DAMA SIN TACÓN")
                if v_zapato == 3:
                    print("CALZADO DE VESTIR DAMA CON TACÓN")
            print(f"TALLA: {v_talla}")
            print(f"COLOR DEL CALZADO: {v_colorcal}")
            print(f"COSTO FINAL: {v_preciodep}\n")
        print("MUCHAS GRACIAS POR SU PREFERENCIA")
        print("----------ZAPATERIA LOS CAMILOS-------")
        input("Presione cualquier tecla para realizar otra venta ")
