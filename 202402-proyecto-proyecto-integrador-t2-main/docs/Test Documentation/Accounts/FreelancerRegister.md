# Documentación de Pruebas Unitarias: `FreelancerRegisterTests`

## Configuración del Escenario para `FreelancerRegisterTests`

| Nombre                     | Clase                | Escenario                                                              |
|----------------------------|----------------------|------------------------------------------------------------------------|
| `freelancer_register_url`  | `str`                | URL del formulario de registro de freelancers.                        |
| `valid_data`               | `dict`              | Conjunto de datos válidos para realizar un registro de freelancer.     |

---

## Pruebas

### Test: `testFreelancerRegisterPageLoads`

**Objetivo:** Verificar que la página de registro de freelancers se cargue correctamente.

**Precondiciones:**
- Ninguna.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Hacer una solicitud `GET` a la URL del registro de freelancers.
2. Verificar el código de estado HTTP de la respuesta.
3. Verificar que se utiliza la plantilla `accounts/freelancerRegister.html`.
4. Verificar que el formulario en el contexto es una instancia de `SignUpFormFreelancer`.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                   |
|------------------------------|-------------------------------------------------------------------|
| Código de estado correcto     | La respuesta debe tener un código de estado `200`.               |
| Uso de plantilla correcta     | Debe utilizarse la plantilla `accounts/freelancerRegister.html`. |
| Instancia de formulario correcta | El formulario en el contexto debe ser una instancia de `SignUpFormFreelancer`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la página de registro de freelancers se carga correctamente.

---

### Test: `testFreelancerRegisterValidPost`

**Objetivo:** Verificar que un freelancer con datos válidos se registre correctamente.

**Precondiciones:**
- Ninguna.

**Datos de Entrada:**
- Datos válidos para el registro:
  - `username`: "testuser".
  - `first_name`: "Test".
  - `last_name`: "User".
  - `email`: "testuser@example.com".
  - `password1`: "TestPass123#".
  - `password2`: "TestPass123#".
  - `phoneNumber`: "123456789".
  - `identification`: "1005967728".

**Pasos Realizados:**
1. Realizar una solicitud `POST` con datos válidos a la URL de registro.
2. Verificar que se crean un objeto `Userk` y un objeto `Freelancer`.
3. Verificar que el código de estado HTTP sea `302` (redirección).
4. Verificar que los datos del freelancer se guardan correctamente en la base de datos.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                   |
|------------------------------|-------------------------------------------------------------------|
| Objetos creados correctamente | Se debe crear un objeto `Userk` y un objeto `Freelancer`.        |
| Redirección correcta          | La respuesta debe redirigir a una página (código `302`).         |
| Datos guardados correctamente | Los datos del freelancer deben coincidir con los datos enviados. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que un freelancer con datos válidos se registra correctamente.

---

### Test: `testFreelancerRegisterInvalidPasswordPost`

**Objetivo:** Verificar que los errores de validación se manejen correctamente cuando las contraseñas no coinciden.

**Precondiciones:**
- Ninguna.

**Datos de Entrada:**
- Datos de registro con contraseñas no coincidentes:
  - `password1`: "TestPass123#".
  - `password2`: "WrongPassword".

**Pasos Realizados:**
1. Realizar una solicitud `POST` con datos inválidos (contraseñas no coincidentes) a la URL de registro.
2. Verificar que no se crean objetos `Userk` ni `Freelancer`.
3. Verificar que el código de estado HTTP sea `200`.
4. Verificar que se utiliza la plantilla `accounts/freelancerRegister.html`.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                   |
|------------------------------|-------------------------------------------------------------------|
| Objetos no creados            | No se deben crear objetos `Userk` ni `Freelancer`.               |
| Código de estado correcto     | La respuesta debe tener un código de estado `200`.               |
| Uso de plantilla correcta     | Debe utilizarse la plantilla `accounts/freelancerRegister.html`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los errores de validación se manejan correctamente cuando las contraseñas no coinciden.

---
