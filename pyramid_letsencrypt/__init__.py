from pyramid.response import Response
from pyramid.security import NO_PERMISSION_REQUIRED

import logging

# nose.plugin.cover fix
from pyramid_letsencrypt import nose_fix  # noqa


logger = logging.getLogger(__name__)


def letsencrypt_content(request):
    return Response(
        body=request.registry.settings['letsencrypt.content'],
        content_type='text/plain',
    )


def includeme(config):
    """Activate ``pyramid_letsencrypt``.

    Usually called via ``config.include('pyramid_letsencrypt')`` instead of
    being invoked
    directly.
    """
    if not config.registry.settings.get('letsencrypt.content'):
        logger.warning(
            'The "letsencrypt.content" registry setting is not set, '
            'disabling pyramid_letsencrypt.'
        )
        return

    route = '.well-known/acme-challenge/{}'.format(
        config.registry.settings['letsencrypt.content'].split('.')[0])
    config.add_route('letsencrypt', route)
    config.add_view(
        view=letsencrypt_content,
        route_name='letsencrypt',
        permission=NO_PERMISSION_REQUIRED,
    )
