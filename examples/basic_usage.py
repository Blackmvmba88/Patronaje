#!/usr/bin/env python3
"""
Ejemplo básico de uso de PhantomFit Studio
"""

import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from phantomfit_studio import PhantomFitStudio


def main():
    """Ejemplo básico de generación de patrón y visualización."""
    
    print("="*60)
    print("PhantomFit Studio - Ejemplo Básico")
    print("="*60)
    print()
    
    # Crear instancia del estudio
    studio = PhantomFitStudio()
    
    # Definir medidas corporales
    measurements = {
        "bust": 90,
        "waist": 70,
        "hip": 95,
        "shoulder": 40,
        "back_length": 40,
        "sleeve_length": 58,
        "height": 165
    }
    
    print("1. Generando patrón de blusa...")
    pattern = studio.generate_pattern(
        garment_type="blouse",
        measurements=measurements,
        style_options={"ease": 5}
    )
    
    print(f"   ✓ Patrón generado con {len(pattern['pieces'])} piezas")
    print(f"   ✓ Tela requerida: {pattern['fabric_required']['linear_meters']:.2f} metros")
    print()
    
    print("2. Cargando modelo fantasma...")
    studio.load_phantom_model(
        body_measurements=measurements,
        pose="default"
    )
    print("   ✓ Modelo fantasma cargado")
    print()
    
    print("3. Visualizando patrón en 3D...")
    studio.visualize_pattern()
    print("   ✓ Patrón mapeado al modelo")
    print()
    
    print("4. Mostrando vista 3D...")
    studio.show_3d_view()
    print()
    
    print("5. Información del patrón:")
    info = studio.get_pattern_info()
    print(f"   - Estado: {info['status']}")
    print(f"   - Tipo: {info['type']}")
    print(f"   - Piezas: {info['pieces']}")
    print()
    
    print("="*60)
    print("Ejemplo completado exitosamente!")
    print("="*60)


if __name__ == "__main__":
    main()
