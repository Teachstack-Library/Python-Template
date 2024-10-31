def test_hello_world(capsys):
    from ..exercise import main
    out, err = capsys.readouterr()
    assert out.strip() == 'Hello World!'
