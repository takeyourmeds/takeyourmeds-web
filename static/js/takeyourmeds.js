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

$.feature('f_reminders_create', function() {
  var reminder_form = $('#reminder-setup');

  var schedule = {
    1: ["8:00"],
    2: ["8:00", "17:00"],
    3: ["8:00", "12:00", "17:00"],
    4: ["8:00", "11:00", "14:00", "17:00"]
  }

  // Capture form submit and send ajax
  // request with data

  reminder_form.submit(function(e) {
    e.preventDefault();

    var data = reminder_form.serializeArray();

    var telnumber = "";
    var message = "";
    var cronstring = "";
    var reminder_times = [];
    var audiourl = "";
    var dataobject = {};

    data.forEach(function(formField) {
      if (formField.name === "phone_number") {
        telnumber = formField.value;
      };
      if (formField.name === "message") {
        message = formField.value;
      };
      if (formField.name === "audio_url") {
        audiourl = formField.value;
      };
      if (formField.name.lastIndexOf("time", 0) === 0) {
        var hourDigits = formField.value.split(":")[0];
        var minDigits = formField.value.split(":")[1].substr(0,2);
      var cronstring = minDigits + " " + hourDigits + " * * *";
      reminder_times.push(cronstring);
      };
    });

    dataobject.telnumber = telnumber;
    dataobject.message = message;
    dataobject.reminder_times = reminder_times;
    dataobject.audiourl = audiourl;

    var jsonresult = JSON.stringify(dataobject);

    $.ajax(reminder_form.data('url'), {
      data : jsonresult,
      contentType : 'application/json',
      type : 'POST',
      success: function() {
        document.location = reminder_form.data('success-url');
        // // Show success message on success
        // var content_container = $('#content .container');
        // content_container.empty();
        // var success_template = $('.success-message');
        // success_template.appendTo(content_container);
        // success_template.show();
      }
    });
  });

  // Configure medication schedule based on frequency

  var frequency_selector = reminder_form.find('#frequency');
  var reminder_schedule_container = reminder_form.find('#reminder-schedule');
  var reminder_schedule_list = reminder_schedule_container.find('ol');

  frequency_selector.change(function() {
    var times = schedule[frequency_selector.val()];
    var template = $('#reminder_template').clone();

    reminder_schedule_list.empty()

    times.forEach(function(t, n){
      var time = template.clone().appendTo(reminder_schedule_list);
      var time_value = time.find("select");

      time_value.val(t);
      time_value.attr('name', 'time_' + String(n));
      time_value.attr('id', 'time_' + String(n));
    });

    reminder_schedule_container.show()
  });


  // Show the right message details option

  $('.radio-selector').each(function() {
    var el = $(this);
    el.click(function() {
      $('.message-type').each(function() {
        $(this).hide();
      });
      var element = $('#'+this.dataset.element);
      element.show();
    });
  });
});

$.feature('f_reminders_create', function() {
  $('.cron').each(function(i, el) {
    var cronstring = $(el).text();
    $(el).text(prettyCron.toString(cronstring))
  })
});
