import py_compile


def test_python_tutor_compiles():
    # Ensure the main script compiles (syntax check)
    py_compile.compile("python_tutor.py", doraise=True)
