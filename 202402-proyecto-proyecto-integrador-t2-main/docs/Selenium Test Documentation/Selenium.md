# Diseño de los casos de prueba 

## Funcionalidades que van a ser probadas con Selenium

- Inicio de sesión (Login)
- Registro de Freelancer
- Registro de Cliente
- Navegación y postulación a proyectos
- Creación de proyectos
- Navegación y visualización de proyectos
- Creación de chat entre clientes y freelancers
- Manejo de errores en el registro

## Casos de Prueba que serán realizados con Selenium

---

### Escenario: Navegar y Postularse a un Proyecto

#### Caso de Prueba 1: Postulación Exitosa a un Proyecto
- **Descripción**: Verificar que un freelancer puede postularse exitosamente a un proyecto.
- **Precondiciones**: 
  - El freelancer debe estar registrado y autenticado.
  - Deben existir proyectos en la plataforma.
- **Pasos**:
  1. Iniciar sesión como freelancer.
  2. Navegar a la página "Browse Projects".
  3. Seleccionar el primer proyecto de la lista.
  4. Hacer clic en el botón "Apply Project".
- **Resultado Esperado**:
  - El sistema confirma que la postulación fue exitosa.

#### Caso de Prueba 2: Navegar y Visualizar Proyectos
- **Descripción**: Verificar que un freelancer puede navegar y ver la información de varios proyectos.
- **Precondiciones**: 
  - El freelancer debe estar registrado y autenticado.
  - Deben existir proyectos en la plataforma.
- **Pasos**:
  1. Iniciar sesión como freelancer.
  2. Navegar a la página "Browse Projects".
  3. Seleccionar el primer proyecto y verificar la información.
  4. Regresar a la lista de proyectos y seleccionar el segundo proyecto.
- **Resultado Esperado**:
  - Se muestra la información detallada de ambos proyectos al navegar.

---

### Escenario: Creación de Chat

#### Caso de Prueba 1: Listar Freelancers para Crear un Chat
- **Descripción**: Verificar que un cliente puede listar freelancers asociados a un proyecto para iniciar un chat.
- **Precondiciones**:
  - El cliente debe estar autenticado.
  - Debe haber freelancers asociados a los proyectos del cliente.
- **Pasos**:
  1. Iniciar sesión como cliente.
  2. Navegar a "My Projects".
  3. Seleccionar un proyecto.
- **Resultado Esperado**:
  - Se muestra la información del proyecto y la lista de freelancers asociados.

---

### Escenario: Creación de Proyectos

#### Caso de Prueba 1: Creación Exitosa de Proyecto
- **Descripción**: Verificar que un cliente puede crear un proyecto proporcionando datos válidos.
- **Precondiciones**:
  - El cliente debe estar registrado y autenticado.
- **Pasos**:
  1. Iniciar sesión como cliente.
  2. Navegar a la página "My Projects".
  3. Hacer clic en "Create Project".
  4. Llenar el formulario con datos válidos.
  5. Confirmar la creación del proyecto.
- **Resultado Esperado**:
  - El proyecto aparece listado en la sección "My Projects".

---

### Escenario: Navegar por Proyectos

#### Caso de Prueba 1: Navegar al Primer Proyecto
- **Descripción**: Verificar que un freelancer puede acceder a la información del primer proyecto listado en la página de "Browse Projects".
- **Precondiciones**:
  - El freelancer debe estar registrado y autenticado.
  - Deben existir proyectos disponibles en la página "Browse Projects".
- **Pasos**:
  1. Iniciar sesión como freelancer.
  2. Navegar a la página "Browse Projects".
  3. Hacer clic en el primer proyecto listado.
- **Resultado Esperado**:
  - Se muestra la información detallada del primer proyecto.

---

#### Caso de Prueba 2: Navegar por Múltiples Proyectos
- **Descripción**: Verificar que un freelancer puede acceder a la información de varios proyectos navegando entre ellos.
- **Precondiciones**:
  - El freelancer debe estar registrado y autenticado.
  - Deben existir al menos dos proyectos disponibles en la página "Browse Projects".
- **Pasos**:
  1. Iniciar sesión como freelancer.
  2. Navegar a la página "Browse Projects".
  3. Hacer clic en el primer proyecto listado.
  4. Verificar que se muestra la información del primer proyecto.
  5. Regresar a la página "Browse Projects".
  6. Hacer clic en el segundo proyecto listado.
- **Resultado Esperado**:
  - Se muestra la información detallada del segundo proyecto.

