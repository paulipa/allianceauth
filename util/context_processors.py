from django.conf import settings


def alliance_id(request):
    return {'ALLIANCE_ID': settings.ALLIANCE_ID}


def alliance_name(request):
    return {'ALLIANCE_NAME': settings.ALLIANCE_NAME}


def jabber_url(request):
    return {'JABBER_URL': settings.JABBER_URL}


def domain_url(request):
    return {'DOMAIN': settings.DOMAIN, 'MUMBLE_URL': settings.MUMBLE_URL,
            'FORUM_URL': settings.FORUM_URL,
            'ENABLE_ALLIANCE_FORUM': settings.ENABLE_ALLIANCE_FORUM,
            'ENABLE_ALLIANCE_JABBER': settings.ENABLE_ALLIANCE_JABBER,
            'ENABLE_ALLIANCE_MUMBLE': settings.ENABLE_ALLIANCE_MUMBLE,
            'ENABLE_BLUE_JABBER': settings.ENABLE_BLUE_JABBER,
            'ENABLE_BLUE_FORUM': settings.ENABLE_BLUE_FORUM,
            'ENABLE_BLUE_MUMBLE': settings.ENABLE_BLUE_MUMBLE}