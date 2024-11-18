# Documentación de Pruebas Unitarias: `ClientRegisterTests`

## Configuración del Escenario para `ClientRegisterTests`

| Nombre                | Clase     | Escenario                                                                 |
|-----------------------|-----------|---------------------------------------------------------------------------|
| `client_register_url` | `str`     | URL de acceso a la página de registro de cliente (`clientRegister`).       |
| `valid_data`          | `dict`    | Datos de entrada válidos para realizar un registro exitoso.                |

---

## Pruebas

### Test: `testClientRegisterPageLoads`

**Objetivo:** Verificar que la página de registro de cliente se carga correctamente.

**Precondiciones:**
- Ninguna.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Realiza una solicitud GET a la URL de registro de cliente.
2. Verifica que el código de estado de la respuesta sea `200`.
3. Verifica que se utiliza la plantilla `accounts/clientRegister.html`.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                   |
|------------------------------|-------------------------------------------------------------------|
| Código de estado correcto     | La respuesta debe tener un código `200`.                         |
| Uso de plantilla correcta     | Debe utilizarse la plantilla `accounts/clientRegister.html`.      |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la página de registro se carga correctamente.

---

### Test: `testClientRegisterValidPost`

**Objetivo:** Verificar que un cliente válido se registre correctamente.

**Precondiciones:**
- Ninguna.

**Datos de Entrada:**
- Datos válidos para el registro:
  - `username`: "testuser".
  - `password1`: "StrongPassword123".
  - Otros datos requeridos del cliente.

**Pasos Realizados:**
1. Realiza una solicitud POST a la URL de registro de cliente con datos válidos.
2. Verifica que el código de estado sea `302`.
3. Verifica que se crea un nuevo usuario en la base de datos.
4. Verifica que se crea un nuevo cliente asociado al usuario.
5. Comprueba que los datos del cliente coinciden con los datos de entrada.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                                                     |
|---------------------------|---------------------------------------------------------------------|
| Código de redirección      | La respuesta debe tener un código `302`.                           |
| Usuario creado             | Debe existir un nuevo usuario en la base de datos.                 |
| Cliente creado             | Debe existir un nuevo cliente en la base de datos.                |
| Datos correctos            | Los datos del cliente deben coincidir con los datos proporcionados.|

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el cliente se registra correctamente.

---

### Test: `testClientRegisterInvalidPost`

**Objetivo:** Verificar que los errores de validación en el formulario de registro se manejen correctamente.

**Precondiciones:**
- Ninguna.

**Datos de Entrada:**
- Datos inválidos con contraseñas que no coinciden:
  - `password1`: "StrongPassword123".
  - `password2`: "WrongPassword".

**Pasos Realizados:**
1. Realiza una solicitud POST a la URL de registro de cliente con datos inválidos.
2. Verifica que el código de estado sea `200`.
3. Comprueba que no se crea ningún usuario ni cliente en la base de datos.
4. Verifica que el formulario muestra el error "The two password fields didn’t match.".

**Resultados Esperados:**

| **Resultado**             | **Descripción**                                                     |
|---------------------------|---------------------------------------------------------------------|
| Código de estado correcto  | La respuesta debe tener un código `200`.                           |
| Usuario no creado          | No debe existir un nuevo usuario en la base de datos.              |
| Cliente no creado          | No debe existir un nuevo cliente en la base de datos.             |
| Error en el formulario     | El formulario debe mostrar un error en el campo `password2`.       |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los errores de validación se manejan correctamente.

---

### Test: `testRequiredFields`

**Objetivo:** Verificar que todos los campos requeridos en el formulario de registro se validen correctamente.

**Precondiciones:**
- Ninguna.

**Datos de Entrada:**
- Datos de registro con un campo requerido vacío.

**Pasos Realizados:**
1. Itera sobre cada campo requerido en los datos de entrada.
2. Realiza una solicitud POST a la URL de registro de cliente con el campo vacío.
3. Verifica que el código de estado sea `200`.
4. Comprueba que el formulario muestra un error para el campo vacío.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                                                     |
|---------------------------|---------------------------------------------------------------------|
| Código de estado correcto  | La respuesta debe tener un código `200`.                           |
| Error en el formulario     | El formulario debe mostrar un error para el campo vacío.           |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que todos los campos requeridos son validados correctamente.
