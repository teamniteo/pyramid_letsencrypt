from pyramid import testing

import unittest


class TestLetsencryptContent(unittest.TestCase):

    def test_response(self):
        from pyramid_letsencrypt import letsencrypt_content

        request = testing.DummyRequest()
        request.registry.settings = {'letsencrypt.content': 'foo.bar'}
        response = letsencrypt_content(request)

        self.assertEqual(response.body, b'foo.bar')
        self.assertEqual(response.content_type, 'text/plain')



class TestIncludeME(unittest.TestCase):

    def test_no_content(self):
        from pyramid_letsencrypt import includeme

        config = testing.setUp()

        includeme(config)

        self.assertEqual(len(config.get_routes_mapper().get_routes()), 0)

    def test_route_and_view_configured(self):
        from pyramid_letsencrypt import includeme

        config = testing.setUp()
        config.registry.settings = {'letsencrypt.content': 'foo.bar'}

        includeme(config)

        self.assertEqual(len(config.get_routes_mapper().get_routes()), 1)

        route = config.get_routes_mapper().get_route('letsencrypt')
        self.assertEqual(route.name, 'letsencrypt')
        self.assertEqual(route.path, '.well-known/acme-challenge/foo')
