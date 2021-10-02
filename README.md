<h1> Lookdaluv </h1>

![alt text](https://github.com/NicolasMuras/CryptoHero_IV/blob/master/images/hierarchy.jpg?raw=true)

<h2><a id="user-content-tabla-de-contenido" class="anchor" aria-hidden="true" href="#tabla-de-contenido"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Tabla de contenido
</h2>
<ul>
  <li><a href="#introduccion-al-proyecto">Introducción al proyecto</a></li>
  <li><a href="#implementacion-del-proyecto">Implementacion del proyecto</a></li>
  <li><a href="#instalacion-de-dependencias">Instalacion de dependencias</a></li>
  <li><a href="#iniciar-la-aplicacion">Iniciar la aplicación</a></li>
  <li><a href="#comandos-utiles">Comandos utiles</a></li>
</ul>

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
GRANT ALL PRIVILEGES ON DATABASE lookdaluv TO <EL ROL RECIEN CREADO>;
</code></pre>

<em>
  Nota: Para sistemas Linux.
</em>
