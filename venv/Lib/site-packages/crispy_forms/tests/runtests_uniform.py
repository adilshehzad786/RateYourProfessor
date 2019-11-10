#!/usr/bin/env python

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
parent = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)
)))

sys.path.insert(0, parent)

from django.conf import settings

settings.CRISPY_TEMPLATE_PACK = 'uni_form'


def runtests():
    from crispy_forms.tests.utils import DiscoverRunner, setup
    setup()
    return DiscoverRunner(failfast=False).run_tests([
        'crispy_forms.tests.TestBasicFunctionalityTags',
        'crispy_forms.tests.TestFormHelper',
        'crispy_forms.tests.TestUniformFormHelper',
        'crispy_forms.tests.TestFormLayout',
        'crispy_forms.tests.TestUniformFormLayout',
        'crispy_forms.tests.TestLayoutObjects',
        'crispy_forms.tests.TestDynamicLayouts',
        'crispy_forms.tests.TestUniformDynamicLayouts',
    ], verbosity=1, interactive=True)


if __name__ == '__main__':
    if runtests():
        sys.exit(1)
