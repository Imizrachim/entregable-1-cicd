# entregable-1-cicd
Primer entregable del curso de CI/CD

## Integrantes

Ioav Mizrachi - [@Imizrachim](https://github.com/Imizrachim) (Propietario del repositorio)
Mateo Muñoz - [@mateomunozb](https://github.com/usuario2_github)

### Eventos
Se implementaron los evento push y ejecucion manual. 

**Push:** Sirve para validar los cambios que se estan subiendo en el momento subirlos a la rama que se esta ejecutando, en este caso se agrego para correr el flujo una vez se suben los cambios y mirar el comportamiento de cada uno de los job. En la practica sive para ejecutar pruebas unitarias, linters o incluso desplegar una vez se suban los cambios a la rama.

**Ejecución manual ( workflow_dispatch):** Sirve para ejecutar tareas o despliegues bajo demanda. En algunos casos se necesita validar configuraciones realizadas y no es necesario hacer un commit vacio para disparar un evento. En algunos casos despliegues que requieren autorización o que solo los puede hacer cierta persona. Tambien se puede personalizar la ejecución. Sirve para tener mas control y flexibilidad sin tocar el codigo.

### Servidor
El sistema operativo del servidor virtual que se configuro es el siguiente: 

```yml
runs-on: ubuntu-latest
```
Independientemente del sistema operativo que tenga la maquina donde se escribe el codigo el pipeline configurado en el workflow va correr en un entorno virtual de GitHub  de manera aislada para ese flujo, el codigo no se ejecuta en la maquina personal.

La definición del sistema operativo tambien determina los comando que va interpretar en este caso para ubuntu se utiliza bash como shell por defecto

### Acciones pre-construidas de GitHub
- **fluidattacks/sast-action:** Sirve para integrar un analisis estatico de seguridad de las aplicaciones. Se utiliza para escaneo de vulnerabildiades de codigo fuente, hacer deteccion temprana de problemas de seguirdad y generar reportes de vulnerabildiaes.


