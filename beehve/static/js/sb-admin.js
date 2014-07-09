$(function() {

    jQuery('#side-menu').metisMenu();

});

//Loads the correct sidebar on window load,
//collapses the sidebar on window resize.
jQuery(function() {
    jQuery(window).bind("load resize", function() {
        width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
        if (width < 768) {
            jQuery('div.sidebar-collapse').addClass('collapse')
        } else {
            jQuery('div.sidebar-collapse').removeClass('collapse')
        }
    })
})
