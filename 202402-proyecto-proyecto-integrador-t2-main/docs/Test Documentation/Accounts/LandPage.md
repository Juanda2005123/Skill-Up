# Documentación de Pruebas Unitarias: `TestLandPage`

## Configuración del Escenario para `TestLandPage`

| Nombre        | Clase           | Escenario                                        |
|---------------|-----------------|--------------------------------------------------|
| `client`      | `TestClient`    | Cliente de prueba para realizar solicitudes HTTP.|
| `landpage`    | `str`           | URL de la página de inicio (`landpage`).         |

---

## Pruebas

### Test: `test_LandpageStatusCode`

**Objetivo:** Verificar que la página de inicio (`landpage`) cargue correctamente y devuelva un código de estado HTTP `200`.

**Precondiciones:**
- La URL de la página de inicio debe estar configurada correctamente en el archivo `urls.py`.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Hacer una solicitud `GET` a la URL de la `landpage`.
2. Verificar el código de estado HTTP de la respuesta.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                   |
|------------------------------|-------------------------------------------------------------------|
| Código de estado correcto     | La respuesta debe tener un código de estado `200`.               |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la página de inicio carga correctamente.

---

### Test: `test_LandpageContainsTitle`

**Objetivo:** Verificar que el título de la página (`SkillUp`) esté presente en el contenido HTML de la página de inicio.

**Precondiciones:**
- La plantilla utilizada para la `landpage` debe incluir el título `SkillUp`.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Hacer una solicitud `GET` a la URL de la `landpage`.
2. Verificar que el contenido HTML de la respuesta contiene el título `<h1 class="u-text u-text-default u-text-1">SkillUp</h1>`.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                   |
|------------------------------|-------------------------------------------------------------------|
| Título presente               | El título `SkillUp` debe estar presente en el contenido HTML.    |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el título `SkillUp` está presente en la página de inicio.

---

### Test: `test_LandpageContainsNavigationLinks`

**Objetivo:** Verificar que los enlaces de navegación principales (`Find Work`, `Find Talent`, `Log In`) estén presentes en la página de inicio.

**Precondiciones:**
- La plantilla utilizada para la `landpage` debe incluir enlaces de navegación a las funcionalidades principales.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Hacer una solicitud `GET` a la URL de la `landpage`.
2. Verificar que el contenido HTML de la respuesta contiene los enlaces `Find Work`, `Find Talent` y `Log In`.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                   |
|------------------------------|-------------------------------------------------------------------|
| Enlace `Find Work` presente   | El enlace `Find Work` debe estar presente en el contenido HTML.   |
| Enlace `Find Talent` presente | El enlace `Find Talent` debe estar presente en el contenido HTML. |
| Enlace `Log In` presente      | El enlace `Log In` debe estar presente en el contenido HTML.      |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los enlaces de navegación principales están presentes en la página de inicio.

---
