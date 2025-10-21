from fastapi import FastAPI, UploadFile, File
from typing import List
from color_extractor import ColorExtractor
from recolor import recolor_image_with_palette
from PIL import Image
import io

app = FastAPI(
    title="Gridspiration API",
    description="API para extraer paletas de color y aplicar paletas a imágenes.",
    version="1.0.0"
)

# Instancia del extractor (se carga una sola vez)
extractor = ColorExtractor()

@app.get("/")
async def message():
    return "Bienvenido a Gridspiration"

@app.post("/extract_colors/")
async def extract_colors(files: List[UploadFile] = File(...)):
    """
    Extrae la paleta de colores dominante de una lista de imágenes.
    """
    # Guardar temporalmente las imágenes en disco
    image_paths = []
    for file in files:
        content = await file.read()
        path = f"temp_{file.filename}"
        with open(path, "wb") as f:
            f.write(content)
        image_paths.append(path)

    # Procesar imágenes
    resultado = extractor.process_images(image_paths)

    # Devolver resultados
    return {
        "colores_rgb": resultado["paleta_rgb"],
        "paleta_detectada": resultado['nombre_paleta'],
        "archivo_resultante": resultado['archivo_guardado']
    }
