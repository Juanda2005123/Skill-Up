# Documentación de Pruebas Unitarias: `TestDashboard`

## Configuración del Escenario para `TestDashboard`

| **Nombre**               | **Clase**           | **Escenario**                                                                                      |
|--------------------------|---------------------|----------------------------------------------------------------------------------------------------|
| `TestDashboard`          | `TestCase`         | Pruebas para las vistas de dashboard de freelancer y cliente.                                     |
| `clientUser`             | `Userk`            | Usuario autenticado como cliente.                                                                |
| `freelancerUser`         | `Userk`            | Usuario autenticado como freelancer.                                                             |
| `testClientInstance`     | `Client`           | Perfil asociado al usuario cliente.                                                              |
| `freelancer`             | `Freelancer`       | Perfil asociado al usuario freelancer.                                                           |
| `project`                | `Project`          | Proyecto de prueba asociado al cliente.                                                          |
| `projectContributor`     | `ProjectContributor` | Relación entre el proyecto y el freelancer.                                                      |
| `dashboard_freelancer_url` | `URL`            | URL para el acceso al dashboard del freelancer.                                                  |
| `dashboard_client_url`   | `URL`              | URL para el acceso al dashboard del cliente.                                                     |

---

## Pruebas

### Test: `testFreelancerAccessToDashboard`

**Objetivo:** Verificar que un freelancer autenticado pueda acceder a su dashboard.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Iniciar sesión como freelancer.
2. Acceder a la URL `dashboardFreelancer`.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                                    |
|----------------------------|--------------------------------------------------|
| Código de estado correcto  | La respuesta debe tener un código de estado `200`. |
| Contenido del dashboard     | La página debe mostrar "Welcome" y "My Projects". |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el freelancer puede acceder a su dashboard y ver el contenido esperado.

---

### Test: `testClientAccessToDashboard`

**Objetivo:** Verificar que un cliente autenticado pueda acceder a su dashboard.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Acceder a la URL `dashboardClient`.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                                    |
|----------------------------|--------------------------------------------------|
| Código de estado correcto  | La respuesta debe tener un código de estado `200`. |
| Contenido del dashboard     | La página debe mostrar "Welcome" y "My Projects". |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el cliente puede acceder a su dashboard y ver el contenido esperado.

---

### Test: `testUnauthenticatedUserAccessToFreelancerDashboard`

**Objetivo:** Verificar que un usuario no autenticado sea redirigido al login al intentar acceder al dashboard del freelancer.

**Precondiciones:**
- El usuario no debe estar autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Intentar acceder a la URL `dashboardFreelancer` sin autenticarse.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                                 |
|---------------------------|-----------------------------------------------|
| Redirección al login      | El usuario debe ser redirigido a `/login/`.     |
| Código de estado correcto | La respuesta debe tener un código de estado `302`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando la redirección al login para usuarios no autenticados.

---

### Test: `testFreelancerDashboardShowsProjects`

**Objetivo:** Verificar que el dashboard del freelancer muestre los proyectos asociados.

**Precondiciones:**
- Debe existir al menos un proyecto asociado al freelancer.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Iniciar sesión como freelancer.
2. Acceder a la URL `dashboardFreelancer`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                      |
|-----------------------------|----------------------------------------------------|
| Código de estado correcto   | La respuesta debe tener un código de estado `200`.   |
| Proyecto en el contenido     | El proyecto "Test Project" debe aparecer en el contenido. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los proyectos asociados se muestran correctamente.

---

### Test: `testClientDashboardShowsFinances`

**Objetivo:** Verificar que el dashboard del cliente muestre la sección de finanzas.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Acceder a la URL `dashboardClient`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                      |
|-----------------------------|----------------------------------------------------|
| Código de estado correcto   | La respuesta debe tener un código de estado `200`.   |
| Contenido financiero         | El texto "My Finances" debe aparecer en la página.   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la sección de finanzas se muestra correctamente en el dashboard del cliente.

---

### Test: `testFreelancerDashboardShowsBalance`

**Objetivo:** Verificar que el dashboard del freelancer muestre el balance disponible.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Iniciar sesión como freelancer.
2. Acceder a la URL `dashboardFreelancer`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                      |
|-----------------------------|----------------------------------------------------|
| Código de estado correcto   | La respuesta debe tener un código de estado `200`.   |
| Contenido financiero         | El texto "Available Balance" debe aparecer en la página. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el balance disponible se muestra correctamente
