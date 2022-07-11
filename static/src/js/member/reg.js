;
const member_reg_ops = {
  init: function () {
    this.eventBind();
  },
  eventBind: function () {
    $(".reg-wrap .do-reg").click(function () {
      const btn_target = $(this)
      if (btn_target.hasClass('disabled')) {
        common_ops.alert('正在处理中，请不要重复点击')
        return false;
      }

      const login_name = $(".reg-wrap input[name='login_name']").val();
      const nick_name = $(".reg-wrap input[name='nick_name']").val();
      const login_pwd = $(".reg-wrap input[name='login_pwd']").val();
      const login_pwd2 = $(".reg-wrap input[name='login_pwd2']").val();

      if (!login_name || login_name.length < 2) {
        common_ops.alert('请输入正确的用户名，长度不能小于2位')
        return false
      }
      if (!login_pwd || login_pwd.length < 6) {
        common_ops.alert('请输入正确的密码，长度不能小于6位')
        return false
      }
      if (!login_pwd2 || login_pwd2.length < 6) {
        common_ops.alert('请输入正确的确认密码，长度不能小于6位')
        return false
      }
      if (login_pwd !== login_pwd2) {
        common_ops.alert('两次输入的密码不一致，请重新输入')
        return false
      }

      btn_target.addClass('disabled')

      // 发出请求
      $.ajax({
        url: common_ops.buildUrl('/register'),
        type: 'post',
        data: {
          login_name,
          login_pwd,
          nick_name,
        },
        dataType: 'json',
        success: function (res) {
          console.log('success:', res);
          btn_target.removeClass('disabled');
          common_ops.alert(res.msg, () => {
            window.location.href = common_ops.buildUrl('/');
          })
        },
        error: function (err) {
          console.log('err:', err);
          btn_target.removeClass('disabled');
          common_ops.alert(err.responseJSON.msg);
        }
      })
    })
  }
};

$(document).ready(() => {
  member_reg_ops.init();
});
