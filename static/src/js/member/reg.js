;
const member_reg_ops = {
  init: function () {
    this.eventBind();
  },
  eventBind: function () {
    $(".reg-wrap .do-reg").click(function () {
      const login_name = $(".reg-wrap input[name='login_name']").val();
      const login_pwd = $(".reg-wrap input[name='login_pwd']").val();
      const login_pwd2 = $(".reg-wrap input[name='login_pwd2']").val();
      console.log('login_name:', login_name)
      console.log('login_pwd:', login_pwd)
      console.log('login_pwd2:', login_pwd2)
    })
  }
};

$(document).ready(() => {
  member_reg_ops.init();
});
