# Documentación de Pruebas Unitarias: `testViews`

## Configuración del Escenario para `testViews`

| Nombre           | Clase          | Escenario                                                          |
|------------------|----------------|--------------------------------------------------------------------|
| `Client`         | Django Client  | Cliente simulado para enviar solicitudes HTTP durante las pruebas. |
| `Userk`          | Modelo Usuario | Usuario creado para pruebas relacionadas con autenticación.        |
| `SignUpFormFreelancer` | Formulario | Formulario para pruebas de registro de freelancers.               |

---

## Pruebas

### Test: `test_login_view_GET`

**Objetivo:** Verificar que la vista de inicio de sesión sea accesible mediante una solicitud GET.

**Precondiciones:**
- La URL `login` debe estar configurada y apuntar a la vista de inicio de sesión.

**Datos de Entrada:**
- Solicitud HTTP GET a la URL de inicio de sesión.

**Pasos Realizados:**
1. Realiza una solicitud GET a la URL `login`.
2. Verifica que el código de estado sea `200`.
3. Verifica que se utilice la plantilla `accounts/login.html`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                               |
|-----------------------------|-----------------------------------------------|
| Código de estado correcto    | La respuesta debe tener un código `200`.      |
| Uso de plantilla correcta    | Debe utilizar la plantilla `accounts/login.html`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista de inicio de sesión responde correctamente.

---

### Test: `test_login_invalid_user_view_POST`

**Objetivo:** Verificar que un inicio de sesión con credenciales inválidas no permite acceso.

**Precondiciones:**
- Un usuario debe existir previamente con credenciales específicas.

**Datos de Entrada:**
- `username`: `testuser`
- `password`: `password123`

**Pasos Realizados:**
1. Realiza una solicitud POST a la URL `login` con credenciales inválidas.
2. Verifica que el código de estado sea `200` (no redirige).
3. Verifica que se utilice la plantilla `accounts/login.html`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                 |
|-----------------------------|-----------------------------------------------|
| Código de estado correcto    | La respuesta debe tener un código `200`.       |
| Uso de plantilla correcta    | Debe utilizar la plantilla `accounts/login.html`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que las credenciales inválidas no permiten acceso.

---

### Test: `test_login_view_POST`

**Objetivo:** Verificar que un inicio de sesión con credenciales válidas redirige correctamente.

**Precondiciones:**
- El usuario debe existir con credenciales válidas.

**Datos de Entrada:**
- `username`: `c`
- `password`: `client0105`

**Pasos Realizados:**
1. Realiza una solicitud POST a la URL `login` con credenciales válidas.
2. Verifica que el código de estado sea `302`.
3. Verifica que redirige correctamente a la vista `clientProject`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                               |
|-----------------------------|-----------------------------------------------|
| Código de redirección         | La respuesta debe tener un código `302`.      |
| Redirección correcta          | Debe redirigir a la vista `clientProject`.    |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el inicio de sesión con credenciales válidas funciona correctamente.

---

### Test: `test_signup_form_not_valid_data`

**Objetivo:** Verificar que el formulario de registro no sea válido con una contraseña común.

**Precondiciones:**
- El formulario `SignUpFormFreelancer` debe estar configurado y funcional.

**Datos de Entrada:**
- Contraseña: `password123` (común y no segura).

**Pasos Realizados:**
1. Crea una instancia del formulario `SignUpFormFreelancer` con datos no válidos.
2. Valida el formulario.
3. Verifica que el formulario no pase la validación.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                       |
|------------------------------|-----------------------------------------------------|
| Formulario inválido           | El formulario no debe pasar la validación.           |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el formulario no acepta contraseñas comunes.

---

### Test: `test_signup_form_valid_data`

**Objetivo:** Verificar que el formulario de registro sea válido con datos correctos.

**Precondiciones:**
- El formulario `SignUpFormFreelancer` debe estar configurado y funcional.

**Datos de Entrada:**
- Contraseña: `EySiMrJohn095` (segura y válida).

**Pasos Realizados:**
1. Crea una instancia del formulario `SignUpFormFreelancer` con datos válidos.
2. Valida el formulario.
3. Verifica que el formulario pase la validación.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                       |
|------------------------------|-----------------------------------------------------|
| Formulario válido             | El formulario debe pasar la validación.              |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el formulario acepta datos válidos.

---

## Resumen de Resultados

- Todas las pruebas se ejecutaron exitosamente.
- Se verificó la funcionalidad básica de las vistas de inicio de sesión y el formulario de registro.
