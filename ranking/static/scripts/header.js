$(function() {
    $(".menu-item").hover(
        function() {
            console.log("hover")
            $(".menu-sub:not(:animated)", this).slideDown();
        },
        function() {
            $(".menu-sub", this).slideUp();
        }
    );
});