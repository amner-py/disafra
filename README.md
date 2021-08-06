╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ /////////////////\     ////   ////////////////       ///////.    ////////////   ////////////////       ///////.  ║
║   /////¨¨       ||\    ////   ////¨¨                ////¨ ////   ////¨¨         ////¨¨   ..////       ////¨ //// ║
║    /////        ///    ////   ////...              ////.  ////   ////////       ////////////         ////.  //// ║
║     /////      ///     ////   ////////////////    ////¨¨..////   ////¨          ////¨    ////       ////¨¨..//// ║
║    /////..    ///      ////            ¨¨¨////   ////     ////   ////           ////      ////     ////     //// ║
║ ////////////////       ////   ////////////////  ////      ////   ////           ////        ////  ////      //// ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

# README.md

## Español

## - CREAR UN FORK:

1. En la parte derecha superior de este repositorio aparece un botón llamado **fork**, por favor hacer clic para generar tu propia
 versión de este repositorio en tu cuenta.

## - CONFIGURAR MI GIT:

1. Se debe instalar GIT según el sistema Windows, MacOs o Linux.
```
	https://git-scm.com/downloads
```
2. Una vez instalado hay que ingresar a la consola que se prefiera.
3. Para configurar nombre y correo se escribe los siguientes comandos:
```
	git config --global user.name "Mi Nombre"
	git config --global user.email "Mi correo"
```

## - CREAR MI REPOSITORIO LOCAL CON GIT:

1. Entrar a la consola y ubicarnos en la ruta donde clonaremos nuestro repositorio.
2. Escribir el siguiente comando para clonar el repositorio:

```
	git clone https://github.com/miCuenta/miCopia
```
3. Comenzar a programar, o agregar documentos.

## CONFIGURAR MI FORK

1. Revisaremos el URL remoto de nuestro repositorio con:

```
	git remote -v
```

2. Se cambiara el nombre de nuestro git remoto a fork con el siguiente comando:

```
	git remote rename origin fork
	git remote -v
```

3. Se agregará el URL remoto del repositorio original, para eso se colocará el siguiente comando:

```
	git remote add origin https://github.com/amner-py/disafra.git
	git remote -v
```

## CREAR MI PROPIA RAMA/BRANCH LOCAL:	\*Es necesario crear una rama para evitar errores en el repositorio principal\*

1. Con la consola dentro de la carpeta del repositorio existen diferentes maneras de crear nuestra rama/branch:

\*Es necesario reemplazar miRama por su nombre, ejemplo: git branch juan \*

```
	git branch miRama
	git checkout miRama
```

	o

```
	git checkout -b miRama
```

## UNIENDO MIS RAMAS A LA MASTER:

1. En consola escribimos los siguientes comandos:
```
	git checkout master
	git merge miRama
```

	o

```
	git merge master miRama
```

## SUBIR LOS CAMBIOS QUE REALICE A GITHUB

1. En la consola escribir el siguiente comando:

```
	git push fork miRama
```

## HACER PULL REQUEST

1. Entrar a github
2. Entrar al repositorio copia que nos creo dentro de nuestra copia llamada disafra deberia salir así: miUsuario/disafra
3. Dar clic en branches
4. Dar clic en el botón: **New pull request**
5. Observar que en en base fork se muestre:

**base fork: amner-py/disafra	base: master	head fork: miUsuario/disafra	compare: miRama**

6. Se escribe un mensaje o comentario de lo que se realizó o una previa de qué se agregará.
7. Clic en **Create pull request**


