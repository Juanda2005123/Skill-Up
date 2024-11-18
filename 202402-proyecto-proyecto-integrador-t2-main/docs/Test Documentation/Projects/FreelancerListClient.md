# Documentación de Pruebas Unitarias: `listFreelancer`

## Descripción General
Este conjunto de pruebas asegura la funcionalidad de la vista que lista freelancers asociados a un proyecto. La funcionalidad incluye la correcta visualización de freelancers aprobados y la exclusión de aquellos rechazados.

---

## Configuración del Escenario

| **Nombre**               | **Clase**                 | **Escenario**                                                                 |
|--------------------------|---------------------------|-------------------------------------------------------------------------------|
| `freelancer_user`        | `Userk`                  | Usuario autenticado como freelancer.                                         |
| `freelancer`             | `Freelancer`             | Perfil de freelancer asociado al usuario freelancer.                         |
| `client_user`            | `Userk`                  | Usuario autenticado como cliente propietario del proyecto.                   |
| `client`                 | `ClientModel`            | Perfil de cliente asociado al usuario cliente.                               |
| `project1`               | `Project`                | Proyecto creado por el cliente y asociado a freelancers.                     |
| `project_contributor1`   | `ProjectContributor`      | Contribuidor del proyecto con estado `approved` y enviado (`is_send=True`).  |
| `project_contributor2`   | `ProjectContributor`      | Contribuidor del proyecto con estado `rejected` y no enviado (`is_send=False`). |

---

## Pruebas

### Test: `testGetFreelancerList`

**Objetivo:** Verificar que la página de la lista de freelancers se carga correctamente.

**Precondiciones:**
- El cliente debe estar autenticado.
- El proyecto debe existir y estar asociado al cliente.

**Pasos Realizados:**
1. Realizar una solicitud GET a la URL `listFreelancer` con el `id` del proyecto.
2. Verificar el código de estado de la respuesta.
3. Confirmar que se usa la plantilla correcta.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                              |
|--------------------------|----------------------------------------------|
| Código de estado 200     | La página se carga correctamente.            |
| Plantilla correcta       | Se utiliza `projects/listFreelancer.html`.   |

---

### Test: `test_client_can_view_approved_freelancers`

**Objetivo:** Verificar que solo los freelancers aprobados y enviados aparecen en la lista.

**Precondiciones:**
- El cliente debe estar autenticado.
- Debe existir al menos un freelancer con estado `approved` y uno con estado `rejected`.

**Datos de Entrada:**
- **Freelancer Aprobado:**
  - `title`: "Developer"
  - `approval_status`: "approved"
  - `is_send`: `True`
- **Freelancer Rechazado:**
  - `title`: "Designer"
  - `approval_status`: "rejected"
  - `is_send`: `False`

**Pasos Realizados:**
1. Realizar una solicitud GET a la URL `listFreelancer` con el `id` del proyecto.
2. Verificar que los freelancers con estado `approved` aparecen en la respuesta.
3. Confirmar que los freelancers con estado `rejected` no aparecen en la respuesta.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Freelancer aprobado visible    | El freelancer con estado `approved` aparece en la lista.           |
| Freelancer rechazado no visible| El freelancer con estado `rejected` no aparece en la lista.        |
| Datos completos mostrados      | Se muestran `title`, `username` y `progress` del freelancer aprobado. |

---

### Detalles del Test

**Freelancer Aprobado (`project_contributor1`):**
- **Estado:** Aprobado (`approved`).
- **Enviado:** Sí (`is_send=True`).
- **Progreso:** Se muestra como porcentaje (`progress`).

**Freelancer Rechazado (`project_contributor2`):**
- **Estado:** Rechazado (`rejected`).
- **Enviado:** No (`is_send=False`).
- **Progreso:** No debe mostrarse.

---

## Consideraciones
Estas pruebas garantizan que los freelancers listados en la vista sean únicamente aquellos aprobados y enviados (`approved` y `is_send=True`), proporcionando una experiencia coherente y segura para el cliente.
