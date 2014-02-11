$(function() {
  // TODO: make it DRYer.
  // TODO: learn JS
  $('#use').on('click', function(event) {
        event.preventDefault(); 
        
        fields = $('#ingredient-list').find("input[name^='dontuse']");
        fields.attr('name', 'use');
        
        $('#ingredient-list').toggleClass('hidden', false);
        $('#use-label').toggleClass('hidden', false);
        $('#dontuse-label').toggleClass('hidden', true)       
        $('#cuisine-form').toggleClass('hidden', false);
        $('#submitbutton').toggleClass('hidden', false);
  });
    
   $('#dontuse').on('click', function(event) {
        event.preventDefault(); 
        
        fields = $('#ingredient-list').find("input[name^='use']");
        fields.attr('name', 'dontuse');
        
        $('#ingredient-list').toggleClass('hidden', false);
        $('#use-label').toggleClass('hidden', true);
        $('#dontuse-label').toggleClass('hidden', false)       
        $('#cuisine-form').toggleClass('hidden', false);
        $('#submitbutton').toggleClass('hidden', false);
  });
 });

