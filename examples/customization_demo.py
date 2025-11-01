#!/usr/bin/env python3
"""
Demo de opciones de personalización de patrones de calcetines y boxers
"""

import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from phantomfit_studio import PhantomFitStudio


def main():
    """Demo de personalización de colores y cuadros de datos."""
    
    print("="*70)
    print(" PhantomFit Studio - Demo de Personalización")
    print("="*70)
    print()
    
    # Crear instancia del estudio
    studio = PhantomFitStudio()
    
    # Crear directorio de salida
    output_dir = "/tmp/phantomfit_custom"
    os.makedirs(output_dir, exist_ok=True)
    
    print("🎨 EJEMPLO 1: Calcetín con colores personalizados")
    print("-" * 70)
    
    sock_measurements = {
        "foot_length": 25,
        "foot_width": 10,
        "ankle_circumference": 22,
        "calf_circumference": 35,
        "sock_height": 20
    }
    
    # Generar calcetín con colores personalizados
    sock_pattern = studio.generate_pattern(
        garment_type="sock",
        measurements=sock_measurements,
        style_options={
            "style": "crew",
            "ease": 1,
            "colors": {
                "body": "#FF6B6B",      # Rojo coral
                "heel": "#4ECDC4",      # Turquesa
                "toe": "#FFE66D"        # Amarillo brillante
            }
        }
    )
    
    print("  ✓ Patrón generado con colores personalizados:")
    print("    - Cuerpo: Rojo coral (#FF6B6B)")
    print("    - Talón: Turquesa (#4ECDC4)")
    print("    - Punta: Amarillo brillante (#FFE66D)")
    
    # Exportar con cuadro de datos en posición superior derecha
    sock_file = os.path.join(output_dir, "calcetin_colores_personalizados.svg")
    studio.export_pattern(
        sock_file,
        format="svg",
        export_options={
            "show_data_box": True,
            "data_box_position": "top-right",
            "show_measurements": True,
            "show_fabric_info": True,
            "stroke_color": "#333333",
            "stroke_width": 2,
            "text_color": "#1a1a1a",
            "font_family": "Arial",
            "font_size": 12
        }
    )
    print(f"  ✓ Exportado: {sock_file}")
    print()
    
    print("🎨 EJEMPLO 2: Boxer con colores y posición de cuadro personalizada")
    print("-" * 70)
    
    boxer_measurements = {
        "waist": 75,
        "hip": 95,
        "inseam": 10,
        "thigh_circumference": 55,
        "rise": 25
    }
    
    # Generar boxer con colores personalizados
    boxer_pattern = studio.generate_pattern(
        garment_type="boxer",
        measurements=boxer_measurements,
        style_options={
            "ease": 5,
            "colors": {
                "front": "#95E1D3",     # Verde menta
                "back": "#F38181",      # Rosa salmón
                "waistband": "#AA96DA"  # Lavanda
            }
        }
    )
    
    print("  ✓ Patrón generado con colores personalizados:")
    print("    - Delantero: Verde menta (#95E1D3)")
    print("    - Trasero: Rosa salmón (#F38181)")
    print("    - Pretina: Lavanda (#AA96DA)")
    
    # Exportar con cuadro de datos en posición inferior izquierda
    boxer_file = os.path.join(output_dir, "boxer_colores_personalizados.svg")
    studio.export_pattern(
        boxer_file,
        format="svg",
        export_options={
            "show_data_box": True,
            "data_box_position": "bottom-left",
            "show_measurements": True,
            "show_fabric_info": True,
            "stroke_color": "#2C3E50",
            "stroke_width": 1.5,
            "text_color": "#2C3E50",
            "font_family": "Verdana",
            "font_size": 11
        }
    )
    print(f"  ✓ Exportado: {boxer_file}")
    print()
    
    print("🎨 EJEMPLO 3: Sin cuadro de datos (solo patrón)")
    print("-" * 70)
    
    # Generar otro calcetín
    sock_pattern2 = studio.generate_pattern(
        garment_type="sock",
        measurements=sock_measurements,
        style_options={
            "style": "ankle",
            "ease": 1,
            "colors": {
                "body": "#A8DADC",      # Azul pálido
                "heel": "#457B9D",      # Azul acero
                "toe": "#1D3557"        # Azul marino
            }
        }
    )
    
    print("  ✓ Patrón con esquema de azules")
    
    # Exportar sin cuadro de datos
    sock_file2 = os.path.join(output_dir, "calcetin_sin_cuadro.svg")
    studio.export_pattern(
        sock_file2,
        format="svg",
        export_options={
            "show_data_box": False,  # Sin cuadro de datos
            "stroke_color": "#1D3557",
            "stroke_width": 2
        }
    )
    print(f"  ✓ Exportado (sin cuadro de datos): {sock_file2}")
    print()
    
    print("🎨 EJEMPLO 4: Estilos de texto personalizados")
    print("-" * 70)
    
    # Generar boxer con estilo diferente
    boxer_pattern2 = studio.generate_pattern(
        garment_type="boxer",
        measurements=boxer_measurements,
        style_options={
            "ease": 5,
            "colors": {
                "front": "#FFD93D",     # Amarillo dorado
                "back": "#6BCB77",      # Verde brillante
                "waistband": "#4D96FF"  # Azul brillante
            }
        }
    )
    
    print("  ✓ Patrón con colores vibrantes")
    
    # Exportar con fuente más grande y cuadro en esquina superior izquierda
    boxer_file2 = os.path.join(output_dir, "boxer_texto_grande.svg")
    studio.export_pattern(
        boxer_file2,
        format="svg",
        export_options={
            "show_data_box": True,
            "data_box_position": "top-left",
            "show_measurements": True,
            "show_fabric_info": True,
            "stroke_color": "#000000",
            "stroke_width": 2.5,
            "text_color": "#000000",
            "font_family": "Courier New",
            "font_size": 14
        }
    )
    print(f"  ✓ Exportado con texto grande: {boxer_file2}")
    print()
    
    print("="*70)
    print("📊 RESUMEN DE OPCIONES DE PERSONALIZACIÓN")
    print("-" * 70)
    print()
    print("  Colores de piezas:")
    print("    • Calcetín: body, heel, toe")
    print("    • Boxer: front, back, waistband")
    print("    • Formato: Códigos hexadecimales (#RRGGBB)")
    print()
    print("  Posiciones de cuadro de datos:")
    print("    • top-right (superior derecha)")
    print("    • top-left (superior izquierda)")
    print("    • bottom-right (inferior derecha)")
    print("    • bottom-left (inferior izquierda)")
    print()
    print("  Opciones de exportación:")
    print("    • show_data_box: True/False")
    print("    • show_measurements: True/False")
    print("    • show_fabric_info: True/False")
    print("    • stroke_color: Color de líneas")
    print("    • stroke_width: Grosor de líneas")
    print("    • text_color: Color de texto")
    print("    • font_family: Fuente del texto")
    print("    • font_size: Tamaño de fuente")
    print()
    print("="*70)
    print("✓ Demo completado exitosamente!")
    print(f"  Archivos generados en: {output_dir}")
    print("="*70)
    print()


if __name__ == "__main__":
    main()
