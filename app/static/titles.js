jQuery(document).ready(function() {
	$('.post').on('mouseenter',(event)=>{
		$(event.currentTarget).find('img').addClass('hide');
		$(event.currentTarget).find('.description').removeClass('hide');
	});
	$('.post').on('mouseleave',(event)=>{
		$(event.currentTarget).find('img').removeClass('hide');
		$(event.currentTarget).find('.description').addClass('hide');
	});
});