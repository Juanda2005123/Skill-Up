# Documentación de Pruebas Unitarias: `freelancerProfileSettings`

## Descripción General
Este conjunto de pruebas asegura la funcionalidad correcta de la vista de configuración del perfil del freelancer, incluyendo la edición de la información personal, la adición de nuevas habilidades, y la gestión del portafolio.

---

## Configuración del Escenario

| **Nombre**              | **Clase**                | **Escenario**                                                       |
|-------------------------|--------------------------|----------------------------------------------------------------------|
| `freelancer_user`       | `Userk`                 | Usuario autenticado como freelancer.                                |
| `freelancer_group`      | `Group`                 | Grupo asociado al freelancer.                                       |
| `freelancer`            | `Freelancer`            | Perfil del freelancer autenticado.                                  |
| `skill1`, `skill2`      | `FreelancerSkillExpertise` | Habilidades iniciales asignadas al freelancer.                     |
| `portfolio`             | `Portfolio`             | Proyecto asociado al portafolio del freelancer.                     |

---

## Pruebas

### Test: `test_get_profile_settings`

**Objetivo:** Verificar que la página de configuración del perfil se carga correctamente.

**Precondiciones:**
- El freelancer debe estar autenticado.
- La vista debe renderizar correctamente el formulario `FreelancerForm`.

**Pasos Realizados:**
1. Realizar una solicitud GET a la URL `freelancerProfileSettings`.
2. Verificar el código de estado de la respuesta.
3. Confirmar que el formulario `FreelancerForm` está presente en el contexto.
4. Validar que la plantilla correcta es utilizada.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                   |
|--------------------------|--------------------------------------------------|
| Código de estado 200     | La página se carga correctamente.                |
| Contexto del formulario  | El formulario `FreelancerForm` está disponible.  |
| Plantilla correcta       | Se utiliza `freelancerProfileSettings.html`.     |

---

### Test: `test_update_profile`

**Objetivo:** Verificar que los datos del perfil del freelancer se actualicen correctamente.

**Precondiciones:**
- El freelancer debe estar autenticado.
- El formulario debe ser válido.

**Datos de Entrada:**
- `phoneNumber`: "9876543210"
- `email`: "new@example.com"
- `experience_level`: "Senior"
- `new_skills`: "React,Node.js"

**Pasos Realizados:**
1. Realizar una solicitud POST con los nuevos datos.
2. Verificar la redirección posterior a la misma URL.
3. Confirmar que los datos del perfil se han actualizado en la base de datos.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                                       |
|----------------------------|------------------------------------------------------|
| Redirección correcta        | La solicitud POST redirige a la misma URL.           |
| Datos actualizados          | Los nuevos valores están reflejados en el perfil.   |

---

### Test: `test_add_portfolio`

**Objetivo:** Verificar que se puedan añadir proyectos al portafolio del freelancer.

**Precondiciones:**
- El freelancer debe estar autenticado.
- Los datos del formulario de portafolio deben ser válidos.

**Datos de Entrada:**
- `project_name`: "Test Project"
- `project_description`: "Test Description"
- `project_duration_months`: 6
- `project_link`: "https://example.com/project"
- `project_image`: Imagen cargada de prueba.

**Pasos Realizados:**
1. Realizar una solicitud POST con los datos del portafolio.
2. Verificar la redirección posterior a la misma URL.
3. Confirmar que el proyecto aparece en la base de datos.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                       |
|-----------------------------|------------------------------------------------------|
| Redirección correcta         | La solicitud POST redirige a la misma URL.           |
| Proyecto agregado al portafolio | Los datos del proyecto están almacenados correctamente. |

---

### Consideraciones
- Todas las pruebas aseguran que las acciones realizadas estén restringidas al freelancer autenticado.
- Se validan las relaciones entre el freelancer, las habilidades y los proyectos asociados.
