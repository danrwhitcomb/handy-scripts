jQuery.fn.extend({
	fixedTableHeader: function() {
		var $table = $(this)
		$(window).scroll(function(){
			var $header = $table.find("thead");
			var offset = $table.offset().top
			var bottomOffset = offset + $table.height();

			if ($(window).scrollTop() > bottomOffset){
				$header.css({'position':'static'});

			} else if($(window).scrollTop() > offset){
				var left = $header.offset().left;
				$header.css({
					'position':'fixed',
					'top':'0',
					'left':left
				});
			} else {
				$header.css({'position':'static'});
			} 
		})
	}
})
