let all = takeAllImages('/images/church/church1.png', '/images/flag/slider__flag-img.png', '/images/bolotnov/bolotnov1.png');
let allText = takeAllText('Картинка один бла бла', 'Картинка два бла', 'Картинка три');
followEvent('.poster__arrow--left', '.poster__arrow--right', '.poster__item-img', '.poster__item-text', all, allText);