# CORRER PROGRAMA CORRECTAMENTE | PYTHON

## Antes de comenzar, asegúrese de que Python 3 no esté instalado en su computadora. 

1. Abrimos la línea de comando a través de la aplicación _Terminal_ que se encuentra en **Aplicaciones -> Utilidades -> Terminal.**
2. Escriba el comando **python --version** seguido de la tecla **Enter** para ver la versión de Python actualmente instalada.

## Instalar XCode

El primer paso para Python 3 es instalar el programa **Xcode** de Apple, que es necesario para el desarrollo de iOS y para la mayoría de las tareas de programación. 

**Usaremos XCode para instalar Homebrew.**

En su aplicación **Terminal**, ejecute el siguiente comando para instalar XCode y sus herramientas de línea de comandos:

1. **xcode-select --install**

## Instalar Homebrew

A continuación, instale **Homebrew** copiando y pegando el siguiente comando en la _Terminal_ y luego presione **Enter**:

1. curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install

**Para confirmar que Homebrew se instaló correctamente, ejecute este comando:**

* brew doctor

## Instalar Python 3

Luego de tener **Homebrew** correctamente instalado, podemos instalar la última versión de **Python 3**. 

Escriba el siguiente comando en la _Terminal_ y presiona **Enter**:

1. brew install python3

Para confirmar qué versión de **Python 3** se instaló, ejecute el siguiente comando en la _Terminal_:

* python3 --version

Debe aparecer algo como: **Python 3.8.5** (_3.8.5_ puede cambiar según su versión instalada).

## Correr script de Python

1. Colocar el documento.py dentro de un folder. 
2. Vamos a la _Terminal_. 
3. Escribimos el comando **cd** (change directory) seguido por el nombre de la carpeta donde se encuentra nuestro documento.py descargado.
4. Procedemos a escribir _python3 [nombredeldocumento].py_
5. El programa debería iniciar su ejecución en la _Terminal_. 

### REFERENCIA: 

1. https://installpython3.com/mac/
