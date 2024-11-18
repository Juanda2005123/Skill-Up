# Documentación de Pruebas Unitarias: Registro de Clientes

## Descripción General
Este conjunto de pruebas verifica el correcto funcionamiento del formulario de registro de clientes, incluyendo la validación de campos requeridos, manejo de errores y creación de objetos en la base de datos.

---

## Configuración del Escenario

| **Nombre**         | **Clase**  | **Descripción**                                    |
|--------------------|------------|----------------------------------------------------|
| `client_register_url` | `reverse` | URL para la página de registro de clientes.       |
| `valid_data`       | `dict`     | Datos válidos de prueba para el formulario.       |
| `Userk`            | `Model`    | Modelo de usuario extendido.                     |
| `Client`           | `Model`    | Modelo de perfil de cliente asociado al usuario. |

---

## Pruebas

### Test: `testClientRegisterPageLoads`

**Objetivo:** Verificar que la página de registro de clientes cargue correctamente.

**Precondiciones:**
- La URL `client_register_url` debe estar configurada.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Realizar una solicitud GET a la página de registro.
2. Verificar que el código de respuesta sea 200.
3. Confirmar que la plantilla `accounts/clientRegister.html` se utiliza para renderizar la página.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                    |
|-----------------------|----------------------------------------------------|
| Código de estado 200  | La solicitud se procesa correctamente.            |
| Plantilla correcta    | La plantilla utilizada es `clientRegister.html`.  |

---

### Test: `testClientRegisterValidPost`

**Objetivo:** Verificar que un formulario de registro válido cree correctamente los objetos `Userk` y `Client`.

**Precondiciones:**
- La URL `client_register_url` debe estar configurada.

**Datos de Entrada:**
- `valid_data`: Datos válidos de registro.

**Pasos Realizados:**
1. Realizar una solicitud POST con `valid_data`.
2. Verificar que los modelos `Userk` y `Client` se hayan creado.
3. Verificar que la respuesta sea una redirección.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                    |
|-----------------------|----------------------------------------------------|
| Código de estado 302  | Redirección después del registro exitoso.          |
| Objetos creados       | Se crean los objetos `Userk` y `Client`.          |

---

### Test: `testClientRegisterInvalidPost`

**Objetivo:** Verificar que los errores de validación sean manejados correctamente cuando los datos no son válidos.

**Precondiciones:**
- La URL `client_register_url` debe estar configurada.

**Datos de Entrada:**
- Datos con `password2` diferente de `password1`.

**Pasos Realizados:**
1. Realizar una solicitud POST con contraseñas que no coinciden.
2. Verificar que no se hayan creado objetos `Userk` ni `Client`.
3. Verificar que el formulario retorne un error en el campo `password2`.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                    |
|-----------------------|----------------------------------------------------|
| Código de estado 200  | La solicitud permanece en la misma página.         |
| Sin objetos creados   | No se crean objetos `Userk` ni `Client`.          |
| Error en el formulario| Mensaje de error en el campo `password2`.         |

---

### Test: `testRequiredFields`

**Objetivo:** Verificar que todos los campos requeridos sean validados correctamente.

**Precondiciones:**
- La URL `client_register_url` debe estar configurada.

**Datos de Entrada:**
- Datos con un campo requerido vacío.

**Pasos Realizados:**
1. Iterar sobre todos los campos requeridos.
2. En cada iteración, realizar una solicitud POST con el campo vacío.
3. Verificar que el formulario retorne un error en el campo correspondiente.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                    |
|-----------------------|----------------------------------------------------|
| Código de estado 200  | La solicitud permanece en la misma página.         |
| Errores por campo     | Se muestra un error para cada campo vacío.         |

---
