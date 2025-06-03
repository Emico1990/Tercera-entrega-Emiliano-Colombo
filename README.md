
# Mi primer Blog. Tercera entrega Curso Python

## Pasos para instalar y configurar el entorno
Tipos de terminal: 
    powershell barras para atras "\"
    bash barras para delante "/"

### Paso 1. Crear un entorno virtual
Se crea un entonrno virtual para evitar dañar el sistema y poder trabajar de manera independiente sin afectar otros proyectos. 

Nos movemos por terminal a la carpeta del proyecto: `cd mi_primer_blog` + enter
Ahora creamos el entorno virtual en la terminal, con: `python -m venv v_blog` + enter (Loading...)
Activamos el entorno virtual: `source v_blog/Scripts/activate` + enter (Se utiliza terminal bash en VSC)
Cuando este OK te va a aparecer entre paréntesis (v_blog)

### Paso 2. Instalar django dentro del entorno virtual anterior
Dentro de la terminal de VSC escribimos: `pip install django` + enter (Loading...)

#### Iniciar/Activar el proyecto 
En terminal escribimos: `django-admin startproject mi_primer_blog`


### Paso 3. Modificaciones en archivo Settings.py
Dentro de settings.py, buscar la línea DATABASES y modificar el valor del atributo NAME cambiando el string por `blog.db`
\

ORIGINAL: `'NAME': BASE_DIR / 'db.sqlite3' ` \
MODIFICADO: `'NAME': BASE_DIR / 'blog.db'  `

Luego nos dirigimos a la línea LENGUAGE_CODE y modificamos el lenguajea "es" y en TIME_ZONE indicamos la zona horaria de nuestro país.

ORIGINAL: \
    `LANGUAGE_CODE = 'en_us'`\
    `TIME_ZONE = 'UTC'` 

MODIFICADO: \
    `LANGUAGE_CODE = 'es'`\
    `TIME_ZONE = 'America/Uruguay/Montevideo'`


### Paso 4. Iniciar APP
En terminal a la misma altura del archivo de manage.py ejecutamos el comando: `python manage.py startapp blog_app` (Loading...)

blog_app puede ser modificado por el nombre que se desee para la aplicación en cuestion, ejemplo: cursos, clientes, etc.

### Paso 5. Crear tablas para la base de datos de la app
Por terminal, escribir `python manage.py migrate` (Loading...)
Esto nos genera los archivos correspondientes a la base de datos que tendrán el nombre de (para este caso) blog.db

### Paso 6. Aplicaiones instaladas dentro de la BD
En el archivo settings.py, buscar la línea INSTALLED_APPS y agregar la línea" ` "blog_app", `

### Paso 7. CREAR LAS TABLAS DE LA BASE DE DATOS 
Nos dirigimos al archivo models.py dentro de la carpeta blog_app y añadimos las clases correspondientes. En este proyecto, las clases son: Autor, Posteo, Categoria. 

### Paso 8. AñADIR LAS TABLAS CREADAS A LA BASE DE DATOS
En la terminal y dentro de la carpeta de proyecto, escribimos: `python manage.py makemigrations` + enter (Loading... rapidín)

Luego en la terminal escribimos: `python manage.py migrate` + enter (Loading...)

### Paso 9. CONFIGURAR URLS DE LA APP
Dentro de la carpeta de la app, blog_app, creamos un archivo llamado urls.py. 

Dentro de urls.py (el que acabamos de crear) en la línea urlpatterns agregás:\
`path('admin/', admin.site.urls),` (ya viene por defecto)\
`path("app/", include("blog_app.urls")),`

Además importaremos views `from . import views` al comienzo del archivo urls.py recién creada.

Ahora nos dirigimos al archivo views.py (dentro de blog_app) y creamos las funciones correspondientes: Autor, Posteo y Categoria

### Paso 10. LEVANTAR SERVER
