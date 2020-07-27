jQuery(function($) {
    $('div.inline-group').sortable({
        /*containment: 'parent',
        zindex: 10, */
        items: 'div.inline-related',
        handle: 'h3:first',
        update: function() {
            $(this).find('div.inline-related').each(function(i) {
                let name = $(this).find('input[id$=name]');
                // If the found element has a name value or an accept property: 
                if ( name.val() || name.prop('accept') ) {
                    // Then update the ordering
                    $(this).find('input[id$=order]').val(i+1);
                }
            });
        }
    });
    $('div.inline-related h3').css('cursor', 'move');
    $('div.inline-related').find('input[id$=order]').parent('div').hide();
});
