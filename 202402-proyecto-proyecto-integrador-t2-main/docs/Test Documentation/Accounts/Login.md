# Documentación de Pruebas Unitarias: `LoginTests`

## Configuración del Escenario para `LoginTests`

| **Nombre**           | **Clase**       | **Escenario**                                                                                                                                  |
|-----------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `client_user`         | `Userk`         | Usuario cliente autenticado con atributo `is_client=True`.                                                                                     |
| `freelancer_user`     | `Userk`         | Usuario freelancer autenticado con atributo `is_freelancer=True`.                                                                              |
| `client_profile`      | `Client`        | Perfil de cliente asociado al `client_user`.                                                                                                   |
| `freelancer_profile`  | `Freelancer`    | Perfil de freelancer asociado al `freelancer_user`.                                                                                           |
| `login_url`           | `str`           | URL de la página de inicio de sesión, definida como `reverse('login')`.                                                                        |

---

## Pruebas

### Test: `test_login_page_loads_for_unauthenticated`

**Objetivo:** Verificar que la página de inicio de sesión carga correctamente para usuarios no autenticados.

**Precondiciones:**
- Ningún usuario debe estar autenticado al acceder a la página.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Realizar una solicitud `GET` a la URL de inicio de sesión (`login_url`).

**Resultados Esperados:**

| **Resultado**           | **Descripción**                              |
|-------------------------|----------------------------------------------|
| Código de estado `200`   | La página de inicio de sesión se carga correctamente. |
| Plantilla correcta       | Se utiliza la plantilla `accounts/login.html`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la página se carga correctamente.

---

### Test: `test_login_redirects_authenticated_client`

**Objetivo:** Verificar que un cliente autenticado sea redirigido a `clientProject`.

**Precondiciones:**
- El cliente debe estar autenticado antes de acceder a la página de inicio de sesión.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Autenticar al cliente utilizando `self.client.login`.
2. Realizar una solicitud `GET` a la URL de inicio de sesión.

**Resultados Esperados:**

| **Resultado**           | **Descripción**                                   |
|-------------------------|-------------------------------------------------|
| Redirección correcta     | El cliente es redirigido a la URL `clientProject`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando la redirección.

---

### Test: `test_client_login_success`

**Objetivo:** Verificar que un cliente puede iniciar sesión correctamente.

**Precondiciones:**
- El cliente debe estar registrado con credenciales válidas.

**Datos de Entrada:**

| **Campo**   | **Valor**          |
|-------------|--------------------|
| `username`  | `clientuser`       |
| `password`  | `papasFritas123`   |

**Pasos Realizados:**
1. Realizar una solicitud `POST` con las credenciales del cliente.
2. Verificar la redirección tras el inicio de sesión.
3. Verificar que el cliente está autenticado.

**Resultados Esperados:**

| **Resultado**           | **Descripción**                                       |
|-------------------------|-----------------------------------------------------|
| Redirección correcta     | El cliente es redirigido a `dashboardClient`.        |
| Autenticación exitosa    | El cliente está autenticado y `is_client=True`.     |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el cliente puede iniciar sesión.

---

### Test: `test_freelancer_login_success`

**Objetivo:** Verificar que un freelancer puede iniciar sesión correctamente.

**Precondiciones:**
- El freelancer debe estar registrado con credenciales válidas.

**Datos de Entrada:**

| **Campo**   | **Valor**          |
|-------------|--------------------|
| `username`  | `freelanceruser`   |
| `password`  | `huevosFritos123`  |

**Pasos Realizados:**
1. Realizar una solicitud `POST` con las credenciales del freelancer.
2. Verificar la redirección tras el inicio de sesión.
3. Verificar que el freelancer está autenticado.

**Resultados Esperados:**

| **Resultado**           | **Descripción**                                       |
|-------------------------|-----------------------------------------------------|
| Redirección correcta     | El freelancer es redirigido a `dashboardFreelancer`. |
| Autenticación exitosa    | El freelancer está autenticado y `is_freelancer=True`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el freelancer puede iniciar sesión.

---

### Test: `test_login_fail_invalid_credentials`

**Objetivo:** Verificar que el inicio de sesión falla si se proporcionan credenciales inválidas.

**Precondiciones:**
- El usuario debe estar registrado, pero las credenciales proporcionadas no son correctas.

**Datos de Entrada:**

| **Campo**   | **Valor**          |
|-------------|--------------------|
| `username`  | `clientuser`       |
| `password`  | `contraseñaIncorrecta` |

**Pasos Realizados:**
1. Realizar una solicitud `POST` con credenciales incorrectas.
2. Verificar que no se redirige al dashboard.
3. Verificar que se muestra un mensaje de error.

**Resultados Esperados:**

| **Resultado**           | **Descripción**                                        |
|-------------------------|------------------------------------------------------|
| Código de estado `200`   | La página de inicio de sesión se carga nuevamente.     |
| Mensaje de error         | Se muestra "Username or password is incorrect".       |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el inicio de sesión falla con credenciales inválidas.

---

### Test: `test_login_with_empty_fields`

**Objetivo:** Verificar que el inicio de sesión falla cuando los campos están vacíos.

**Precondiciones:**
- Ninguno.

**Datos de Entrada:**

| **Campo**   | **Valor** |
|-------------|-----------|
| `username`  | `""`      |
| `password`  | `""`      |

**Pasos Realizados:**
1. Realizar una solicitud `POST` con campos vacíos.
2. Verificar que no se redirige al dashboard.
3. Verificar que se muestra un mensaje de error.

**Resultados Esperados:**

| **Resultado**           | **Descripción**                                        |
|-------------------------|------------------------------------------------------|
| Código de estado `200`   | La página de inicio de sesión se carga nuevamente.     |
| Mensaje de error         | Se muestra un mensaje de error para campos vacíos.    |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el inicio de sesión falla con campos vacíos.

---
