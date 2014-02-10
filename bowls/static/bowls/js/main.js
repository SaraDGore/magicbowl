$(function() {
  $('#use').on('click', function(event) {
        event.preventDefault(); // To prevent following the link (optional)
        $('#ingredient-list').removeClass('hidden');
        $('#ingredient-list').addClass('show');
        
        fields = $('#ingredient-list').find("input[name^='dontuse']");
        fields.attr('name', 'use');
        
        if ($('#use-label').hasClass('hidden')) {
            $('#use-label').removeClass('hidden');
            $('#use-label').addClass('show');
        };
        if ($('#dontuse-label').hasClass('show')) {
            $('#dontuse-label').removeClass('show');
            $('#dontuse-label').addClass('hidden');
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
        $('#ingredient-list').removeClass('hidden');
        $('#ingredient-list').addClass('show');
        
        fields = $('#ingredient-list').find("input[name^='use']");
        fields.attr('name', 'dontuse');
        
        if ($('#dontuse-label').hasClass('hidden')) {
            $('#dontuse-label').removeClass('hidden');
            $('#dontuse-label').addClass('show');
        };
        if ($('#use-label').hasClass('show')) {
            $('#use-label').removeClass('show');
            $('#use-label').addClass('hidden');
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


