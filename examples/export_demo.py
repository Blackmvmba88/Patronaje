#!/usr/bin/env python3
"""
Demostración de exportación de patrones a diferentes formatos
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from phantomfit_studio import PhantomFitStudio


def main():
    """Demuestra la exportación de patrones."""
    
    print("\n" + "="*60)
    print("PHANTOMFIT STUDIO - DEMO DE EXPORTACIÓN")
    print("="*60)
    print()
    
    # Crear directorio de salida
    output_dir = "/tmp/phantomfit_exports"
    os.makedirs(output_dir, exist_ok=True)
    print(f"Directorio de exportación: {output_dir}")
    print()
    
    studio = PhantomFitStudio()
    
    measurements = {
        "bust": 90,
        "waist": 70,
        "hip": 95,
        "shoulder": 40,
        "back_length": 40,
        "sleeve_length": 58,
        "height": 165,
        "inseam": 75,
        "outseam": 100,
        "skirt_length": 60,
        "dress_length": 100
    }
    
    garment_types = ["blouse", "pants", "skirt", "dress"]
    
    print("Generando y exportando patrones...")
    print()
    
    for garment_type in garment_types:
        print(f"Procesando {garment_type}...")
        
        # Generar patrón
        pattern = studio.generate_pattern(garment_type, measurements)
        
        # Exportar a SVG
        svg_path = os.path.join(output_dir, f"{garment_type}_pattern.svg")
        studio.export_pattern(svg_path, format="svg")
        
        # Verificar exportación
        if os.path.exists(svg_path):
            file_size = os.path.getsize(svg_path)
            print(f"  ✓ Exportado a SVG: {svg_path}")
            print(f"    Tamaño: {file_size} bytes")
            print(f"    Piezas: {len(pattern['pieces'])}")
            print(f"    Tela: {pattern['fabric_required']['linear_meters']:.2f}m")
        else:
            print(f"  ✗ Error exportando {garment_type}")
        
        print()
    
    print("="*60)
    print("ARCHIVOS GENERADOS:")
    print("="*60)
    
    for filename in sorted(os.listdir(output_dir)):
        filepath = os.path.join(output_dir, filename)
        size = os.path.getsize(filepath)
        print(f"  {filename:<30} {size:>8} bytes")
    
    print()
    print("="*60)
    print("NOTA: Los archivos SVG pueden ser:")
    print("  - Abiertos en navegadores web")
    print("  - Editados en Inkscape, Adobe Illustrator, etc.")
    print("  - Importados a software CAD/CAM")
    print("  - Enviados a cortadoras CNC o plotters")
    print("="*60)
    print()


if __name__ == "__main__":
    main()
