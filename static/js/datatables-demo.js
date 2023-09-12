

$(document).ready(function() {
  var table = $('#dataTable').DataTable();
  if (table != 'undefined' && table != null) {
    table.destroy();
  }
  $('#dataTable').DataTable({
    paging: false,
    searching: false
  });
});