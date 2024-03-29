new Swiper('.partners-slider', {
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
    },
    // pagination: {
    //     el: '.swiper-pagination',
    //     clickable: true,
    //     dynamicBullets: true
    // },
    slidesPerView: 1,
    spaceBetween: 50,
    breakpoints: {
        // 320: {
        //     slidesPerView: 1,
        // },
        480: {
            slidesPerView: 1,
        },
        981: {
            slidesPerView: 2,
        },
        1431: {
            slidesPerView: 3,
        }
    },
});

new Swiper('.virtual__slider', {
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
        dynamicBullets: true
    },
    slidesPerView: 2,
    spaceBetween: 100,
    autoheight: true,
    breakpoints: {
        320: {
            slidesPerView: 1,
        },
        900: {
            slidesPerView: 1,
        },
        920: {
            slidesPerView: 2,
        },
    },
});

new Swiper('.slider__text-page', {
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
    },

    slidesPerView: 1,
    spaceBetween: 10,
    autoheight: true,

});


new Swiper('.poster-slider', {
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
    },

    slidesPerView: 1,
    spaceBetween: 100,
    // autoheight: true,

});