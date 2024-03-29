var tblproducto;
var modal_title;

function getdata(){ 
    tblproducto = $('#data').DataTable({
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
            { "data": "id" },
            { "data": "name" },
            { "data": "talla.talla" },
            { "data": "price" },
            { "data": "price_buy" },
            { "data": "cat.name_cat" },
            { "data": "cantidad" },
            { "data": "cantidad" },


            
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
            {
                targets: [6],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if(data>0){
                        return '<span class="badge badge-success">'+data+'</span>'
                    }
                    return '<span class="badge badge-danger">'+data+'</span>'
                }
            },
            {
                targets: [3,4],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return 'Gs ' + parseFloat(data).toLocaleString("es-AR");

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
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });
    $('.btnAdd').on('click', function () {
        $('input[name="action"]').val('add');
        modal_title.find('span').html('Creación de un producto');
        console.log(modal_title.find('i'));
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        // $('select[name="cat"]').on('change', function () {
        //     var id = $(this).val();
        //     var select_products = $('select[name="talla"]');
        //     var options = '<option value="">--------------------</option>';
        //     if(id === ''){
        //         select_products.html(options);
        //         return false;
        //     }
        //     $.ajax({
        //         url: window.location.pathname,
        //         type: 'POST',
        //         data: {
        //             'action': 'add',
        //             'id': id
        //         },
        //         dataType: 'json',
        //     }).done(function (data) {
        //         console.log(data)
        //         if (!data.hasOwnProperty('error')) {
        //             $.each(data, function (key, value) {
        //                 options+='<option value="'+value.id+'">'+value.talla+'</option>';
        //             });
        //             return false;
        //         }
        //         message_error(data.error);
        //     }).fail(function (jqXHR, textStatus, errorThrown) {
        //         alert(textStatus + ': ' + errorThrown);
        //     }).always(function (data) {
        //         select_products.html(options);
        //     });
        // });
        $('form')[0].reset();
        $('#myModalProduct').modal('show');
    });

    
    


    $('#data tbody')
    
        .on('click', 'a[rel="edit"]', function () {
            modal_title.find('span').html('Edición de un producto');
            modal_title.find('i').removeClass().addClass('fas fa-edit');
            var tr = tblproducto.cell($(this).closest('td, li')).index();
            var data = tblproducto.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="id"]').val(data.id);
            $('input[name="name"]').val(data.name);
            $('input[name="talla"]').val(data.talla.id);
            document.getElementById('id_talla').value = data.talla.id  
            $('input[name="price"]').val(data.price);
            $('input[name="price_buy"]').val(data.price_buy);
            $('input[name="cat"]').val(data.cat.id);
            document.getElementById('id_cat').value = data.cat.id 
            $('input[name="cantidad"]').val(data.cantidad);
            $('#myModalProduct').modal('show');
        })

        .on('click', 'a[rel="delete"]', function () {
            var tr = tblproducto.cell($(this).closest('td, li')).index();
            var data = tblproducto.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id', data.id);
            submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar eliminar el siguiente registro?', parameters, function () {
                tblproducto.ajax.reload();
            });
        });

    
    
   
    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            $('#myModalProduct').modal('hide');
            tblproducto.ajax.reload();
        });
    });
    // $('#formrproduct').on('submit', function (e) {
    //     e.preventDefault();
    //     var parameters = $(this).serializeArray();
    //     alert_jqueryconfirm(window.location.pathname, parameters, function () {
    //         $('#myModalProduct').modal('hide');
    //         tblProduct.ajax.reload();
    //     });
    // });

});
// var select_cat = $('select[name="cat"]');
//         $(function () {

//             $('.select2').select2({
//                 theme: "bootstrap4",
//                 language: 'es'
//             });

//             $('select[name="cat"]').on('change', function () {
//                 var id = $(this).val();
//                 var options = '<option value="">--------------------</option>';
//                 if (id === '') {
//                     select_cat.html(options);
//                     return false;
//                 }
        
//                 $.ajax({
//                     url: window.location.pathname,
//                     type: 'POST',
//                     data: {
//                         'action': 'search_cat_id',
//                         'id': id
//                     },
//                     dataType: 'json',
//                 }).done(function (data) {
//                     if (!data.hasOwnProperty('error')) {
//                         select_cat.html('').select2({
//                             theme: "bootstrap4",
//                             language: 'es',
//                             data: data
//                         });
//                         /*$.each(data, function (key, value) {
//                             options += '<option value="' + value.id + '">' + value.name + '</option>';
//                         });*/
//                         return false;
//                     }
//                     message_error(data.error);
//                 }).fail(function (jqXHR, textStatus, errorThrown) {
//                     alert(textStatus + ': ' + errorThrown);
//                 }).always(function (data) {
//                     //select_products.html(options);
//                 });
//             });

//             select_cat.on('change', function () {
//                 var value = select_cat.select2('data')[0];
//                 console.log(value);
//             });

            
//         });

