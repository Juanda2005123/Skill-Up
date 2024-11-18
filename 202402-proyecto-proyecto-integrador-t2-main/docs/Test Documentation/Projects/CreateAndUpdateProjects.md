# Documentación de Pruebas Unitarias: Creación y Actualización de Proyectos

## Descripción General
Este conjunto de pruebas verifica el correcto funcionamiento de las funcionalidades de creación y actualización de proyectos, incluyendo validaciones de campos, manejo de autenticación, y actualizaciones relacionadas con habilidades y versiones.

---

## Configuración del Escenario

| **Nombre**         | **Clase**  | **Descripción**                                    |
|--------------------|------------|----------------------------------------------------|
| `createProject`    | `reverse`  | URL para la creación de proyectos.                |
| `updateProject`    | `reverse`  | URL para la actualización de proyectos.           |
| `Project`          | `Model`    | Modelo de proyectos.                              |
| `ProjectComplexity`| `Model`    | Nivel de complejidad de un proyecto.              |
| `ProjectSkillExpertise` | `Model` | Habilidades requeridas para un proyecto.         |

---

## Pruebas

### Test: `test_create_project_missing_field`

**Objetivo:** Verificar que no se pueda crear un proyecto si falta un campo obligatorio.

**Precondiciones:**
- El cliente debe estar autenticado.

**Datos de Entrada:**
- Formulario con el campo `title` vacío.

**Pasos Realizados:**
1. Realizar una solicitud POST a la URL de creación con datos incompletos.
2. Verificar que la solicitud permanece en la misma página con un error.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                    |
|-----------------------|----------------------------------------------------|
| Código de estado 200  | La solicitud no pasa y se muestran errores.        |
| Sin proyecto creado   | No se crea un proyecto en la base de datos.        |

---

### Test: `test_update_project_invalid_budget`

**Objetivo:** Verificar que no se pueda actualizar un proyecto con un presupuesto no válido.

**Precondiciones:**
- Un proyecto debe existir.
- El cliente debe estar autenticado.

**Datos de Entrada:**
- Presupuesto inválido (`"invalid_budget"`).

**Pasos Realizados:**
1. Realizar una solicitud POST a la URL de actualización con un presupuesto no válido.
2. Verificar que la solicitud permanece en la misma página con un error.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                    |
|-----------------------|----------------------------------------------------|
| Código de estado 200  | La solicitud no pasa y se muestran errores.        |
| Sin cambios           | El proyecto no es actualizado.                    |

---

### Test: `test_update_project_skill_expertise`

**Objetivo:** Verificar que se puedan actualizar las habilidades requeridas de un proyecto.

**Precondiciones:**
- Un proyecto debe existir con habilidades iniciales.

**Datos de Entrada:**
- Habilidades nuevas para el proyecto.

**Pasos Realizados:**
1. Realizar una solicitud POST a la URL de actualización con nuevas habilidades.
2. Verificar que las nuevas habilidades se asignan correctamente.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                    |
|-----------------------|----------------------------------------------------|
| Código de estado 302  | Redirección tras la actualización exitosa.         |
| Habilidades actualizadas | Las nuevas habilidades se guardan en el proyecto.|

---

### Test: `test_create_project_redirect_authenticated_user`

**Objetivo:** Verificar que un cliente autenticado pueda crear un proyecto y sea redirigido correctamente.

**Precondiciones:**
- El cliente debe estar autenticado.

**Datos de Entrada:**
- Datos válidos para un nuevo proyecto.

**Pasos Realizados:**
1. Realizar una solicitud POST a la URL de creación con datos válidos.
2. Verificar que se redirige al cliente a la página de proyectos.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                    |
|-----------------------|----------------------------------------------------|
| Código de estado 302  | Redirección tras la creación exitosa.              |
| Proyecto creado       | Un nuevo proyecto se guarda en la base de datos.   |

---

### Test: `test_create_project_with_multiple_skills`

**Objetivo:** Verificar que se puedan asignar múltiples habilidades a un proyecto al crearlo.

**Precondiciones:**
- Habilidades existentes en el sistema.

**Datos de Entrada:**
- Datos válidos con varias habilidades.

**Pasos Realizados:**
1. Realizar una solicitud POST a la URL de creación con múltiples habilidades seleccionadas.
2. Verificar que el proyecto contiene todas las habilidades seleccionadas.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                    |
|-----------------------|----------------------------------------------------|
| Código de estado 302  | Redirección tras la creación exitosa.              |
| Habilidades asignadas | El proyecto contiene todas las habilidades dadas. |

---

### Test: `test_project_version_increment_on_update`

**Objetivo:** Verificar que al actualizar un proyecto, su versión se incremente automáticamente.

**Precondiciones:**
- Un proyecto debe existir.

**Datos de Entrada:**
- Datos válidos para actualización del proyecto.

**Pasos Realizados:**
1. Realizar una solicitud POST a la URL de actualización.
2. Verificar que la versión del proyecto se incrementa.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                    |
|-----------------------|----------------------------------------------------|
| Código de estado 302  | Redirección tras la actualización exitosa.         |
| Versión incrementada  | La versión del proyecto aumenta en 1.              |

---

