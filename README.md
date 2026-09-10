# Restaurante App (Semana 13)

## 1. Propósito de esta nueva base
El propósito de esta versión base de `restaurante_app` es realizar la transición orientada a objetos desde la aplicación anterior basada en consola hacia una interfaz gráfica de usuario (GUI) utilizando la librería nativa **Tkinter** de Python. 

En esta etapa no se trasladan todas las funcionalidades complejas del restaurante, sino que se establece una **arquitectura base modular y escalable** basada en capas (Modelos, Servicios y Vistas), permitiendo autenticar usuarios, consultar datos desde archivos locales JSON y manejar un flujo de navegación dentro de una única ventana principal.

---

## 2. Estructura de carpetas y archivos

```text
restaurante_app/
├── datos/
│   ├── productos.json       # Persistencia local de los productos del restaurante
│   └── usuarios.json        # Persistencia local de los usuarios registrados
├── modelos/
│   ├── __init__.py          # Convierte la carpeta en paquete de Python
│   ├── producto.py          # Clase Modelo que representa la entidad Producto
│   └── usuario.py           # Clase Modelo que representa la entidad Usuario
├── servicios/
│   ├── __init__.py          # Convierte la carpeta en paquete de Python
│   ├── archivo_servicio.py  # Servicio genérico para la lectura y manejo de archivos JSON
│   └── restaurante_servicio.py # Servicio principal con la lógica de negocio y validaciones
├── ui/
│   ├── __init__.py          # Convierte la carpeta en paquete de Python
│   ├── login_view.py        # Componente de interfaz gráfica para el acceso al sistema
│   └── main_view.py         # Componente de interfaz gráfica para el panel principal
├── main.py                  # Punto de entrada, configuración de dependencias y control de vistas
└── README.md                # Documentación del proyecto



##  3. Flujo de la aplicación
El flujo de ejecución de la aplicación sigue el ciclo mínimo requerido:

Inicio: Se ejecuta main.py, el cual crea la ventana principal de Tkinter (tk.Tk()) y gestiona una única instancia de la aplicación.

Inicialización de Servicios: Se instancia RestauranteServicio, cargando la información de usuarios.json y productos.json a través de ArchivoServicio.

Pantalla de Login (LoginView): La aplicación muestra el formulario de ingreso.

Validación de Credenciales: El usuario ingresa su credencial. LoginView solicita a RestauranteServicio validar el acceso.

Si los campos están vacíos o son incorrectos, la vista muestra una retroalimentación en pantalla.

Si las credenciales son válidas, se procede al cambio de vista.

Panel Principal (MainView): Oculta la vista de Login y despliega el panel de control. El servicio provee las listas de productos y usuarios cargados para mostrarlos en tablas de Tkinter (ttk.Treeview).

Cierre de Sesión: El botón de "Cerrar Sesión" en la interfaz principal destruye/oculta MainView y vuelve a mostrar LoginView dentro del mismo ciclo mainloop(), sin abrir ventanas secundarias.

## 4. Vistas implementadas
LoginView (ui/login_view.py):

Diseñada con componentes ttk.

Contiene cajas de texto para usuario y contraseña.

Ofrece un mensaje de retroalimentación visual en caso de datos inválidos o vacíos.

No accede directamente a los archivos JSON, sino que delega la autenticación al servicio.

MainView (ui/main_view.py):

Muestra un saludo personalizado con el nombre y rol del usuario autenticado.

Organizada mediante pestañas (ttk.Notebook):

Pestaña Productos: Muestra el listado de productos consultados a través del servicio.

Pestaña Usuarios: Muestra los usuarios del sistema cargados desde el servicio.

Pestaña Ventas: Identificada claramente como funcionalidad pendiente para próximas entregas del curso.

## 5. Pasos necesarios para ejecutar main.py
Requisitos previos
Tener instalado Python 3.8 o superior.

Contar con la librería nativa tkinter (incluida automáticamente en las instalaciones estándar de Python para Windows y macOS).

5. Pasos necesarios para ejecutar main.py
Requisitos previos
Tener instalado Python 3.8 o superior.

Contar con la librería nativa tkinter (incluida automáticamente en las instalaciones estándar de Python para Windows y macOS).

Instrucciones de ejecución
Clonar o descargar el repositorio:
Asegúrate de que la carpeta del proyecto mantenga la estructura completa de archivos descrita.

Abrir la terminal o consola de mandos:
Navega hasta la carpeta raíz del proyecto (restaurante_app):

Bash
cd restaurante_app
Ejecutar el archivo principal:
Ejecuta el siguiente comando en la terminal:

Bash
python main.py
(En algunos sistemas Linux/Mac puede requerir python3 main.py).

Credenciales de prueba:
Puedes ingresar al sistema utilizando las credenciales registradas en datos/usuarios.json:

Usuario: Malena Ramirez | Contraseña: 123

Usuario: Luis Campos | Contraseña: 123