$(function() {
    $('.edit-description').on('click', function(e) {
        $(this).parent().find('input').prop('disabled', false);
        $(this).toggleClass('active disactive');
        $(this).next('span').toggleClass('active disactive');
    });
    $('.edited-description').on('click', function(e) {
        let target = $(this);
        let input = target.parent().find('input');
        $.ajax({
            type: "POST",
            url: "/api/routes/" + input.data('id'),
            data: "description=" + input.val(),
            success: function(data) {
                target.parent().find('input').prop('disabled', true);
                target.toggleClass('active disactive');
                target.prev('span').toggleClass('active disactive');
            },
            error: function(data) {
                console.info(data)
            }
        });
    });
    $('input').keypress(function(e) {
        if (e.which == 13) {
            $(this).parent().find('.edited-description').click();
        }
    });
});