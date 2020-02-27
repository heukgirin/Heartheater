$(document).ready(function() {
  canvas = $(".input_attr");
  formset = "<span class='label'><input type='text' maxlength='5' /></span><span class='form'><input type='text' maxlength='20' /></span>";
  button_add = "<span class='input_button_s' action='add'><i class='fa fa-plus'></i></span>";
  button_del = "<span class='input_button_s' action='del'><i class='fa fa-minus'></i></span>";
  button_up = "<span class='input_button_s' action='up'><i class='fa fa-chevron-up'></i></span>";
  button_down = "<span class='input_button_s' action='down'><i class='fa fa-chevron-down'></i></span>";
  datPass();
});

function datPass() {
  $('.submit').click(function() {
    final = true;
    $('.basicset input').each(function(index, item) {
      if ($(item).val() == '') {
        final = false;
      }
    });

    if (final) {
      inform = "";
      $('.formset').each(function(index, item) {
        var title = $(item).find('.label input').val();
        var cont = $(item).find('.form input').val();
        inform += "{" + title + ":" + cont + "}";
      });
      alert(inform);
      $("#input_form input[name=inform]").val(inform);
      $('#input_form').submit();
    }
  });
}

$(document).on("click", ".input_button_s", function() {
  action = $(this).attr('action');
  line = $(this).parents('p');

  switch (action) {
    case 'add':
      $(canvas).append("<p class='formset'>" + formset + "</p>").trigger("create");
      break;
    case 'del':
      $(line).remove();
      break;
    case 'up':
      $(line).insertBefore($(line).prev('.formset'));
      break;
    case 'down':
      $(line).insertAfter($(line).next('.formset'));
      break;
  }
  $(".formset .input_button_s").remove();

  count = $(".formset").length - 1;

  for (var i = 0; i <= count; i++) {
    if (count == 0) {
      $(".formset:eq(" + i + ")").append(button_add);
    } else if (i == 0) {
      $(".formset:eq(" + i + ")").append(button_del + button_down);
    } else if (i == count) {
      $(".formset:eq(" + i + ")").append(button_add);
    } else if (i == (count - 1)) {
      $(".formset:eq(" + i + ")").append(button_del + button_up);
    } else {
      $(".formset:eq(" + i + ")").append(button_del + button_down + button_up);
    }
  }
});
