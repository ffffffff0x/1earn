# miniforge

- https://github.com/conda-forge/miniforge

---

**安装 miniforge**
```bash
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh
mv Miniforge3-MacOSX-arm64.sh ~/
cd
bash Miniforge3-MacOSX-arm64.sh
```

```bash
source .zshrc
conda --version     # 测试一下conda是否安装完成
```

**创建一个 Conda 虚拟环境**
```bash
# 用Python 3.9创建一个名为 f0x 的虚拟环境
conda create -n f0x python=3.9

# 查看所有环境
conda info --envs

# 激活虚拟环境
conda activate f0x

# 安装库
conda install jupyter
```

**配置镜像源**
```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes
conda update --all
```
