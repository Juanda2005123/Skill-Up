# Documentación de Pruebas Unitarias: `FreelancerProfileSettingsTest`

## Configuración del Escenario para `FreelancerProfileSettingsTest`

| Nombre                | Clase                 | Escenario                                                                 |
|-----------------------|-----------------------|---------------------------------------------------------------------------|
| `freelancer_user`     | `User`               | Usuario freelancer creado para la ejecución del test.                     |
| `freelancer_profile`  | `Freelancer`         | Perfil asociado al usuario freelancer.                                    |
| `client_user`         | `User`               | Usuario cliente creado para las pruebas de calificación.                  |
| `client_profile`      | `Client`             | Perfil asociado al usuario cliente.                                       |
| `resume_file`         | `SimpleUploadedFile` | Archivo de prueba para simular la subida de un currículum.                |
| `freelancer_url`      | `str`                | URL de la configuración del perfil del freelancer (`freelancerProfileSettings`). |

---

## Pruebas

### Test: `testGetFreelancerProfile`

**Objetivo:** Verificar que la página de configuración del perfil de freelancer se carga correctamente.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Acceder a la URL de configuración del perfil de freelancer con un usuario autenticado.
2. Verificar que el código de estado sea `200`.
3. Verificar que se utiliza la plantilla `accounts/freelancerProfileSettings.html`.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                   |
|------------------------------|-------------------------------------------------------------------|
| Código de estado correcto     | La respuesta debe tener un código `200`.                         |
| Uso de plantilla correcta     | Debe utilizarse la plantilla `accounts/freelancerProfileSettings.html`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la página de configuración se carga correctamente.

---

### Test: `test_redirect_unauthenticated_user`

**Objetivo:** Verificar que los usuarios no autenticados son redirigidos a la página de inicio de sesión.

**Precondiciones:**
- Ninguna.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Cerrar sesión del usuario freelancer.
2. Acceder a la URL de configuración del perfil de freelancer.
3. Verificar que se realiza una redirección al inicio de sesión.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                   |
|------------------------------|-------------------------------------------------------------------|
| Código de redirección         | La respuesta debe tener un código `302`.                         |
| Redirección al login          | Debe redirigirse a la página de inicio de sesión.                |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los usuarios no autenticados son redirigidos.

---

### Test: `testUpdateFreelancerProfile`

**Objetivo:** Verificar que se puede actualizar el perfil del freelancer correctamente.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.

**Datos de Entrada:**
- Datos actualizados para el perfil:
  - `description`: "Experienced SQL and noSQL developer".
  - `experience_level`: "Senior".
  - `linkedin_url`: "https://linkedin.com/in/freelancer_test".
  - `github_url`: "https://github.com/freelancer_test".
  - Habilidades: `Javascript`, `SQL`.

**Pasos Realizados:**
1. Realizar una solicitud POST con los datos actualizados.
2. Verificar que el código de estado sea `302`.
3. Verificar que los datos se actualizan en la base de datos.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                   |
|------------------------------|-------------------------------------------------------------------|
| Perfil actualizado correctamente | Los datos del perfil deben reflejar los cambios realizados.       |
| Habilidades añadidas         | Las habilidades seleccionadas deben asociarse al freelancer.     |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el perfil se actualiza correctamente.

---

### Test: `testAddExperienceFreelancerProfile`

**Objetivo:** Verificar que se puede añadir experiencia laboral al perfil del freelancer.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.

**Datos de Entrada:**
- Experiencia laboral:
  - `job`: "Tester".
  - `company`: "Amazonas".
  - `start_date`: `2020-05-01`.
  - `end_date`: `2023-05-01`.

**Pasos Realizados:**
1. Crear una instancia de experiencia laboral asociada al freelancer.
2. Verificar que se guarda correctamente en la base de datos.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                   |
|------------------------------|-------------------------------------------------------------------|
| Experiencia añadida           | La experiencia debe asociarse al freelancer.                    |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la experiencia se añade correctamente.

---

### Test: `testAddPortfolioFreelancerProfile`

**Objetivo:** Verificar que se puede añadir un proyecto al portafolio del freelancer.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.

**Datos de Entrada:**
- Proyecto de portafolio:
  - `project_name`: "Testing Project".
  - `project_description`: "Description of a testing project".
  - `project_duration_months`: `12`.
  - `project_link`: "https://github.com/freelancer_test".

**Pasos Realizados:**
1. Crear una instancia de proyecto de portafolio asociada al freelancer.
2. Verificar que se guarda correctamente en la base de datos.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                   |
|------------------------------|-------------------------------------------------------------------|
| Portafolio añadido            | El proyecto debe asociarse al freelancer.                       |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el proyecto se añade correctamente.

---

### Test: `testAddRatingFreelancerProfile`

**Objetivo:** Verificar que se puede añadir una calificación al perfil del freelancer.

**Precondiciones:**
- El cliente debe estar autenticado y asociado al freelancer.

**Datos de Entrada:**
- Calificación:
  - `rating`: `5`.
  - `comment`: "Excellent work.".
  - `date_posted`: Fecha actual.

**Pasos Realizados:**
1. Crear una instancia de calificación asociada al freelancer y al cliente.
2. Verificar que se guarda correctamente en la base de datos.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                   |
|------------------------------|-------------------------------------------------------------------|
| Calificación añadida          | La calificación debe asociarse al freelancer.                   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la calificación se añade correctamente.
