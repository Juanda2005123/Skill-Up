# Documentación de Pruebas Unitarias: `TestSecurity`

## Configuración del Escenario para `TestSecurity`

| **Nombre**                   | **Clase**          | **Escenario**                                                                                      |
|------------------------------|--------------------|----------------------------------------------------------------------------------------------------|
| `TestSecurity`               | `TestCase`         | Pruebas de seguridad para las vistas del dashboard.                                               |
| `clientUser`                 | `Userk`            | Usuario de prueba con permisos de cliente.                                                        |
| `freelancerUser`             | `Userk`            | Usuario de prueba con permisos de freelancer.                                                     |
| `testClientInstance`         | `Client`           | Perfil de cliente asociado al usuario `clientUser`.                                               |
| `freelancer`                 | `Freelancer`       | Perfil de freelancer asociado al usuario `freelancerUser`.                                        |

---

## Pruebas

### Test: `testFreelancerAccessToDashboardFreelancer`

**Objetivo:** Verificar que un freelancer pueda acceder a su dashboard correctamente.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Iniciar sesión como freelancer.
2. Acceder a la URL de `dashboardFreelancer`.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                   |
|--------------------------|-------------------------------------------------|
| Código de estado correcto| La respuesta debe tener un código de estado `200`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el freelancer puede acceder a su dashboard.

---

### Test: `testClientAccessToDashboardFreelancer`

**Objetivo:** Verificar que un cliente no pueda acceder al dashboard del freelancer.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Acceder a la URL de `dashboardFreelancer`.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                             |
|--------------------------|-----------------------------------------------------------|
| Mensaje de restricción   | El mensaje "You are not God to view this page bro" debe mostrarse. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el cliente no tiene acceso al dashboard del freelancer.

---

### Test: `testUnauthenticatedUserAccessToDashboardFreelancer`

**Objetivo:** Verificar que un usuario no autenticado sea redirigido al login al intentar acceder al dashboard del freelancer.

**Precondiciones:**
- El usuario no debe estar autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Intentar acceder a la URL de `dashboardFreelancer` sin autenticarse.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                   |
|--------------------------|-------------------------------------------------|
| Redirección al login      | El usuario debe ser redirigido a la página de login. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los usuarios no autenticados son redirigidos.

---

### Test: `testClientAccessToDashboardClient`

**Objetivo:** Verificar que un cliente pueda acceder a su dashboard correctamente.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Acceder a la URL de `dashboardClient`.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                   |
|--------------------------|-------------------------------------------------|
| Código de estado correcto| La respuesta debe tener un código de estado `200`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el cliente puede acceder a su dashboard.

---

### Test: `testFreelancerAccessToDashboardClient`

**Objetivo:** Verificar que un freelancer no pueda acceder al dashboard del cliente.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Iniciar sesión como freelancer.
2. Acceder a la URL de `dashboardClient`.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                             |
|--------------------------|-----------------------------------------------------------|
| Mensaje de restricción   | El mensaje "You are not God to view this page bro" debe mostrarse. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el freelancer no tiene acceso al dashboard del cliente.

---

### Test: `testUnauthenticatedUserAccessToDashboardClient`

**Objetivo:** Verificar que un usuario no autenticado sea redirigido al login al intentar acceder al dashboard del cliente.

**Precondiciones:**
- El usuario no debe estar autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Intentar acceder a la URL de `dashboardClient` sin autenticarse.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                   |
|--------------------------|-------------------------------------------------|
| Redirección al login      | El usuario debe ser redirigido a la página de login. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los usuarios no autenticados son redirigidos.

---

### Test: `testFreelancerAccessToFreelancerAnalysis`

**Objetivo:** Verificar que un freelancer pueda acceder a la vista de análisis del freelancer correctamente.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Iniciar sesión como freelancer.
2. Acceder a la URL de `freelancerAnalysis`.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                   |
|--------------------------|-------------------------------------------------|
| Código de estado correcto| La respuesta debe tener un código de estado `200`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el freelancer puede acceder a su vista de análisis.

---

### Test: `testClientAccessToFreelancerAnalysis`

**Objetivo:** Verificar que un cliente no pueda acceder a la vista de análisis del freelancer.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Acceder a la URL de `freelancerAnalysis`.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                             |
|--------------------------|-----------------------------------------------------------|
| Mensaje de restricción   | El mensaje "You are not God to view this page bro" debe mostrarse. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el cliente no tiene acceso a la vista de análisis del freelancer.

---

