# mi_script.py
import platform
import datetime
from zoneinfo import ZoneInfo

AUTOR = "Ioav Mizrachi | Mateo Muñoz"  # Nombres completos del saludo y del README, en el mismo orden; para parejas usa "Nombre 1 | Nombre 2".

def main():
    print(f"Autor: {AUTOR}")
    print(f"Sistema Operativo: {platform.system()} {platform.release()}")
    ahora_co = datetime.datetime.now(ZoneInfo("America/Bogota"))
    fecha_formateada = ahora_co.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Fecha y hora desde Python: {fecha_formateada}")

if __name__ == "__main__":
    main()