from requests import get
from sys import (exit, argv)
from os import (remove, path, environ, system)
from shutil import (unpack_archive, rmtree)
import threading
from subprocess import (Popen, run)
import subprocess
import tkinter as tk
from tkinter import ttk
from base64 import b64decode


## Objetivo ##
"""
    Este programa se basa en un lanzador de tu programa propio,
    este va a comprobar que exista alguna version y si es asi
    la va a descargar e reemplazar por la anterior version del programa

    This program is based on a launcher for your own program.
    It will check if there is any version, and if so,
    it will download and replace the previous version of the program.
    
"""



###--- VARIABLES ---###

nombre_del_programa = "JLJ Launcher"

nombre_del_exe_a_ejecutar = "LegendCraft.exe"

######################################################
######             Ruta del programa            ######
######################################################

ruta_programa = f"C:\\{nombre_del_programa}\\LegendCraft"

nombre_archivo_version = f"{ruta_programa}\\data\\vers.txt"


# URL donde se aloja el programa comprimido o 
url_update = "http://badomain.ddns.net:8000/update/launcher_LegendCraft.zip"

# URL PasteBin, para comprobar 
url_pastebin = "https://pastebin.com/raw/eqDAeJci"
version_nueva = get(url_pastebin).content.decode('utf-8')

icon_base64 = ("iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAAnFBMVEUAAAAYNikMMCgOPzU+LRILJB4PQzoWLCEOQDUWJhxJNxYOPzUoHgoIJR8NQDUZU0kQOzIWKB0pHgqKzcU3wKqn/fKk/e+V9+uI8uaX4dmJ39Uz7cw05cU11bo6zLM3xasqyKwcl4GLZyeJZiYdind+YCgfgG4XbF5kTR4VYlQYU0hKNxUMRjsaPTQNQDYMPDMqHwoIKiUIJSAJIh29/1pjAAAAFXRSTlMAHyElJCVCQr2929rb29zf39/5+/oczHVZAAAEUklEQVR42u2YjXKiMBSFFbW2q7DdH+m2grZWpbBAmvD+77Zwb0IawKEjJplZ+zG2znSq35zk5KIjQ0wWeTdfAsYEvK8lsL8EpCQnAmMC4wlw8z1RESojzTi3iwrv+69HhV8ZQwytPUkeVwqPWVFiVMD3V35NJcDAwKCAQilgfAn8D6xMCgAWBQiAm9AvH6YEHLX/0dMDYiQB7D8g+v+04TysTAjI6Sf6/7B5BswJqLvfuoAvBXybAlvTArL/5pfAq/vvf9yE24cVoE9g3N3/P2UDt5uSJz6O713EWP//oMhTkgH38xmice3b/cfoAXdmbfMx4L8XyK42AXX+t2bASqOAc6r/KNDs/52jv/9bOHkCYL1p9N/RNP8het+H/iPBGgiJ6L+5+Y+sawFWYV4gUAWuM4HAiICX8/7DHjSYwPhk/5FNCPzW2H/P8zrmP9Z/HaYEkP3XuPZl+Db773fXL2dX2n8UCK7iBFTv/4f335mofHL+x83+h43+jz/fa4XbE/84FvP/d4go/S/XPjmz/7imksWkZ/6Ha+S5p/8XF1ioAkFLgAEmBPAtewQMJxAYFlATCET99Ap4BECBQCYANhcRSKsr9W4mwLh7/qdxuA6AcPD8VwXSmOMh4jxwbr2ShVf3X5w7wbq6zu5/O4GYk+aANxF/19P/0wJiL3QL9Kz9UIFIJrDoTUCDgPUEImUPGE4gFUuQk4oPAgTQlIAcs17dAsTjtarn/yZAnofN/zYT5MZLc7iOHBfxRP9fOMG6Z/4PWApSLcVxv3/Z7/dHyiqKXET/sgdeevs/ZC+gAIACtCAtAZgE8v5fpwBlrC3Q2P12EjAmcCqBwIhAwZjVJSCU0vKRb4MwDD7UsDX/NQigASdCjmEAbFr91yMgifCMjsKe/usSOEYwIkBA2f0GBWQChgWQGEABawmgQKBXwOtJQFP/2/cFR6T0OEIZhcD2UvO//74ASOIoiqurfA6fWoim/vd/TiB5BWF6+t//SSlHCGWAQQE4gZoC9JoS4KQWBSKjCYynwPw+Q5K4uuJEJkArXF01nN59Q96Qv5STcwjH1XQQTb/9Rd44jLGCFQUjOdJaCt0ClAFUFcgIMyXAENpKwJ4AYkLgUAkUTQH7eyDTswemyLwp8MNFSANKL3oeyP4fXuE6vCNL/gZzF04gRhn/3TwPnEtFf9jtdq+vu1pgOgJmbnUeAPiEXHYvSIHXkwIqQoBdVgAT2HUKFExSUK0JdAuoaBHABIAuAXMJ9AswOngPTFTmdQKcJSLGrXPnqmQEOF9goXL/xnkHfi7nU2TEcWYSPBcAdrZArpJJAWB58gVlK+CyKAAMFZBYFZAJHK4yASISOFgSSOHHG2eJ9IzX1rlw55wrECMJLSrYDz7/p6MeZirOaIAAIM90Q4j8a4HCuAACX/6BgP0ECjsJANeYAEHyJE7gKwDjLYB7fEZrmGkBVgMmzJYA8iXwJXCNAv8AoR4VirPjj5cAAAAASUVORK5CYII=")
icon_data = b64decode(icon_base64)
## NO TOCAR ##

