var tblCliente;
var modal_title;

function getdata() {
    tblCliente = $('#data').DataTable({
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
            { "data": "name" },
            { "data": "correo" },
            { "data": "telefono" },
            { "data": "Ruc" },
            { "data": "direccion" },
            { "data": "opciones" },
        ],
        columnDefs: [
            {
                targets: [-1],
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
$(function () {

    modal_title = $('.modal-title');

    getdata();

    $('.btnAdd')
        .on('click', function () {
            $('input[name="action"]').val('add');
            modal_title.find('span').html('Creación de un cliente');
            console.log(modal_title.find('i'));
            modal_title.find('i').removeClass().addClass('fas fa-plus');
            $('form')[0].reset();
            $('#myModalCliente').modal('show');
        });


    $('#data tbody')
    
        .on('click', 'a[rel="edit"]', function () {
            modal_title.find('span').html('Edición de un cliente');
            modal_title.find('i').removeClass().addClass('fas fa-edit');
            var tr = tblCliente.cell($(this).closest('td, li')).index();
            var data = tblCliente.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="id"]').val(data.id);
            $('input[name="name"]').val(data.name);
            $('input[name="correo"]').val(data.correo);
            $('input[name="telefono"]').val(data.telefono);
            $('input[name="Ruc"]').val(data.Ruc);
            $('input[name="direccion"]').val(data.direccion);
            $('#myModalCliente').modal('show');
        })

        .on('click', 'a[rel="delete"]', function () {
            var tr = tblCliente.cell($(this).closest('td, li')).index();
            var data = tblCliente.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id', data.id);
            submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar eliminar el siguiente registro?', parameters, function () {
                tblCliente.ajax.reload();
            });
        });

    

   
    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            $('#myModalCliente').modal('hide');
            tblCliente.ajax.reload();
        });
    });

});

