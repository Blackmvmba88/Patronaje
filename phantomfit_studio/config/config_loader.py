"""
Cargador de configuración para PhantomFit Studio
"""

import json
import os
from typing import Dict, Any, Optional


DEFAULT_CONFIG = {
    "studio": {
        "name": "PhantomFit Studio",
        "version": "1.0.0"
    },
    "viewer": {
        "resolution": [1920, 1080],
        "antialiasing": True,
        "camera": {
            "position": [0, 0, 300],
            "fov": 45
        },
        "background_color": [0.2, 0.2, 0.25, 1.0]
    },
    "modules": {
        "led": {
            "max_modules": 100,
            "default_color": [255, 255, 255],
            "default_intensity": 100,
            "default_pattern": "static"
        },
        "reflective": {
            "max_materials": 50,
            "default_reflectivity": 0.8,
            "default_color": [200, 200, 200]
        }
    },
    "patterns": {
        "default_ease": 5,
        "default_seam_allowance": 1.5,
        "export_formats": ["svg", "pdf", "dxf"]
    },
    "units": {
        "measurement": "cm",
        "display": "cm"
    }
}


class ConfigLoader:
    """
    Cargador de configuración para el estudio.
    """
    
    @staticmethod
    def load_config(filepath: Optional[str] = None) -> Dict[str, Any]:
        """
        Carga la configuración desde un archivo o usa la configuración por defecto.
        
        Args:
            filepath: Ruta al archivo de configuración JSON
            
        Returns:
            Diccionario de configuración
        """
        if filepath is None or not os.path.exists(filepath):
            return DEFAULT_CONFIG.copy()
        
        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
            
            # Fusionar con configuración por defecto
            config = DEFAULT_CONFIG.copy()
            ConfigLoader._deep_merge(config, user_config)
            
            return config
        except Exception as e:
            print(f"Error cargando configuración: {e}")
            print("Usando configuración por defecto")
            return DEFAULT_CONFIG.copy()
    
    @staticmethod
    def save_config(config: Dict[str, Any], filepath: str) -> None:
        """
        Guarda la configuración en un archivo.
        
        Args:
            config: Configuración a guardar
            filepath: Ruta del archivo
        """
        try:
            with open(filepath, 'w') as f:
                json.dump(config, f, indent=2)
        except Exception as e:
            raise IOError(f"Error guardando configuración: {e}")
    
    @staticmethod
    def _deep_merge(base: Dict[str, Any], override: Dict[str, Any]) -> None:
        """
        Fusiona recursivamente el diccionario override en base.
        
        Args:
            base: Diccionario base
            override: Diccionario con valores a sobrescribir
        """
        for key, value in override.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                ConfigLoader._deep_merge(base[key], value)
            else:
                base[key] = value
