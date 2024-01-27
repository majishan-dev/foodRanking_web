$(function () {
    $('.items').paginathing({
        limitPagination: 2,
        pageNumbers: true,
        perPage: 2,
        firstText: '<i class="fas fa-angle-double-left"></i>',
        lastText: '<i class="fas fa-angle-double-right"></i>',
        prevText: '<i class="fas fa-angle-left"></i>',
        nextText: '<i class="fas fa-angle-right"></i>',
        activeClass: 'active',
    });
});