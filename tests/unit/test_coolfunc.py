from shop_app.coolfunc import stringfunc, hello_world


def test_hello_world():
    assert hello_world() == "<p>Hello, World!</p>"


def test_stringfunc():
    assert stringfunc(string="Janne") == "<p> ennaJ </p>"
