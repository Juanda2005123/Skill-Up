# Documentación de Pruebas Unitarias: `TestUrls`

## Configuración del Escenario para `TestUrls`

| **Nombre**               | **Clase**         | **Escenario**                                                                                       |
|--------------------------|-------------------|-----------------------------------------------------------------------------------------------------|
| `SimpleTestCase`          | `TestUrls`        | Pruebas unitarias para verificar el correcto mapeo de URLs a sus respectivas vistas en la aplicación. |

---

## Pruebas

### Test: `testUrlLogin`

**Objetivo:** Verificar que la URL para el inicio de sesión (`login`) resuelva correctamente a la función de vista `loginPage`.

**Precondiciones:**
- La URL `login` debe estar definida en el archivo de URLs del proyecto.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Obtener la URL mediante `reverse('login')`.
2. Resolver la URL para verificar a qué función apunta.

**Resultados Esperados:**

| **Resultado**        | **Descripción**                                      |
|----------------------|----------------------------------------------------|
| URL resuelta         | La URL `login` apunta a la función `loginPage`.     |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL `login` resuelve correctamente.

---

### Test: `testUrlLandpage`

**Objetivo:** Verificar que la URL para la página de inicio (`landpage`) resuelva correctamente a la función de vista `landpage`.

**Precondiciones:**
- La URL `landpage` debe estar definida en el archivo de URLs del proyecto.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Obtener la URL mediante `reverse('landpage')`.
2. Resolver la URL para verificar a qué función apunta.

**Resultados Esperados:**

| **Resultado**        | **Descripción**                                        |
|----------------------|------------------------------------------------------|
| URL resuelta         | La URL `landpage` apunta a la función `landpage`.     |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL `landpage` resuelve correctamente.

---

### Test: `testUrlFreelancerRegister`

**Objetivo:** Verificar que la URL para el registro de freelancers (`freelancerRegister`) resuelva correctamente a la función de vista `freelancerRegister`.

**Precondiciones:**
- La URL `freelancerRegister` debe estar definida en el archivo de URLs del proyecto.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Obtener la URL mediante `reverse('freelancerRegister')`.
2. Resolver la URL para verificar a qué función apunta.

**Resultados Esperados:**

| **Resultado**        | **Descripción**                                             |
|----------------------|-----------------------------------------------------------|
| URL resuelta         | La URL `freelancerRegister` apunta a la función `freelancerRegister`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL `freelancerRegister` resuelve correctamente.

---

### Test: `testUrlClientRegister`

**Objetivo:** Verificar que la URL para el registro de clientes (`clientRegister`) resuelva correctamente a la función de vista `clientRegister`.

**Precondiciones:**
- La URL `clientRegister` debe estar definida en el archivo de URLs del proyecto.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Obtener la URL mediante `reverse('clientRegister')`.
2. Resolver la URL para verificar a qué función apunta.

**Resultados Esperados:**

| **Resultado**        | **Descripción**                                        |
|----------------------|------------------------------------------------------|
| URL resuelta         | La URL `clientRegister` apunta a la función `clientRegister`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL `clientRegister` resuelve correctamente.

---

### Test: `test_recoverPassword_url_resolves`

**Objetivo:** Verificar que la URL para la recuperación de contraseña (`recoverPassword`) resuelva correctamente a la clase de vista `PasswordResetView`.

**Precondiciones:**
- La URL `recoverPassword` debe estar definida en el archivo de URLs del proyecto.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Obtener la URL mediante `reverse('recoverPassword')`.
2. Resolver la URL para verificar a qué clase apunta.

**Resultados Esperados:**

| **Resultado**        | **Descripción**                                                 |
|----------------------|---------------------------------------------------------------|
| URL resuelta         | La URL `recoverPassword` apunta a la clase `PasswordResetView`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL `recoverPassword` resuelve correctamente.

---

### Test: `test_recoverPasswordConfirm_url_resolves`

**Objetivo:** Verificar que la URL para confirmar el restablecimiento de contraseña (`password_reset_confirm`) resuelva correctamente a la clase de vista `PasswordResetConfirmView`.

**Precondiciones:**
- La URL `password_reset_confirm` debe estar definida en el archivo de URLs del proyecto.

**Datos de Entrada:**
- Argumentos dinámicos: `uidb64` y `token`.

**Pasos Realizados:**
1. Obtener la URL mediante `reverse('password_reset_confirm', args=['uidb64', 'token'])`.
2. Resolver la URL para verificar a qué clase apunta.

**Resultados Esperados:**

| **Resultado**        | **Descripción**                                                          |
|----------------------|------------------------------------------------------------------------|
| URL resuelta         | La URL `password_reset_confirm` apunta a la clase `PasswordResetConfirmView`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL `password_reset_confirm` resuelve correctamente.

---

### Test: `testUrlClientProfile`

**Objetivo:** Verificar que la URL para el perfil de clientes (`clientProfile`) resuelva correctamente a la función de vista `client_profile`.

**Precondiciones:**
- La URL `clientProfile` debe estar definida en el archivo de URLs del proyecto.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Obtener la URL mediante `reverse('clientProfile')`.
2. Resolver la URL para verificar a qué función apunta.

**Resultados Esperados:**

| **Resultado**        | **Descripción**                                        |
|----------------------|------------------------------------------------------|
| URL resuelta         | La URL `clientProfile` apunta a la función `client_profile`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL `clientProfile` resuelve correctamente.

---

### Test: `testUrlFreelancerProfile`

**Objetivo:** Verificar que la URL para el perfil de freelancers (`freelancerProfile`) resuelva correctamente a la función de vista `freelancer_profile`.

**Precondiciones:**
- La URL `freelancerProfile` debe estar definida en el archivo de URLs del proyecto.

**Datos de Entrada:**
- Argumento dinámico: `id` del freelancer.

**Pasos Realizados:**
1. Obtener la URL mediante `reverse('freelancerProfile', args=[1])`.
2. Resolver la URL para verificar a qué función apunta.

**Resultados Esperados:**

| **Resultado**        | **Descripción**                                               |
|----------------------|-------------------------------------------------------------|
| URL resuelta         | La URL `freelancerProfile` apunta a la función `freelancer_profile`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL `freelancerProfile` resuelve correctamente.

---
