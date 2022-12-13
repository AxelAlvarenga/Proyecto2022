var tblcat;
var modal_title;

function getdata(){ 
    tblcat = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            }, // parametros
            dataSrc: ""
        },
        columns: [
            { "data": "name_cat" },
        ],
        columnDefs: [
            {
                targets: [1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" rel="edit" class="btn btn-warning btn-xs btn-flat btnEdit"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="#" rel="delete" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
}

$(function(){

    modal_title = $('.modal-title');
    
    getdata();

    $('.btnAdd')
    .on('click', function () {
        $('input[name="action"]').val('add');
        modal_title.find('span').html('Creación de una categoria');
        console.log(modal_title.find('i'));
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset();
        $('#myModalCat').modal('show');
    })

    $('#data tbody')
    .on('click', 'a[rel="delete"]', function () {
        var tr = tblcat.cell($(this).closest('td, li')).index();
        var data = tblcat.row(tr.row).data();
        var parameters = new FormData();
        parameters.append('action', 'delete');
        parameters.append('id', data.id);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar eliminar el siguiente registro?', parameters, function () {
            tblcat.ajax.reload();
        });
    });

    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData();
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            $('#myModalCat').modal('hide');
            tblcat.ajax.reload();
        });
    });
});    