from __future__ import absolute_import, unicode_literals

from django.conf import settings

# Imported for historical reasons
from django.core.exceptions import ImproperlyConfigured

from wagtail import __semver__, __version__  # noqa

default_app_config = 'wagtail.wagtailcore.apps.WagtailCoreAppConfig'


def get_page_model_string():
    """
    Get the dotted ``app.Model`` name for the page model as a string.
    Useful for developers making Wagtail plugins that need to refer to the
    page model, such as in foreign keys, but the model itself is not required.
    """
    return getattr(settings, 'WAGTAILCORE_PAGE_MODEL', 'wagtailcore.Page')


def get_page_model():
    """
    Get the page model from the ``WAGTAILCORE_PAGE_MODEL`` setting.
    Useful for developers making Wagtail plugins that need the page model.
    Defaults to the standard :class:`~wagtail.wagtailcore.models.Page` model
    if no custom model is defined.
    """
    from django.apps import apps
    model_string = get_page_model_string()
    try:
        return apps.get_model(model_string)
    except ValueError:
        raise ImproperlyConfigured("WAGTAILCORE_PAGE_MODEL must be of the form `app_label.ModelName`")
    except LookupError:
        raise ImproperlyConfigured(
            "WAGTAILCORE_PAGE_MODEL reffers to model `%s` that has not been installed" % model_string
        )


def setup():
    import warnings
    from wagtail.utils.deprecation import removed_in_next_version_warning

    warnings.simplefilter("default", removed_in_next_version_warning)


setup()
