# webSite
Explicación para windows.
Para poder ejecutar el proyecto se debe instalar un IDE de su preferencia, ya sea sublime text, atom o visual studio code
También se necesita instalar python, en este link se puede descargar python: https://www.python.org/downloads/
Iniciando el IDE y abriendo el proyecto procedemos a instalar un entorno virtual,
desde la consola del IDE ejecutará las líneas:
"Pip install virtualenv".
python3.(aquí su versión de python) -m venv env, (ejemplo python3.7 -m venv env).
Estando en la consola en la dirección del proyecto se debe ejecutar "bin/bin/activate" para activar el entorno virtual,
si por alguna razón al abrir la consola se activa el entorno virtual, escribimos deactivate para desactivarla, ya que este entorno no es el que usamos y luego de esto se ejecuta "bin/bin/activate" nuevamente,
si esta vez le indica un error de que no reconoce "bin" es porque tiene habilitado la opción de no ejecutar scripts de terceros, así que debe cerrar el IDE y ejecutarlo como administrador, es decir, click derecho en la aplicación del IDE->Ejecutar como administrador, estando en la consola se corre la línea "Set-ExecutionPolicy Unrestricted" para deshabilitar esta restricción, luego puede habilitarla nuevamente con el comando "Set-ExecutionPolicy Restricted" (esto cuando ya se haya hecho todo y no se va a trabajar más con el proyecto), cerramos el IDE y lo abrimos normalmente.
Estando nuevamente en la consola con la dirección del proyecto ejecutamos bin/bin/activate,
luego de esto instalamos los requerimientos que esto necesita para funcionar a cabalidad así:
"pip install -r requirements.txt"
Luego de esto corremos el servidor escribiendo "python manage.py runserver".
Esta es la dirección de la página principal al correr el servidor
http://localhost:8000/Home/
