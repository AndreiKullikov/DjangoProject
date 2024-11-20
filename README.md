# Обязательное задание

## Проект “Сайт рецептов” на Django

### Краткое описание задания

Используя фреймворк Django, создайте сайт, на котором пользователи смогут добавлять свои рецепты блюд и просматривать рецепты других пользователей. Готовый проект необходимо сдать в виде ссылки на рабочий сайт в сети интернет и репозитория с исходным кодом проекта.

### Подробное описание задания

1. **Создайте проект Django и приложение(я) для сайта рецептов.**

   #### Модели

   Для работы с пользователями используйте встроенного в Django User`a. Подготовьте нижеперечисленные модели:

   - **Рецепты:**
     - Название
     - Описание
     - Шаги приготовления
     - Время приготовления
     - Изображение
     - Автор
     - *Другие поля на ваш выбор, например, ингредиенты и т.п.

   - **Категории рецептов:**
     - Название
     - *Другие поля на ваш выбор

   - **Связующая таблица для связи Рецептов и Категории:**
     - *Обязательные для связи поля
     - *Другие поля на ваш выбор

2. **Шаблоны**

   Подготовьте базовый шаблон проекта и нижеперечисленные дочерние шаблоны:

   - Главная с 5 случайными рецептами кратко
   - Страница с одним подробным рецептом
   - Страницы регистрации, авторизации и выхода пользователя
   - Страница добавления/редактирования рецепта
   - *Другие шаблоны на ваш выбор

3. **Формы**

   Создайте формы для ввода и редактирования информации (рецептов) в вашем проекте. Интегрируйте их в шаблоны.

4. **Представления**

   Создайте представления, которые охватывают весь ваш проект: модели, формы, шаблоны.

5. **Маршруты**

   Подключите маршруты, убедитесь в работоспособности представлений и связанных с ними моделей, форм и шаблонов.

6. **Облачный сервер и наполнение**

   Разверните рабочий проект на сервере. Наполните базу данных как минимум пятью рецептами.

   *Если вы обучаетесь в группе, обменяйтесь ссылками с одногруппниками. Заполните рецептами их сайт, а они заполнят ваш.
