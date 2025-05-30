PROYECTO FINAL ING SOFTWARE 3
# PROYECTO FINAL ING SOFTWARE 3

Este proyecto es una aplicación web desarrollada con Django para la gestión de propinas, pedidos y usuarios (clientes y trabajadores) en un restaurante.

## Estructura del Proyecto

- **Cliente/**: Módulo para la gestión de clientes.
- **Trabajador/**: Módulo para la gestión de trabajadores y locales.
- **Servicio/**: Módulo para la gestión de servicios (pedidos) y propinas.
- **propinas/**: Configuración principal del proyecto Django.
- **manage.py**: Script para la administración del proyecto.

## Requisitos

- Python 3.11+
- Django 5.2.1
- MySQL Server
- Paquetes adicionales:
  - `pyautogui`
  - `mysqlclient` o `PyMySQL` (para conectar Django con MySQL)
  - `webbrowser` (incluido en la librería estándar de Python)

## Instalación

1. **Clona el repositorio**  
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd propinas
   ```

2. **Crea y activa un entorno virtual**  
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias**  
   ```sh
   pip install django==5.2.1 pyautogui mysqlclient
   ```

4. **Configura la base de datos MySQL**  
   - Crea una base de datos llamada `propinas`.
   - Ajusta el usuario y contraseña en `propinas/settings.py` si es necesario.

5. **Aplica las migraciones**  
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crea un superusuario para el panel de administración**  
   ```sh
   python manage.py createsuperuser
   ```

7. **Ejecuta el servidor de desarrollo**  
   ```sh
   python manage.py runserver
   ```

8. **Accede a la aplicación**  
   - Cliente: [http://127.0.0.1:8000/LogIn/](http://127.0.0.1:8000/LogIn/)
   - Trabajador: [http://127.0.0.1:8000/LogIn_2/](http://127.0.0.1:8000/LogIn_2/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Funcionalidades

- **Clientes**: Registro, inicio de sesión, consulta y calificación de servicios, propinas y recomendaciones por WhatsApp.
- **Trabajadores**: Inicio de sesión, creación de clientes y pedidos, edición de pedidos.
- **Administrador**: Gestión de usuarios, locales, servicios y propinas desde el panel de Django.

## Notas

- El sistema utiliza sesiones para controlar el acceso de trabajadores y clientes.
- El envío de recomendaciones por WhatsApp requiere tener WhatsApp Web abierto y permisos para controlar el teclado (pyautogui).
- Los archivos de configuración de la base de datos están en `propinas/settings.py`.

## Licencia

Uso académico.