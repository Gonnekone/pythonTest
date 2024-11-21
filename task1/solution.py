def strict(func):
    def wrapper(*args, **kwargs):
        requirements = func.__annotations__
        args_index = 0

        for arg_name in requirements:
            arg_type = requirements[arg_name].__name__

            if arg_name == "return":
                continue

            if arg_type != type(args[args_index]).__name__:
                raise TypeError(f"Argument {arg_name} must be {arg_type}")

            args_index += 1

        return func(*args, **kwargs)

    return wrapper

def test_strict_decorator():
    @strict
    def add(a: int, b: int) -> int:
        return a + b

    assert add(2, 3) == 5, "Ошибка: корректные типы аргументов должны работать."

    try:
        add(2, "3")
    except TypeError as e:
        assert str(e) == "Argument b must be int", f"Ошибка: {e}"
    else:
        assert False, "Ошибка: должен был быть вызван TypeError."

    @strict
    def concatenate(a: str, b: str) -> str:
        return a + b

    assert concatenate("hello, ", "world!") == "hello, world!", "Ошибка: корректные строки должны работать."

    try:
        concatenate("hello, ", 123)
    except TypeError as e:
        assert str(e) == "Argument b must be str", f"Ошибка: {e}"
    else:
        assert False, "Ошибка: должен был быть вызван TypeError."

    @strict
    def no_annotations(a, b):
        return a + b

    assert no_annotations(5, 10) == 15, "Ошибка: функция без аннотаций не должна проверять типы."

    @strict
    def mixed_types(a: int, b: str, c: float) -> str:
        return f"{a} - {b} - {c}"

    assert mixed_types(1, "test", 2.5) == "1 - test - 2.5", "Ошибка: корректные типы аргументов должны работать."

    try:
        mixed_types(1, "test", "2.5")
    except TypeError as e:
        assert str(e) == "Argument c must be float", f"Ошибка: {e}"
    else:
        assert False, "Ошибка: должен был быть вызван TypeError."

    print("Все тесты успешно пройдены!")


if __name__ == "__main__":
    test_strict_decorator()