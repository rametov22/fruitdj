(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner(0);


    // Fixed Navbar
    $(window).scroll(function () {
        if ($(window).width() < 992) {
            if ($(this).scrollTop() > 55) {
                $('.fixed-top').addClass('shadow');
            } else {
                $('.fixed-top').removeClass('shadow');
            }
        } else {
            if ($(this).scrollTop() > 55) {
                $('.fixed-top').addClass('shadow').css('top', -55);
            } else {
                $('.fixed-top').removeClass('shadow').css('top', 0);
            }
        } 
    });
    
    
   // Back to top button
   $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
        $('.back-to-top').fadeIn('slow');
    } else {
        $('.back-to-top').fadeOut('slow');
    }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Testimonial carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 2000,
        center: false,
        dots: true,
        loop: true,
        margin: 25,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsiveClass: true,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:1
            },
            992:{
                items:2
            },
            1200:{
                items:2
            }
        }
    });


    // vegetable carousel
    $(".vegetable-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        center: false,
        dots: true,
        loop: true,
        margin: 25,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsiveClass: true,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            },
            1200:{
                items:4
            }
        }
    });


    // Modal Video
    $(document).ready(function () {
        var $videoSrc;
        $('.btn-play').click(function () {
            $videoSrc = $(this).data("src");
        });
        console.log($videoSrc);

        $('#videoModal').on('shown.bs.modal', function (e) {
            $("#video").attr('src', $videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0");
        })

        $('#videoModal').on('hide.bs.modal', function (e) {
            $("#video").attr('src', $videoSrc);
        })
    });



    // Product Quantity
    $('.quantity button').on('click', function () {
        var button = $(this);
        var oldValue = button.parent().parent().find('input').val();
        if (button.hasClass('btn-plus')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        button.parent().parent().find('input').val(newVal);
    });

})(jQuery);

document.addEventListener("DOMContentLoaded", function() {
    const stars = document.querySelectorAll('input[name="stars"]');

    stars.forEach((star, index) => {
        star.addEventListener('change', () => {
            // Удалить класс 'checked' у всех звезд
            stars.forEach((s, i) => {
                if (i <= index) {
                    s.classList.add('checked');
                } else {
                    s.classList.remove('checked');
                }
            });
        });
    });
});


document.addEventListener("DOMContentLoaded", function() {
    const shippingMethods = document.querySelectorAll('input[name="shipping_method"]');
    const updateTotalBtn = document.querySelector('#update_total_btn');
    const totalDisplay = document.querySelector('#total_display');
    const subtotalInput = document.querySelector('#subtotal_input');

        // Function to update total based on selected shipping method
    function updateTotal() {
        console.log('Updating total...');

        let subtotal = parseFloat(subtotalInput.value);
        console.log('subtotal', subtotal);

        let selectedShippingPrice = 0;

        shippingMethods.forEach(function(method) {
            if (method.checked) {
                selectedShippingPrice = parseFloat(method.dataset.price);
            }
        });
        console.log('Selected shipping price', selectedShippingPrice);

        let total = subtotal + selectedShippingPrice;
        console.log('Total', total);

        totalDisplay.textContent = '$' + total.toFixed(2);
        console.log('Total display updated', totalDisplay.textContent);
    }

        // Add event listener to update total when shipping method changes
    shippingMethods.forEach(function(method) {
        method.addEventListener('change', updateTotal);
    });

        // Add event listener to update total when update total button is clicked
     updateTotalBtn.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent form submission
        console.log('Update total button clicked.');
        updateTotal();
    });
});
