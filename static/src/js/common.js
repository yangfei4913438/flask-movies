;
var common_ops = {
  buildUrl: function (path, params) {
    var url = "" + path;
    var _params_url = "";
    if (params) {
      _params_url = Object.entries(params).map(function ([k, v], index) {
        return [encodeURIComponent(k), encodeURIComponent(v)].join('=')
      }).join('&')
      _params_url = '?' + _params_url;
    }

    return url + _params_url;
  },
  alert: function (msg, cb) {
    layer.alert(msg, {
      yes: function (index) {
        if (typeof cb === 'function') {
          cb();
        }
        layer.close(index);
      }
    })
  }
}