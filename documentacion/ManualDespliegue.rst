.. header::
	Manual de Despliegue

===========================================================================================
Sistema de registro de Producción y Almacén | Oficina de Publicaciones e Impresiones | UNCP
===========================================================================================

Este sistema ha sido desarrollado con software libre pero el despliegue de la aplicación era 
necesario realizarlo en Windows xp (que es el requerimiento del cliente y este es el sistema
operativo actual con el que se cuenta en la oficina), cabe señalar que la instalación de este
software solo se realizará en una máquina (de la jefatura).

Los primeros pasos a realizar son la instalación de los siguientes programas:

**Python**

Python es un lenguaje de programación de alto nivel que se caracteriza por ser multifuncional,
multiparadigma y es libre (Python Software Fundation License).
Para empezar debemos descargarlo desde aquí http://www.python.org/download/. Luego al ejecutar
el instalador se mostrará la ventana de inicio, seleccionaremos "Install for all users" luego a
Next >.

.. image:: images/python/py1.png
	:height: 800px
	:width: 1000 px

Luego seleccionaremos donde se va a instalar Python en este caso será en el disco D, D:\Python27, 
solo debemos seleccionarlo y darle click en Next >

.. image:: images/python/py2.png
	:height: 800px
	:width: 1000 px

El siguiente paso es seleccionar que características de Python se desea instalar, lo dejaremos como
esta por defecto y le damos click en Next > (si se quisiera modificar alguna característica se da
click en los iconos que se desprenden del árbol de Python).

.. image:: images/python/py3.png
	:height: 800px
	:width: 1000 px
	
Luego podemos observar como se completa la instalación de Python

.. image:: images/python/py4.png
	:height: 800px
	:width: 1000 px
	
Y en la última ventana podremos ver que la instalación está lista y le damos click en Finish y de 
esta manera Python 2.7 ya está en la pc, ahora tendremos que seguir unos pasos de configuración para
poder ejecutar Python desde el terminal de Windows XP.

.. image:: images/python/py5.png
	:height: 800px
	:width: 1000 px

Para la siguiente configuración nos dirijimos a MI PC y damos click derecho para ver las Propiedades,

.. image:: images/python/py6.png
	:height: 1200px
	:width: 1000 px

Seleccionaremos en la ventana, la pestaña de Opciones Avanzadas y damos click en Variables de entorno.

.. image:: images/python/py7.png
	:height: 1000px
	:width: 900 px

Luego en el área de Variables del Sistema, seleccionamos la variable Path y damos click en modificar,

.. image:: images/python/py8.png
	:height: 1000px
	:width: 900 px
	
Ya en la ventana que se nos muestra agregamos la ruta en la que se encuentra instalado Python, en este
caso escribimos D:\Python27, finalmente damos click en Aceptar.

.. image:: images/python/py9.png
	:height: 1000px
	:width: 900 px
	
Y con esto se termina la configuración de Python para que pueda ser utilizado incluso desde la terminal 
de Windows XP.

**Django**

Después de haber instalado Python, tenemos que instalar Django, para esto descargamos esto 
http://modwsgi.googlecode.com/files/mod_wsgi-win32-ap22py27-3.3.so 

.. image:: images/django/django-project.png
	:height: 1200px
	:width: 1900 px
	
luego haremos lo siguiente: este archivo deberemos copiarlo en la ruta donde hemos instalado Apache, en este caso
en C:\Program Files\Apache Software Foundation\Apache2.2\modules

.. image:: images/django/2.png
	:height: 1000px
	:width: 1400 px
	
Después de esto debemos crear un directorio llamado wsgi_app fuera de la ruta en la que nos encontramos, por ejemplo
en C:\wsgi_app desde la que se administrará el mod_wsgi-application

.. image:: images/django/4.png
	:height: 1000px
	:width: 1400 px

Debemos encontrar el archivo httpd.conf-file y abrirlo con un editor de textos, en mi caso se encuentra en la siguiente
ruta C:\Program Files\Apache Software Foundation\Apache2.2\conf\httpd.conf

.. image:: images/django/5.png
	:height: 1000px
	:width: 1400 px

Luego debemos buscar las líneas de "LoadModule" y donde estas terminen, agregar lo siguiente: 
LoadModule wsgi_module modules/mod_wsgi.so

.. image:: images/django/6.png
	:height: 1000px
	:width: 1400 px
	
Luego debemos ubicar el bloque <Directory> y escribiremos lo siguiente:

WSGIScriptAlias /wsgi “C:/wsgi_app/wsgi_handler.py”

<Directory “C:/wsgi_app”>
AllowOverride None
Options None
Order deny,allow
Allow from all
</Directory>

