<h1> Lookdaluv </h1>

![alt text](https://github.com/NicolasMuras/lookdaluv/core/static/images/banner.jpg?raw=true)

<h2><a id="user-content-tabla-de-contenido" class="anchor" aria-hidden="true" href="#tabla-de-contenido"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Tabla de contenido
</h2>
<ul>
  <li><a href="#introduccion-al-proyecto">Introducción al proyecto</a></li>
  <li><a href="#implementacion-del-proyecto">Implementación del proyecto</a></li>
  <li><a href="#instalacion-de-dependencias">Instalación de dependencias</a></li>
  <li><a href="#iniciar-la-aplicacion">Iniciar la aplicación</a></li>
  <li><a href="#comandos-utiles">Comandos utiles</a></li>
</ul>

<h2><a id="user-content-introduccion-al-proyecto" class="anchor" aria-hidden="true" href="#introduccion-al-proyecto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Introducción al proyecto</h2>

Desafio tecnico utilizando Test-Driven Development, Docker, PostgreSQL y Django REST Framework. La idea es simular el ecosistema para una criptodivisa, los usuarios deberan poder intercambiar dicha moneda entre ellos. Realizare la creación de los diferentes endpoints para proporcionar un acceso a las wallets y tambien para gestionar el intercambio de la criptodivisa.

<h2><a id="user-content-implementacion-del-proyecto" class="anchor" aria-hidden="true" href="#implementación-del-proyecto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Implementación del proyecto</h2>
<ul>
<li><strong>Python</strong>: El lenguaje utilizado para la elaboracion del codigo.</li>
<li><strong>Test-Driven Development</strong>: Metodología de trabajo utilizada.</li>
<li><strong>Django</strong>: Framework open-source utilizado para la elaboración del proyecto.</li>
<li><strong>Django REST Framework</strong>: Es una aplicación de django que nos permitira construir el proyecto bajo la arquitectura REST.</li>
<li><strong>Ecosistema Docker (docker, Dockerfile, Docker-Compose)</strong>:  A partir del Dockerfile en el raíz del proyecto se puede compilar la imagen que corre la REST API hecha en Django REST Framework, con todas sus dependencias y código fuente dentro. Con Docker-Compose se puede ejecutar la aplicación con un único comando, creando además un servidor de base de datos PostgreSQL.</li>
<li><strong>PostgreSQL</strong>: Sistema de gestion de base de datos elegido.</li>
<li><strong>Insomnia</strong>: Utilizo insomnia para ir testeando la aplicación mediante requests a medida que avanzo.</li>
</ul>

Empiezo construyendo el proyecto a través de Docker, utilizo como plantilla el Dockerfile de mi proyecto anterior 'CryptoHero III', dicho proyecto tenia un sistema simple para guardar pagos, en esta versión mi idea es ir un paso mas allá, quiero hacer todo siguiendo la metodología TDD y desarrollar aun mas este proceso de transacción.

La idea es utilizar el sistema de blockchain para almacenar los registros de las transacciones, tendremos un sistema que se encargue de encadenar los bloques, los bloques mismos se van a ir llenando de transacciones, al llegar a cierto punto, el bloque se llenara y se añadirá a la blockchain. Por otro lado, tendremos un sistema de autenticación con tokens, este nos permitirá visualizar el balance de nuestra cuenta y emitir transacciones hacia la cuenta de otro usuario. 
Los wallet address se representaran con nombres en lugar de con una cadena alfanumérica aleatoria con el simple motivo de hacerlo mas intuitivo.

<h2><a id="user-content-instalacion-de-dependencias" class="anchor" aria-hidden="true" href="#instalación-de-dependencias"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Instalación de dependencias</h2>

<p>Para correr este proyecto se necesitan las siguientes dependencias:</p>
<ul>
<li><a href="https://www.python.org/" rel="nofollow">Python 3+</a> (sólo necesario para modo desarrollo o testing).</li>
<li><a href="https://docs.docker.com/get-docker/" rel="nofollow">Docker</a>.</li>
<li><a href="https://docs.docker.com/compose/install/" rel="nofollow">Docker compose</a>.</li>
</ul>
<p>Una vez instaladas las dependencias se puede correr la aplicación.</p>

<h2><a id="user-content-iniciar-la-aplicacion" class="anchor" aria-hidden="true" href="#iniciar-la-aplicacion"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Iniciar la aplicación</h2>

La aplicación funciona sobre Docker-Compose, de esta manera se puede correr la misma en cualquier sistema operativo.

El primer paso es ejecutar la aplicación con el comando a continuación.

<pre><code>docker-compose up
</code></pre>
<em>
  Nota: Si es la primera vez que se ejecuta la aplicación, puede haber errores con respecto a existencia de la base de datos 'app', usted puede ejecutar primero el servicio PostgreSQL y crearla con los siguientes comandos.
</em><br>
<br>
<pre>
<code># su postgres
</code>
</pre>

<pre>
<code># psql
</code>
</pre>

<pre>
<code>postgres-# create database app;
</code>
</pre>

Es necesario notar que esto sólo ocurrirá la primera vez que se ejecute la aplicación.

<h2><a id="user-content-comandos-utiles" class="anchor" aria-hidden="true" href="#comandos-utiles"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Comandos utiles</h2>


<strong>Generar demo data:</strong>

Te permite eliminar los datos de la base de datos y volver a crear datos demo que sirven para hacer pruebas.

<pre><code>from core.scripts.generate_demo_data import execute
execute()
</code></pre>

<em>
  Nota: Te advertira sobre si deseas cancelar o continuar con la operación.
</em>

<br>
<br>
<strong>Crear usuario admin:</strong>
<br>
<br>
Te permite crear un usuario para el panel /admin.
<br>
<br>
<pre><code>python manage.py createsuperuser
</code></pre>

<em>
  Nota: Debes seguir las instrucciones.
</em>

<br>
<br>
<strong>Configurar Base de Datos:</strong>
<br>
<br>
Instrucciones para la creación de la base de datos.
<br>
<br>
<pre><code>sudo su postgres
createuser --interactive
psql
CREATE DATABASE lookdaluv;
GRANT ALL PRIVILEGES ON DATABASE lookdaluv TO 'EL ROL RECIEN CREADO';
exit
exit
python manage.py migrate_schemas
</code></pre>

<em>
  Nota: Para sistemas Linux.
</em>
