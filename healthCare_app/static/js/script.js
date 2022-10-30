$(function() {
      $("#header-include").load("headerfooter/header.html");
      $('#footer-include').load("footer.html");

      $(window).scroll(function() {
        if ($(this).scrollTop() > 50) {
          $('.navbar').addClass('solid bg-dark');
        } else {
          $('.navbar').removeClass('solid bg-dark');
        }

      });
    })
