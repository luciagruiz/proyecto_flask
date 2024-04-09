# Enunciado
# Vamos a crear una aplicación web a partir de un fichero json (podéis utilizar el mismo que empleásteis en vuestro proyecto) con las siguientes características:
    • La aplicación debe tener una hoja de estilo. Para ello lo mejor es que busques una plantilla HTML/CSS.
    • Las plantillas que uses en la aplicación se heredarán de la plantilla base.html (esta plantilla la puedes crear a partir de la plantilla HTML que has buscado).
    • La plantilla base tendrá al menos dos bloques: uno para indicar el título y otro para poner el contenido.
    • La página principal tendrá una imagen con el logotipo al pulsar sobre está imagen nos llevará a una página /xxxs.
    • La página /xxxs nos mostrara un buscador, para ello pon un formulario con un cuadro de texto donde puedas poner el nombre de un xxx que quieres buscar. Cuando pulséis el botón de buscar enviará la información a la página /listaxxxs. El formulario enviará los datos con el método POST.
    • En la página /listaxxxs (qué sólo se puede acceder por el método POST) aparecerán los xxxs cuyo nombre empiezan por la cadena que hemos añadido al formulario. Si no hemos indicado ninguna cadena mostrará todos los xxxs.
    • La página /listaxxxs mostrará una tabla generada dinámicamente a partir de los datos de vuestro fichero json y la búsqueda que se haya realizado.
    • La tabla tendrá al menos tres columnas: en la primera aparecerá el nombre, en la segunda otra información relevante y en la tercera habrá un enlace con la palabra “Detalle” que me llevará a la página del xxx con la ruta /xxx/<identificador> o /xxx?id=xxxxxxxxxx.
    • Como ves, estamos volviendo a hacer el patrón de diseño : Lista - detalle. La lista está en la página /listaxxx y el detalle está en la página /xxx/<identificador> o /xxx?id=xxxxxxx donde aparecerán todos los datos del xxx que tenga ese identificador. Si el identificador no existe devolverá un 404. Tendrá un enlace que me devuelve a la página /xxxs.
    • Teneís que buscar una Plataforma como Servicio (PaaS) basada en la nube que sea gratuita (Railway, Dokku,,..).y desplegar vuestra aplicación en ella. Debéis indicar el proceso de despliege en la misma.
# Hasta aquí es suficiente para sacar la mitad de los puntos que vale la práctica. Te propongo varias mejoras que irán sumando puntos al resultados final, tienes que hacerlas en orden y puede hacer las que quieras.
    1. Realizar la búsqueda utilizando una sola ruta: Es decir que en la página /xxxs este el formulario de búsqueda y la lista de xxxs seleccionado. La información del formulario se enviará a la misma página. No existirá la página /listaxxxs.
    2. Como el protocolo HTTP no tiene estado, no es capaz de acordarse de los datos anteriores, por lo tanto cada vez que hagáis una búsqueda aparecerá la lista de xxxs pero el formulario estará vacío, no recuerda lo que pusimos. Modifica el programa para que aparezca en el formulario la cadena que habías introducido en la búsqueda (Pista: tendrá que utilizar el atributo value del elemento input).
    3. Añade otro criterio de búsqueda. Para buscar por ese segundo criterio vas a generar dinámicamente una lista desplegable (elemento select) en el formulario con las valores de los xxx). 
    4. De la misma forma que en el apartado 1 programar la lista desplegable para que recuerde la opción elegida en la búsqueda. (Pista: Usar el atributo selected del elemento option del elemento select)
# ¿Qué debes entregar?
    1. La url del repositorio github donde has desarrollado el programa. Recuerda que debes hacer el programa poco a poco y que los cambios lo tienes que ir guardando con distintos commits.
    2. Debes entregar la URL de la aplicación funcionando en la plataforma PaaS seleccionada
    3. Entrega capturas de pantallas de las páginas de la aplicación desplegada en la plataforma como servicio elegida donde se vean todos los elementos que se han solicitado.
    4. Indica qué mejoras has desarrollado 
