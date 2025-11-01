#!/usr/bin/env python3
"""
Demo completo de generación de patrones de calcetines y boxers
"""

import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from phantomfit_studio import PhantomFitStudio


def main():
    """Demo completo de calcetines y boxers."""
    
    print("="*70)
    print(" PhantomFit Studio - Patrones de Calcetines y Boxers a la Medida")
    print("="*70)
    print()
    
    # Crear instancia del estudio
    studio = PhantomFitStudio()
    
    print("🧦 GENERACIÓN DE PATRÓN DE CALCETÍN")
    print("-" * 70)
    
    # Medidas para calcetín
    sock_measurements = {
        "foot_length": 25,          # Longitud del pie en cm
        "foot_width": 10,            # Ancho del pie en cm
        "ankle_circumference": 22,   # Circunferencia del tobillo en cm
        "calf_circumference": 35,    # Circunferencia de la pantorrilla en cm
        "sock_height": 20            # Altura del calcetín en cm
    }
    
    print("\n  Medidas ingresadas:")
    for key, value in sock_measurements.items():
        print(f"    - {key}: {value} cm")
    
    print("\n  Generando patrón de calcetín estilo 'crew'...")
    print("  (Con colores personalizados)")
    sock_pattern = studio.generate_pattern(
        garment_type="calcetín",
        measurements=sock_measurements,
        style_options={
            "style": "crew", 
            "ease": 1,
            "colores": {
                "cuerpo": "#87CEEB",  # Azul cielo
                "talón": "#FFB6C1",   # Rosa claro
                "punta": "#98FB98"    # Verde claro
            }
        }
    )
    
    print(f"\n  ✓ Patrón generado exitosamente!")
    print(f"    - Tipo: {sock_pattern['garment_type']}")
    print(f"    - Número de piezas: {len(sock_pattern['pieces'])}")
    print(f"    - Piezas del patrón:")
    for piece in sock_pattern['pieces']:
        print(f"      • {piece['name']} ({piece['type']}) - Margen de costura: {piece['seam_allowance']} cm")
    print(f"    - Tela requerida: {sock_pattern['fabric_required']['linear_meters']:.2f} metros lineales")
    print(f"    - Área total: {sock_pattern['fabric_required']['total_area_cm2']:.2f} cm²")
    print(f"    - Ancho de tela estándar: {sock_pattern['fabric_required']['fabric_width_cm']} cm")
    
    print("\n" + "="*70)
    print("🩲 GENERACIÓN DE PATRÓN DE BOXER")
    print("-" * 70)
    
    # Medidas para boxer
    boxer_measurements = {
        "waist": 75,                 # Cintura en cm
        "hip": 95,                   # Cadera en cm
        "inseam": 10,                # Entrepierna en cm
        "thigh_circumference": 55,   # Circunferencia del muslo en cm
        "rise": 25                   # Altura del tiro en cm
    }
    
    print("\n  Medidas ingresadas:")
    for key, value in boxer_measurements.items():
        print(f"    - {key}: {value} cm")
    
    print("\n  Generando patrón de boxer...")
    print("  (Con colores personalizados)")
    boxer_pattern = studio.generate_pattern(
        garment_type="boxer",
        measurements=boxer_measurements,
        style_options={
            "ease": 5, 
            "leg_opening": "loose",
            "colores": {
                "delantero": "#FFE4B5",  # Beige claro
                "trasero": "#F0E68C",    # Amarillo claro
                "pretina": "#DDA0DD"     # Ciruela
            }
        }
    )
    
    print(f"\n  ✓ Patrón generado exitosamente!")
    print(f"    - Tipo: {boxer_pattern['garment_type']}")
    print(f"    - Número de piezas: {len(boxer_pattern['pieces'])}")
    print(f"    - Piezas del patrón:")
    for piece in boxer_pattern['pieces']:
        print(f"      • {piece['name']} ({piece['type']}) - Margen de costura: {piece['seam_allowance']} cm")
    print(f"    - Tela requerida: {boxer_pattern['fabric_required']['linear_meters']:.2f} metros lineales")
    print(f"    - Área total: {boxer_pattern['fabric_required']['total_area_cm2']:.2f} cm²")
    print(f"    - Ancho de tela estándar: {boxer_pattern['fabric_required']['fabric_width_cm']} cm")
    
    print("\n" + "="*70)
    print("💾 EXPORTACIÓN DE PATRONES")
    print("-" * 70)
    
    # Crear directorio de salida
    output_dir = "/tmp/phantomfit_output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Exportar calcetín con opciones de personalización
    sock_svg = os.path.join(output_dir, "calcetin_patron.svg")
    studio.export_pattern(
        sock_svg, 
        format="svg",
        export_options={
            "show_data_box": True,
            "data_box_position": "top-right",
            "show_measurements": True,
            "show_fabric_info": True
        }
    )
    print(f"\n  ✓ Patrón de calcetín exportado: {sock_svg}")
    print(f"    (Con cuadro de datos en esquina superior derecha)")
    
    # Generar boxer nuevamente (para que sea el patrón actual)
    studio.generate_pattern("boxer", boxer_measurements, style_options={
        "ease": 5,
        "colores": {
            "delantero": "#FFE4B5",
            "trasero": "#F0E68C",
            "pretina": "#DDA0DD"
        }
    })
    boxer_svg = os.path.join(output_dir, "boxer_patron.svg")
    studio.export_pattern(
        boxer_svg, 
        format="svg",
        export_options={
            "show_data_box": True,
            "data_box_position": "bottom-left",
            "show_measurements": True,
            "show_fabric_info": True
        }
    )
    print(f"  ✓ Patrón de boxer exportado: {boxer_svg}")
    print(f"    (Con cuadro de datos en esquina inferior izquierda)")
    
    print("\n" + "="*70)
    print("📊 RESUMEN")
    print("-" * 70)
    print(f"\n  Patrones generados: 2")
    print(f"  • Calcetín: 3 piezas, {sock_pattern['fabric_required']['linear_meters']:.2f}m")
    print(f"  • Boxer: 3 piezas, {boxer_pattern['fabric_required']['linear_meters']:.2f}m")
    print(f"\n  Total de tela requerida: {sock_pattern['fabric_required']['linear_meters'] + boxer_pattern['fabric_required']['linear_meters']:.2f} metros")
    
    print("\n" + "="*70)
    print("✓ Demo completado exitosamente!")
    print("="*70)
    print()
    print("Los archivos SVG generados pueden ser:")
    print("  - Visualizados en cualquier navegador web")
    print("  - Importados en software de diseño como Inkscape, Adobe Illustrator")
    print("  - Enviados a máquinas de corte CNC o plotter")
    print("  - Impresos a escala real para uso en patronaje manual")
    print()


if __name__ == "__main__":
    main()
