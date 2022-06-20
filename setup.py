from setuptools import setup


# 必要な依存ライブラリ
install_requires = [
]

# 含めるパッケージ
packages = [
    'chinolab',
    'chinolab.vlp',
    'chinolab.figure',
]

# CLIコマンドにしたいもの
console_scripts = [
]

setup(
    name='chinolab',
    version='0.0.4',
    packages=packages,
    install_requires=install_requires,
    entry_points={'console_scripts': console_scripts}
)
