$(function() {
    $('form#form_routes').submit(function() {
        $.map($('input#is_enabled[data-is-enabled="false"]:checked'), function(value) {
            $('<input/>', {
                name: 'actived[]',
                type: 'hidden',
                value: $(value).data('id')
            }).appendTo('#form_routes');
        });
        $.map($('input#is_enabled[data-is-enabled="true"]:not(:checked)'), function(value) {
        	$('<input/>', {
                name: 'disabled[]',
                type: 'hidden',
                value: $(value).data('id')
            }).appendTo('#form_routes');
        });
    });
})