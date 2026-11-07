# entregable-1-cicd

Primer entregable del curso de CI/CD

## Integrantes

Ioav Mizrachi - [@Imizrachim](https://github.com/Imizrachim) (propietario del repositorio)

Mateo Muñoz - [@mateomunozb](https://github.com/usuario2_github)

### Eventos

Se implementaron los eventos push y ejecución manual.

**Push:** Sirve para validar los cambios realizados en el momento de hacerles push a la rama que se está ejecutando. En este caso, se agregó para correr el flujo una vez se suben los cambios y mirar el comportamiento de cada uno de los jobs. En la práctica, sirve para ejecutar pruebas unitarias, linters o incluso desplegar una vez se suban los cambios a la rama.

**Ejecución manual (`workflow_dispatch`):** Sirve para ejecutar tareas o despliegues bajo demanda. En algunos casos se necesita validar configuraciones realizadas y no es necesario hacer un commit vacío para disparar un evento. En algunos casos, despliegues que requieren autorización o que solo los puede hacer cierta persona. También se puede personalizar la ejecución. Sirve para tener más control y flexibilidad sin tocar el código.

### Servidor

El sistema operativo del servidor virtual que se configuró es el siguiente:

```yml
runs-on: ubuntu-latest
```

Independientemente del sistema operativo que tenga la máquina donde se escribe el código, el pipeline configurado en el workflow va correr en un entorno virtual de GitHub de manera aislada para ese flujo; el código no se ejecuta en la máquina personal para este caso.

La definición del sistema operativo también determina los comandos que va interpretar. En este caso, para Ubuntu se utiliza Bash como shell por defecto.

### Acciones pre-construidas de GitHub

- **fluidattacks/sast-action:** Sirve para integrar un análisis estático de seguridad de las aplicaciones. Se utiliza para escaneo de vulnerabilidades de código fuente, hacer detección temprana de problemas de seguridad y generar reportes de vulnerabilidades.

- **SonarSource/sonarqube-scan-action:** Sirve para hacer análisis de calidad de código, detección de bugs y vulnerabilidades y verificación de cobertura de pruebas basado en un quality gate configurado y evaluado durante el escaneo.

- **docker/build-push-action:** Sirve para compilar imágenes de Docker y subirlas directamente a registros de contenedores como ECR en AWS y Docker Hub. Simplifica la creación y publicación de imágenes para contenedores en arquitecturas basadas en Docker o microservicios.

### Secret

Un secreto en GitHub es una variable de entorno encriptada que se guarda de manera segura en el entorno del proyecto. El objetivo es que la información que sea sensible no esté en texto plano en el código fuente o en los archivos de configuración del pipeline y no quede expuesta.

Se utiliza para guardar cualquier dato confidencial o credencial, por ejemplo, tokens o claves de acceso a GitHub, a nubes o API de terceros, credenciales de autenticación, certificados o llaves privadas.

Estos secretos se guardan dentro de la configuración del repositorio. GitHub utiliza un mecanismo de encriptado y tiene un control de accesos. En el archivo del pipeline se referencia de la siguiente manera:

```yml
${{ secrets.NOMBRE_DEL_SECRETO }}
```

### Reflexión

**Mateo Muñoz:** Teniendo en cuenta que en mi trabajo, como política general se usa Jenkins para todos los ambientes, el uso de GitHub Actions se podría implementar en las ramas feature, ya que actualmente los flujos de los pipelines solo se ejecutan cuando se hace un PR a las ramas principales, pero no se hace con los cambios dentro de las feature. Esto podría facilitar una capa adicional de detección de vulnerabilidades, buenas prácticas de código, verificación de pruebas incluso antes de que lleguen a la rama de desarrollo.

**Ioav Mizrachi:** En mi caso, teniendo en cuenta que actualmente me dedico sobre todo al desarrollo de proyectos propios, el uso de GitHub Actions se podría implementar para automatizar la validación del código en mis repositorios, ejecutando pruebas y verificaciones cada vez que implemento nuevos cambios. Esto permitiría detectar posibles errores y vulnerabilidades antes de integrar las actualizaciones, manteniendo buenas prácticas y un estándar profesional en mi portafolio.
