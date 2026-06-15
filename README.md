


Comando Para CI 
¡Excelente! Vamos a poner orden en todo el proceso. Esto es lo que se conoce como X11 Forwarding (enviar la interfaz gráfica de un sistema a otro).

Aquí tienes la guía definitiva paso a paso para que tu calculadora "salte" del contenedor a tu pantalla de Windows.

Paso 1: Configurar el Servidor X (VcXsrv)
Abre la aplicación XLaunch que instalaste y sigue estos pasos al pie de la letra:

Select display settings: Elige "Multiple windows". Haz clic en Next.

Select how to start clients: Elige "Start no client". Haz clic en Next.

Extra settings:

Aquí marca "Disable access control". (Esto es vital, es el permiso para que Docker pase).

Puedes dejar el resto marcado por defecto (Clipboard, Native OpenGL).

Haz clic en Next.

Finish: Haz clic en Finish.

Ejecutador
docker run --rm -it -e DISPLAY=host.docker.internal:0 mi-calculadora

o

Admin open MiCalculadora.bat

