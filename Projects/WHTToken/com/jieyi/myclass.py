# -*- coding: utf-8 -*-
"""
模块的说明文档 module docstring
- 放置在在模块的import之前
- 成对的三个双引号包裹
- 可以提供模块的简要信息，如：
    @file: filename
    @author:yourname
    @date:2017-xx-xx
    @version: 1.0.0.0
    @description:
     - your description
- 使用者可以通过  moduleName.__doc__ 来获取此区域内容，示例中，即myclass.__doc
"""
# import numpy as np

class MyClass:
    """
    类的文档说明class doc
    - 紧随放置在类的声明之后
    - 成对的三个双引号包裹
    - 可以提供模块的简要信息
    - 使用者可以通过class的实例名.__doc__来访问该区域内容
    """
    def __init__(self):
        print("initial MyClass")

    def func1(self):
        print("I am public function1")


if __name__ == "__mian__":
     print("test module")