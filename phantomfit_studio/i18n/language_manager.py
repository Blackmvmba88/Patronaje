"""
Gestor de idiomas y detección automática
"""

import os
import locale
from typing import Dict, Optional


def detect_system_language() -> str:
    """
    Detecta el idioma del sistema de manera temprana.
    
    Returns:
        Código de idioma (es, en, fr, de, pt, it)
    """
    try:
        # Intentar detectar desde variables de entorno
        lang = os.environ.get('LANG', '')
        if lang:
            lang_code = lang.split('_')[0].lower()
            if lang_code in ['es', 'en', 'fr', 'de', 'pt', 'it']:
                return lang_code
        
        # Intentar detectar desde locale
        system_locale = locale.getdefaultlocale()[0]
        if system_locale:
            lang_code = system_locale.split('_')[0].lower()
            if lang_code in ['es', 'en', 'fr', 'de', 'pt', 'it']:
                return lang_code
    except:
        pass
    
    # Idioma por defecto: español
    return 'es'


class LanguageManager:
    """
    Gestor de idiomas con soporte multilingüe.
    
    Idiomas soportados:
    - es: Español
    - en: English
    - fr: Français
    - de: Deutsch
    - pt: Português
    - it: Italiano
    """
    
    def __init__(self, language: Optional[str] = None):
        """
        Inicializa el gestor de idiomas.
        
        Args:
            language: Código de idioma (es, en, fr, de, pt, it).
                     Si es None, se detecta automáticamente.
        """
        self.language = language or detect_system_language()
        self.translations = self._load_translations()
    
    def _load_translations(self) -> Dict[str, Dict[str, str]]:
        """Carga las traducciones para todos los idiomas."""
        return {
            'es': {
                # Mensajes generales
                'studio_name': 'PhantomFit Studio',
                'studio_description': 'Entorno de diseño textil inteligente',
                'version': 'Versión',
                'welcome': 'Bienvenido a PhantomFit Studio',
                'initialized': 'Estudio inicializado',
                'pattern_generator_ready': 'Generador de patrones listo',
                'viewer_ready': 'Visualizador 3D listo',
                'module_manager_ready': 'Gestor de módulos listo',
                
                # Tipos de prenda
                'blouse': 'blusa',
                'shirt': 'camisa',
                'pants': 'pantalón',
                'skirt': 'falda',
                'dress': 'vestido',
                'jacket': 'chaqueta',
                
                # Acciones
                'generating_pattern': 'Generando patrón de',
                'pattern_generated': 'Patrón generado',
                'loading_model': 'Cargando modelo fantasma',
                'model_loaded': 'Modelo fantasma cargado',
                'visualizing_pattern': 'Visualizando patrón en 3D',
                'pattern_visualized': 'Patrón mapeado al modelo',
                'showing_3d_view': 'Mostrando vista 3D',
                'exporting_pattern': 'Exportando patrón',
                'pattern_exported': 'Patrón exportado',
                
                # Medidas
                'body_measurements': 'Medidas corporales',
                'bust': 'busto',
                'waist': 'cintura',
                'hip': 'cadera',
                'shoulder': 'hombro',
                'height': 'altura',
                'back_length': 'largo de espalda',
                'sleeve_length': 'largo de manga',
                'inseam': 'entrepierna',
                'outseam': 'costura lateral',
                
                # Información
                'pieces': 'piezas',
                'fabric_required': 'Tela requerida',
                'linear_meters': 'metros lineales',
                'pattern_info': 'Información del patrón',
                'status': 'estado',
                'type': 'tipo',
                'active': 'activo',
                'no_pattern': 'sin patrón',
                
                # Módulos LED
                'led_modules': 'Módulos LED',
                'adding_led': 'Agregando módulo LED',
                'led_added': 'LED agregado',
                'led_color': 'color LED',
                'led_intensity': 'intensidad',
                'led_pattern': 'patrón',
                'power_consumption': 'Consumo de energía',
                'total_power': 'Consumo total',
                
                # Materiales reflectantes
                'reflective_materials': 'Materiales reflectantes',
                'adding_reflective': 'Agregando material reflectante',
                'reflective_added': 'Material reflectante agregado',
                'reflectivity': 'reflectividad',
                'coverage': 'cobertura',
                'surface_area': 'área superficial',
                
                # Errores
                'error': 'Error',
                'no_pattern_available': 'No hay patrón disponible',
                'no_model_loaded': 'Primero debe cargar un modelo fantasma',
                'garment_not_supported': 'Tipo de prenda no soportado',
                'module_not_found': 'Módulo no encontrado',
                'invalid_format': 'Formato no válido',
                
                # Poses
                'pose': 'pose',
                'default': 'por defecto',
                'arms_up': 'brazos arriba',
                'arms_out': 'brazos extendidos',
                'sitting': 'sentado',
                
                # Vista 3D
                '3d_view_title': 'PHANTOMFIT STUDIO - VISTA 3D',
                'phantom_model': 'Modelo Fantasma',
                'current_pattern': 'Patrón Actual',
                'mapped_pieces': 'Piezas Mapeadas en 3D',
                'camera': 'Cámara',
                'lighting': 'Iluminación',
                'controls': 'CONTROLES',
                'rotate_camera': 'Ratón: Rotar cámara',
                'zoom': 'Rueda: Zoom',
                'move': 'Teclas: W/A/S/D para mover',
            },
            'en': {
                # General messages
                'studio_name': 'PhantomFit Studio',
                'studio_description': 'Intelligent textile design environment',
                'version': 'Version',
                'welcome': 'Welcome to PhantomFit Studio',
                'initialized': 'Studio initialized',
                'pattern_generator_ready': 'Pattern generator ready',
                'viewer_ready': '3D viewer ready',
                'module_manager_ready': 'Module manager ready',
                
                # Garment types
                'blouse': 'blouse',
                'shirt': 'shirt',
                'pants': 'pants',
                'skirt': 'skirt',
                'dress': 'dress',
                'jacket': 'jacket',
                
                # Actions
                'generating_pattern': 'Generating pattern for',
                'pattern_generated': 'Pattern generated',
                'loading_model': 'Loading phantom model',
                'model_loaded': 'Phantom model loaded',
                'visualizing_pattern': 'Visualizing pattern in 3D',
                'pattern_visualized': 'Pattern mapped to model',
                'showing_3d_view': 'Showing 3D view',
                'exporting_pattern': 'Exporting pattern',
                'pattern_exported': 'Pattern exported',
                
                # Measurements
                'body_measurements': 'Body measurements',
                'bust': 'bust',
                'waist': 'waist',
                'hip': 'hip',
                'shoulder': 'shoulder',
                'height': 'height',
                'back_length': 'back length',
                'sleeve_length': 'sleeve length',
                'inseam': 'inseam',
                'outseam': 'outseam',
                
                # Information
                'pieces': 'pieces',
                'fabric_required': 'Fabric required',
                'linear_meters': 'linear meters',
                'pattern_info': 'Pattern information',
                'status': 'status',
                'type': 'type',
                'active': 'active',
                'no_pattern': 'no pattern',
                
                # LED modules
                'led_modules': 'LED Modules',
                'adding_led': 'Adding LED module',
                'led_added': 'LED added',
                'led_color': 'LED color',
                'led_intensity': 'intensity',
                'led_pattern': 'pattern',
                'power_consumption': 'Power consumption',
                'total_power': 'Total power',
                
                # Reflective materials
                'reflective_materials': 'Reflective materials',
                'adding_reflective': 'Adding reflective material',
                'reflective_added': 'Reflective material added',
                'reflectivity': 'reflectivity',
                'coverage': 'coverage',
                'surface_area': 'surface area',
                
                # Errors
                'error': 'Error',
                'no_pattern_available': 'No pattern available',
                'no_model_loaded': 'Must load phantom model first',
                'garment_not_supported': 'Garment type not supported',
                'module_not_found': 'Module not found',
                'invalid_format': 'Invalid format',
                
                # Poses
                'pose': 'pose',
                'default': 'default',
                'arms_up': 'arms up',
                'arms_out': 'arms out',
                'sitting': 'sitting',
                
                # 3D View
                '3d_view_title': 'PHANTOMFIT STUDIO - 3D VIEW',
                'phantom_model': 'Phantom Model',
                'current_pattern': 'Current Pattern',
                'mapped_pieces': 'Mapped 3D Pieces',
                'camera': 'Camera',
                'lighting': 'Lighting',
                'controls': 'CONTROLS',
                'rotate_camera': 'Mouse: Rotate camera',
                'zoom': 'Wheel: Zoom',
                'move': 'Keys: W/A/S/D to move',
            },
            'fr': {
                # Messages généraux
                'studio_name': 'PhantomFit Studio',
                'studio_description': 'Environnement de conception textile intelligent',
                'version': 'Version',
                'welcome': 'Bienvenue à PhantomFit Studio',
                'initialized': 'Studio initialisé',
                'pattern_generator_ready': 'Générateur de patrons prêt',
                'viewer_ready': 'Visualiseur 3D prêt',
                'module_manager_ready': 'Gestionnaire de modules prêt',
                
                # Types de vêtements
                'blouse': 'chemisier',
                'shirt': 'chemise',
                'pants': 'pantalon',
                'skirt': 'jupe',
                'dress': 'robe',
                'jacket': 'veste',
                
                # Actions
                'generating_pattern': 'Génération du patron pour',
                'pattern_generated': 'Patron généré',
                'loading_model': 'Chargement du modèle fantôme',
                'model_loaded': 'Modèle fantôme chargé',
                'visualizing_pattern': 'Visualisation du patron en 3D',
                'pattern_visualized': 'Patron mappé sur le modèle',
                'showing_3d_view': 'Affichage de la vue 3D',
                'exporting_pattern': 'Exportation du patron',
                'pattern_exported': 'Patron exporté',
                
                # Mesures
                'body_measurements': 'Mesures corporelles',
                'bust': 'buste',
                'waist': 'taille',
                'hip': 'hanche',
                'shoulder': 'épaule',
                'height': 'hauteur',
                'back_length': 'longueur du dos',
                'sleeve_length': 'longueur de manche',
                'inseam': 'entrejambe',
                'outseam': 'couture latérale',
                
                # Information
                'pieces': 'pièces',
                'fabric_required': 'Tissu requis',
                'linear_meters': 'mètres linéaires',
                'pattern_info': 'Information du patron',
                'status': 'statut',
                'type': 'type',
                'active': 'actif',
                'no_pattern': 'pas de patron',
                
                # Modules LED
                'led_modules': 'Modules LED',
                'adding_led': 'Ajout du module LED',
                'led_added': 'LED ajouté',
                'led_color': 'couleur LED',
                'led_intensity': 'intensité',
                'led_pattern': 'motif',
                'power_consumption': 'Consommation d\'énergie',
                'total_power': 'Puissance totale',
                
                # Matériaux réfléchissants
                'reflective_materials': 'Matériaux réfléchissants',
                'adding_reflective': 'Ajout de matériau réfléchissant',
                'reflective_added': 'Matériau réfléchissant ajouté',
                'reflectivity': 'réflectivité',
                'coverage': 'couverture',
                'surface_area': 'surface',
                
                # Erreurs
                'error': 'Erreur',
                'no_pattern_available': 'Aucun patron disponible',
                'no_model_loaded': 'Doit charger le modèle fantôme d\'abord',
                'garment_not_supported': 'Type de vêtement non supporté',
                'module_not_found': 'Module non trouvé',
                'invalid_format': 'Format invalide',
                
                # Poses
                'pose': 'pose',
                'default': 'par défaut',
                'arms_up': 'bras levés',
                'arms_out': 'bras étendus',
                'sitting': 'assis',
                
                # Vue 3D
                '3d_view_title': 'PHANTOMFIT STUDIO - VUE 3D',
                'phantom_model': 'Modèle Fantôme',
                'current_pattern': 'Patron Actuel',
                'mapped_pieces': 'Pièces Mappées en 3D',
                'camera': 'Caméra',
                'lighting': 'Éclairage',
                'controls': 'CONTRÔLES',
                'rotate_camera': 'Souris: Rotation caméra',
                'zoom': 'Molette: Zoom',
                'move': 'Touches: W/A/S/D pour déplacer',
            },
            'de': {
                # Allgemeine Nachrichten
                'studio_name': 'PhantomFit Studio',
                'studio_description': 'Intelligente Textildesign-Umgebung',
                'version': 'Version',
                'welcome': 'Willkommen bei PhantomFit Studio',
                'initialized': 'Studio initialisiert',
                'pattern_generator_ready': 'Mustergenerator bereit',
                'viewer_ready': '3D-Viewer bereit',
                'module_manager_ready': 'Modulmanager bereit',
                
                # Kleidungstypen
                'blouse': 'Bluse',
                'shirt': 'Hemd',
                'pants': 'Hose',
                'skirt': 'Rock',
                'dress': 'Kleid',
                'jacket': 'Jacke',
                
                # Aktionen
                'generating_pattern': 'Muster wird generiert für',
                'pattern_generated': 'Muster generiert',
                'loading_model': 'Phantom-Modell wird geladen',
                'model_loaded': 'Phantom-Modell geladen',
                'visualizing_pattern': 'Muster wird in 3D visualisiert',
                'pattern_visualized': 'Muster auf Modell abgebildet',
                'showing_3d_view': '3D-Ansicht wird angezeigt',
                'exporting_pattern': 'Muster wird exportiert',
                'pattern_exported': 'Muster exportiert',
                
                # Maße
                'body_measurements': 'Körpermaße',
                'bust': 'Brust',
                'waist': 'Taille',
                'hip': 'Hüfte',
                'shoulder': 'Schulter',
                'height': 'Höhe',
                'back_length': 'Rückenlänge',
                'sleeve_length': 'Ärmellänge',
                'inseam': 'Innenbeinlänge',
                'outseam': 'Seitennaht',
                
                # Information
                'pieces': 'Teile',
                'fabric_required': 'Benötigter Stoff',
                'linear_meters': 'Laufmeter',
                'pattern_info': 'Musterinformation',
                'status': 'Status',
                'type': 'Typ',
                'active': 'aktiv',
                'no_pattern': 'kein Muster',
                
                # LED-Module
                'led_modules': 'LED-Module',
                'adding_led': 'LED-Modul wird hinzugefügt',
                'led_added': 'LED hinzugefügt',
                'led_color': 'LED-Farbe',
                'led_intensity': 'Intensität',
                'led_pattern': 'Muster',
                'power_consumption': 'Stromverbrauch',
                'total_power': 'Gesamtleistung',
                
                # Reflektierende Materialien
                'reflective_materials': 'Reflektierende Materialien',
                'adding_reflective': 'Reflektierendes Material wird hinzugefügt',
                'reflective_added': 'Reflektierendes Material hinzugefügt',
                'reflectivity': 'Reflektivität',
                'coverage': 'Abdeckung',
                'surface_area': 'Oberfläche',
                
                # Fehler
                'error': 'Fehler',
                'no_pattern_available': 'Kein Muster verfügbar',
                'no_model_loaded': 'Phantom-Modell muss zuerst geladen werden',
                'garment_not_supported': 'Kleidungstyp nicht unterstützt',
                'module_not_found': 'Modul nicht gefunden',
                'invalid_format': 'Ungültiges Format',
                
                # Posen
                'pose': 'Pose',
                'default': 'Standard',
                'arms_up': 'Arme hoch',
                'arms_out': 'Arme ausgestreckt',
                'sitting': 'sitzend',
                
                # 3D-Ansicht
                '3d_view_title': 'PHANTOMFIT STUDIO - 3D-ANSICHT',
                'phantom_model': 'Phantom-Modell',
                'current_pattern': 'Aktuelles Muster',
                'mapped_pieces': 'Abgebildete 3D-Teile',
                'camera': 'Kamera',
                'lighting': 'Beleuchtung',
                'controls': 'STEUERUNG',
                'rotate_camera': 'Maus: Kamera drehen',
                'zoom': 'Rad: Zoom',
                'move': 'Tasten: W/A/S/D zum Bewegen',
            },
            'pt': {
                # Mensagens gerais
                'studio_name': 'PhantomFit Studio',
                'studio_description': 'Ambiente de design têxtil inteligente',
                'version': 'Versão',
                'welcome': 'Bem-vindo ao PhantomFit Studio',
                'initialized': 'Estúdio inicializado',
                'pattern_generator_ready': 'Gerador de padrões pronto',
                'viewer_ready': 'Visualizador 3D pronto',
                'module_manager_ready': 'Gerenciador de módulos pronto',
                
                # Tipos de roupa
                'blouse': 'blusa',
                'shirt': 'camisa',
                'pants': 'calça',
                'skirt': 'saia',
                'dress': 'vestido',
                'jacket': 'jaqueta',
                
                # Ações
                'generating_pattern': 'Gerando padrão para',
                'pattern_generated': 'Padrão gerado',
                'loading_model': 'Carregando modelo fantasma',
                'model_loaded': 'Modelo fantasma carregado',
                'visualizing_pattern': 'Visualizando padrão em 3D',
                'pattern_visualized': 'Padrão mapeado no modelo',
                'showing_3d_view': 'Mostrando vista 3D',
                'exporting_pattern': 'Exportando padrão',
                'pattern_exported': 'Padrão exportado',
                
                # Medidas
                'body_measurements': 'Medidas corporais',
                'bust': 'busto',
                'waist': 'cintura',
                'hip': 'quadril',
                'shoulder': 'ombro',
                'height': 'altura',
                'back_length': 'comprimento das costas',
                'sleeve_length': 'comprimento da manga',
                'inseam': 'entrepernas',
                'outseam': 'costura lateral',
                
                # Informação
                'pieces': 'peças',
                'fabric_required': 'Tecido necessário',
                'linear_meters': 'metros lineares',
                'pattern_info': 'Informação do padrão',
                'status': 'status',
                'type': 'tipo',
                'active': 'ativo',
                'no_pattern': 'sem padrão',
                
                # Módulos LED
                'led_modules': 'Módulos LED',
                'adding_led': 'Adicionando módulo LED',
                'led_added': 'LED adicionado',
                'led_color': 'cor LED',
                'led_intensity': 'intensidade',
                'led_pattern': 'padrão',
                'power_consumption': 'Consumo de energia',
                'total_power': 'Potência total',
                
                # Materiais refletivos
                'reflective_materials': 'Materiais refletivos',
                'adding_reflective': 'Adicionando material refletivo',
                'reflective_added': 'Material refletivo adicionado',
                'reflectivity': 'refletividade',
                'coverage': 'cobertura',
                'surface_area': 'área superficial',
                
                # Erros
                'error': 'Erro',
                'no_pattern_available': 'Nenhum padrão disponível',
                'no_model_loaded': 'Deve carregar o modelo fantasma primeiro',
                'garment_not_supported': 'Tipo de roupa não suportado',
                'module_not_found': 'Módulo não encontrado',
                'invalid_format': 'Formato inválido',
                
                # Poses
                'pose': 'pose',
                'default': 'padrão',
                'arms_up': 'braços levantados',
                'arms_out': 'braços estendidos',
                'sitting': 'sentado',
                
                # Vista 3D
                '3d_view_title': 'PHANTOMFIT STUDIO - VISTA 3D',
                'phantom_model': 'Modelo Fantasma',
                'current_pattern': 'Padrão Atual',
                'mapped_pieces': 'Peças Mapeadas em 3D',
                'camera': 'Câmera',
                'lighting': 'Iluminação',
                'controls': 'CONTROLES',
                'rotate_camera': 'Mouse: Girar câmera',
                'zoom': 'Roda: Zoom',
                'move': 'Teclas: W/A/S/D para mover',
            },
            'it': {
                # Messaggi generali
                'studio_name': 'PhantomFit Studio',
                'studio_description': 'Ambiente di progettazione tessile intelligente',
                'version': 'Versione',
                'welcome': 'Benvenuto a PhantomFit Studio',
                'initialized': 'Studio inizializzato',
                'pattern_generator_ready': 'Generatore di modelli pronto',
                'viewer_ready': 'Visualizzatore 3D pronto',
                'module_manager_ready': 'Gestore moduli pronto',
                
                # Tipi di indumento
                'blouse': 'camicetta',
                'shirt': 'camicia',
                'pants': 'pantaloni',
                'skirt': 'gonna',
                'dress': 'vestito',
                'jacket': 'giacca',
                
                # Azioni
                'generating_pattern': 'Generazione modello per',
                'pattern_generated': 'Modello generato',
                'loading_model': 'Caricamento modello fantasma',
                'model_loaded': 'Modello fantasma caricato',
                'visualizing_pattern': 'Visualizzazione modello in 3D',
                'pattern_visualized': 'Modello mappato sul modello',
                'showing_3d_view': 'Visualizzazione vista 3D',
                'exporting_pattern': 'Esportazione modello',
                'pattern_exported': 'Modello esportato',
                
                # Misure
                'body_measurements': 'Misure corporee',
                'bust': 'busto',
                'waist': 'vita',
                'hip': 'anca',
                'shoulder': 'spalla',
                'height': 'altezza',
                'back_length': 'lunghezza schiena',
                'sleeve_length': 'lunghezza manica',
                'inseam': 'cavallo',
                'outseam': 'cucitura laterale',
                
                # Informazioni
                'pieces': 'pezzi',
                'fabric_required': 'Tessuto richiesto',
                'linear_meters': 'metri lineari',
                'pattern_info': 'Informazioni modello',
                'status': 'stato',
                'type': 'tipo',
                'active': 'attivo',
                'no_pattern': 'nessun modello',
                
                # Moduli LED
                'led_modules': 'Moduli LED',
                'adding_led': 'Aggiunta modulo LED',
                'led_added': 'LED aggiunto',
                'led_color': 'colore LED',
                'led_intensity': 'intensità',
                'led_pattern': 'motivo',
                'power_consumption': 'Consumo energetico',
                'total_power': 'Potenza totale',
                
                # Materiali riflettenti
                'reflective_materials': 'Materiali riflettenti',
                'adding_reflective': 'Aggiunta materiale riflettente',
                'reflective_added': 'Materiale riflettente aggiunto',
                'reflectivity': 'riflettività',
                'coverage': 'copertura',
                'surface_area': 'area superficiale',
                
                # Errori
                'error': 'Errore',
                'no_pattern_available': 'Nessun modello disponibile',
                'no_model_loaded': 'Deve caricare il modello fantasma prima',
                'garment_not_supported': 'Tipo di indumento non supportato',
                'module_not_found': 'Modulo non trovato',
                'invalid_format': 'Formato non valido',
                
                # Pose
                'pose': 'posa',
                'default': 'predefinito',
                'arms_up': 'braccia alzate',
                'arms_out': 'braccia estese',
                'sitting': 'seduto',
                
                # Vista 3D
                '3d_view_title': 'PHANTOMFIT STUDIO - VISTA 3D',
                'phantom_model': 'Modello Fantasma',
                'current_pattern': 'Modello Attuale',
                'mapped_pieces': 'Pezzi Mappati in 3D',
                'camera': 'Telecamera',
                'lighting': 'Illuminazione',
                'controls': 'CONTROLLI',
                'rotate_camera': 'Mouse: Ruotare telecamera',
                'zoom': 'Rotella: Zoom',
                'move': 'Tasti: W/A/S/D per muovere',
            }
        }
    
    def t(self, key: str, default: Optional[str] = None) -> str:
        """
        Traduce una clave al idioma actual.
        
        Args:
            key: Clave de traducción
            default: Valor por defecto si no se encuentra la traducción
            
        Returns:
            Texto traducido
        """
        if self.language in self.translations:
            return self.translations[self.language].get(key, default or key)
        return default or key
    
    def set_language(self, language: str) -> bool:
        """
        Cambia el idioma actual.
        
        Args:
            language: Código del nuevo idioma
            
        Returns:
            True si el idioma fue cambiado exitosamente
        """
        if language in self.translations:
            self.language = language
            return True
        return False
    
    def get_available_languages(self) -> Dict[str, str]:
        """
        Obtiene la lista de idiomas disponibles.
        
        Returns:
            Diccionario con códigos y nombres de idiomas
        """
        return {
            'es': 'Español',
            'en': 'English',
            'fr': 'Français',
            'de': 'Deutsch',
            'pt': 'Português',
            'it': 'Italiano'
        }
    
    def get_current_language(self) -> str:
        """
        Obtiene el idioma actual.
        
        Returns:
            Código del idioma actual
        """
        return self.language
