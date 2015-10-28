$.extend({
  feature: function(body_class, callback) {
    // calling $.feature('bclass', function () {}) means that the function will
    // only get called when your body tag has the correct class.
    if ($('body').hasClass(body_class)) {
      $(callback);
    }
  }
});

$(function() {
  var csrftoken = $.cookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
      }
    }
  });
});

$.feature('f_reminders_create', function() {
  var update = function() {
    var val = $('input[name=message_type]:checked').val();

    $('[data-message_type]').each(function() {
      $(this).toggleClass('hide', $(this).data('message_type') !== val);
    });
  };

  $('input[name=message_type]').on('change', update);

  // Pageload
  update();
});
