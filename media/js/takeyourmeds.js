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
  var elem = $('select[name=frequency]');

  var update = function() {
    var val = parseInt(elem.val(), 10);

    $('[data-time_field]').each(function() {
      var x = parseInt($(this).data('time_field'), 10);

      $(this).toggleClass('hide', val < x);
    });
  };

  elem.on('change', update);
  update();
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

$.feature('f_reminders_create', function() {
  var wrapper = $('.js-record-request');

  var update = function() {
    var val = $('select[name=audio_url]').val();

    wrapper
      .toggleClass('hide', val !== '')
      .removeClass('has-error')
      .find('button')
        .button('reset')
      .end()
      .find('.help-block')
        .remove()
      .end()
      ;
  };

  $('select[name=audio_url]').on('change', update);

  // Pageload
  update();

  wrapper.find('button').on('click', function () {
    var button = $(this);

    button.button('loading');

    wrapper
      .find('.help-block')
        .remove()
      .end()
      ;

    wrapper.removeClass('has-error');

    var phone_number = wrapper
      .find('.js-record-request-phone-number')
      .val()
      ;

    $.post($(this).data('url'), {
      'phone_number': phone_number
    }, function (data) {
      switch (data.status) {
      case 'success':
        (function poll() {
          $.ajax({
              url: data.url,
              type: 'POST',
              success: function(data) {
                switch (data.status) {
                case 'success':
                  break;
                case 'continue':
                  setTimeout(function() {
                    poll();
                  }, 1000);
                  break;
                }
              },
              dataType: 'json',
              timeout: 2000
          });
        })();
        break;

      case 'error':
        wrapper.addClass('has-error');

        $.each(data.errors, function (field, errors) {
          $.each(errors, function (idx, error) {
            $('<p class="help-block"></p>')
              .text(error.message)
              .insertBefore(button)
              ;
          });
        });

        button.button('reset');
        break;
      }
    }).fail(function() {
      button.button('reset');
    });
  });
});
