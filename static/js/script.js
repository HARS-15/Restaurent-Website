$(function (){
    $("#navbarToggle").blur(function(event){
        var screenWidth=window.innerWidth;
        if (screenWidth<768){
            $("#collapsable-nav").collapse('hide');
        }
    });
    $(".item_buttons").click(function(event){
        $(".cart").addClass("hidden");
        $(this).siblings(".cart").toggleClass("hidden");
    });
});