.. image:: images/django/7.png
	:height: 1000px
	:width: 1400 px


**Apache**

El servidor HTTP Apache es un servidor web HTTP que implementa el protocolo HTTP/1.1 y la noción de sitio virtual.
Para empezar con la instalación, ingresaremos a httpd.apache.org/download.cgi y seleccionaremos el archivo llamado
Win32 Binary including OpenSSL 0.9.8r (MSI Installer).
Después de esto ejecutaremos el archivo obtenido, veremos esta ventana y le daremos click en Next >

.. image:: images/apache/apache0.png
	:height: 800px
	:width: 1000 px
	
Luego en esta ventana aceptaremos los términos de la licencia y daremos click en Next >

.. image:: images/apache/apache1.png
	:height: 800px
	:width: 1000 px

Ahora leeremos información adicional necesaria de saber sobre Apache, luego damos click en Next >

.. image:: images/apache/apache2.png
	:height: 800px
	:width: 1000 px

Nos aparecerá la siguiente ventana en la cual deberemos agregar información, en este caso en el campo de Network
Domain y de Server Name colocaremos localhost, esto es porque debemos probar en nuestra pc si Apache estará 
funcionando correctamente y en el email address colocar el mail del administrador, en este caso es el mail de la
oficina de Publicaciones e Impresiones, en las opciones debajo seleccionaremos que Apache se instale para todos
los usuarios de la pc en el puerto 80 ya que de lo contrario se necesitaria una configuración distinta

.. image:: images/apache/apache3.png
	:height: 800px
	:width: 1000 px
	
Al dar click en Next > en la siguiente ventana seleccionaremos la instalación personalizada (custom) y damos click
a Next >

.. image:: images/apache/apache4.png
	:height: 800px
	:width: 1000 px

Luego, en la venta siguiente veremos el árbol que nos indica todo lo que se instalará en la pc, damos click en Next >

.. image:: images/apache/apache5.png
	:height: 800px
	:width: 1000 px

En la siguiente ventana indicaremos al dar Next > que estamos listos para instalar.

.. image:: images/apache/apache6.png
	:height: 800px
	:width: 1000 px
	
Esperamos el progreso de la instalación

.. image:: images/apache/apache7.png
	:height: 800px
	:width: 1000 px
	
Y listo, habremos terminado con la instalación de Apache dandole click a Finish

.. image:: images/apache/apache8.png
	:height: 800px
	:width: 1000 px
	
Desde cualquier browser al entrar al localhost podremos ver que el servidor Apache está funcionando

.. image:: images/apache/apache9.png
	:height: 800px
	:width: 1000 px

En el desktop podremos ver como ya Apache se encuentra funcionando y nos muestra las opciones de Stop
y Restart para usarlos si es necesario.

.. image:: images/apache/apache10.png
	:height: 800px
	:width: 1000 px

**SmartGit**

Ahora instalaremos SmartGit, este es un cliente gráfico para manejar git, el sistema controlador de versiones que se usó para el desarrollo, lo descargaremos de la página
http://www.syntevo.com/smartgit/download.html, al descargar el archivo comprimido, le daremos click al archivo setup

.. image:: images/smartgit/smartgit0.png
	:height: 800px
	:width: 1000 px
	
Obtendremos la ventana de inicio de instalación y daremos click a Next >

.. image:: images/smartgit/smartgit1.png
	:height: 800px
	:width: 1000 px
	
A continuación seleccionaremos la ubicación en la que lo instalaremos, en este caso dejaremos la ruta por defecto 

.. image:: images/smartgit/smartgit2.png
	:height: 800px
	:width: 1000 px
	
Ahora seleccionaremos el folder del menú de inicio que será el lugar para iniciar Smartgit

.. image:: images/smartgit/smartgit3.png
	:height: 800px
	:width: 1000 px
	
Al dar click en Next> encontraremos algunas opciones adicionales

.. image:: images/smartgit/smartgit4.png
	:height: 800px
	:width: 1000 px

En la siguiente ventana veremos si todo ya está listo para empezar con la instalación y damos click en la opción Install

.. image:: images/smartgit/smartgit5.png
	:height: 800px
	:width: 1000 px
	
Aquí podremos observar como la instalación está en progreso

.. image:: images/smartgit/smartgit6.png
	:height: 800px
	:width: 1000 px
	
Y finalmente damos click en Finish lo que nos indicará que habremos terminado con la instalación

.. image:: images/smartgit/smartgit7.png
	:height: 800px
	:width: 1000 px
	
En la siguiente imagen podremos darnos cuenta como Smartgit está funcionando correctamente en la pc de la oficina y desde este se está
administrando el proyecto.

