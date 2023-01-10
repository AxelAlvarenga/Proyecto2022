var tblProveedor;
var modal_title;

function getdata() {
    tblProveedor = $('#data').DataTable({
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
            { "data": "nombre" },
            { "data": "ruc" },
            { "data": "telefono" },
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
            modal_title.find('span').html('Creación de un proveedor');
            console.log(modal_title.find('i'));
            modal_title.find('i').removeClass().addClass('fas fa-plus');
            $('form')[0].reset();
            $('#myModalProveedor').modal('show');
        });


    $('#data tbody')
    
        .on('click', 'a[rel="edit"]', function () {
            modal_title.find('span').html('Edición de un proveedor');
            modal_title.find('i').removeClass().addClass('fas fa-edit');
            var tr = tblProveedor.cell($(this).closest('td, li')).index();
            var data = tblProveedor.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="id"]').val(data.id);
            $('input[name="nombre"]').val(data.nombre);
            $('input[name="ruc"]').val(data.ruc);
            $('input[name="telefono"]').val(data.telefono);
            $('input[name="direccion"]').val(data.direccion);
            $('#myModalProveedor').modal('show');
        })

        .on('click', 'a[rel="delete"]', function () {
            var tr = tblProveedor.cell($(this).closest('td, li')).index();
            var data = tblProveedor.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id', data.id);
            submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar eliminar el siguiente registro?', parameters, function () {
                tblProveedor.ajax.reload();
            });
        });

    

   
    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            $('#myModalProveedor').modal('hide');
            tblProveedor.ajax.reload();
        });
    });

});