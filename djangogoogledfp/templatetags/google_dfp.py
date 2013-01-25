from django import template
from djangogoogledfp import settings
from django.conf import settings as django_settings
import uuid

register = template.Library()

@register.inclusion_tag('dfp_init_script.html')
def google_dfp_init_script():
    """
    Generates the required JS for displaying google dfp ad units
    :rtype : dict
    """
    return {'SCRIPT_URL': settings.DFP_INIT_SCRIPT_URL}


@register.inclusion_tag("dfp_ad_unit.html")
def dfp_ad_unit(name, width_in_px, height_in_px):
    """
    Generates the required HTML + JS to display the given ad unit

    :rtype : dict
    """
    unique_element_id = "%s_%sX%s_%s" % (name, width_in_px, height_in_px, str(uuid.uuid1()))
    dfp_account_id = getattr(django_settings, 'GOOGLE_DFP_ACCOUNT_ID')

    return {'ACCOUNT_ID': dfp_account_id,
            'AD_UNIT_NAME': name,
            'HEIGHT_PX': height_in_px,
            'WIDTH_PX': width_in_px,
            'DISPLAY_ELEMENT_ID': unique_element_id
    }