---

### Escenario: Inicio de Sesión (Login)

#### Caso de Prueba 1: Inicio de Sesión Exitoso con Credenciales Válidas
- **Descripción**: Verificar que un usuario (cliente o freelancer) puede iniciar sesión exitosamente.
- **Precondiciones**:
  - El usuario debe estar registrado.
- **Pasos**:
  1. Navegar a la página de inicio de sesión.
  2. Ingresar un nombre de usuario y contraseña válidos.
  3. Hacer clic en "Login".
- **Resultado Esperado**:
  - El usuario es redirigido al dashboard correspondiente.

#### Caso de Prueba 2: Inicio de Sesión Fallido con Credenciales Inválidas
- **Descripción**: Verificar que el sistema no permite el inicio de sesión con credenciales incorrectas.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de inicio de sesión.
  2. Ingresar un nombre de usuario y contraseña inválidos.
  3. Hacer clic en "Login".
- **Resultado Esperado**:
  - Se muestra un mensaje de error indicando que las credenciales son incorrectas.

#### Caso de Prueba 3: Inicio de Sesión Fallido con Campos Vacíos
- **Descripción**: Verificar que el sistema no permite el inicio de sesión si los campos están vacíos.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de inicio de sesión.
  2. Dejar los campos vacíos y hacer clic en "Login".
- **Resultado Esperado**:
  - Se muestra un mensaje de error indicando que los campos son obligatorios.

#### Caso de Prueba 4: Inicio de Sesión Exitoso como Cliente Específico
- **Descripción**: Verificar que un cliente específico puede iniciar sesión con sus credenciales válidas.
- **Precondiciones**:
  - El cliente debe estar registrado.
- **Pasos**:
  1. Navegar a la página de inicio de sesión.
  2. Ingresar el nombre de usuario "juanperez123" y la contraseña "TestPassword123".
  3. Hacer clic en "Login".
- **Resultado Esperado**:
  - El cliente es redirigido a su dashboard.

#### Caso de Prueba 5: Inicio de Sesión Exitoso como Freelancer
- **Descripción**: Verificar que un freelancer puede iniciar sesión con sus credenciales válidas.
- **Precondiciones**:
  - El freelancer debe estar registrado.
- **Pasos**:
  1. Navegar a la página de inicio de sesión.
  2. Ingresar el nombre de usuario "juanQuintero" y la contraseña "TestPassword123".
  3. Hacer clic en "Login".
- **Resultado Esperado**:
  - El freelancer es redirigido a su dashboard.

---

### Escenario: Registro de Cliente

#### Caso de Prueba 1: Registro Exitoso con Datos Válidos
- **Descripción**: Verificar que un cliente puede registrarse exitosamente con datos válidos.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción "Register as Client".
  3. Llenar todos los campos obligatorios con datos válidos.
  4. Confirmar el registro.
- **Resultado Esperado**:
  - El cliente es redirigido a la página de inicio de sesión.

#### Caso de Prueba 2: Registro Fallido por Formato Inválido
- **Descripción**: Verificar que el sistema no permite registrar un cliente con datos inválidos (por ejemplo, correo o teléfono en formato incorrecto).
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción "Register as Client".
  3. Llenar los campos con datos inválidos (ej. correo con formato incorrecto).
  4. Intentar confirmar el registro.
- **Resultado Esperado**:
  - Se muestra un mensaje de error indicando que los datos no son válidos.

#### Caso de Prueba 3: Registro Fallido por Contraseñas No Coincidentes
- **Descripción**: Verificar que el sistema no permite registrar un cliente si las contraseñas no coinciden.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción "Register as Client".
  3. Ingresar contraseñas que no coinciden.
  4. Intentar confirmar el registro.
- **Resultado Esperado**:
  - Se muestra un mensaje de error indicando que las contraseñas no coinciden.

#### Caso de Prueba 4: Registro Fallido por Campos Vacíos
- **Descripción**: Verificar que el sistema no permite registrar un cliente si hay campos obligatorios vacíos.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción "Register as Client".
  3. Dejar uno o más campos obligatorios vacíos.
  4. Intentar confirmar el registro.
- **Resultado Esperado**:
  - Se muestra un mensaje de error indicando que los campos obligatorios deben llenarse.

---

### Escenario: Registro de Freelancer

#### Caso de Prueba 1: Registro Exitoso con Credenciales Válidas
- **Descripción**: Verificar que un freelancer puede registrarse correctamente con credenciales válidas.
- **Precondiciones**:
  - El usuario debe estar en la página de aterrizaje.
  - No debe existir un usuario con las mismas credenciales.
