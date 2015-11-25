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
  var form = $('form.js-record-own-message');
  var select = $('select[name=audio_url]');
  var recording = $('input[name=recording]');

  var reset = function() {
    form.find('.js-call').button('reset');
    form.find('.js-cancel').show();
    form.find('.help-block').remove();
    form.find('.form-group').removeClass('has-error');
  };

  select.on('change', function () {
    recording.val('');

    if ($(this).val() === '') {
      reset();
      form.find('.modal')
        .modal()
        .on('shown.bs.modal', function () {
          form.find('.form-control').eq(0).focus()
        })
        ;
    }
  });

  form.on('submit', function (e) {
    e.preventDefault();

    reset();
    form.find('.js-call').button('loading');
    form.find('.js-cancel').hide();

    $.post(form.attr('action'), form.serialize(), function (data) {
      switch (data['status']) {

      // Our request to call has been submitted
      case 'ok':
        var poll = function() {
          $.ajax({
              url: data['result']['create_request']['xhr-poll-url'],
              type: 'POST',
              success: function(data) {
                // Unknown error
                if (data['status'] != 'ok') {
                  setTimeout(poll, 2000);
                  return;
                }

                var recording_id = data['result']['create_request']['recording_id'];

                // We need to keep polling
                if (recording_id === null) {
                  setTimeout(poll, 1000);
                  return;
                }

                // The call was completed
                form.find('.modal').modal('hide');

                // Save the recording_id in the "parent" form
                recording.val(recording_id);

                // Update the UI so that .change() fires again
                select
                  .find('option')
                  .hide()
                  .filter('[data-show-on-custom-recording]')
                  .show()
                  .eq(-2)
                    .prop('selected', true)
                  ;
              },
              error: function() {
                setTimeout(poll, 2000);
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
        reset();
        $.each(data['errors'], function (name, errors) {
          $.each(errors, function (_, error) {
            form.find('.form-control[name=' + name + ']')
              .closest('.form-group')
              .addClass('has-error')
              .append($('<p class="help-block"></p>').text(error))
              ;
            });
        });
        break;

      }
    }).fail(function() {
      reset();
    });
  });
});
