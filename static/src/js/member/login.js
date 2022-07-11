;
const member_login_ops = {
  init: function () {
    this.eventBind();
  },
  eventBind: function () {
    $(".login-wrap .do-login").click(function () {
      const btn_target = $(this)
      if (btn_target.hasClass('disabled')) {
        common_ops.alert('正在处理中，请不要重复点击')
        return false;
      }

      const login_name = $(".login-wrap input[name='login_name']").val();
      const login_pwd = $(".login-wrap input[name='login_pwd']").val();

      if (!login_name || login_name.length < 2) {
        common_ops.alert('请输入正确的用户名，长度不能小于2位')
        return false
      }
      if (!login_pwd || login_pwd.length < 6) {
        common_ops.alert('请输入正确的密码，长度不能小于6位')
        return false
      }

      btn_target.addClass('disabled')

      // 发出请求
      $.ajax({
        url: common_ops.buildUrl('/login'),
        type: 'post',
        data: {
          login_name,
          login_pwd,
        },
        dataType: 'json',
        success: function (res) {
          console.log('success:', res);
          btn_target.removeClass('disabled');
          common_ops.alert(res.msg, function () {
            window.location.href = common_ops.buildUrl('/');
          })
        },
        error: function (err) {
          console.log('err:', err.responseJSON.msg);
          common_ops.alert(err.responseJSON.msg, () => {
            btn_target.removeClass('disabled');
          });
        }
      })
    })
  }
};

$(document).ready(() => {
  member_login_ops.init();
});
