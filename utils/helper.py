from flask import g, jsonify, render_template


def ops_render_json(code=200, msg='操作成功', data={}):
    resp = {"code": code, "msg": msg, "data": data}

    return jsonify(resp)


def ops_render_err_json(msg="系统繁忙，请稍后再试～", data={}):
    return ops_render_json(code=-1, msg=msg, data=data)


# 渲染模板的时候，统一添加用户信息
def auth_render(template, **context):
    # 后台登陆后会添加全局变量 g.current_user
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template, **context)
