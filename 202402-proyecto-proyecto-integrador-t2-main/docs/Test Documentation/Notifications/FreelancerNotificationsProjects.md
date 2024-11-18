# Documentación de Pruebas Unitarias: `TestFreelancerNotificationViews`

## Configuración del Escenario para `TestFreelancerNotificationViews`

| **Nombre**               | **Clase**                  | **Escenario**                                                                 |
|--------------------------|----------------------------|-------------------------------------------------------------------------------|
| `client_user`            | `User`                    | Usuario cliente utilizado para pruebas de notificaciones.                    |
| `freelancer_user`        | `User`                    | Usuario freelancer utilizado para pruebas de notificaciones.                 |
| `project`                | `Project`                 | Proyecto de prueba creado por el cliente.                                    |
| `project_contributor`    | `ProjectContributor`       | Freelancer asignado al proyecto para pruebas de interacciones.               |
| `Notification`           | `Notification`            | Modelo utilizado para verificar las notificaciones generadas.                |

---

## Pruebas

### Test: `test_send_request_notification`

**Objetivo:** Verificar que se envíe una notificación al cliente cuando el freelancer solicita unirse al proyecto.

**Precondiciones:**
- Un freelancer debe estar registrado y asociado al proyecto como contribuyente.

**Datos de Entrada:**
- ID del contribuyente (`project_contributor.pk`).

**Pasos Realizados:**
1. El freelancer solicita unirse al proyecto (`POST` en `sendRequest`).
2. Consultar las notificaciones del cliente.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                       |
|--------------------------------|------------------------------------------------------------------------|
| Notificación creada            | Existe una notificación para el cliente con un mensaje relacionado.   |
| Contiene título del proyecto   | La notificación incluye el título del proyecto.                       |

**Resultados Obtenidos:**
- Notificación generada exitosamente con el título del proyecto.

---

### Test: `test_add_milestone_notification`

**Objetivo:** Verificar que cuando se añade un entregable y se solicita aprobación, el cliente reciba una notificación.

**Precondiciones:**
- El entregable debe estar asociado a un hito del proyecto.

**Datos de Entrada:**
- ID del entregable (`deliverable.id`).

**Pasos Realizados:**
1. Crear un entregable asociado a un hito.
2. Solicitar la aprobación del cliente (`POST` en `deliverablesProject`).
3. Consultar las notificaciones del cliente.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                       |
|--------------------------------|------------------------------------------------------------------------|
| Notificación creada            | Existe una notificación para el cliente con un mensaje relacionado.   |
| Contiene título del proyecto   | La notificación incluye el título del proyecto.                       |

**Resultados Obtenidos:**
- Notificación generada exitosamente tras la solicitud de aprobación.

---

### Test: `test_apply_for_job_notification`

**Objetivo:** Verificar que se envíe una notificación al cliente cuando el freelancer aplica a un trabajo.

**Precondiciones:**
- El freelancer debe estar asociado a un proyecto.

**Datos de Entrada:**
- ID del contribuyente (`project_contributor.pk`).

**Pasos Realizados:**
1. El freelancer aplica a un trabajo (`POST` en `apply_for_job`).
2. Consultar las notificaciones del cliente.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                       |
|--------------------------------|------------------------------------------------------------------------|
| Notificación creada            | Existe una notificación para el cliente con un mensaje relacionado.   |
| Contiene título del proyecto   | La notificación incluye el título del proyecto.                       |

**Resultados Obtenidos:**
- Notificación generada exitosamente tras la aplicación del freelancer.

---

### Test: `test_freelancer_browse_projects`

**Objetivo:** Verificar que no se cree ninguna notificación cuando el freelancer navega por proyectos.

**Precondiciones:**
- Freelancer autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. El freelancer accede a la lista de proyectos (`GET` en `browseProjects`).
2. Consultar las notificaciones del freelancer.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                       |
|--------------------------------|------------------------------------------------------------------------|
| Sin notificaciones creadas     | Ninguna notificación debe generarse durante la navegación.            |

**Resultados Obtenidos:**
- Sin notificaciones creadas durante la navegación por proyectos.

---

### Test: `test_freelancer_browse_own_projects`

**Objetivo:** Verificar que no se cree ninguna notificación cuando el freelancer navega por sus propios proyectos.

**Precondiciones:**
- Freelancer autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. El freelancer accede a su lista de proyectos (`GET` en `browseOwnProjects`).
2. Consultar las notificaciones del freelancer.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                       |
|--------------------------------|------------------------------------------------------------------------|
| Sin notificaciones creadas     | Ninguna notificación debe generarse durante la navegación.            |

**Resultados Obtenidos:**
- Sin notificaciones creadas durante la navegación por los propios proyectos.

---

### Test: `test_deliverable_assigned_notification`

**Objetivo:** Verificar que el cliente reciba una notificación cuando se asigna un entregable.

**Precondiciones:**
- Entregable asignado a un hito.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Asignar un entregable.
2. Guardar los cambios.
3. Consultar las notificaciones del cliente.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                       |
|--------------------------------|------------------------------------------------------------------------|
| Notificación creada            | Existe una notificación para el cliente con un mensaje relacionado.   |
| Contiene título del proyecto   | La notificación incluye el título del proyecto.                       |

**Resultados Obtenidos:**
- Notificación generada exitosamente tras la asignación del entregable.

---
