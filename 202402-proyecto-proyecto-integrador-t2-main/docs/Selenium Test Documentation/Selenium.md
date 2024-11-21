Aquí tienes el documento completo con todos los casos de prueba en formato Markdown, incluyendo los escenarios Gherkin que compartiste. Se han comparado y agregado los casos que no estaban previamente documentados para evitar repeticiones.

---

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
- Notificaciones de proyectos y chats

---

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
  3. Seleccionar el segundo proyecto de la lista.
  4. Hacer clic en el botón "Apply Project".
  5. Cerrar sesión.
  6. Iniciar sesión como cliente.
  7. Navegar a la página de "Notifications".
- **Resultado Esperado**:
  - El cliente recibe una notificación indicando que un freelancer ha aplicado al proyecto.

#### Caso de Prueba 2: Cliente Rechaza la Postulación
- **Descripción**: Verificar que un cliente puede rechazar la postulación de un freelancer.
- **Precondiciones**: 
  - El freelancer debe haber aplicado a un proyecto.
- **Pasos**:
  1. Iniciar sesión como cliente.
  2. Navegar a la página de "Notifications".
  3. Leer la notificación de postulación.
  4. Rechazar la postulación.
  5. Cerrar sesión.
  6. Iniciar sesión como freelancer.
  7. Navegar a "Notifications".
- **Resultado Esperado**:
  - El freelancer recibe una notificación de que su postulación fue rechazada.

---

### Escenario: Notificaciones de Proyectos y Propuestas

#### Caso de Prueba 1: Enviar Propuesta con Entregables
- **Descripción**: Verificar que un freelancer puede enviar una propuesta con entregables, y el cliente recibe la notificación.
- **Precondiciones**:
  - El freelancer debe estar registrado y autenticado.
  - Debe existir un proyecto activo.
- **Pasos**:
  1. Iniciar sesión como freelancer.
  2. Navegar a la página de "Notifications".
  3. Seleccionar una notificación.
  4. Llenar los hitos del proyecto.
  5. Cerrar sesión.
  6. Iniciar sesión como cliente.
  7. Navegar a la página de "Notifications".
- **Resultado Esperado**:
  - El cliente recibe una notificación con la propuesta enviada.

#### Caso de Prueba 2: Cliente Rechaza la Propuesta
- **Descripción**: Verificar que un cliente puede rechazar la propuesta de un freelancer.
- **Precondiciones**:
  - El freelancer debe haber enviado una propuesta.
- **Pasos**:
  1. Iniciar sesión como cliente.
  2. Navegar a la página de "Notifications".
  3. Leer la notificación de propuesta.
  4. Rechazar la propuesta.
  5. Cerrar sesión.
  6. Iniciar sesión como freelancer.
  7. Navegar a "Notifications".
- **Resultado Esperado**:
  - El freelancer recibe una notificación indicando que la propuesta fue rechazada.

#### Caso de Prueba 3: Cliente Aprueba la Propuesta
- **Descripción**: Verificar que un cliente puede aprobar la propuesta de un freelancer.
- **Precondiciones**:
  - El freelancer debe haber enviado una propuesta.
- **Pasos**:
  1. Iniciar sesión como cliente.
  2. Navegar a la página de "Notifications".
  3. Leer la notificación de propuesta.
  4. Aprobar la propuesta.
  5. Cerrar sesión.
  6. Iniciar sesión como freelancer.
  7. Navegar a "Notifications".
- **Resultado Esperado**:
  - El freelancer recibe una notificación indicando que la propuesta fue aprobada.

---

### Escenario: Inicio de Sesión (Login)

#### Caso de Prueba 1: Inicio de Sesión Exitoso
- **Descripción**: Verificar que un usuario puede iniciar sesión con credenciales válidas.
- **Precondiciones**:
  - El usuario debe estar registrado.
- **Pasos**:
  1. Navegar a la página de inicio de sesión.
  2. Ingresar credenciales válidas.
  3. Hacer clic en "Login".
- **Resultado Esperado**:
  - El usuario es redirigido al dashboard.

#### Caso de Prueba 2: Inicio de Sesión Fallido por Credenciales Inválidas
- **Descripción**: Verificar que no se permite el inicio de sesión con credenciales incorrectas.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de inicio de sesión.
  2. Ingresar credenciales inválidas.
  3. Hacer clic en "Login".
- **Resultado Esperado**:
  - Aparece un mensaje de error indicando credenciales incorrectas.

---

### Escenario: Registro de Usuarios

#### Caso de Prueba 1: Registro de Cliente con Datos Válidos
- **Descripción**: Verificar que un cliente puede registrarse correctamente.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar "Register as Client".
  3. Completar los campos obligatorios.
  4. Confirmar el registro.
- **Resultado Esperado**:
  - El cliente es redirigido a la página de inicio de sesión.

#### Caso de Prueba 2: Registro Fallido por Campos Vacíos
- **Descripción**: Verificar que no se permite el registro con campos vacíos.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar "Register as Client".
  3. Dejar campos obligatorios vacíos.
  4. Intentar registrar.
- **Resultado Esperado**:
  - Aparece un mensaje de error indicando que los campos son obligatorios.

#### Caso de Prueba 3: Registro de Freelancer con Datos Válidos
- **Descripción**: Verificar que un freelancer puede registrarse correctamente.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar "Register as Freelancer".
  3. Completar los campos obligatorios.
  4. Confirmar el registro.
- **Resultado Esperado**:
  - El freelancer es redirigido a la página de inicio de sesión.

---

### Escenario: Creación de Proyectos

#### Caso de Prueba 1: Creación Exitosa
- **Descripción**: Verificar que un cliente puede crear un proyecto con datos válidos.
- **Precondiciones**:
  - El cliente debe estar autenticado.
- **Pasos**:
  1. Iniciar sesión como cliente.
  2. Navegar a "My Projects".
  3. Hacer clic en "Create Project".
  4. Completar el formulario con datos válidos.
- **Resultado Esperado**:
  - El proyecto aparece listado en "My Projects".

#### Caso de Prueba 2: Creación Fallida por Campos Vacíos
- **Descripción**: Verificar que no se permite crear un proyecto con campos vacíos.
- **Precondiciones**:
  - El cliente debe estar autenticado.
- **Pasos**:
  1. Iniciar sesión como cliente.
  2. Navegar a "My Projects".
  3. Hacer clic en "Create Project".
  4. Completar algunos campos y dejar otros vacíos.
  5. Intentar guardar.
- **Resultado Esperado**:
  - Aparece un mensaje de error indicando que los campos son obligatorios.

---

### Escenario: Creación y Notificación de Chat

#### Caso de Prueba 1: Cliente Inicia un Chat
- **Descripción**: Verificar que un cliente puede iniciar un chat con un freelancer.
- **Precondiciones**:
  - El cliente debe estar autenticado.
- **Pasos**:
  1. Iniciar sesión como cliente.
  2. Navegar a "Notifications".
  3. Seleccionar una notificación de proyecto.
  4. Iniciar un chat con un freelancer.
- **Resultado Esperado**:
  - Se crea un chat y aparece en la lista de mensajes.

