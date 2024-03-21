# Desafio-Diagrama-de-clases

Este repositorio contiene una solución al problema de diseño y desarrollo de software para la gestión de encuestas. El objetivo es permitir a los usuarios crear y responder encuestas a través de una aplicación de software.

## Problema

La empresa **ConsultoraX** necesita desarrollar un software que permita la creación y contestación de encuestas. El software debe permitir la creación de encuestas con preguntas y alternativas, así como la gestión de las respuestas de los usuarios. Además, se necesitan dos tipos específicos de encuestas: **encuestas limitadas por edad** y **encuestas limitadas por región**.

## Solución

Se ha implementado una solución que incluye clases y métodos para modelar la estructura de las encuestas, preguntas, alternativas, usuarios y respuestas. Aquí hay una descripción general de las clases implementadas:

- **`Alternativa`**: Representa una opción de respuesta para una pregunta.
- **`Pregunta`**: Representa una pregunta dentro de una encuesta, con su enunciado, ayuda (opcional) y lista de alternativas.
- **`Encuesta`**: Representa una encuesta con un nombre, lista de preguntas y lista de listados de respuestas.
- **`EncuestaLimitadaPorEdad`**: Subclase de `Encuesta` que agrega restricciones de edad.
- **`EncuestaLimitadaPorRegion`**: Subclase de `Encuesta` que agrega restricciones de región.
- **`ListadoRespuestas`**: Representa un conjunto de respuestas asociadas a un usuario para una encuesta específica.
- **`Usuario`**: Representa un usuario con correo electrónico, edad y región.

Además, se ha proporcionado un diagrama de clases (**`diagrama_clases.png`**) que ilustra la estructura de las clases y sus relaciones.

## Archivos y Estructura del Repositorio

El repositorio está organizado de la siguiente manera:

- **`alternativa.py`**: Contiene la clase `Alternativa`.
- **`pregunta.py`**: Contiene la clase `Pregunta`.
- **`encuesta.py`**: Contiene las clases `Encuesta`, `EncuestaLimitadaPorEdad` y `EncuestaLimitadaPorRegion`.
- **`listado_respuestas.py`**: Contiene la clase `ListadoRespuestas`.
- **`usuario.py`**: Contiene la clase `Usuario`.
- **`diagrama_clases.png`**: Diagrama de clases que ilustra la estructura del software.

