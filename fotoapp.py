
# --- fotoapp.py modulo ---
# no guarda nada, solo crea el modulo

# Importaciones necesarias para el módulo
from PIL import Image, ImageOps, ImageFilter
import matplotlib.pyplot as plt
import requests
from io import BytesIO
import numpy as np

# --- Función 1 ---
def redimensionar_para_redes(ruta_imagen, palabra_clave):
    try:
        if ruta_imagen.startswith('http'):
            respuesta = requests.get(ruta_imagen)
            img = Image.open(BytesIO(respuesta.content))
        else:
            img = Image.open(ruta_imagen)
    except Exception as e:
        print(f"Error al abrir la imagen: {e}")
        return None
    if palabra_clave.lower() == 'youtube': tamano = (1280, 720)
    elif palabra_clave.lower() == 'instagram': tamano = (1080, 1080)
    elif palabra_clave.lower() == 'twitter': tamano = (1600, 900)
    elif palabra_clave.lower() == 'facebook': tamano = (1200, 630)
    else: return img
    img.thumbnail(tamano)
    print(f"Imagen redimensionada para {palabra_clave}. Nuevo tamaño: {img.size}")
    return img

# --- Función 2 ---
def ajustar_contraste_con_histograma(img_original):
    if img_original.mode == 'RGBA':
        img_original = img_original.convert('RGB')
    return ImageOps.equalize(img_original)

# --- Función 3 ---
def aplicar_filtro(img_original, nombre_filtro):
    FILTROS = {
        'BLUR': ImageFilter.BLUR, 'CONTOUR': ImageFilter.CONTOUR, 'DETAIL': ImageFilter.DETAIL,
        'EDGE_ENHANCE': ImageFilter.EDGE_ENHANCE, 'EDGE_ENHANCE_MORE': ImageFilter.EDGE_ENHANCE_MORE,
        'EMBOSS': ImageFilter.EMBOSS, 'FIND_EDGES': ImageFilter.FIND_EDGES,
        'SHARPEN': ImageFilter.SHARPEN, 'SMOOTH': ImageFilter.SMOOTH,
    }
    filtro_a_aplicar = FILTROS.get(nombre_filtro.upper())
    if filtro_a_aplicar:
        return img_original.filter(filtro_a_aplicar)
    else:
        return img_original

# --- Función 4 ---
def crear_boceto(img_original, persona=True):
    if not persona:
        return img_original
    img_gris = img_original.convert('L')
    img_bordes = img_gris.filter(ImageFilter.FIND_EDGES)
    img_invertida = ImageOps.invert(img_bordes)
    return ImageOps.autocontrast(img_invertida, cutoff=5)

# --- Función 5 (El menú va DENTRO del módulo) ---
def iniciar_app():
    print("--- BIENVENIDO A FOTOAPP (Versión Módulo) ---")
    imagen_cargada = None
    while True:
        print("\nMENÚ DE OPCIONES:")
        print("1. Cargar y Redimensionar imagen")
        print("2. Ajustar Contraste (Histograma)")
        print("3. Aplicar un Filtro")
        print("4. Crear Boceto para Pintores")
        print("5. Salir")
        try:
            opcion = int(input("\nIngresa el número de la opción: "))
        except ValueError:
            print("Error! Debes ingresar un número.")
            continue
        if opcion == 1:
            url = input("Ingresa la URL de la imagen: ")
            red_social = input("¿Para qué red social quieres la foto? (Youtube, Instagram, etc): ")
            imagen_cargada = redimensionar_para_redes(url, red_social)
            if imagen_cargada:
                print("Imagen cargada!")
                plt.imshow(imagen_cargada); plt.axis('off'); plt.show()
            else:
                print("Error cargando la imagen.")
        elif opcion in [2, 3, 4]:
            if imagen_cargada is None:
                print("Upps! Primero debes cargar una imagen (Opción 1).")
                continue
            if opcion == 2:
                img_res = ajustar_contraste_con_histograma(imagen_cargada)
                plt.imshow(img_res); plt.title("Contraste Ajustado"); plt.axis('off'); plt.show()
            elif opcion == 3:
                nombre_filtro = input("Escribe el nombre del filtro: ")
                img_res = aplicar_filtro(imagen_cargada, nombre_filtro)
                plt.imshow(img_res); plt.title(f"Filtro: {nombre_filtro}"); plt.axis('off'); plt.show()
            elif opcion == 4:
                es_persona = input("¿La foto contiene una persona? (s/n): ").lower() == 's'
                img_res = crear_boceto(imagen_cargada, persona=es_persona)
                plt.imshow(img_res, cmap='gray'); plt.title("Boceto"); plt.axis('off'); plt.show()
        elif opcion == 5:
            print("¡Gracias por usar FotoApp! Cerrando programa...")
            break
        else:
            print("Opción incorrecta.")
