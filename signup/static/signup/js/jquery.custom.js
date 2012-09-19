//Start the Custom JavaScript(Requires jQuery library)
//may be moved just below the head but not reccomended for preformance also follow best practices on compression in production enviornment
//Flexislide
jQuery(window).load(function () {
    //Flexislide
    $('.slider').flexslider({
        animation: "fade",
                     
        directionNav: false
    });


});

jQuery(document).ready(function () {

    //Carosoul
    $('#carousel').elastislide({
        imageW: 215,
        onClick: null //important do not remove(will break colorbox)
    });
    //ColorBox(Aka a lightbox plugin)
    $('a.colorbox').colorbox({
        rel: 'gal'
    });
    //Enter your twitter username 
    $(".tweet").tweet({
        username: "twsjonathan",
        avatar_size: 36,
        count: 2,
        loading_text: "loading tweets..."
    });

    //Tipsy(aka Tooltip) 
    // Plugin Documention can be found http://onehackoranother.com/projects/jquery/tipsy/
    $('.tip').tipsy({
        gravity: 's'
    });
});
