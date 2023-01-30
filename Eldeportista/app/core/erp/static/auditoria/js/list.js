$(function (){
    $('#data').DataTable( {
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action':'searchdata'
                },
                dataSrc: ""
            },
            order: [[0, 'desc']],
            columns: [
                { "data": "codigo_auditoria"},
                { "data": "tabla"},
                { "data": "action"},
                { "data": "datos_viejos"},
                { "data": "datos_nuevos"},
                { "data": "usuario"},
                { "data": "fecha"},
               
               
                
            ],
            columnDefs: [
                {
                    targets: [2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        if(row.accion == 'I'){
                            return 'Creacion';
                        }
                        if(row.accion == 'D'){
                            return 'Eliminacion';
                        }
                        return 'Actualizacion';
                        
                    }
                },
            ],
            initComplete: function(settings, json) {
            
            }
            });
        
    });