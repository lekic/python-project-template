from package import module


def test_add_numbers() -> None:
    assert module.add_numbers(2, 3) == 5


def test_module() -> None:
    assert module.main() is None


def test_main(capsys):
    module.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello world!"
