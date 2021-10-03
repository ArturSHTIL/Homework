from contextlib import contextmanager


@contextmanager
def context(file_name, flag='r'):
    """
    Implement context manager for opening and working with file,
     including handling exceptions with @contextmanager decorator.

    :param file_name: xample_2.txt
    :param flag: "w","r","a"...
    :return: class '_io.TextIOWrapper'
    """
    file_data = None
    try:
        file_data = open(file_name, flag)
        yield file_data

    except FileNotFoundError:
        print("No such file or directory")
    except IsADirectoryError:
        print('IsADirectoryError')
    except PermissionError:
        print('PermissionError')
    except (AttributeError,):
        print('AttributeError')
    except RuntimeError:
        print("RuntimeError")
    except ValueError:
        print('Not writable file')

    finally:
        if file_data is not None:
            file_data.close()


if __name__ == '__main__':
    with context('example_2.txt') as data:
        data.write('Figure none')
    with context('example_2.txt', 'w') as data:
        data.write("Python is Really A Huge Snake!)))")
