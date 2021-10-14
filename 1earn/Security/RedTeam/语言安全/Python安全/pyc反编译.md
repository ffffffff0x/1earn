# pyc反编译

---

**相关工具**
- [python反编译](https://tool.lu/pyc)
- [rocky/python-uncompyle6](https://github.com/rocky/python-uncompyle6)
    ```bash
    # 例如有一个 test.pyc，想反编译输出文件为 test.py
    uncompyle6 -o test.py test.pyc
    ```
- [extremecoders-re/pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor) - 反编译 pyinstaller 生成的 exe
    ```bash
    python pyinstxtractor.py test.exe
    ```
