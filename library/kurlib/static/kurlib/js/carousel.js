function carouselMove(widthImage, countImage, currPosition, carouselElem) {
    let width = widthImage; 
    let count = countImage; 
    let carousel = document.querySelector(carouselElem);
    let list = carousel.querySelector('ul');
    let listElems = carousel.querySelectorAll('li');

    let position = currPosition; // положение ленты прокрутки

    carousel.querySelector('.prev').onclick = function() {
      // сдвиг влево
      position += width * count;
      // последнее передвижение влево может быть не на 3, а на 2 или 1 элемент
      position = Math.min(position, 0)
      list.style.marginLeft = position + 'px';
    };

    carousel.querySelector('.next').onclick = function() {
      // сдвиг вправо
      position -= width * count;
      // последнее передвижение вправо может быть не на 3, а на 2 или 1 элемент
      position = Math.max(position, -width * (listElems.length - count));
      list.style.marginLeft = position + 'px';
    };
    }

    // а еще лучше бы найти куда кликнули и оттуда уже плясать
    // но и так уже неплохо, к тому же стоят другие параметры
    carouselMove(365, 3, 0, '.carousel');
