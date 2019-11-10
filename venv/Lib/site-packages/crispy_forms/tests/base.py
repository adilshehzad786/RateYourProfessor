import os

import django
from django.conf import settings
from django.template import loader
from django.test import TestCase

from crispy_forms.tests.utils import override_settings
from crispy_forms.tests.test_settings import InvalidVarException


class BaseCrispyTestCase(TestCase):

    @property
    def current_template_pack(self):
        return getattr(settings, 'CRISPY_TEMPLATE_PACK', 'bootstrap')

    if not hasattr(TestCase, 'assertInHTML'):
        def assertInHTML(self, needle, haystack, count=None, msg_prefix=''):
            """Backport from Django 1.6.
            """
            from django.test.testcases import assert_and_parse_html

            needle = assert_and_parse_html(
                self, needle, None, 'First argument is not valid HTML:',
            )
            haystack = assert_and_parse_html(
                self, haystack, None, 'Second argument is not valid HTML:',
            )
            real_count = haystack.count(needle)
            if count is not None:
                self.assertEqual(
                    real_count, count,
                    msg_prefix + "Found %d instances of '%s' in response"
                    " (expected %d)" % (real_count, needle, count),
                )
            else:
                self.assertTrue(
                    real_count != 0,
                    msg_prefix + "Couldn't find '%s' in response" % needle,
                )


class VintageCrispyTestCase(BaseCrispyTestCase):
    """CrispyTestCase for Djagno < 1.8.
    """
    def setUp(self):
        template_dirs = [os.path.join(os.path.dirname(__file__), 'templates')]
        template_dirs = template_dirs + list(settings.TEMPLATE_DIRS)
        template_loaders = ['django.template.loaders.filesystem.Loader']
        template_loaders = template_loaders + list(settings.TEMPLATE_LOADERS)

        # ensuring test templates directory is loaded first
        self.__overriden_settings = override_settings(**{
            'TEMPLATE_LOADERS': template_loaders,
            'TEMPLATE_DIRS': template_dirs,
        })
        self.__overriden_settings.enable()

        # resetting template loaders cache
        self.__template_source_loaders = loader.template_source_loaders
        loader.template_source_loaders = None

    def tearDown(self):
        loader.template_source_loaders = self.__template_source_loaders
        self.__overriden_settings.disable()


class ModernCrispyTestCase(BaseCrispyTestCase):
    """CrispyTestCase for Djagno >= 1.8.
    """
    def setUp(self):
        template_settings = settings.TEMPLATES[:]
        django_template_setting = [
            s for s in template_settings
            if s['BACKEND'] == 'django.template.backends.django.DjangoTemplates'
        ][0]
        django_template_setting['DIRS'].insert(
            0, os.path.join(os.path.dirname(__file__), 'templates'),
        )
        self.__overriden_settings = override_settings(
            TEMPLATES=[django_template_setting],
        )
        self.__overriden_settings.enable()

    def tearDown(self):
        self.__overriden_settings.disable()


if django.VERSION >= (1, 8):
    CrispyTestCase = ModernCrispyTestCase
else:
    CrispyTestCase = VintageCrispyTestCase
