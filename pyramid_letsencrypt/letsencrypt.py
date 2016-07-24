from pyramid.response import FileResponse
from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.view import view_config

import os


@view_config(
    route_name='letsencrypt',
    permission=NO_PERMISSION_REQUIRED,
)
def letsencrypt(request):
    return request.registry.settings['letsencrypt.content']