# Documentación de Pruebas Unitarias: `ClientProfileTest`

## Configuración del Escenario para `ClientProfileTest`

| Nombre             | Clase      | Escenario                                                                 |
|--------------------|------------|---------------------------------------------------------------------------|
| `client_user`      | `User`     | Usuario con rol de cliente.                                               |
| `client_profile`   | `Client`   | Perfil asociado al usuario cliente.                                       |
| `client_url`       | `str`      | URL de acceso a la página de perfil del cliente (`clientProfile`).         |

---

## Pruebas

### Test: `testGetClientProfile`

**Objetivo:** Verificar que la página de configuración del perfil del cliente se carga correctamente.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Realiza una solicitud GET a la URL del perfil del cliente (`clientProfile`).
2. Verifica que el código de estado sea `200`.
3. Verifica que se utilice la plantilla `accounts/clientProfile.html`.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                                             |
|---------------------------|-----------------------------------------------------------|
| Código de estado correcto  | La respuesta debe tener un código `200`.                   |
| Uso de plantilla correcta  | Se debe utilizar la plantilla `accounts/clientProfile.html`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la página se carga correctamente.

---

### Test: `testRedirectUnauthenticatedUser`

**Objetivo:** Verificar que un usuario no autenticado sea redirigido a la página de inicio de sesión al intentar acceder al perfil del cliente.

**Precondiciones:**
- El usuario no debe estar autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Cierra la sesión del usuario cliente.
2. Realiza una solicitud GET a la URL del perfil del cliente.
3. Verifica que el código de estado sea `302`.
4. Verifica que redirige a la página de inicio de sesión (`/login`).

**Resultados Esperados:**

| **Resultado**             | **Descripción**                                             |
|---------------------------|-----------------------------------------------------------|
| Código de redirección      | La respuesta debe tener un código `302`.                   |
| Redirección al login       | El usuario debe ser redirigido a la página de inicio de sesión. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los usuarios no autenticados no pueden acceder al perfil del cliente.

---

### Test: `testUpdateClientProfile`

**Objetivo:** Verificar que los datos del perfil del cliente se puedan actualizar correctamente.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.

**Datos de Entrada:**
- Nuevos datos para actualizar el perfil:
  - `phoneNumber`: "111222333".
  - `description_company`: "Updated description".

**Pasos Realizados:**
1. Realiza una solicitud POST a la URL del perfil del cliente con los datos de entrada.
2. Verifica que el código de estado sea `302`.
3. Refresca el objeto `client_profile` desde la base de datos.
4. Verifica que los datos del perfil se han actualizado correctamente.

**Resultados Esperados:**

| **Resultado**                     | **Descripción**                                             |
|-----------------------------------|-----------------------------------------------------------|
| Código de redirección              | La respuesta debe tener un código `302`.                   |
| Actualización de datos             | Los datos en la base de datos deben coincidir con los nuevos valores proporcionados. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los datos del perfil se actualizan correctamente.

---

### Test: `testUploadProfilePicture`

**Objetivo:** Verificar que el cliente pueda subir una imagen de perfil válida.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.

**Datos de Entrada:**
- Archivo de imagen válido (`test_image.jpg`).

**Pasos Realizados:**
1. Realiza una solicitud POST a la URL del perfil del cliente con el archivo de imagen.
2. Verifica que el código de estado sea `302`.
3. Refresca el objeto `client_profile` desde la base de datos.
4. Verifica que el campo `profile_pic` contiene el archivo subido.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                                             |
|---------------------------|-----------------------------------------------------------|
| Código de redirección      | La respuesta debe tener un código `302`.                   |
| Archivo subido correctamente| El campo `profile_pic` del perfil debe contener la nueva imagen. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que las imágenes de perfil se pueden subir correctamente.

---

### Test: `testInvalidFileUpload`

**Objetivo:** Verificar que no se permitan subir archivos no válidos como imágenes de perfil.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.

**Datos de Entrada:**
- Archivo no válido (`test.txt` con contenido de texto plano).

**Pasos Realizados:**
1. Realiza una solicitud POST a la URL del perfil del cliente con el archivo no válido.
2. Verifica que el código de estado sea `200`.
3. Verifica que el formulario muestra un error para el campo `profile_pic`.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                             |
|------------------------------|-----------------------------------------------------------|
| Código de estado correcto     | La respuesta debe tener un código `200`.                   |
| Error en el formulario         | El formulario debe mostrar un error en el campo `profile_pic`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los archivos no válidos no se permiten como imágenes de perfil.
