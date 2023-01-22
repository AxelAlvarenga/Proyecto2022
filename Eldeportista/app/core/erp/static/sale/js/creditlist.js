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
                    
                        var buttons ='<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-search"></i></a> ';
                        buttons += '<a href="/erp/sale/invoiceCredito/pdf/' + row.id + '/" target="_blank" class="btn btn-info btn-xs btn-flat"><i class="fas fa-file-pdf"></i></a> ';
                        return buttons;
                    
                }
            },
        ],
        
        initComplete: function (settings, json) {

        }
    });
});