# Documentación de Pruebas Unitarias: `test_create_project`

## Descripción General
Esta prueba garantiza que un cliente autenticado pueda crear un proyecto correctamente utilizando la vista correspondiente. Valida tanto la respuesta del servidor como la creación del proyecto en la base de datos.

---

## Configuración del Escenario

| **Nombre**        | **Clase**          | **Escenario**                                     |
|-------------------|--------------------|--------------------------------------------------|
| `user`            | `User`            | Usuario autenticado como cliente.               |
| `client_profile`  | `Client`          | Perfil del cliente asociado al usuario.         |
| `project_data`    | `dict`            | Datos proporcionados para la creación del proyecto. |

---

## Pruebas

### Test: `test_create_project`

**Objetivo:** Verificar que un cliente autenticado puede crear un proyecto exitosamente.

**Precondiciones:**
- El cliente debe estar registrado y autenticado.
- Los datos del proyecto deben ser válidos.

**Datos de Entrada:**
```json
{
    "name": "Test Project",
    "description": "This is a test project",
    "client": "<client_profile.id>"
}
