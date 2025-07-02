# test-is-invalid-mage

## Объяснение
На задание было потрачено 2 часа 12 минут, где около часа пытался разобратся с API (p.s. так и не разобрался)

В тех задание по указанному URL https://deepai.org/machine-learning-model/nsfw-detector, ничего не работает
В документации по API даже близко не нашел на nsfw-detector, попробывав другую ручку с неудачей бросил затею проверять реальную работоспособность api

В Итоге было принято решение использование 1 заглушки application.image_ai_moderation.ImageAIModeration.__extract_data для извлечении данных (какие бы данные не хранились в ответе).

В свою очередь я рассчитваю на рассмотрения моего проекта, на предмет логического мышления и построение кодовой базы.


## Конфигурация
Для использование тестов создайте папку images ипоместите туда 2 файла
* test_image_false.jpeg
* test_image_true.jpeg

с сожержащем контентом согласно названию файла
создайте .env в корне проекта с переменными из .env.example

## Запуск

```bash
docker build -t test-api -f ./api.dockerfile .
```
```bash
docker network create test_api_network
```
```bash
docker run -d \
--name test-api \
-p 8000:8000 \
--network test_api_network \
--env-file .env \
-v .:/app \
test-api
```