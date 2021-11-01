# pyc反编译

---

**相关文章**
- [py可执行文件反编译教程--exe转换py](https://blog.csdn.net/m0_37552052/article/details/88093427)
- [Python代码保护 | pyc 混淆从入门到工具实现](https://zhuanlan.zhihu.com/p/145811103)

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

    如果转换格式错误,可以手动修复,在该文件起始位置加上8个字节的pyc头即可
    ```
    03 F3 0D 0A 00 00 00 00
    ```
