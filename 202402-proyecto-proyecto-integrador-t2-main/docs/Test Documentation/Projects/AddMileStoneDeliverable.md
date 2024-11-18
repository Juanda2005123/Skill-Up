# Documentación de Pruebas Unitarias: `addMilestoneDeliverable`

## Descripción General
Este conjunto de pruebas garantiza la funcionalidad correcta de agregar entregables (deliverables) a hitos (milestones) dentro de proyectos. Las pruebas incluyen validaciones de acceso, restricciones de datos y manejo de errores.

---

## Configuración del Escenario

| **Nombre**             | **Clase**             | **Escenario**                                                                   |
|------------------------|-----------------------|---------------------------------------------------------------------------------|
| `client_user`           | `Userk`              | Usuario autenticado como cliente propietario del proyecto.                     |
| `freelancer_user`       | `Userk`              | Usuario autenticado como freelancer asignado al proyecto.                      |
| `project_contributor`   | `ProjectContributor` | Freelancer asignado al proyecto como contribuyente.                            |
| `milestone`             | `Milestone`          | Hito asociado al contribuyente para agregar entregables.                       |

---

## Pruebas

### Test: `test_add_deliverable`

**Objetivo:** Verificar que un freelancer asignado pueda agregar un entregable válido a un hito.

**Precondiciones:**
- El freelancer debe estar autenticado.
- El freelancer debe estar asignado al proyecto y al hito.

**Datos de Entrada:**
- `name`: "New Deliverable"
- `description`: "Description"
- `deadlineInDays`: 5
- `requiresEvidence`: `True`

**Pasos Realizados:**
1. Realizar una solicitud POST con los datos del entregable.
2. Verificar que la solicitud responda con un código de estado 302 (redirección).
3. Confirmar que el entregable se haya creado correctamente en la base de datos.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                            |
|--------------------------------|-----------------------------------------------------------|
| Código de estado 302           | El entregable debe ser procesado correctamente.           |
| Entregable creado              | Debe aparecer en la base de datos asociado al hito.       |

---

### Test: `test_add_deliverable_not_authenticated`

**Objetivo:** Verificar que un usuario no autenticado no pueda agregar entregables.

**Precondiciones:**
- El usuario debe estar desconectado.

**Datos de Entrada:**
- `name`: "Deliverable Unauthenticated"

**Pasos Realizados:**
1. Realizar una solicitud POST sin autenticación.
2. Confirmar que la solicitud redirija al login.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                            |
|--------------------------------|-----------------------------------------------------------|
| Código de estado 302           | El usuario debe ser redirigido al login.                  |
| Entregable no creado           | No debe aparecer en la base de datos.                     |

---

### Test: `test_add_deliverable_without_permission`

**Objetivo:** Verificar que un freelancer no asignado al proyecto no pueda agregar entregables.

**Precondiciones:**
- El usuario debe ser un freelancer que no esté asignado al hito.

**Datos de Entrada:**
- `name`: "Unauthorized Deliverable"

**Pasos Realizados:**
1. Realizar una solicitud POST como freelancer no asignado.
2. Confirmar que la solicitud responda con un código de estado 403 (prohibido).

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                            |
|--------------------------------|-----------------------------------------------------------|
| Código de estado 403           | La solicitud debe ser rechazada por falta de permisos.    |
| Entregable no creado           | No debe aparecer en la base de datos.                     |

---

### Test: `test_add_deliverable_without_name`

**Objetivo:** Verificar que no se puedan agregar entregables sin un nombre válido.

**Precondiciones:**
- El nombre del entregable debe estar vacío.

**Datos de Entrada:**
- `name`: ""

**Pasos Realizados:**
1. Realizar una solicitud POST con un nombre vacío.
2. Confirmar que la solicitud responda con un código de estado 400 (solicitud incorrecta).

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                            |
|--------------------------------|-----------------------------------------------------------|
| Código de estado 400           | La solicitud debe devolver un error de validación.        |
| Entregable no creado           | No debe aparecer en la base de datos.                     |

---

### Test: `test_add_deliverable_with_negative_deadline`

**Objetivo:** Verificar que no se puedan agregar entregables con un plazo negativo.

**Precondiciones:**
- El plazo (`deadlineInDays`) debe ser un valor negativo.

**Datos de Entrada:**
- `deadlineInDays`: -5

**Pasos Realizados:**
1. Realizar una solicitud POST con un plazo negativo.
2. Confirmar que la solicitud responda con un código de estado 400 (solicitud incorrecta).

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                            |
|--------------------------------|-----------------------------------------------------------|
| Código de estado 400           | La solicitud debe devolver un error de validación.        |
| Entregable no creado           | No debe aparecer en la base de datos.                     |

---

### Test: `test_add_duplicate_deliverable`

**Objetivo:** Verificar que no se puedan agregar entregables duplicados al mismo hito.

**Precondiciones:**
- Debe existir un entregable con el mismo nombre en el hito.

**Datos de Entrada:**
- `name`: "Duplicate Deliverable"

**Pasos Realizados:**
1. Crear un entregable existente con el mismo nombre.
2. Realizar una solicitud POST para crear un entregable duplicado.
3. Confirmar que la solicitud responda con un código de estado 400 (solicitud incorrecta).

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                            |
|--------------------------------|-----------------------------------------------------------|
| Código de estado 400           | La solicitud debe devolver un error de validación.        |
| Entregable no duplicado        | No debe existir más de un entregable con el mismo nombre. |

---
