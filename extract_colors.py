import os
import cv2
import math
import random
import numpy as np
import pandas as pd
from collections import Counter
from sklearn.cluster import KMeans
from itertools import combinations
from PIL import Image, ImageDraw, ImageFont
from skimage.color import deltaE_cie76, rgb2lab

from choose_pallets import choose_pallet


class ColorExtractor:
    def __init__(self):
        # Carga la paleta de colores base
        self.df, self.lista_colores = choose_pallet(True)

        # Convierte todos los hex a RGB
        self.df['RGB'] = [self.hex_to_rgb(color) for color in self.df['Hexadecimal'].to_list()]

    # ---------- FUNCIONES AUXILIARES ----------
    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def calculate_luminance(self, rgb_color):
        r, g, b = [x / 255.0 for x in rgb_color]
        r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
        g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
        b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
        return 0.2126*r + 0.7152*g + 0.0722*b

    def get_text_color(self, rgb_color, threshold=0.5):
        return 'white' if self.calculate_luminance(rgb_color) < threshold else 'black'

    def color_distance(self, c1, c2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))

    def best_color_combination(self, colors):
        colors_rgb = [self.hex_to_rgb(color) for color in colors]
        best_combination = None
        max_distance_sum = -1
        for combination in combinations(colors_rgb, 3):
            d_sum = sum(self.color_distance(a, b) for a, b in combinations(combination, 2))
            if d_sum > max_distance_sum:
                max_distance_sum = d_sum
                best_combination = combination
        return ['#%02x%02x%02x' % color for color in best_combination]

    def calcular_distancia_entre_colores(self, c1, c2):
        return math.sqrt(sum((a - b)**2 for a, b in zip(c1, c2)))

    def buscar_color_mas_cercano(self, color_rgb, lista_colores):
        min_dist = float('inf')
        closest = None
        for color_hex in lista_colores:
            color_lista = tuple(int(color_hex[i:i+2], 16) for i in (1, 3, 5))
            dist = self.calcular_distancia_entre_colores(color_rgb, color_lista)
            if dist < min_dist:
                min_dist = dist
                closest = color_hex
        return closest

    def filtrar_colores_con_lista(self, colores):
        filtrados, unicos = [], set()
        for color in colores:
            cercano = self.buscar_color_mas_cercano(color, self.lista_colores)
            if cercano not in unicos:
                filtrados.append(cercano)
                unicos.add(cercano)
        return filtrados

    def verificar_diccionario(self, conteo):
        if 3 in conteo.values():
            return [3]
        elif 2 in conteo.values():
            return [k for k, v in conteo.items() if v == 2]
        elif 1 in conteo.values():
            return [random.choice([k for k, v in conteo.items() if v == 1])]
        else:
            return [None]

    def encontrar_color_mas_parecido(self, color, paleta_colores):
        color_lab = rgb2lab(np.array(color).reshape(1, 1, 3) / 255.0)
        paleta_lab = rgb2lab(np.array(paleta_colores) / 255.0)
        distancias = [deltaE_cie76(color_lab[0][0], lab) for lab in paleta_lab]
        return paleta_colores[np.argmin(distancias)]

    def corregir_colores(self, colores_usuario, nombre_paleta):
        paleta_colores = self.df[self.df['Paleta'] == nombre_paleta]['RGB'].tolist()
        corregidos = []
        for c in colores_usuario:
            if c in paleta_colores:
                corregidos.append(c)
            else:
                corregidos.append(self.encontrar_color_mas_parecido(c, paleta_colores))
        return corregidos

    def crear_imagen_con_colores(self, colores, df):
        resultados = df[df['RGB'].isin(colores)][['Hexadecimal', 'Nombres', 'Pantone', 'RGB']]
        nombre_pantones = [(r.Nombres, r.Pantone) for r in resultados.itertuples()]
        font_title = ImageFont.truetype('coolvetica/coolvetica compressed hv.otf', 65)
        font_sub = ImageFont.truetype('coolvetica/coolvetica rg.otf', 20)

        tam_imagen = 1000
        imagen = Image.new("RGB", (tam_imagen, tam_imagen), "white")
        draw = ImageDraw.Draw(imagen)

        posiciones = [(0, 0, tam_imagen*2/3, tam_imagen),
                      (tam_imagen*2/3, 0, tam_imagen, tam_imagen*2/3),
                      (tam_imagen*2/3, tam_imagen*2/3, tam_imagen, tam_imagen)]

        for i, color in enumerate(colores):
            draw.rectangle(posiciones[i], fill=color)
            text_color = self.get_text_color(self.hex_to_rgb(color))
            nombre, pantone = nombre_pantones[i]
            x, y = (50, 40 + i*300) if i == 0 else (700, 40 + (i-1)*640)
            draw.text((x, y), nombre.title(), fill=text_color, font=font_title)
            draw.text((x, y + 70), pantone, fill=text_color, font=font_sub)
        return imagen

    # ---------- MÉTODO PRINCIPAL ----------
    def process_images(self, lista_imagenes):
        colores_totales = []

        for img in lista_imagenes:
            imagen = cv2.imread(img)
            imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
            imagen_peq = cv2.resize(imagen, (100, 100))
            pixeles = imagen_peq.reshape((-1, 3))

            kmeans = KMeans(n_clusters=5, random_state=0)
            kmeans.fit(pixeles)

            colores = np.round(kmeans.cluster_centers_).astype(int)
            frecuencias = np.bincount(kmeans.labels_)
            indices = np.argsort(frecuencias)[::-1]
            colores = colores[indices]

            colores_filtrados = self.filtrar_colores_con_lista(colores)
            for c in colores_filtrados:
                if c not in colores_totales:
                    colores_totales.append(c)

        top3_colors = self.best_color_combination(colores_totales)
        paletas = [self.df[self.df['Hexadecimal'] == c]['Paleta'].values[0] for c in top3_colors]
        conteo = Counter(paletas)
        resultado = self.verificar_diccionario(conteo)
        paleta_final = resultado[0]

        # corregir colores si no pertenece a la paleta principal
        colors_rgb = [self.hex_to_rgb(c) for c in top3_colors]
        if paleta_final not in [3, None]:
            colors_rgb = self.corregir_colores(colors_rgb, paleta_final)

        imagen_resultante = self.crear_imagen_con_colores(colors_rgb, self.df)

        # Guarda o regresa
        output_path = 'imagen_gridspiration.png'
        imagen_resultante.save(output_path)

        return {
            'imagen': imagen_resultante,
            'paleta_rgb': colors_rgb,
            'nombre_paleta': paleta_final,
            'archivo_guardado': output_path
        }
