# Creación y Uso de Entornos Virtuales en Python con Visual Studio Code

Este tutorial está basado en las transcripciones "Entornos Virtuales con Python (Módulo virtualenv)" y "Cómo crear un entorno virtual en Visual Code con Python 2024". En él te guiaré paso a paso sobre cómo crear y manejar entornos virtuales en Python utilizando **Visual Studio Code** y la herramienta **virtualenv**. 

Los entornos virtuales son fundamentales para mantener los proyectos Python organizados y evitar conflictos entre librerías de diferentes proyectos.

---

## **Índice**
1. ¿Qué es un entorno virtual y por qué es importante?
2. Requisitos previos
3. Crear un entorno virtual desde la terminal en Visual Studio Code
4. Activar y desactivar el entorno virtual
5. Instalar paquetes en el entorno virtual
6. Exportar e importar dependencias usando `requirements.txt`
7. Conclusión

---

## **1. ¿Qué es un entorno virtual y por qué es importante?**

Un **entorno virtual** es un entorno aislado que permite tener una instalación independiente de Python y sus librerías para un proyecto específico. Esto es útil para evitar conflictos entre diferentes versiones de librerías o frameworks que pueden ser necesarias para distintos proyectos.

- **Ejemplo**: Si tienes un proyecto que requiere **Django 3.0** y otro que necesita **Django 4.0**, usar un entorno virtual te permitirá mantener ambos proyectos separados sin interferencias.

---

## **2. Requisitos previos**

Antes de comenzar, asegúrate de tener lo siguiente:

- **Python instalado**: Si no lo tienes, puedes descargarlo desde [python.org](https://www.python.org/downloads/). Durante la instalación, asegúrate de marcar la opción "Agregar Python al PATH".
- **Visual Studio Code**: Descárgalo desde [Visual Studio Code](https://code.visualstudio.com/) si no lo tienes instalado.
- **Extensión Python para Visual Studio Code**: En Visual Studio Code, asegúrate de instalar la extensión de Python para que funcione correctamente.

---

## **3. Crear un entorno virtual desde la terminal en Visual Studio Code**

### **Paso 1: Crear la carpeta de trabajo**

1. Abre **Visual Studio Code**.
2. Crea una nueva carpeta en tu computadora que servirá como directorio del proyecto, por ejemplo, `proyecto_entorno`.
3. Abre esa carpeta en Visual Studio Code arrastrándola dentro del editor o seleccionando **Archivo > Abrir carpeta**.

### **Paso 2: Crear el entorno virtual**

1. Abre la **terminal integrada** en Visual Studio Code. Ve a **Ver > Terminal** o presiona `Ctrl + ñ` en Windows/Linux o `Cmd + ñ` en macOS.
2. Dentro de la terminal, navega a la carpeta del proyecto que creaste previamente (si aún no estás allí) con el comando:
   ```bash
   cd ruta_de_tu_carpeta
   ```
3. Ejecuta el siguiente comando para instalar **virtualenv** si no lo tienes instalado:
   ```bash
   pip install virtualenv
   ```
4. Ahora, crea el entorno virtual con el siguiente comando:
   ```bash
   virtualenv env
   ```
   - **Nota**: El nombre `env` es comúnmente utilizado para nombrar el entorno virtual, pero puedes cambiarlo por cualquier otro nombre.

Después de unos segundos, se habrá creado el entorno virtual en una carpeta llamada `env` dentro de tu proyecto.

---

## **4. Activar y desactivar el entorno virtual**

### **Activar el entorno virtual**

- **Windows**: 
   - Una vez creado el entorno, activa el entorno virtual con el siguiente comando en la terminal:
     ```bash
     .\env\Scripts\activate
     ```
   - Si aparece un error relacionado con permisos, puedes intentar:
     ```bash
     .\env\Scripts\activate.bat
     ```

- **Mac/Linux**:
   - Usa el siguiente comando para activar el entorno:
     ```bash
     source env/bin/activate
     ```

Después de activar el entorno, verás el nombre del entorno entre paréntesis al inicio de la línea en la terminal, lo que indica que estás trabajando dentro de él.

### **Desactivar el entorno virtual**

Una vez que termines de trabajar en tu proyecto y quieras salir del entorno virtual, simplemente ejecuta:
```bash
deactivate
```

---

## **5. Instalar paquetes en el entorno virtual**

Una vez que el entorno virtual esté activado, puedes instalar las librerías y dependencias que tu proyecto necesite. Para hacerlo, usa `pip` de la misma forma en que lo harías normalmente:

### **Instalar paquetes**

Por ejemplo, si quieres instalar **Flask**, usa el siguiente comando:
```bash
pip install flask
```

Este comando instalará Flask solo dentro del entorno virtual, sin afectar a otros proyectos.

### **Ver los paquetes instalados**

Puedes ver qué paquetes están instalados dentro del entorno virtual ejecutando:
```bash
pip list
```

Este comando mostrará una lista de todos los paquetes instalados en ese entorno específico.

---

## **6. Exportar e importar dependencias usando `requirements.txt`**

### **Exportar dependencias**

Es común que quieras compartir los paquetes que has instalado en tu entorno virtual para que otros puedan replicar tu configuración. Para hacerlo, puedes crear un archivo `requirements.txt` con los paquetes instalados:

1. Asegúrate de estar dentro del entorno virtual.
2. Ejecuta el siguiente comando para generar el archivo:
   ```bash
   pip freeze > requirements.txt
   ```

Esto creará un archivo `requirements.txt` en tu proyecto que lista todas las dependencias con sus versiones exactas.

### **Importar dependencias en otro entorno virtual**

Si más tarde quieres configurar otro entorno virtual y tener los mismos paquetes instalados, usa el siguiente comando para instalar todo lo que esté listado en el archivo `requirements.txt`:

1. Asegúrate de estar en el nuevo entorno virtual.
2. Ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

Esto instalará todas las librerías mencionadas en el archivo `requirements.txt`.

---

## **7. Conclusión**

Usar entornos virtuales es fundamental para mantener la organización en proyectos Python, ya que te permite trabajar con versiones específicas de librerías y evitar conflictos con otros proyectos. Con los pasos que hemos cubierto, ya sabes cómo crear, activar, desactivar y manejar entornos virtuales usando **Visual Studio Code**. Además, aprendiste cómo exportar e importar las dependencias de tu proyecto utilizando `requirements.txt`, lo que facilita la portabilidad de tu trabajo.

Con este conocimiento, podrás trabajar de manera eficiente en tus proyectos Python y asegurarte de que cada uno tenga sus propias dependencias controladas. ¡Ahora estás listo para usar entornos virtuales en todos tus proyectos de Python! 