cerrar = False

### FUNCIONES ###
## Todas estas funciones son unicamente para este archivo, es independiente del resto ##

def comprobar_archivo_version():
    print(f"Comprobar si existe el documento {nombre_archivo_version}")
    if existe_archivo(nombre_archivo_version):
        print("Archivo encontrado")
    else:
        print("Archivo no encontrado")
        crear_archivo_version(nombre_archivo_version)
    

def existe_archivo(nombre_archivo):
    # Funcion que comprueba la existencia de un archivo
    try:
        with open(nombre_archivo, 'r'):
            return True
    except FileNotFoundError:
        return False


def crear_archivo_version(nombre_archivo):
    print("Aqui entra a crear el archivo")
    try:
        with open(nombre_archivo, 'w') as archivo:
            # Puedes agregar contenido al archivo si lo deseas
            archivo.write("0.00")
        print(f"El archivo '{nombre_archivo}' se ha creado con éxito.")
    except Exception as e:
        print(f"Error al crear el archivo: {str(e)}")

def comprobar_server_online():
    try:

        # Realiza una solicitud GET a la URL
        response = get(url_update, timeout=4)  # Puedes ajustar el tiempo de espera según tus necesidades

        # Verifica si la solicitud fue exitosa (código de respuesta 200)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return False


def leer_version_actual():
    print("Entra a comprobar la version")

    nombre_archivo = nombre_archivo_version

    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo '{nombre_archivo}': {str(e)}")
    return None


def actualizar():
    print("Aqui entra a actualizar")

    descargar_archivo_desde_url(url_update, f"{ruta_programa}\\launcher.zip")

    borrar_antiguo(f"{ruta_programa}\\data")

    descomprimir(f"{ruta_programa}\\launcher.zip", f"{ruta_programa}")

    borrar_comprimido(f"{ruta_programa}\\launcher.zip")


def descargar_archivo_desde_url(url, nombre_archivo):
    try:
        # Realiza una solicitud GET a la URL
        response = get(url)

        # Verifica si la solicitud fue exitosa (código de respuesta 200)
        if response.status_code == 200:
            # Abre el archivo en modo binario y guarda el contenido descargado
            with open(nombre_archivo, 'wb') as archivo:
                archivo.write(response.content)
            print(f"Archivo '{nombre_archivo}' descargado correctamente.")
        else:
            print(f"Error al descargar el archivo. Código de respuesta: {response.status_code}")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")


def borrar_antiguo(directorio_borrar):

    print("Aqui entra a borrar los archivos")
    try:

        rmtree(directorio_borrar)
    except Exception as e:
        print(f"No se pudo borrar el directorio antes de descomprimir: {str(e)}")


def borrar_comprimido(borrar_archivo_comprimido):
    print("Aqui entra a borrar el archivo comprimido")
    try:
        remove(borrar_archivo_comprimido)
    except FileNotFoundError:
        print("No existe el archivo cargado en variable")
    except Exception as e:
        print(f"No se pudo eliminar el archivo comprimido: {str(e)}")


def descomprimir(ruta_descomprimir, ruta_destino):
    try:
        unpack_archive(ruta_descomprimir, ruta_destino)
    except Exception as e:
        print(f"Error al descomprimir el archivo comprimido: {str(e)}")


def inciar_programa(ruta_al_exe, exe):
    try:
        system(f"start /d \"{ruta_al_exe}\" {exe}")
        print(f"El archivo '{ruta_al_exe}' se está ejecutando en segundo plano.")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{ruta_al_exe}'.")