.. image:: images/smartgit/smartgit8.JPG
	:height: 800px
	:width: 1000 px
	
**Notepad++**

Es también importante contar con un editor de textos que nos permita editar nuestros cambios por ejemplo, Notepad++ es una herramienta
libre con licencia GPL que nos permitirá editar lo que necesitemos, una característica importante es que soporta muchos lenguajes de 
programación. Descargaremos la última versión a la fecha desde este link http://notepad-plus-plus.org/download/v5.9.8.html

Al dar click en el archivo ejecutable obtendremos la siguiente ventanita que nos pide indicar el idioma, seleccionaremos español

.. image:: images/notepad++/1.png
	:height: 800px
	:width: 1000 px

Luego nos aparecerá la bienvenida al inicio de instalación de Notepad++

.. image:: images/notepad++/2.png
	:height: 800px
	:width: 1000 px
	
Aceptamos la licencia y le damos click en Siguiente

.. image:: images/notepad++/3.png
	:height: 800px
	:width: 1000 px
	
A continuación elegiremos el lugar de la instalación, en este caso se quedará la ruta por defecto

.. image:: images/notepad++/4.png
	:height: 800px
	:width: 1000 px
	
Luego elegiremos los componentes que deseamos que tenga nuestra instalación

.. image:: images/notepad++/6.png
	:height: 800px
	:width: 1000 px

Y algunos otros detalles 

.. image:: images/notepad++/7.png
	:height: 800px
	:width: 1000 px

Al darle click en instalar, veremos que el proceso de instalación es rápido

.. image:: images/notepad++/8.png
	:height: 800px
	:width: 1000 px
	
Al dar click en Terminar el asistente de configuración nos indicará que hemos finalizado correctamente con la instalación

.. image:: images/notepad++/9.png
	:height: 800px
	:width: 1000 px
	
Finalmente Notepad++ ya estará listo 

.. image:: images/notepad++/10.png
	:height: 800px
	:width: 1000 px
	
Podemos ver como en la pc de la oficina nos permite editar los archivos que necesitemos (en este ejemplo es el archivo de
settings.py) y podemos notar lo interesante que es este editor de textos.

.. image:: images/notepad++/11.JPG
	:height: 800px
	:width: 1000 px

**Dropbox**

Usaremos esta herramienta para poder obtener un backup del archivo de la base de datos que registrará todos los datos que se 
ingresen al día.

Para instalarlo, debemos descargarlo de este link https://www.dropbox.com/, al obtener el archivo, lo ejecutaremos

.. image:: images/dropbox/1.png
	:height: 800px
	:width: 1000 px
	
Obtendremos la ventana de bienvenida para iniciar la instalación

.. image:: images/dropbox/2.png
	:height: 800px
	:width: 1000 px
	
Veremos el proceso de instalación

.. image:: images/dropbox/3.png
	:height: 800px
	:width: 1000 px
	
A continuación deberemos indicar si contamos o no con una cuenta en Dropbox, en esta ocasión crearemos una nueva

.. image:: images/dropbox/4.png
	:height: 800px
	:width: 1000 px
	
En la siguiente ventana completaremos los datos que se nos solicitan y de esta manera nuestra cuenta estará creada

.. image:: images/dropbox/5.png
	:height: 800px
	:width: 1000 px
	
Nosotros podríamos escoger que la cuenta de Dropbox obtenga más especio que 2 GB que es el espacio que se nos da para 
obtenerlo gratuitamente, en este caso eligiremos obtener una cuenta free.

.. image:: images/dropbox/6.png
	:height: 800px
	:width: 1000 px
	
Nos pide escoger el tipo de configuración, seleccionaremos la personalizada

.. image:: images/dropbox/7.png
	:height: 800px
	:width: 1000 px
	
En esta parte tenemos la capacidad de poder elegir en que ruta instalaremos nuestro Dropbox

.. image:: images/dropbox/8.png
	:height: 800px
	:width: 1000 px
	
También seleccionaremos los detalles de la sincronización

.. image:: images/dropbox/9.png
	:height: 800px
	:width: 1000 px
	
Dropbox nos da la bienvenida y nos da la opción de seguir un recorrido en el cual dará información importante, para verlos seguiremos
dando click en Siguiente para terminar de leer esta importante información

.. image:: images/dropbox/10.png
	:height: 800px
	:width: 1000 px
	
La última pantalla sería esta, daremos click en Terminar y la instalación estará lista.

.. image:: images/dropbox/11.png
	:height: 800px
	:width: 1000 px
	
Podremos ver como todo está ahora sincronizado y correctamente instalado
