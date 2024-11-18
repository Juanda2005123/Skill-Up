# Documentación de Pruebas Unitarias: `deleteMilestone`

## Descripción General
Este conjunto de pruebas garantiza la funcionalidad correcta de la eliminación de hitos (**milestones**) asociados a proyectos. Las pruebas incluyen validaciones de acceso, restricciones de datos y manejo de errores.

---

## Configuración del Escenario

| **Nombre**             | **Clase**             | **Escenario**                                                              |
|------------------------|-----------------------|-----------------------------------------------------------------------------|
| `client_user`          | `Userk`              | Usuario autenticado como cliente propietario del proyecto.                 |
| `freelancer_user`      | `Userk`              | Usuario autenticado como freelancer asignado al proyecto.                  |
| `project_contributor`  | `ProjectContributor` | Freelancer asignado al proyecto como contribuyente.                        |
| `milestone`            | `Milestone`          | Hito asociado al contribuyente para pruebas de eliminación.                |

---

## Pruebas

### Test: `test_delete_milestone`

**Objetivo:** Verificar que un freelancer asignado pueda eliminar un hito existente.

**Precondiciones:**
- El freelancer debe estar autenticado.
- El freelancer debe estar asignado al proyecto y al hito.

**Datos de Entrada:**
- ID del hito: `self.milestone.id`

**Pasos Realizados:**
1. Realizar una solicitud POST para eliminar el hito.
2. Verificar que el hito ya no exista en la base de datos.

**Resultados Esperados:**

| **Resultado**          | **Descripción**                                               |
|------------------------|---------------------------------------------------------------|
| Código de estado 302   | El hito debe ser eliminado correctamente y redirigido.        |
| Hito eliminado         | El hito ya no debe estar presente en la base de datos.        |

---

### Test: `test_delete_milestone_not_authenticated`

**Objetivo:** Verificar que un usuario no autenticado no pueda eliminar un hito.

**Precondiciones:**
- El usuario debe estar desconectado.

**Datos de Entrada:**
- ID del hito: `self.milestone.id`

**Pasos Realizados:**
1. Cerrar sesión del usuario actual.
2. Realizar una solicitud POST para eliminar el hito.
3. Verificar que el hito siga existiendo en la base de datos.

**Resultados Esperados:**

| **Resultado**          | **Descripción**                                               |
|------------------------|---------------------------------------------------------------|
| Código de estado 302   | El usuario debe ser redirigido a la página de inicio de sesión. |
| Hito no eliminado      | El hito debe permanecer en la base de datos.                  |

---

### Test: `test_delete_milestone_different_user`

**Objetivo:** Verificar que un usuario diferente al contribuyente asociado no pueda eliminar un hito.

**Precondiciones:**
- El usuario debe ser un freelancer que no esté asignado al hito.

**Datos de Entrada:**
- ID del hito: `self.milestone.id`

**Pasos Realizados:**
1. Iniciar sesión con un usuario freelancer diferente.
2. Realizar una solicitud POST para eliminar el hito.
3. Verificar que el hito siga existiendo en la base de datos.

**Resultados Esperados:**

| **Resultado**          | **Descripción**                                               |
|------------------------|---------------------------------------------------------------|
| Código de estado 302   | La solicitud debe ser rechazada y redirigida.                 |
| Hito no eliminado      | El hito debe permanecer en la base de datos.                  |

---

### Test: `test_delete_milestone_with_associated_deliverables`

**Objetivo:** Verificar que al eliminar un hito, también se eliminen sus entregables (**deliverables**) asociados.

**Precondiciones:**
- El hito debe tener entregables asociados.

**Datos de Entrada:**
- ID del hito: `self.milestone.id`

**Pasos Realizados:**
1. Crear un entregable asociado al hito.
2. Realizar una solicitud POST para eliminar el hito.
3. Verificar que tanto el hito como los entregables asociados sean eliminados.

**Resultados Esperados:**

| **Resultado**          | **Descripción**                                               |
|------------------------|---------------------------------------------------------------|
| Código de estado 302   | El hito y los entregables deben ser eliminados.               |
| Hito eliminado         | El hito ya no debe estar presente en la base de datos.        |
| Deliverables eliminados| Los entregables asociados deben ser eliminados de la base de datos. |

---

### Test: `test_delete_nonexistent_milestone`

**Objetivo:** Verificar que intentar eliminar un hito inexistente devuelva un error 404.

**Precondiciones:**
- El ID del hito no debe existir en la base de datos.

**Datos de Entrada:**
- ID del hito inexistente: `9999`

**Pasos Realizados:**
1. Realizar una solicitud POST para eliminar un hito inexistente.
2. Confirmar que se devuelva un error 404.

**Resultados Esperados:**

| **Resultado**          | **Descripción**                                               |
|------------------------|---------------------------------------------------------------|
| Código de estado 404   | El sistema debe devolver un error 404 indicando que no se encontró el hito. |

---

### Test: `test_delete_milestone_different_contributor`

**Objetivo:** Verificar que un freelancer no pueda eliminar un hito asociado a otro contribuyente.

**Precondiciones:**
- El hito debe estar asociado a un contribuyente diferente.

**Datos de Entrada:**
- ID del hito asociado al otro contribuyente.

**Pasos Realizados:**
1. Crear un segundo contribuyente con un hito asociado.
2. Realizar una solicitud POST para eliminar el hito con un freelancer diferente.
3. Verificar que el hito siga existiendo en la base de datos.

**Resultados Esperados:**

| **Resultado**          | **Descripción**                                               |
|------------------------|---------------------------------------------------------------|
| Código de estado 302   | La solicitud debe ser rechazada y redirigida.                 |
| Hito no eliminado      | El hito debe permanecer en la base de datos.                  |
