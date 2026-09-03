# Desarrollo de una API REST en dominio de banca

En un banco digital, se necesita desarrollar una API REST que maneje las transacciones de los clientes. La API debe permitir crear, leer, actualizar y eliminar transacciones. Los clientes se autenticarán mediante JWT. Las transacciones se almacenarán en una base de datos relacional. El sistema debe manejar errores comunes y garantizar la idempotencia de las operaciones.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | python-fastapi |
| **Nivel** | junior-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Configuración del entorno y autenticación

**Objetivo:** Configurar el entorno de desarrollo y establecer la autenticación mediante JWT.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Configurar el entorno de desarrollo para utilizar FastAPI.
- Implementar la autenticación mediante JWT para asegurar que solo los clientes autorizados puedan acceder a las transacciones.

**Entregable:** Entorno de desarrollo configurado con autenticación JWT funcional.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo almacenar y validar los tokens JWT.
- Piensa en la seguridad de las claves utilizadas para firmar los tokens.

</details>

### Fase 2: Creación y lectura de transacciones

**Objetivo:** Implementar las operaciones de creación y lectura de transacciones.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Crear un endpoint para registrar nuevas transacciones.
- Crear un endpoint para obtener la lista de transacciones de un cliente específico.

**Entregable:** Endpoints funcionales para crear y leer transacciones.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo validar los datos de entrada para las transacciones.
- Piensa en cómo manejar errores comunes durante la creación y lectura de transacciones.

</details>

### Fase 3: Actualización y eliminación de transacciones

**Objetivo:** Implementar las operaciones de actualización y eliminación de transacciones.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Crear un endpoint para actualizar los detalles de una transacción existente.
- Crear un endpoint para eliminar una transacción específica.

**Entregable:** Endpoints funcionales para actualizar y eliminar transacciones.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo garantizar la idempotencia de las operaciones de actualización y eliminación.
- Piensa en cómo manejar los casos en los que una transacción no se encuentra.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una API REST y cómo se utiliza en el contexto de un banco digital?
- **paraQueSirve**: ¿Para qué sirve la autenticación mediante JWT en este sistema?
- **comoSeUsa**: ¿Cómo se utiliza la idempotencia en las operaciones de actualización y eliminación de transacciones?
- **erroresComunes**: ¿Qué errores comunes pueden ocurrir durante la creación y lectura de transacciones y cómo se manejan?
- **queDecisionesImplica**: ¿Qué decisiones implica la implementación de los endpoints de actualización y eliminación de transacciones?

## Criterios de Evaluacion

- Configuración del entorno de desarrollo con autenticación JWT funcional.
- Implementación de endpoints para crear y leer transacciones con validación de datos y manejo de errores.
- Implementación de endpoints para actualizar y eliminar transacciones con garantía de idempotencia y manejo de casos no encontrados.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
