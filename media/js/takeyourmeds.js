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
  var modal = $('#modal-record-own-message');
  var recording = $('input[name=recording]');

  var reset = function() {
    modal.find('.js-call').button('reset');
    modal.find('.js-cancel').show();
    modal.find('.help-block').remove();
    modal.find('.form-group').removeClass('has-error');
  };

  $('select[name=audio_url]').on('change', function () {
    recording.val('');

    if ($(this).val() === '') {
      reset();
      modal.modal();
    }
  });

  modal.find('.js-call').on('click', function () {
    var form = modal.find('form');
    var button = $(this);

    reset();
    button.button('loading');
    modal.find('.js-cancel').hide();

    $.post(form.attr('action'), form.serialize(), function (data) {
      switch (data.status) {

      // Our request to call has been submitted
      case 'success':
        var poll = function() {
          $.ajax({
              url: data.url,
              type: 'POST',
              success: function(data) {
                switch (data.status) {

                // The call was completed
                case 'success':
                  modal.modal('hide');

                  // Save the recording_id in the "parent" form
                  recording.val(data.recording_id);
                  break;

                // We need to keep polling
                case 'continue':
                  setTimeout(poll, 1000);
                  break;
                }
              },
              dataType: 'json',
              timeout: 2000
          });
        };

        // No need to start polling for a while, which also helps to test the
        // UI when settings.TWILIO_ENABLED = False.
        setTimeout(poll, 2000);
        break;

      // Validation errors
      case 'error':
        var form_group = modal.find('.js-form-group');

        reset();

        form_group.addClass('has-error');

        $.each(data.errors, function (idx, error) {
          $('<p class="help-block"></p>')
            .text(error)
            .appendTo(form_group)
            ;
        });
        break;

      }
    }).fail(function() {
      reset();
    });
  });
});