- **Pasos**:
  1. Hacer clic en el botón "Register" en la página de aterrizaje.
  2. Seleccionar la opción "Register as Freelancer".
  3. Completar los campos requeridos con datos válidos.
  4. Enviar el formulario.
- **Resultado Esperado**:
  - El usuario es redirigido a la página de inicio de sesión.

---

#### Caso de Prueba 2: Registro Fallido por Usuario ya Existente
- **Descripción**: Verificar que se muestra un mensaje de error al intentar registrar un usuario ya existente.
- **Precondiciones**:
  - El usuario debe estar en la página de aterrizaje.
  - El usuario ya debe estar registrado.
- **Pasos**:
  1. Hacer clic en el botón "Register" en la página de aterrizaje.
  2. Seleccionar la opción "Register as Freelancer".
  3. Completar los campos con datos de un usuario ya registrado.
  4. Enviar el formulario.
  5. Hacer clic en "Login" y autenticarse con las credenciales existentes.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error y permite iniciar sesión con el usuario existente.

---

#### Caso de Prueba 3: Registro Fallido con Número de Teléfono Inválido
- **Descripción**: Verificar que se muestra un mensaje de error al intentar registrar un usuario con un número de teléfono inválido.
- **Precondiciones**:
  - El usuario debe estar en la página de aterrizaje.
- **Pasos**:
  1. Hacer clic en el botón "Register" en la página de aterrizaje.
  2. Seleccionar la opción "Register as Freelancer".
  3. Completar los campos requeridos, ingresando un número de teléfono en un formato inválido.
  4. Enviar el formulario.
- **Resultado Esperado**:
  - Se muestra un mensaje de error indicando el formato incorrecto del número de teléfono.

---

#### Caso de Prueba 4: Registro Fallido con Identificación Inválida
- **Descripción**: Verificar que se muestra un mensaje de error al intentar registrar un usuario con un formato de identificación inválido.
- **Precondiciones**:
  - El usuario debe estar en la página de aterrizaje.
- **Pasos**:
  1. Hacer clic en el botón "Register" en la página de aterrizaje.
  2. Seleccionar la opción "Register as Freelancer".
  3. Completar los campos requeridos, ingresando un formato inválido en el campo de identificación.
  4. Enviar el formulario.
- **Resultado Esperado**:
  - Se muestra un mensaje de error indicando el formato incorrecto del campo de identificación.

---

#### Caso de Prueba 5: Registro Fallido con Contraseñas que No Coinciden
- **Descripción**: Verificar que se muestra un mensaje de error al intentar registrar un usuario con contraseñas que no coinciden.
- **Precondiciones**:
  - El usuario debe estar en la página de aterrizaje.
- **Pasos**:
  1. Hacer clic en el botón "Register" en la página de aterrizaje.
  2. Seleccionar la opción "Register as Freelancer".
  3. Completar los campos requeridos con contraseñas que no coincidan.
  4. Enviar el formulario.
- **Resultado Esperado**:
  - Se muestra un mensaje de error indicando que las contraseñas no coinciden.

---

#### Caso de Prueba 6: Registro Fallido con Campos Vacíos
- **Descripción**: Verificar que se muestra un mensaje de error al intentar registrar un usuario dejando campos requeridos vacíos.
- **Precondiciones**:
  - El usuario debe estar en la página de aterrizaje.
- **Pasos**:
  1. Hacer clic en el botón "Register" en la página de aterrizaje.
  2. Seleccionar la opción "Register as Freelancer".
  3. Intentar enviar el formulario dejando algunos campos vacíos.
- **Resultado Esperado**:
  - Se muestra un mensaje de error indicando que los campos están vacíos.

---

#### Caso de Prueba 7: Registro Fallido con Correo Electrónico Inválido
- **Descripción**: Verificar que se muestra un mensaje de error al intentar registrar un usuario con un formato de correo electrónico inválido.
- **Precondiciones**:
  - El usuario debe estar en la página de aterrizaje.
- **Pasos**:
  1. Hacer clic en el botón "Register" en la página de aterrizaje.
  2. Seleccionar la opción "Register as Freelancer".
  3. Completar los campos requeridos, ingresando un correo electrónico en un formato inválido.
  4. Enviar el formulario.
- **Resultado Esperado**:
  - Se muestra un mensaje de error indicando el formato incorrecto del correo electrónico.