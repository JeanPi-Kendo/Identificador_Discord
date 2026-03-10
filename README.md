Discord Anime Image Classifier Bot 🤖🎌

Bot de Discord que utiliza un modelo de TensorFlow/Keras para clasificar imágenes de personajes de anime enviadas por los usuarios.

El bot analiza una imagen subida en un mensaje y responde con:

personaje detectado

porcentaje de confianza

barra visual de confianza

indicador de seguridad con emojis

Características

Clasificación automática de imágenes

Integración con modelos .h5 de Keras

Lectura de etiquetas desde labels.txt

Porcentaje de confianza de la predicción

Barra visual de confianza

Indicador de seguridad con emojis

Comando adicional para obtener imágenes aleatorias de patos

Compatible con bots creados con discord.py

Requisitos

Antes de ejecutar el proyecto, instala las siguientes dependencias:

Python 3.8+

discord.py

TensorFlow

NumPy

Pillow

requests

Instalación:

pip install discord.py tensorflow numpy pillow requests
Estructura del proyecto
project/
│
├── main.py
├── model.py
├── keras_model.h5
├── labels.txt
└── README.md
Descripción de archivos
main.py

Archivo principal del bot de Discord.

Incluye:

conexión con Discord

comandos del bot

barra visual de confianza

sistema de emojis según seguridad

análisis de imágenes enviadas por los usuarios

model.py

Archivo encargado de:

cargar el modelo .h5

procesar la imagen enviada

realizar la predicción

devolver el personaje detectado y el porcentaje de confianza

keras_model.h5

Modelo entrenado de clasificación de imágenes.

labels.txt

Archivo que contiene las clases que el modelo puede reconocer.

Ejemplo:

Gojo
Naruto
Luffy
Goku

Comandos del bot
Clasificar una imagen

Comando:

#check
Cómo usarlo

Escribe #check en un canal donde esté el bot.

Adjunta una imagen en el mismo mensaje.

El bot analizará la imagen y responderá con la predicción.

Ejemplo de respuesta del bot:

🟢 Personaje detectado: Gojo
📊 Confianza: 91%

▰▰▰▰▰▰▰▰▰▱

Estoy muy seguro de esta predicción.

Si no se adjunta ninguna imagen:

⚠️ Debes subir una imagen.
Imagen aleatoria de pato

El bot también incluye un comando adicional:

#duck

Este comando envía una imagen aleatoria de un pato usando una API pública.

Cómo funciona la predicción

El modelo devuelve probabilidades entre 0 y 1 para cada clase.

Estas probabilidades se convierten en porcentajes para mostrar qué tan seguro está el modelo de su predicción.

Dependiendo del porcentaje, el bot muestra:

Confianza	Indicador
80% o más	🟢 Alta confianza
50–79%	🟡 Confianza media
menos de 50%	🔴 Baja confianza
Posibles mejoras

Este proyecto puede ampliarse con nuevas funcionalidades:

mostrar Top 3 predicciones del modelo

enviar resultados usando embeds de Discord

soporte para múltiples modelos

panel web usando Flask o FastAPI

sistema de estadísticas del modelo

Entrenamiento del modelo

Puedes entrenar tu propio modelo usando Teachable Machine.

Recomendaciones:

usar 50–100 imágenes por personaje

incluir diferentes ángulos

incluir diferentes iluminaciones

usar diferentes estilos de dibujo

Esto mejora la precisión del modelo.

Licencia

Este proyecto es de uso educativo y puede ser modificado libremente para aprendizaje, experimentación o desarrollo de bots con inteligencia artificial.

Ejemplo Gráfico:
<img width="536" height="617" alt="image" src="https://github.com/user-attachments/assets/64ae08f2-a464-4e41-b2f5-7baa5c7fbc2b" />

