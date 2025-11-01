"""
Sistema de internacionalización (i18n) para PhantomFit Studio
"""

from .language_manager import LanguageManager, detect_system_language

__all__ = ["LanguageManager", "detect_system_language"]
