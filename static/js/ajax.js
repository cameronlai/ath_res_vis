 var ajax_response = function() {
   var school_choice = $("#id_school_choice").val();
   var sex_choice = $("#id_sex_choice").val();
   var event_choice = $("#id_event_choice").val();

   $.ajax({
     url: '/ath_res_vis/ajax/get_info/',
     data: {
       'school_choice': school_choice,
       'sex_choice': sex_choice,
       'event_choice': event_choice,
     },
     dataType: 'json',
     success: function (data) {
       $('#id_name_choice').empty();
       name_list = $.parseJSON(data['name_list']);
       $.each(name_list, function(i, item) {
	 $('#id_name_choice').append($('<option></option>').val(item).html(item));
       });

       $('#id_sex_choice').empty();
       sex_list = $.parseJSON(data['sex_list']);
       $.each(sex_list, function(i, item) {
	 $('#id_sex_choice').append($('<option></option>').val(item).html(item)); 
       });
       if (sex_choice && $.inArray(sex_choice, sex_list) >= 0) {
	 $("#id_sex_choice").val(sex_choice);
       }
       
       $('#id_event_choice').empty();
       event_list = $.parseJSON(data['event_list']);
       $.each(event_list, function(i, item) {
	 $('#id_event_choice').append($('<option></option>').val(item).html(item)); 
       });
       if (event_choice && $.inArray(event_choice, event_list) >= 0) {
	       $("#id_event_choice").val(event_choice);
	     }
     }
   })
 }

$("#id_school_choice").change(function () {
  ajax_response();
})
$("#id_sex_choice").change(function () {
  ajax_response();
})
$("#id_event_choice").change(function () {
  ajax_response();
})