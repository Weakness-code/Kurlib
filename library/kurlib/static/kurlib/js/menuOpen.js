
    function bindMenu(triggerSelector, modalSelector, closeSelector) {
        const trigger = document.querySelectorAll(triggerSelector),
              modal = document.querySelector(modalSelector),
              close = document.querySelector(closeSelector);

        trigger.forEach(item => {
            item.addEventListener('click', (e) => {
                if (e.target) {
                    e.preventDefault();
                }
                // item.classList.add('none');
                item.style.opacity = "0";
                // item.style.height = "0";
                // item.style.opacity = "0";
                modal.style.display = "block";

                // document.body.classList.add('modal-open');
            });
        });

        close.addEventListener('click', () => {
            
            modal.style.display = "none";
            // конечно, тут ломается логика. Хорошо бы и здесь сделать перебор
            // trigger[0].classList.remove('none');
            
            trigger[0].style.opacity = "1";

            // document.body.classList.remove('modal-open');
        });

        
    }
bindMenu(".menu__button", ".menu__open", ".menu__close");