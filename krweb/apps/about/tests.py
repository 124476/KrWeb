import http

import django.shortcuts
import django.test


class TestHomepage(django.test.TestCase):
    def test_status_code(self):
        response = django.test.Client().get(
            django.shortcuts.reverse("about:main"),
        )
        self.assertEqual(response.status_code, http.HTTPStatus.OK)