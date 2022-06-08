### 模块目录

存放数据库的表定义model

### 自动生成模块

```shell
flask-sqlacodegen "mysql://yangfei:Yf111111@127.0.0.1:3306/movie" --tables user --outfile "model/user.py" --flask
```

> 提示：
> - 执行脚本之前，需要先创建好数据库中的表（可以是空表）;
> - 数据库用户的密码不能包含特殊符号@，否则无法执行命令（无法解析数据库连接字符串）;
> - 执行完成后，替换一下生成文件里的 db 变量来源。
