# Documentación de Pruebas Unitarias: `browseProjects` y `browseOwnProjects`

## Descripción General
Estas pruebas garantizan la funcionalidad de las vistas para explorar proyectos disponibles (`browseProjects`) y explorar proyectos propios (`browseOwnProjects`). Incluyen validaciones de acceso, funcionalidad de filtros y ordenamiento, y exclusión de proyectos no aprobados.

---

## Configuración del Escenario

| **Nombre**               | **Clase**                  | **Escenario**                                                                   |
|--------------------------|----------------------------|---------------------------------------------------------------------------------|
| `freelancer_user`         | `Userk`                   | Usuario autenticado como freelancer.                                           |
| `client_user`             | `Userk`                   | Usuario autenticado como cliente.                                              |
| `freelancer`              | `Freelancer`              | Perfil del freelancer asociado al usuario.                                     |
| `client`                  | `ClientModel`             | Perfil del cliente asociado al usuario.                                        |
| `project1`, `project2`    | `Project`                 | Proyectos creados por el cliente.                                              |
| `complexity`              | `ProjectComplexity`       | Complejidad asociada a los proyectos.                                          |
| `skill_expertise`         | `ProjectSkillExpertise`   | Habilidad requerida asociada a los proyectos.                                  |
| `project_contributor`     | `ProjectContributor`      | Freelancer asignado a un proyecto con estatus de aprobación.                   |

---

## Pruebas

### Test: `test_browse_projects`

**Objetivo:** Verificar que la vista `browseProjects` lista todos los proyectos disponibles para freelancers.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.
- Deben existir proyectos en la base de datos.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Realizar una solicitud GET a la vista `browseProjects`.
2. Verificar que el código de respuesta sea 200.
3. Confirmar que los proyectos están presentes en el contexto de la respuesta.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                            |
|-----------------------|--------------------------------------------|
| Código de estado 200  | La solicitud es procesada correctamente.  |
| Proyectos en contexto | Los proyectos deben estar en el contexto. |

---

### Test: `test_browse_projects_with_filtering`

**Objetivo:** Verificar que la vista `browseProjects` permite ordenar los proyectos.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.
- Deben existir proyectos en la base de datos.

**Datos de Entrada:**
- `sort_by`: "title"

**Pasos Realizados:**
1. Realizar una solicitud GET con parámetros de ordenamiento.
2. Confirmar que los proyectos están ordenados por título.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                            |
|-----------------------|--------------------------------------------|
| Código de estado 200  | La solicitud es procesada correctamente.  |
| Orden correcto        | Los proyectos deben estar ordenados.      |

---

### Test: `test_browse_own_projects`

**Objetivo:** Verificar que la vista `browseOwnProjects` lista únicamente los proyectos aprobados del freelancer.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.
- El freelancer debe tener proyectos aprobados.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Crear un `ProjectContributor` aprobado.
2. Realizar una solicitud GET a la vista `browseOwnProjects`.
3. Confirmar que solo los proyectos aprobados están en el contexto.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                            |
|-----------------------|--------------------------------------------|
| Código de estado 200  | La solicitud es procesada correctamente.  |
| Proyectos aprobados   | Solo los proyectos aprobados están listados. |

---

### Test: `test_browse_own_projects_not_approved`

**Objetivo:** Verificar que la vista `browseOwnProjects` excluye proyectos no aprobados.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.
- El freelancer debe tener proyectos no aprobados.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Crear un `ProjectContributor` no aprobado.
2. Realizar una solicitud GET a la vista `browseOwnProjects`.
3. Confirmar que los proyectos no aprobados no están en el contexto.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                            |
|-----------------------|--------------------------------------------|
| Código de estado 200  | La solicitud es procesada correctamente.  |
| Exclusión correcta    | Los proyectos no aprobados no están listados. |

---

### Test: `test_browse_own_projects_with_sorting`

**Objetivo:** Verificar que la vista `browseOwnProjects` permite ordenar los proyectos propios.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.
- El freelancer debe tener proyectos aprobados.

**Datos de Entrada:**
- `sort_by`: "title"

**Pasos Realizados:**
1. Crear `ProjectContributor` aprobados para varios proyectos.
2. Realizar una solicitud GET con parámetros de ordenamiento.
3. Confirmar que los proyectos están ordenados por título.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                            |
|-----------------------|--------------------------------------------|
| Código de estado 200  | La solicitud es procesada correctamente.  |
| Orden correcto        | Los proyectos deben estar ordenados.      |

---
