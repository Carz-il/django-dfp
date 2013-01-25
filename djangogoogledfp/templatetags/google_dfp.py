from django import template
from djangogoogledfp import settings
from django.conf import settings as django_settings

register = template.Library()

def google_dfp_init_script():
    """
    Generates the required JS for displaying google dfp ad units
    :rtype : dict
        """
    return {'SCRIPT_URL': settings.DFP_INIT_SCRIPT_URL}


def dfp_ad_unit(name, width_in_px, height_in_px):
    """
    Generates the required HTML + JS to display ad the given ad unit

    :rtype : dict
        """
    return {'ACCOUNT_ID': getattr(django_settings, 'GOOGLE_DFP_ACCOUNT_ID'),
            'AD_UNIT_NAME': name,
            'HEIGHT_PX': height_in_px,
            'width_in_px': width_in_px
    }