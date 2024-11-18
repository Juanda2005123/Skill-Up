# Documentación de Pruebas Unitarias: `TestRecoverMyAccount`

## Configuración del Escenario para `TestRecoverMyAccount`

| **Nombre**                | **Clase**       | **Escenario**                                                                                   |
|---------------------------|-----------------|-------------------------------------------------------------------------------------------------|
| `client`                  | `TestClient`    | Cliente de prueba para realizar solicitudes HTTP simuladas.                                     |
| `landPage`                | `str`           | URL de la página de recuperación de contraseña, definida como `reverse('recoverPassword')`.     |
| `passwordResetDone`       | `str`           | URL de confirmación tras el envío del correo de recuperación, definida como `reverse('password_reset_done')`. |
| `passwordResetConfirm`    | `str`           | URL para confirmar el restablecimiento de contraseña con `uidb64` y `token`.                   |
| `passwordResetComplete`   | `str`           | URL de finalización del restablecimiento de contraseña, definida como `reverse('password_reset_complete')`. |
| `user`                    | `Userk`         | Usuario creado para las pruebas de recuperación de contraseña.                                 |

---

## Pruebas

### Test: `testRecoverPasswordPageAccess`

**Objetivo:** Verificar que la página de recuperación de contraseña se cargue correctamente.

**Precondiciones:**
- Ningún usuario autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Realizar una solicitud `GET` a la URL de recuperación de contraseña (`landPage`).

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                       |
|-----------------------------|-----------------------------------------------------|
| Código de estado `200`       | La página se carga correctamente.                   |
| Plantilla correcta           | Se utiliza la plantilla `accounts/recoverPassword.html`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la página se carga correctamente.

---

### Test: `testRecoverPasswordSentPageAccess`

**Objetivo:** Verificar que la página de confirmación tras el envío de recuperación de contraseña se cargue correctamente.

**Precondiciones:**
- Ningún usuario autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Realizar una solicitud `GET` a la URL `passwordResetDone`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                       |
|-----------------------------|-----------------------------------------------------|
| Código de estado `200`       | La página se carga correctamente.                   |
| Plantilla correcta           | Se utiliza la plantilla `accounts/recoverPasswordSent.html`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la página se carga correctamente.

---

### Test: `testRecoverPasswordEmailSent`

**Objetivo:** Verificar que se envíe un correo tras la solicitud de recuperación de contraseña.

**Precondiciones:**
- El usuario debe estar registrado con un correo válido.

**Datos de Entrada:**

| **Campo**    | **Valor**               |
|--------------|-------------------------|
| `email`      | `testuser@example.com`  |

**Pasos Realizados:**
1. Realizar una solicitud `POST` con el correo del usuario a `landPage`.
2. Verificar que se realiza la redirección a `passwordResetDone`.
3. Verificar que se envía un correo electrónico de recuperación.

**Resultados Esperados:**

| **Resultado**                   | **Descripción**                                  |
|---------------------------------|------------------------------------------------|
| Redirección correcta             | El usuario es redirigido a `passwordResetDone`. |
| Correo enviado                   | Se envía un correo de recuperación.            |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el correo es enviado.

---

### Test: `testPasswordResetConfirmPageAccess`

**Objetivo:** Verificar que la página de confirmación de restablecimiento de contraseña se cargue correctamente.

**Precondiciones:**
- La URL debe incluir un token y un identificador válido.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Realizar una solicitud `GET` a `passwordResetConfirm`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                       |
|-----------------------------|-----------------------------------------------------|
| Código de estado `200`       | La página se carga correctamente.                   |
| Plantilla correcta           | Se utiliza la plantilla `accounts/recoverPasswordForm.html`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la página se carga correctamente.

---

### Test: `testPasswordResetCompletePageAccess`

**Objetivo:** Verificar que la página de finalización del restablecimiento de contraseña se cargue correctamente.

**Precondiciones:**
- La solicitud debe ser válida.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Realizar una solicitud `GET` a `passwordResetComplete`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                       |
|-----------------------------|-----------------------------------------------------|
| Código de estado `200`       | La página se carga correctamente.                   |
| Plantilla correcta           | Se utiliza la plantilla `accounts/recoverPasswordDone.html`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la página se carga correctamente.

---

### Test: `testValidPasswordReset`

**Objetivo:** Verificar el proceso completo de restablecimiento de contraseña, incluyendo:
- Solicitud de restablecimiento.
- Confirmación del enlace recibido por correo.
- Restablecimiento exitoso de la contraseña.

**Precondiciones:**
- El usuario debe estar registrado con un correo válido.

**Datos de Entrada:**

| **Campo**        | **Valor**               |
|------------------|-------------------------|
| `email`          | `testuser@example.com`  |
| `new_password1`  | `password123`           |
| `new_password2`  | `password123`           |

**Pasos Realizados:**
1. Realizar una solicitud `POST` a `landPage` con el correo del usuario.
2. Extraer el enlace de restablecimiento del correo enviado.
3. Realizar una solicitud `POST` con las nuevas contraseñas a `passwordResetConfirm`.
4. Verificar que el usuario pueda iniciar sesión con la nueva contraseña.

**Resultados Esperados:**

| **Resultado**                   | **Descripción**                                       |
|---------------------------------|-----------------------------------------------------|
| Correo enviado                   | Se envía un correo de recuperación.                  |
| Enlace correcto                  | El enlace de restablecimiento extraído es válido.    |
| Restablecimiento exitoso         | El usuario puede iniciar sesión con la nueva contraseña. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el proceso completo de restablecimiento de contraseña funciona correctamente.

---
