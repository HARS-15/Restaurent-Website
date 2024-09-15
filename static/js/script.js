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
    $(".add-item-link").click(function(event){
          var itemName = $(this).data('item-name');
          $("#existing-message").text(itemName + 'Added.').fadeIn();
          setTimeout(function() {
                $("#existing-message").fadeOut(); // Fade out the message
            }, 8000);
    });
    $('#order-form').submit(function(event) {
        $('#existing-message').text('Your order is being placed...').fadeIn();
        setTimeout(function() {
            $('#order-message').fadeOut();
        }, 10000);
    });

});