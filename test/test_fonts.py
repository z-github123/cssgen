import os
import tempfile

import pytest

from opimodel import fonts

TEST_FONT_FILE = """dummy 1 = Dummy one-bold-19pt
dummy 2 = Dummy two-italic-15px
dummy 3 = Dummy one-regular-14
"""


@pytest.fixture
def font_file():
    tmp = tempfile.NamedTemporaryFile('wt', delete=False)
    tmp.write(TEST_FONT_FILE)
    tmp.close()
    yield tmp
    os.unlink(tmp.name)


def test_add_font_to_widget(widget, get_renderer):
    f = fonts.Font(name='Dummy Font Name', fontface='Dummy Font Face', size=12, style=fonts.REGULAR)
    widget.set_font(f)
    renderer = get_renderer(widget)
    renderer.assemble()
    node = renderer.get_node()
    font_nodes = node.findall('./font')
    assert len(font_nodes) == 1
    opifont_nodes = node.findall('./font/opifont.name')
    assert len(opifont_nodes) == 1
    assert opifont_nodes[0].text == 'Dummy Font Name'
    assert opifont_nodes[0].get('fontName') == 'Dummy Font Face'
    assert opifont_nodes[0].get('height') == '12'
    assert opifont_nodes[0].get('style') == '0'


def test_parse_css_font_file(font_file):
    fonts.parse_css_font_file(font_file.name)
    print(fonts.DUMMY_1)
    print(fonts.BOLD)
    assert fonts.DUMMY_1 == fonts.Font('dummy 1', 'Dummy one', 19,
                                       fonts.BOLD, pixels=False)
    assert fonts.DUMMY_2 == fonts.Font('dummy 2', 'Dummy two', 15,
                                       fonts.ITALIC, pixels=True)
    assert fonts.DUMMY_3 == fonts.Font('dummy 3', 'Dummy one', 14,
                                       fonts.REGULAR, pixels=False)
