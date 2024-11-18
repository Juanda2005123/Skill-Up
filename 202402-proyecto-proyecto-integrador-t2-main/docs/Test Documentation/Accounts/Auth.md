# Documentación de Pruebas Unitarias: `TestAuthentication`

## Configuración del Escenario para `TestAuthentication`

| Nombre                      | Clase             | Escenario                                                                 |
|-----------------------------|-------------------|---------------------------------------------------------------------------|
| `clientUser`                | `Userk`           | Usuario con rol de cliente.                                               |
| `freelancerUser`            | `Userk`           | Usuario con rol de freelancer.                                            |
| `testClientInstance`        | `Client`          | Instancia de cliente asociada a `clientUser`.                             |
| `freelancer`                | `Freelancer`      | Instancia de freelancer asociada a `freelancerUser`.                      |
| `projectContributor`        | `ProjectContributor` | Contribuidor del proyecto asociado al freelancer.                         |
| `urls`                      | Django URLs       | Varias URLs configuradas para las pruebas (`login`, `register`, etc.).    |

---

## Pruebas

### Test: `testClientAccessToLogIn`

**Objetivo:** Verificar que un cliente logueado es redirigido correctamente a `clientProject` al acceder a la vista de login.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.

**Datos de Entrada:**
- Usuario autenticado: `clientUser`.

**Pasos Realizados:**
1. Realiza una solicitud GET a la URL `login` con un usuario autenticado como cliente.
2. Verifica que el código de estado sea `302`.
3. Verifica que redirige a la URL `/clientProject/`.

**Resultados Esperados:**

| **Resultado**           | **Descripción**                                    |
|-------------------------|--------------------------------------------------|
| Código de redirección    | La respuesta debe tener un código `302`.           |
| Redirección correcta     | El usuario debe ser redirigido a `/clientProject/`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que un cliente logueado es redirigido correctamente.

---

### Test: `testFreelancerAccessToLogIn`

**Objetivo:** Verificar que un freelancer logueado es redirigido correctamente a `browseProject` al acceder a la vista de login.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.

**Datos de Entrada:**
- Usuario autenticado: `freelancerUser`.

**Pasos Realizados:**
1. Realiza una solicitud GET a la URL `login` con un usuario autenticado como freelancer.
2. Verifica que el código de estado sea `302`.
3. Verifica que redirige a la URL `/browseProject/`.

**Resultados Esperados:**

| **Resultado**           | **Descripción**                                    |
|-------------------------|--------------------------------------------------|
| Código de redirección    | La respuesta debe tener un código `302`.           |
| Redirección correcta     | El usuario debe ser redirigido a `/browseProject/`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que un freelancer logueado es redirigido correctamente.

---

### Test: `testUnauthenticatedUserAccessToLogIn`

**Objetivo:** Verificar que un usuario no autenticado puede acceder a la vista de login.

**Precondiciones:**
- El usuario no debe estar autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Realiza una solicitud GET a la URL `login` sin un usuario autenticado.
2. Verifica que el código de estado sea `200`.

**Resultados Esperados:**

| **Resultado**           | **Descripción**                                    |
|-------------------------|--------------------------------------------------|
| Código de estado correcto| La respuesta debe tener un código `200`.          |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que un usuario no autenticado puede acceder a la vista de login.

---

### Test: `testClientAccessToClientRegister`

**Objetivo:** Verificar que un cliente logueado es redirigido a `clientProject` al acceder a la vista de registro de cliente.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.

**Datos de Entrada:**
- Usuario autenticado: `clientUser`.

**Pasos Realizados:**
1. Realiza una solicitud GET a la URL `clientRegister` con un usuario autenticado como cliente.
2. Verifica que el código de estado sea `302`.
3. Verifica que redirige a la URL `/clientProject/`.

**Resultados Esperados:**

| **Resultado**           | **Descripción**                                    |
|-------------------------|--------------------------------------------------|
| Código de redirección    | La respuesta debe tener un código `302`.           |
| Redirección correcta     | El usuario debe ser redirigido a `/clientProject/`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que un cliente logueado no puede acceder a `clientRegister`.

---

### Test: `testUnauthenticatedUserAccessToFreelancerProfile`

**Objetivo:** Verificar que un usuario no autenticado sea redirigido al login al intentar acceder a un perfil de freelancer.

**Precondiciones:**
- El usuario no debe estar autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Realiza una solicitud GET a la URL `freelancerProfile` con un usuario no autenticado.
2. Verifica que el código de estado sea `302`.
3. Verifica que redirige a la URL `/login`.

**Resultados Esperados:**

| **Resultado**           | **Descripción**                                    |
|-------------------------|--------------------------------------------------|
| Código de redirección    | La respuesta debe tener un código `302`.           |
| Redirección al login     | El usuario debe ser redirigido a `/login`.         |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los usuarios no autenticados no pueden acceder a `freelancerProfile`.

---

### Test: `testFreelancerAccessToFreelancerProfileSettings`

**Objetivo:** Verificar que un freelancer logueado puede acceder a la configuración de su perfil.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.

**Datos de Entrada:**
- Usuario autenticado: `freelancerUser`.

**Pasos Realizados:**
1. Realiza una solicitud GET a la URL `freelancerProfileSettings` con un usuario autenticado como freelancer.
2. Verifica que el código de estado sea `200`.

**Resultados Esperados:**

| **Resultado**           | **Descripción**                                    |
|-------------------------|--------------------------------------------------|
| Código de estado correcto| La respuesta debe tener un código `200`.          |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que un freelancer logueado puede acceder a `freelancerProfileSettings`.

---

## Resumen de Resultados

- Todas las pruebas se ejecutaron exitosamente.
- Se verificó el acceso y la redirección para usuarios autenticados y no autenticados en múltiples vistas.
