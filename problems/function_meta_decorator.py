"""
Write a decorator that show function name and all parameters to console when inner function called.
"""
from collections.abc import Callable


def show_function_meta_on_call(exclude: list[str] = None):

    def inner(function: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            print(f'Calling function: {function.__name__}')
            print('with args: ', args)
            print_kwargs = {
                key: value
                for key, value in kwargs.items()
                if key not in exclude or list()
            }
            print('kwargs', print_kwargs)
            result = function(*args, **kwargs)
            print(result)
            print('_' * 50)
            return result
        return wrapper
    return inner


@show_function_meta_on_call(exclude=['test1'])
def do_something(*args, **kwargs):
    return 25


do_something(1, 2, 3, test1=1, test2=2)
