import numpy as np
from keras.models import load_model
from PIL import Image, ImageOps


def get_class(model_path, labels_path, image_path):

    # cargar modelo
    model = load_model(model_path, compile=False)

    # cargar etiquetas
    with open(labels_path, "r") as f:
        class_names = f.readlines()

    # preparar array
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # abrir imagen
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)

    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)

    # normalizar imagen
    normalized_image = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image

    # predicción
    prediction = model.predict(data)

    index = np.argmax(prediction)

    class_name = class_names[index].strip()

    confidence_score = prediction[0][index]

    confidence_percent = round(confidence_score * 100, 2)

    return class_name, confidence_percent
