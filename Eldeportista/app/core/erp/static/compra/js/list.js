var tblSale;

$(function () {

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
            {"data": "id"},
            {"data": "comprobante"},
            {"data": "prov.nombre"},
            {"data": "date_joined"},
            {"data": "subtotal"},
            {"data": "iva"},
            {"data": "total"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-2, -3, -4],
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
                    var buttons = '<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-search"></i></a> ';
                        buttons += '<a rel="delete" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });

    $('#data tbody')
        .on('click', 'a[rel="details"]', function () {
            var tr = tblSale.cell($(this).closest('td, li')).index();
            var data = tblSale.row(tr.row).data();
            console.log(data);

            $('#tblDet').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                deferRender: true,
                //data: data.det,
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_details_prod',
                        'id': data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    {"data": "prod.name"},
                    {"data": "prod.cat.name_cat"},
                    {"data": "price"},
                    {"data": "cant"},
                    {"data": "subtotal"},
                ],
                columnDefs: [
                    {
                        targets: [-1, -3],
                        class: 'text-center',
                        render: function (data, type, row) {
                            return 'Gs ' + parseFloat(data).toLocaleString("es-AR");
        
                        }
                    },
                    {
                        targets: [-2],
                        class: 'text-center',
                        render: function (data, type, row) {
                            return data;
                        }
                    },
                ],
                initComplete: function (settings, json) {

                }
            });

            $('#myModelDet').modal('show');
        }).on('click', 'a[rel="delete"]', function () {
            var tr = tblSale.cell($(this).closest('td, li')).index();
            var data = tblSale.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id', data.id);
            submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar eliminar el siguiente registro?', parameters, function () {
                tblSale.ajax.reload();
            });
        })
});