from django.apps import AppConfig


class BaseConfig(AppConfig):
    """
    AppConfig for the 'base' app.

    Attributes:
        default_auto_field (str): The default auto-generated field for models.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
