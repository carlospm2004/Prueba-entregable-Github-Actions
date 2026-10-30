# Simulación de un escaneo de seguridad:
# busca en ventas.json palabras típicas de claves API expuestas.
import sys

palabras_sospechosas = ["api_key", "apikey", "secret", "password", "token"]

with open("ventas.json", "r", encoding="utf-8") as f:
    contenido = f.read().lower()

encontradas = [p for p in palabras_sospechosas if p in contenido]

if encontradas:
    print("PELIGRO: posibles claves expuestas:", encontradas)
    sys.exit(1)  # hace fallar el step y el job

print("Escaneo completado: no se han encontrado claves API expuestas")