var tblSale;
var modal_title;
$(function () {
    modal_title = $('.modal-title');
    tblSale = $('#data').DataTable({
        scrollX: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            { "data": "id" },
            { "data": "sale.cli.name" },
            { "data": "date_joined" },
            { "data": "sale.id" },
            { "data": "price" },
            { "data": "opciones" },
        ],
        columnDefs: [
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return 'Gs ' + parseFloat(data).toLocaleString("es-AR");

                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    
                        var buttons ='<a href="/erp/sale/invoiceCredito/pdf/' + row.id + '/" target="_blank" class="btn btn-info btn-xs btn-flat"><i class="fas fa-file-pdf"></i></a> '; 
                        buttons += '<a rel="delete" class="btn btn-danger btn-xs btn-flat"> <i class="fas fa-trash"></i></a> ';
                        return buttons;
                    
                }
            },
        ],
        
        initComplete: function (settings, json) {

        }
    });
    $('#data tbody').on('click', 'a[rel="delete"]', function () {
            
        var tr = tblSale.cell($(this).closest('td, li')).index();
        var data = tblSale.row(tr.row).data();
        var parameters = new FormData();
        parameters.append('action', 'delete');
        parameters.append('id', data.id);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar eliminar el siguiente registro?', parameters, function () {
            tblSale.ajax.reload();
        });
        $('#myModelDets').modal('show'); 

    })
});