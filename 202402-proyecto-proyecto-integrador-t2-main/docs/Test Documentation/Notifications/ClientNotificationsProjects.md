# Documentación de Pruebas Unitarias: `TestClientNotificationProjects`

## Configuración del Escenario para `TestClientNotificationProjects`

| **Nombre**                   | **Clase**               | **Escenario**                                                                 |
|------------------------------|-------------------------|-------------------------------------------------------------------------------|
| `client_user`                | `User`                 | Usuario cliente utilizado para pruebas relacionadas con notificaciones.       |
| `freelancer_user`            | `User`                 | Usuario freelancer utilizado para pruebas relacionadas con notificaciones.    |
| `project`                    | `Project`              | Proyecto de prueba asociado al cliente.                                       |
| `project_contributor`        | `ProjectContributor`   | Freelancer asociado al proyecto para simular solicitudes y respuestas.        |
| `Notification`               | `Notification`         | Modelo utilizado para verificar notificaciones generadas durante las pruebas. |

---

## Pruebas

### Test: `test_project_creation_notification`

**Objetivo:** Verificar que el cliente reciba una notificación al crear un proyecto.

**Precondiciones:**
- Un cliente debe haber creado un proyecto.

**Datos de Entrada:**
- Proyecto titulado "Test Project".

**Pasos Realizados:**
1. Crear un proyecto asociado al cliente.
2. Consultar las notificaciones del cliente.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|--------------------------------|----------------------------------------------------------------------|
| Notificación creada            | Existe una notificación para el cliente con un mensaje relacionado. |

**Resultados Obtenidos:**
- Notificación generada exitosamente tras la creación del proyecto.

---

### Test: `test_freelancer_application_notification`

**Objetivo:** Verificar que el cliente reciba una notificación cuando un freelancer solicita trabajar en su proyecto.

**Precondiciones:**
- Un freelancer debe haber solicitado unirse al proyecto.

**Datos de Entrada:**
- Freelancer asociado al proyecto.

**Pasos Realizados:**
1. Cambiar el estado de `approval_status` del `ProjectContributor` a `pending`.
2. Consultar las notificaciones del cliente.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|--------------------------------|----------------------------------------------------------------------|
| Notificación creada            | Existe una notificación para el cliente con un mensaje relacionado. |
| Contiene título del proyecto   | La notificación incluye el título del proyecto.                      |

**Resultados Obtenidos:**
- Notificación generada exitosamente con el título del proyecto presente.

---

### Test: `test_client_acceptance_notification`

**Objetivo:** Verificar que el freelancer reciba una notificación cuando el cliente acepta su propuesta.

**Precondiciones:**
- Un cliente debe haber aceptado la propuesta de un freelancer.

**Datos de Entrada:**
- Freelancer y proyecto contribuidor.

**Pasos Realizados:**
1. Cambiar el estado de `approval_status` del `ProjectContributor` a `not_rejected`.
2. Consultar las notificaciones del freelancer.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|--------------------------------|----------------------------------------------------------------------|
| Notificación creada            | Existe una notificación para el freelancer con un mensaje relacionado. |
| Contiene título del contribuidor | La notificación incluye el título del contribuidor.                |

**Resultados Obtenidos:**
- Notificación generada exitosamente tras la aceptación.

---

### Test: `test_client_rejection_notification`

**Objetivo:** Verificar que el freelancer reciba una notificación cuando el cliente rechace su propuesta.

**Precondiciones:**
- Un cliente debe haber rechazado la propuesta de un freelancer.

**Datos de Entrada:**
- Freelancer y proyecto contribuidor.

**Pasos Realizados:**
1. Cambiar el estado de `rejectionReason` del `ProjectContributor` a `profile_rejected`.
2. Consultar las notificaciones del freelancer.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|--------------------------------|----------------------------------------------------------------------|
| Notificación creada            | Existe una notificación para el freelancer con un mensaje relacionado. |
| Contiene título del contribuidor | La notificación incluye el título del contribuidor.                |

**Resultados Obtenidos:**
- Notificación generada exitosamente tras el rechazo.

---

### Test: `test_freelancer_submission_notification`

**Objetivo:** Verificar que el cliente reciba una notificación cuando un freelancer envíe su propuesta.

**Precondiciones:**
- Un freelancer debe haber enviado su propuesta al cliente.

**Datos de Entrada:**
- Freelancer y proyecto contribuidor.

**Pasos Realizados:**
1. Cambiar el estado de `is_send` del `ProjectContributor` a `True`.
2. Consultar las notificaciones del cliente.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|--------------------------------|----------------------------------------------------------------------|
| Notificación creada            | Existe una notificación para el cliente con un mensaje relacionado. |
| Contiene título del proyecto   | La notificación incluye el título del proyecto.                      |

**Resultados Obtenidos:**
- Notificación generada exitosamente tras la propuesta del freelancer.

---
