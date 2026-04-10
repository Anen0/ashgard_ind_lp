var crud_form_add   = document.getElementById('crud_form_add');
var s_string        = document.getElementById('s_string');
var s_int           = document.getElementById('s_int');
var s_txt           = document.getElementById('s_txt');


// ADD data
crud_form_add.addEventListener('submit', function(e){
    e.preventDefault();
    console.log(s_string.value);
    console.log(s_int.value);
    console.log(s_txt.value);
    
    $.post('/dashboard', { s_string : s_string.value, s_int : s_int.value, s_txt : s_txt.value }, function(e){
        console.log(e);        
        reloadDT_CRUD();

        //Call NOTIFICATION JS with a slight delay
        setTimeout(notify('ADDED TO DB', 'success'), 1000);
        
    });
});



// Non serverside
// var table = $('#dt-server-processing').DataTable({
//     processing: true,
//     // serverSide: true,
//     responsive: true,
//     ajax:{
//         url     :  Flask.url_for('main.crud_view'),
//         type    : 'GET',
//         dataSrc : ''
//     },
//     columns: [
//         { "data": "ct_id" },
//         { "data": "some_string" },
//         { "data": "some_text" },
//         { "data": "some_int" },
//         { "data": "dtg" },
//     ]
// });





// Server side processing Data-table
var table = $('#dt-server-processing').DataTable({
    bProcessing: true,
    bServerSide: true,
    sServerMethod: 'GET',
    sAjaxSource: Flask.url_for('main.crud_view'),
    columns:[
        { "data": "ct_id" },
        { "data": "some_string" },
        { "data": "some_text" },
        { "data": "some_int" },
        { "data": "dtg" },
    ],
});



function reloadDT_CRUD(){
    // Clear input data
    s_string.value  = '';
    s_int.value     = '';
    s_txt.value     = '';

    // Reload the table
    setTimeout('table.ajax.reload();', 900);

    // Hide the modal
    $('#post-Modal').modal('hide');    
}

