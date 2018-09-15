$(document).ready(function(){
    $(".block-content").hide();
    $(".block-btn").on("click", function(){
        $(this).parent().parent().find($(".block-content")).toggle(1000);
    });
});
