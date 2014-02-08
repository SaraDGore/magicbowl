$(function() {
  $('#use').on('click', function(event) {
    event.preventDefault(); // To prevent following the link (optional)
    $('#use-form').removeClass('hidden');
    $('#use-form').addClass('show');
    if ($('#dontuse-form').hasClass('show')) {
        $('#dontuse-form').removeClass('show');
        $('#dontuse-form').addClass('hidden');
    };
    if ($('#cuisine-form').hasClass('hidden')) {
        $('#cuisine-form').removeClass('hidden');
        $('#cuisine-form').addClass('show');
    };
    if ($('#submitbutton').hasClass('hidden')) {
        $('#submitbutton').removeClass('hidden');
        $('#submitbutton').addClass('show');
    };
  });
    
  $('#dontuse').on('click', function(event) {
    event.preventDefault(); // To prevent following the link (optional)
    $('#dontuse-form').removeClass('hidden');
    $('#dontuse-form').addClass('show');
    if ($('#use-form').hasClass('show')) {
        $('#use-form').removeClass('show');
        $('#use-form').addClass('hidden');
    };
    if ($('#cuisine-form').hasClass('hidden')) {
        $('#cuisine-form').removeClass('hidden');
        $('#cuisine-form').addClass('show');
    };
    if ($('#submitbutton').hasClass('hidden')) {
        $('#submitbutton').removeClass('hidden');
        $('#submitbutton').addClass('show');
    };
   });
 });


