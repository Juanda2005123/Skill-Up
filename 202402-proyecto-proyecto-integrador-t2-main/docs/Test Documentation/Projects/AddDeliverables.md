# Documentación de Pruebas Unitarias: `addDeliverablesProject`

## Descripción General
Este conjunto de pruebas garantiza que la funcionalidad de agregar hitos (milestones) para un contribuyente del proyecto funcione correctamente y maneje diferentes escenarios de validación, acceso y restricciones.

---

## Configuración del Escenario

| **Nombre**            | **Clase**               | **Escenario**                                                                 |
|-----------------------|-------------------------|-------------------------------------------------------------------------------|
| `freelancer_user`      | `User`                 | Usuario freelancer autenticado asignado como contribuyente del proyecto.      |
| `client_user`          | `User`                 | Usuario cliente propietario del proyecto.                                     |
| `project_contributor`  | `ProjectContributor`   | Freelancer asignado al proyecto con permisos para crear hitos.                |

---

## Pruebas

### Test: `test_add_milestone_via_htmx`

**Objetivo:** Verificar que un freelancer autenticado pueda crear un hito (milestone) a través de una solicitud HTMX.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.
- Debe haber un `ProjectContributor` asociado al proyecto.

**Datos de Entrada:**
- `name`: "New Milestone"

**Pasos Realizados:**
1. Realizar una solicitud POST con los datos del hito y el encabezado HTMX.
2. Verificar la respuesta del servidor y que el hito se haya creado.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                           |
|--------------------------------|----------------------------------------------------------|
| Código de estado 200           | La solicitud POST debe procesarse correctamente.         |
| Hito creado en la base de datos| El hito debe aparecer en la base de datos.               |

**Resultados Obtenidos:**
- El hito fue creado correctamente.

---

### Test: `test_add_deliverable_with_empty_name`

**Objetivo:** Asegurar que no se puedan crear hitos con un nombre vacío.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.

**Datos de Entrada:**
- `name`: ""

**Pasos Realizados:**
1. Realizar una solicitud POST con un nombre vacío.
2. Verificar que no se cree el hito.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                           |
|--------------------------------|----------------------------------------------------------|
| Código de estado 200           | La solicitud debe responder con un error de validación.  |
| Hito no creado                 | No debe aparecer un hito con un nombre vacío.            |

**Resultados Obtenidos:**
- El hito no fue creado.

---

### Test: `test_add_deliverable_with_negative_deadline`

**Objetivo:** Garantizar que no se puedan crear hitos con una fecha límite negativa.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.

**Datos de Entrada:**
- `deadlineInDays`: -5

**Pasos Realizados:**
1. Realizar una solicitud POST con un valor negativo para `deadlineInDays`.
2. Verificar que no se cree el hito.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                           |
|--------------------------------|----------------------------------------------------------|
| Código de estado 200           | La solicitud debe responder con un error de validación.  |
| Hito no creado                 | No debe aparecer un hito con un plazo negativo.          |

**Resultados Obtenidos:**
- El hito no fue creado.

---

### Test: `test_add_deliverable_not_authenticated`

**Objetivo:** Verificar que un usuario no autenticado no pueda crear hitos.

**Precondiciones:**
- El usuario no debe estar autenticado.

**Datos de Entrada:**
- `name`: "Unauthenticated Milestone"

**Pasos Realizados:**
1. Realizar una solicitud POST sin autenticación.
2. Verificar que el usuario sea redirigido al login.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                           |
|--------------------------------|----------------------------------------------------------|
| Código de estado 302           | El usuario debe ser redirigido al login.                 |
| Hito no creado                 | No debe aparecer el hito en la base de datos.            |

**Resultados Obtenidos:**
- El usuario fue redirigido al login y el hito no fue creado.

---

### Test: `test_add_deliverable_not_contributor`

**Objetivo:** Asegurar que un freelancer no asignado al proyecto no pueda crear hitos.

**Precondiciones:**
- El usuario debe ser un freelancer no asignado al proyecto.

**Datos de Entrada:**
- `name`: "Unauthorized Milestone"

**Pasos Realizados:**
1. Realizar una solicitud POST como freelancer no asignado.
2. Verificar que se devuelva un error 403.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                           |
|--------------------------------|----------------------------------------------------------|
| Código de estado 403           | La solicitud debe ser rechazada por falta de permisos.   |
| Hito no creado                 | No debe aparecer el hito en la base de datos.            |

**Resultados Obtenidos:**
- El freelancer no asignado no pudo crear el hito.

---

### Test: `test_add_deliverable_duplicate`

**Objetivo:** Verificar que no se puedan crear hitos duplicados para el mismo contribuyente.

**Precondiciones:**
- Debe existir un hito con el mismo nombre.

**Datos de Entrada:**
- `name`: "Duplicate Milestone"

**Pasos Realizados:**
1. Crear un hito existente con el mismo nombre.
2. Intentar crear un hito duplicado.
3. Verificar que no se cree un segundo hito.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                           |
|--------------------------------|----------------------------------------------------------|
| Código de estado 200           | La solicitud debe devolver un error de validación.       |
| Hito no duplicado              | No deben existir dos hitos con el mismo nombre.          |

**Resultados Obtenidos:**
- El hito duplicado no fue creado.

---
