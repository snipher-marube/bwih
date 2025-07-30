import os

settings_module = os.getenv('BW_SETTINGS_MODULE')

if settings_module == 'bwih.settings.production':
    from .production import *
else:
    from .development import *
    