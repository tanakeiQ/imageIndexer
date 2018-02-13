function resizeContent() {
	let top = $('.tbl-content').position().top;
	$('.tbl-content').css('height', window.innerHeight - top - 2);
};

$(window).on("load resize ", function() {
  var scrollWidth = $('.tbl-content').width() - $('.tbl-content table').width();
  $('.tbl-header').css({'padding-right':scrollWidth});
  resizeContent();
}).resize();