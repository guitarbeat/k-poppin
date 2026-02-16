import sys
import os

# Add the root directory to sys.path so we can import customize
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customize import check_js_syntax

def test_check_js_syntax_valid():
    assert check_js_syntax("const a = 1;") is True
    assert check_js_syntax("function foo() { return 'bar'; }") is True
    assert check_js_syntax("const obj = { key: 'value', arr: [1, 2] };") is True

def test_check_js_syntax_invalid():
    assert check_js_syntax("function foo() { return 'bar';") is False
    assert check_js_syntax("const a = (1 + 2") is False
    assert check_js_syntax("const a = [1, 2") is False
    assert check_js_syntax("const a = 'unfinished string") is False
