"""
Clase principal del estudio PhantomFit
"""

from typing import Dict, List, Optional, Any
from .pattern_generator import PatternGenerator
from ..visualization.phantom_viewer import PhantomViewer
from ..integration.module_manager import ModuleManager
from ..i18n import LanguageManager, detect_system_language


class PhantomFitStudio:
    """
    Entorno de diseño textil inteligente PhantomFit Studio.
    
    Proporciona funcionalidades para:
    - Generar patrones de ropa
    - Visualizar en 3D una muñeca fantasma
    - Integración con módulos LED y materiales reflectantes
    - Soporte multilingüe con detección automática
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None, language: Optional[str] = None):
        """
        Inicializa el estudio PhantomFit con detección temprana de idioma.
        
        Args:
            config: Configuración opcional del estudio
            language: Código de idioma (es, en, fr, de, pt, it). 
                     Si es None, se detecta automáticamente del sistema.
        """
        # Detección temprana de idioma
        if language is None:
            language = detect_system_language()
        
        self.config = config or {}
        self.lang = LanguageManager(language)
        self.pattern_generator = PatternGenerator(language_manager=self.lang)
        self.phantom_viewer = PhantomViewer(config=self.config.get('viewer', {}), language_manager=self.lang)
        self.module_manager = ModuleManager(config=self.config.get('modules', {}), language_manager=self.lang)
        self.current_pattern = None
        self.phantom_model = None
        
    def generate_pattern(self, 
                        garment_type: str,
                        measurements: Dict[str, float],
                        style_options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Genera un patrón de ropa basado en las medidas y tipo de prenda.
        
        Args:
            garment_type: Tipo de prenda (e.g., "blouse", "pants", "dress")
            measurements: Diccionario con medidas corporales
            style_options: Opciones de estilo opcionales
            
        Returns:
            Diccionario con los datos del patrón generado
        """
        pattern = self.pattern_generator.generate(
            garment_type=garment_type,
            measurements=measurements,
            style_options=style_options or {}
        )
        self.current_pattern = pattern
        return pattern
    
    def visualize_pattern(self, pattern: Optional[Dict[str, Any]] = None) -> None:
        """
        Visualiza un patrón en 3D sobre la muñeca fantasma.
        
        Args:
            pattern: Patrón a visualizar. Si es None, usa el patrón actual
        """
        pattern_to_show = pattern or self.current_pattern
        if pattern_to_show is None:
            raise ValueError("No hay patrón disponible para visualizar")
        
        self.phantom_viewer.display_pattern(pattern_to_show)
    
    def load_phantom_model(self, 
                          body_measurements: Dict[str, float],
                          pose: str = "default") -> None:
        """
        Carga y configura el modelo de muñeca fantasma.
        
        Args:
            body_measurements: Medidas corporales para el modelo
            pose: Pose del modelo (e.g., "default", "arms_up", "sitting")
        """
        self.phantom_model = self.phantom_viewer.create_phantom(
            measurements=body_measurements,
            pose=pose
        )
    
    def show_3d_view(self) -> None:
        """
        Muestra la vista 3D interactiva del estudio.
        """
        if self.phantom_model is None:
            raise ValueError("Primero debe cargar un modelo fantasma con load_phantom_model()")
        
        self.phantom_viewer.show()
    
    def add_led_module(self, module_config: Dict[str, Any]) -> str:
        """
        Agrega un módulo LED al diseño actual.
        
        Args:
            module_config: Configuración del módulo LED
            
        Returns:
            ID del módulo agregado
        """
        return self.module_manager.add_led_module(module_config)
    
    def add_reflective_material(self, material_config: Dict[str, Any]) -> str:
        """
        Agrega un material reflectante al diseño actual.
        
        Args:
            material_config: Configuración del material reflectante
            
        Returns:
            ID del material agregado
        """
        return self.module_manager.add_reflective_material(material_config)
    
    def export_pattern(self, filepath: str, format: str = "svg") -> None:
        """
        Exporta el patrón actual a un archivo.
        
        Args:
            filepath: Ruta del archivo de salida
            format: Formato de exportación (svg, pdf, dxf)
        """
        if self.current_pattern is None:
            raise ValueError("No hay patrón para exportar")
        
        self.pattern_generator.export(self.current_pattern, filepath, format)
    
    def get_pattern_info(self) -> Dict[str, Any]:
        """
        Obtiene información del patrón actual.
        
        Returns:
            Diccionario con información del patrón
        """
        if self.current_pattern is None:
            return {"status": "no_pattern"}
        
        return {
            "status": "active",
            "type": self.current_pattern.get("garment_type"),
            "pieces": len(self.current_pattern.get("pieces", [])),
            "measurements": self.current_pattern.get("measurements"),
            "modules": self.module_manager.get_active_modules()
        }
    
    def set_language(self, language: str) -> bool:
        """
        Cambia el idioma del estudio.
        
        Args:
            language: Código de idioma (es, en, fr, de, pt, it)
            
        Returns:
            True si el cambio fue exitoso
        """
        return self.lang.set_language(language)
    
    def get_language(self) -> str:
        """
        Obtiene el idioma actual.
        
        Returns:
            Código del idioma actual
        """
        return self.lang.get_current_language()
    
    def get_available_languages(self) -> Dict[str, str]:
        """
        Obtiene los idiomas disponibles.
        
        Returns:
            Diccionario con códigos y nombres de idiomas
        """
        return self.lang.get_available_languages()
