// Проверяем, существует ли элемент с классом 'header'
const header = document.querySelector('.header');

// Проверяем, существует ли элемент с id 'trigger-point'
const triggerPoint = document.getElementById('trigger-point2');

// Проверяем, что оба элемента существуют перед добавлением обработчика прокрутки
if (header && triggerPoint) {
    // Отслеживаем прокрутку страницы
    window.addEventListener('scroll', function() {
        // Получаем координаты triggerPoint относительно верхнего края видимой области окна браузера
        const triggerPointTop = triggerPoint.getBoundingClientRect().top;

        // Если верхняя граница triggerPoint видима в видимой области окна браузера
        if (triggerPointTop <= 0) {
            header.classList.add('full-width-header');
        } else {
            header.classList.remove('full-width-header');
        }
    });
}


function scrollToHeight(height) {
    window.scrollTo({
        top: height,
        behavior: 'smooth' // делаем прокрутку плавной
    });
}
