import subprocess
import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("Directorio creado exitosamente.")
    else:
        print("El directorio ya existe.")

def command_maker_react(directory):
    print("Esto puede tardar unos minutos (depende de su internet)")
    output = subprocess.check_output(f"npx create-react-app {directory}", shell=True)
    print(output.decode())

def command_maker_js(directory):
    html = open(f"{directory}/index.html", "w")
    js = open(f"{directory}/main.js", "w")
    css = open(f"{directory}/style.css", "w")

    html.write('<!DOCTYPE html>\n'
               '<html lang="en">\n'
               '  <head>\n'
               '    <meta charset="utf-8" />\n'
               '    <title></title>\n'
               '  <meta name="viewport" content="initial-scale=1, width=device-width" />\n'
               '  </head>\n'
               '  <body>\n'
               '  </body>\n'
               '</html>\n')

    js.write("alert('test')")

    css.write("* {\n\n}")

    html.close()
    js.close()
    css.close()

    print("Archivos generados exitosamente")

def command_maker_arduino():
    print("Ruta: ")
    path = input()
    print("Nombre del proyecto")
    project_name = input()

    path_full = path + "/" + project_name

    create_directory(path_full)

    ino = open(f"{path_full}/{project_name}.ino", "w")
    ino.write("void setup(){\n\n}\n")
    ino.write("\nvoid loop(){\n\n}\n")
    ino.close()
    print("Archivos generados exitosamente")

if __name__ == "__main__":
    print("Selecciona una opción")
    print("1- React Vanilla (default)\t2- JS Vanilla\t3- Arduino")
    value = input("-> ")
    directory_path = ''
    if value != '3':
        directory_path = input("Ruta (con carpeta vacía) => ")
    
    match value:
        case ''|'1':
            command_maker_react(directory_path)
        case '2': 
            command_maker_js(directory_path)
        case '3':
            command_maker_arduino()            
