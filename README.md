## 项目说明

#### 开发环境依赖

- python 3.10
- pipenv

#### 启动项目

> 需要在项目的根目录下执行

- 安装 python 依赖包

```pipenv install```

- 启动项目（声明一下运行模式）

```MODE=dev python start.py```

- 生产环境启动

```shell
# 测试参数（参数自己调整）
uwsgi --http 127.0.0.1:8080 --wsgi-file start.py --callable app --processes 4 --enable-threads

# 正式启动（调整好的参数，放到配置文件中）
uwsgi --ini uwsgi.ini
```

#### 补充命令

- 安装某个包

```shell
pipenv install python-dotenv
```

- 卸载某个包

```shell
pipenv uninstall python-dotenv
```