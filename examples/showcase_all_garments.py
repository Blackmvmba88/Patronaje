#!/usr/bin/env python3
"""
Showcase de todos los tipos de prendas disponibles en PhantomFit Studio
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from phantomfit_studio import PhantomFitStudio


def showcase_garment(studio, garment_type, measurements, description):
    """Muestra un tipo de prenda específica."""
    print(f"\n{'='*60}")
    print(f"{description.upper()}")
    print('='*60)
    
    pattern = studio.generate_pattern(garment_type, measurements)
    
    print(f"Tipo de prenda: {pattern['garment_type']}")
    print(f"Número de piezas: {len(pattern['pieces'])}")
    print(f"Tela requerida: {pattern['fabric_required']['linear_meters']:.2f} metros")
    print(f"Ancho de tela: {pattern['fabric_required']['fabric_width_cm']} cm")
    
    print("\nPiezas del patrón:")
    for piece in pattern['pieces']:
        print(f"  - {piece['name']}: {piece['type']} "
              f"(margen de costura: {piece['seam_allowance']} cm)")
    
    # Visualizar en 3D
    studio.load_phantom_model(measurements, pose="default")
    studio.visualize_pattern(pattern)
    
    return pattern


def main():
    """Muestra todos los tipos de prendas disponibles."""
    
    print("\n" + "="*60)
    print("PHANTOMFIT STUDIO - SHOWCASE DE PRENDAS")
    print("="*60)
    print("\nDemostración de generación de patrones para todos los tipos")
    print("de prendas soportados por el sistema.")
    
    studio = PhantomFitStudio()
    
    # Medidas corporales base
    measurements_female = {
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
    
    measurements_male = {
        "bust": 100,
        "waist": 85,
        "hip": 100,
        "shoulder": 45,
        "back_length": 44,
        "sleeve_length": 62,
        "height": 178,
        "inseam": 82,
        "outseam": 108
    }
    
    # 1. BLUSA
    showcase_garment(
        studio, "blouse", measurements_female,
        "Blusa - Prenda casual femenina"
    )
    
    # 2. CAMISA
    showcase_garment(
        studio, "shirt", measurements_male,
        "Camisa - Prenda formal unisex"
    )
    
    # 3. PANTALÓN
    showcase_garment(
        studio, "pants", measurements_male,
        "Pantalón - Prenda versátil unisex"
    )
    
    # 4. FALDA
    showcase_garment(
        studio, "skirt", measurements_female,
        "Falda - Prenda femenina clásica"
    )
    
    # 5. VESTIDO
    showcase_garment(
        studio, "dress", measurements_female,
        "Vestido - Prenda femenina elegante"
    )
    
    # 6. CHAQUETA
    showcase_garment(
        studio, "jacket", measurements_male,
        "Chaqueta - Prenda de abrigo unisex"
    )
    
    # Resumen final
    print("\n" + "="*60)
    print("RESUMEN")
    print("="*60)
    print("\nPhantomFit Studio soporta 6 tipos de prendas:")
    print("  1. Blusa/Shirt - Prendas de torso")
    print("  2. Pants - Pantalones completos")
    print("  3. Skirt - Faldas (straight, a-line, circle)")
    print("  4. Dress - Vestidos con corpiño y falda")
    print("  5. Jacket - Chaquetas estructuradas")
    
    print("\nCaracterísticas adicionales:")
    print("  ✓ Cálculo automático de tela requerida")
    print("  ✓ Márgenes de costura incluidos")
    print("  ✓ Visualización 3D en muñeca fantasma")
    print("  ✓ Exportación a SVG, PDF, DXF")
    print("  ✓ Integración con módulos LED y materiales reflectantes")
    
    print("\n" + "="*60)
    print("SHOWCASE COMPLETADO")
    print("="*60)
    print()


if __name__ == "__main__":
    main()
