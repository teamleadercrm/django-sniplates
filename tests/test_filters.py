from django.test import SimpleTestCase
from django.template.loader import get_template
from django import VERSION
from .utils import TemplateTestMixin, template_path, override_settings

@override_settings(
    TEMPLATE_DIRS=[template_path('filters')],
)
class TestFilters(TemplateTestMixin, SimpleTestCase):

    def test_flatattrs(self):
        tmpl = get_template('flatattrs')
        self.ctx['a_dict'] = {
            'a': 'aye',
            'b': 'bee',
            'c': 'cee',
        }
        output = tmpl.render(self.ctx)

        if VERSION[:2] >= (1, 5):
            self.assertEqual(output, ' a="aye" b="bee" c="cee" \n')
        else:
            self.assertTrue(' a=&quot;aye&quot; ' in output)
            self.assertTrue(' b=&quot;bee&quot; ' in output)
            self.assertTrue(' c=&quot;cee&quot; ' in output)
