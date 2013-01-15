$(function() {
 
	$("<select />").appendTo("#topnav");
	 
		// Go to Option
		$("<option />", {
		 "selected": "selected",
		 "value"   : "",
		 "text"    : "Go to..."
		}).appendTo("#topnav select");

		$("#topnav a").each(function() {
		var el = $(this);
		$("<option />", {
		   "value"   : el.attr("href"),
		   "text"    : el.text()
		}).appendTo("#topnav select");
		});
	 
		// Option value
		
		$("#topnav select").change(function() {
		window.location = $(this).find("option:selected").val();
		});
	 


	// Twitter bxSlider callback
	$('#slider1').bxSlider({
		auto: true,
		autoControls: false,
		mode: 'vertical',
	});


		//click and show/hide footer panel	
		$(".footerslidingarrow").click(function(){
			// Toggle the bar up 
			$("#pre_footer").slideToggle();
		}); // end sub panel click function
});

// Start Nivoslider
$(window).load(function() {
        $('.flexslider').flexslider({
        animation: "slide",
		controlNav: false,
		directionNav: true, 
        
        start: function(slider){
          $('body').removeClass('loading');
        }
      });
	$(".block_accordion").tabs(".block_accordion .content", {
		tabs : '.button_outer',
		effect : 'slide',
		initialIndex : 0
	});
});