def grafico():
    global ventana
    ventana = tk.Tk()

    
    ancho_ventana = 400
    alto_ventana = 100

    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana - 100) // 2


    # Configuracion de la ventana
    ventana.title(nombre_del_programa)
    ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')
    ventana.resizable(False, False)
    ventana.iconphoto(True, tk.PhotoImage(data=icon_data))

    

    ### --- Elementos en la ventana --- ###

    espaciovacio = tk.Label(ventana, text="  ")
    espaciovacio.pack()

    etiqueta = tk.Label(ventana, text="Comprobando Actualizaciones")
    etiqueta.pack()

    # - ProgressBar - #
    global progressbar
    progressbar = ttk.Progressbar(ventana, length=300, mode='determinate')
    progressbar.pack()
    progressbar.start(700)
    progressbar.stop()

    ventana.mainloop()

def noconexion():

    global ventana2
    ventana2 = tk.Tk()

    
    ancho_ventana = 225
    alto_ventana = 85

    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana - 100) // 2


    # Configuracion de la ventana
    ventana2.title(nombre_del_programa)
    ventana2.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')
    ventana2.resizable(False, False)
    #ventana2.iconphoto(True, tk.PhotoImage(data=icon_alerta))

    ventana2.bell()

    def cerrar_ventana():
        ventana2.destroy()
        global cerrar
        cerrar = False

    # Función para cerrar completamente el programa
    def cerrar_programa():
        ventana2.destroy()
        global cerrar
        cerrar = True

    ### --- Elementos en la ventana --- ###

    espaciovacio = tk.Label(ventana2, text="  ")
    espaciovacio.pack()

    etiqueta = tk.Label(ventana2, text="No hay conexión con el servidor.\n¿Ejecutar el Launcher encontrado?")
    etiqueta.pack()

    espaciovacio = tk.Label(ventana2, text="            ")
    espaciovacio.pack(side="left")

    aceptar = tk.Button(ventana2, text="Aceptar", command=cerrar_ventana)
    aceptar.pack(side="left", padx=10)

    cerrar = tk.Button(ventana2, text="Cancelar", command=cerrar_programa)
    cerrar.pack(side="left")

    ventana2.mainloop()

def noconexionnolauncher():

    global ventana3
    ventana3 = tk.Tk()

    
    ancho_ventana = 275
    alto_ventana = 100

    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana - 100) // 2


    # Configuracion de la ventana
    ventana3.title(nombre_del_programa)
    ventana3.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')
    ventana3.resizable(False, False)

    ventana3.bell()

    def cerrar_programa():
        ventana3.destroy()

    ### --- Elementos en la ventana --- ###

    espaciovacio = tk.Label(ventana3, text="  ")
    espaciovacio.pack()

    etiqueta = tk.Label(ventana3, text="No hay conexión con el servidor.\nY no se ha detectado ningun launcher instalado.\nSaliendo del programa")
    etiqueta.pack()

    cerrar = tk.Button(ventana3, text="Cancelar", command=cerrar_programa)
    cerrar.pack()

    ventana3.mainloop()


if __name__ == '__main__':

    window_hilo = threading.Thread(target=grafico)

    window_hilo.start()

    # comprobar si existe la estructura de carpetas, si no, la crea
    if path.exists(ruta_programa) == False:
        system(f"mkdir \"{ruta_programa}\\data\"")
        crear_archivo_version(nombre_archivo_version)

    else:
        print("Ya existe la carpeta del programa")

    # Llama a la funcion para comprobar si el servidor esta online y devuelve True o False
    if comprobar_server_online() == False:
        print("El servidor esta offline")
        
        if path.exists(f"{ruta_programa}\\data\\{nombre_del_exe_a_ejecutar}"):
            window_hilo_2 = threading.Thread(target=noconexion)
            window_hilo_2.start()

            window_hilo_2.join()
            if cerrar == False:
                inciar_programa(f"{ruta_programa}\\data", nombre_del_exe_a_ejecutar)
            else:
                ventana.quit()
                exit(0)

        else:
            window_hilo_3 = threading.Thread(target=noconexionnolauncher)
            window_hilo_3.start()

            window_hilo_3.join()
            ventana.quit()
            exit(1)

    else:
        print("El servidor esta online")

        progressbar.step(20)

        version_actual = leer_version_actual()

        print(version_actual)
        print(version_nueva)
        if version_nueva != version_actual:
            actualizar()

        progressbar.step(40)

        inciar_programa(f"{ruta_programa}\\data", nombre_del_exe_a_ejecutar)

    progressbar.step(39.99)


    ventana.quit()