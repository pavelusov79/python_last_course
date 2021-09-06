$(function() {
    var loadForm = function() {
        var btn = $('.js-create-good');
        $.ajax({
            url: btn.attr('href'),
            type: 'GET',
            dataType: 'json',
            beforeSend: function() {
                $('#modal-good').modal('show');
            },
            success: function(data) {
                $('#modal-good .modal-content').html(data.html_form);
            }
        });
    };
    var saveForm = function() {
        var form = $('.js-good-create-form');
        $.ajax({
            url: form.attr('action'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function(data) {
                if(data.form_is_valid) {
                    $('.table tbody').html(data.html_goods_list);
                    $('#modal-good').modal('hide');

                }else {
                    $('#modal-good .modal-content').html(data.html_form);
                }
            }
        });
        return false;
    }
    $('.js-create-good').on('click', loadForm);
    $('#modal-good').on('submit', saveForm);
});