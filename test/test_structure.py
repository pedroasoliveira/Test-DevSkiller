import base64
import unittest

import app.drug_analyzer


class StructureTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.MODULE = app.drug_analyzer
    
    def test_class_exists_druganalyzer(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode()}` "
                f"is not found, but it was marked as required."
        )
        
    def test_class_function_exists_druganalyzer_verify_series(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode()}` "
                f"is not found, but it was marked as required."
        )
        functions = _get_class_function_names(
            self.MODULE,
            base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode()
        )
        self.assertIn(
            base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode(),
            functions,
            msg=f"The function "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode()}` "
                f"is not found in class "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode()}`, "
                f"but it was marked as required."
        )
        
    def test_class_function_signature_match_druganalyzer_verify_series(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode(),
            classes,
            msg=f"The class "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode()}` "
                f"is not found, but it was marked as required."
        )
        functions = _get_class_function_names(
            self.MODULE,
            base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode()
        )
        self.assertIn(
            base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode(),
            functions,
            msg=f"The function "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode()}` "
                f"is not found in class "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode()}`, "
                f"but it was marked as required."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode(),
            base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode()
        )
        self.assertEqual(
            5,
            len(args),
            msg=f"The function "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode()}` "
                f"should have 5 argument(s)."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode(),
            base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode()
        )
        self.assertEqual(
            base64.b64decode(b'c2VsZg==').decode(),
            args[0],
            msg=f"The argument #0 of function "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode()}` "
                f"should be called "
                f"`self`."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode(),
            base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode()
        )
        self.assertEqual(
            base64.b64decode(b'c2VyaWVzX2lk').decode(),
            args[1],
            msg=f"The argument #1 of function "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode()}` "
                f"should be called "
                f"`series_id`."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode(),
            base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode()
        )
        self.assertEqual(
            base64.b64decode(b'YWN0X3N1YnN0X3dndA==').decode(),
            args[2],
            msg=f"The argument #2 of function "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode()}` "
                f"should be called "
                f"`act_subst_wgt`."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode(),
            base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode()
        )
        self.assertEqual(
            base64.b64decode(b'YWN0X3N1YnN0X3JhdGU=').decode(),
            args[3],
            msg=f"The argument #3 of function "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode()}` "
                f"should be called "
                f"`act_subst_rate`."
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode(),
            base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode()
        )
        self.assertEqual(
            base64.b64decode(b'YWxsb3dlZF9pbXA=').decode(),
            args[4],
            msg=f"The argument #4 of function "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVyLnZlcmlmeV9zZXJpZXM=').decode()}` "
                f"in class "
                f"`{base64.b64decode(b'RHJ1Z0FuYWx5emVy').decode()}` "
                f"should be called "
                f"`allowed_imp`."
        )
        

# === Internal functions, do not modify ===
import inspect

from types import ModuleType
from typing import List


def _get_function_names(module: ModuleType) -> List[str]:
    names = []
    functions = inspect.getmembers(module, lambda member: inspect.isfunction(member))
    for name, fn in functions:
        if fn.__module__ == module.__name__:
            names.append(name)
    return names


def _get_function_arg_names(module: ModuleType, fn_name: str) -> List[str]:
    arg_names = []
    functions = inspect.getmembers(module, lambda member: inspect.isfunction(member))
    for name, fn in functions:
        if fn.__module__ == module.__name__:
            if fn.__qualname__ == fn_name:
                args_spec = inspect.getfullargspec(fn)
                arg_names = args_spec.args
                if args_spec.varargs is not None:
                    arg_names.extend(args_spec.varargs)
                if args_spec.varkw is not None:
                    arg_names.extend(args_spec.varkw)
                arg_names.extend(args_spec.kwonlyargs)
                break
    return arg_names


def _get_class_names(module: ModuleType) -> List[str]:
    names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for name, cls in classes:
        if cls.__module__ == module.__name__:
            names.append(name)
    return names


def _get_class_function_names(module: ModuleType, cls_name: str) -> List[str]:
    fn_names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for cls_name_, cls in classes:
        if cls.__module__ == module.__name__:
            if cls_name_ == cls_name:
                functions = inspect.getmembers(
                    cls,
                    lambda member: inspect.ismethod(member)
                    or inspect.isfunction(member),
                )
                for fn_name, fn in functions:
                    fn_names.append(fn.__qualname__)
                break
    return fn_names


def _get_class_function_arg_names(
    module: ModuleType, cls_name: str, fn_name: str
) -> List[str]:
    arg_names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for cls_name_, cls in classes:
        if cls.__module__ == module.__name__:
            if cls_name_ == cls_name:
                functions = inspect.getmembers(
                    cls,
                    lambda member: inspect.ismethod(member)
                    or inspect.isfunction(member),
                )
                for fn_name_, fn in functions:
                    if fn.__qualname__ == fn_name:
                        args_spec = inspect.getfullargspec(fn)
                        arg_names = args_spec.args
                        if args_spec.varargs is not None:
                            arg_names.extend(args_spec.varargs)
                        if args_spec.varkw is not None:
                            arg_names.extend(args_spec.varkw)
                        arg_names.extend(args_spec.kwonlyargs)
                        break
                break
    return arg_names
