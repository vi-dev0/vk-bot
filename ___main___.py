# - ИМПОРТ -
import asyncio
import requests
import random


# - Вк -

from typing import Optional
from vkbottle import GroupEventType, GroupTypes, Keyboard, Text, VKAPIError
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink
from vkbottle.tools import DocMessagesUploader

# Переменные

group_id = '186732930'
secret = 'KEY'
ya = 'doc381260583_611979108'
ya2 = 'photo381260583_457378962'
ya3 = 'video-200537102_456239073'

# Для удобства

bot_token = secret
bot_group_id = group_id
vk = Bot(bot_token, bot_group_id)

# Приветствие

# Есть 3 типа - private_message - ожидание\ответ только в личные сообщения группы!
# chat_message - ожидание\ответ только в беседе!
# message - ожидание\ответ и в беседе и в личные сообщения!

#@vk.on.private_message(text=['Здравствуйте', 'Ку', 'Привет'])
# Сама функция:
#async def privet(message: Message):
	# Ответ на сообщение
#	await message.answer('Приветик!')

# Фото
#@vk.on.private_message(text='фото')
#async def photo(message: Message):
#	await message.answer('Вот твоя фотка ', attachment=ya2)

# Видео
#@vk.on.private_message(text='видео')
#async def video(message: Message):
#	await message.answer('Вот твое видео ', attachment=ya3)

# Файл
#@vk.on.private_message(text='файл')
#async def file(message: Message):
#	await message.answer('Вот твой файл ', attachment=ya)

# Меню
@vk.on.private_message(text=['/mm', 'menu', 'меню', 'начать', 'Начать'])
@vk.on.private_message(payload={'cmd': 'menu'})
async def menu(message: Message):
	await message.answer(
		# Сообщение при отправлении клавиатуры
		message = 'Меню: ',
		# Клавиатура
        keyboard = (
        	# one_time - True - одноразовая клавиатура, False - постоянная клавиатура
        	# inline - True - клавиатура прикрепляется к сообщению(РАССМОТРИМ), False - клавиаутра в стандартном положении
        	# .add - добавить кнопку
        	# .row - отступ
        	# Цвета: POSITIVE - Ярко зеленый, SECONDARY(можно нечего не указывать) - БЛЕДНО БЕЛЫЙ
        	# PRIMARY - СИНИЙ, NEGATIVE - КРАСНЫЙ

            Keyboard(one_time = False, inline = False)
            .add(Text('Режим работы'), color=KeyboardButtonColor.PRIMARY)
            .add(Text('ЧЗВ'), color=KeyboardButtonColor.PRIMARY)
            .row()
            .add(Text('У меня проблема'), color=KeyboardButtonColor.NEGATIVE)
            )
    )


# Режим работы - базовая инфа
@vk.on.private_message(text='Режим работы')
async def regim_raboti(message: Message):
	await message.answer(
		message = 'Графки работы VСЕРВИС:\n'
                  '📅 Понедельник - Суббота | Воскресенье выходной\n'
                  '⏰ С 9:30 до 19:00',
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('В начало', payload={'cmd': 'menu'}))
            )
    )

# ЧЗВ - ответы на Часто Задаваемыые Вопросы
@vk.on.private_message(text='ЧЗВ')
async def faq(message: Message):
	await message.answer(
		message = 'Тут собраны ответы на часто задаваемые вопросы.\n\n'
                  'Раздел будет дополняться',
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Как к вам добраться?'))
            .add(Text('Сколько займет ремонт?'))
            .row()
            .add(Text('Цена на аксессуары'))
            .add(Text('SIMки продаете?'))
            .row()
            .add(Text('Остальные вопросы'))
            .add(Text('В начало', payload={'cmd': 'menu'}), color=KeyboardButtonColor.NEGATIVE)
            )
    )

# ЧЗВ1 - как к вам добраться?
@vk.on.private_message(text='Как к вам добраться?')
async def faq1(message: Message):
	await message.answer(
		message = 'VСервис находится по адресу: г. Евпатория, ул. 9 Мая, 49 (ТЦ Капитал (Яблоко)) у 6-ой кассы\n\n'
                  'Ближайшие остановки общественнго транспорта:\n'
                  '- ТЦ Яблоко – Аптека: 3,6,9\n'
                  '- Супермаркет Фуршет 2, 3, 6, 9\n'
                  '- 7-й магазин 1, 2, 4',
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Как к вам добраться?'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('Сколько займет ремонт?'))
            .row()
            .add(Text('Цена на аксессуары'))
            .add(Text('SIMки продаете?'))
            .row()
            .add(Text('Остальные вопросы'))
            .add(Text('В начало', payload={'cmd': 'menu'}), color=KeyboardButtonColor.NEGATIVE)
            )
    )

# ЧЗВ2 - Сколько займент ремонт?
@vk.on.private_message(text='Сколько займет ремонт?')
async def faq2(message: Message):
	await message.answer(
		message = '❓ Сколько занимает времени замена экарана?\n'
                  '❗ В среднем замена экрана занимает около 20 минут, в случае если мастер свободен.\n\n'
                  '❓ Сколько занимает времени поклейка защитного стекла?\n'
                  '❗ При наличии необходимого стекла, замена занимает около 5-10 минут, в случае если мастер свободен.\n\n'
                  '❓ Сколько ждать деталь которой нет в наличии?\n'
                  '❗ Заказ на недостающие детали делается до 12:00 - в этом случае деталь приходит к 16:00\n'
                  '❗В случае если заказ делается после 12:00 то деталь приходит на следующий день к 16:00\n\n'
                  '❓ Сколько занимает времени переклейка дисплея?\n'
                  '❗ Модели до iPhone X ~ 2.5 часа\n'
                  '❗ Модели после iPhone X ~ 5 часов\n'
                  '❗ Модели Android - в заисимости от телефона от 1 часа до 2х дней',
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Как к вам добраться?'))
            .add(Text('Сколько займет ремонт?'), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('Цена на аксессуары'))
            .add(Text('SIMки продаете?'))
            .row()
            .add(Text('Остальные вопросы'))
            .add(Text('В начало', payload={'cmd': 'menu'}), color=KeyboardButtonColor.NEGATIVE)
            )
    )

# ЧЗВ3 - Цена на аксессуары?
@vk.on.private_message(text='Цена на аксессуары')
async def faq3(message: Message):
	await message.answer(
		message = '❓ Сколь стоит защитное стекло на iPhone?\n'
                  '❗ Средняя цена поклейки защитного стекла - 500р\n\n'
                  '❓ Сколько стоит зарядный кабель?\n'
                  '❗ Кабель хорошего качества (силиконовый, не гнется у коннекторов) стоит 500 руб - Lighting, Type-C, Micro USB\n\n'
                  '❓ Есть ли оригинальные зарядки на iPhone и сколько стоят?\n'
                  '❗ Есть оригинальные блоки и кабеля.\n'
                  '❗ Оригинальный блок 1 500 руб\n'
                  '❗ Оригинальный кабель - 1 200 руб\n'
                  '❗ Кабель Foxcon (в кабеле находится оригинальный чип) - 600 руб'
                  '❓ Сколько стоит чехол\n'
                  '❗ Чехлы есть только для iPhone (всех моделей)\n'
                  '❗ Средняя цена чехла 500 руб\n'
                  '❗ Чехлы для устройств под управлением Android в наличии не держим, только под заказ',
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Как к вам добраться?'))
            .add(Text('Сколько займет ремонт?'))
            .row()
            .add(Text('Цена на аксессуары'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('SIMки продаете?'))
            .row()
            .add(Text('Остальные вопросы'))
            .add(Text('В начало', payload={'cmd': 'menu'}), color=KeyboardButtonColor.NEGATIVE)
            )
    )

# ЧЗВ4 - SIMки продаете?
@vk.on.private_message(text='SIMки продаете?')
async def faq4(message: Message):
	await message.answer(
		message = 'Нет! Сим карты в нашем сервисе не продаются. Приобрести СИМ карту можно в ТЦ Яблоко на любой кассе или у официального диллера Volna и Win Mobile.'
                  ' МТС в Крыму не продается',
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Как к вам добраться?'))
            .add(Text('Сколько займет ремонт?'))
            .row()
            .add(Text('Цена на аксессуары'))
            .add(Text('SIMки продаете?'), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('Остальные вопросы'))
            .add(Text('В начало', payload={'cmd': 'menu'}), color=KeyboardButtonColor.NEGATIVE)
            )
    )

# ЧЗВ5 - Остальные вопросы
@vk.on.private_message(text='Остальные вопросы')
async def faq5(message: Message):
	await message.answer(
		message = 'Этот раздел будет дополняться по мере обращения в наш сервис',
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Как к вам добраться?'))
            .add(Text('Сколько займет ремонт?'))
            .row()
            .add(Text('Цена на аксессуары'))
            .add(Text('SIMки продаете?'))
            .row()
            .add(Text('Остальные вопросы'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('В начало', payload={'cmd': 'menu'}), color=KeyboardButtonColor.NEGATIVE)
            )
    )

# Выбор модели устройства
@vk.on.private_message(text='У меня проблема (В РАЗРАБОТКЕ)')
async def model(message: Message):
	await message.answer(
		message = 'Какой у вас телефон?',
		keyboard = (
			Keyboard(one_time = False, inline = False)
            .add(Text('iPhone'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('Android'), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('В начало', payload={'cmd': 'menu'}),color=KeyboardButtonColor.NEGATIVE)
			#.add(OpenLink('https://blast.hk/', 'ЛУЧШИЙ ПОРТАЛ'))
		)
	)

# Выбор модели - iPhone
@vk.on.private_message(text='iPhone')
async def model_iphone(message: Message):
	await message.answer(
		message = 'Выберите свою модель',
		keyboard = (
			Keyboard(inline=True)
            .add(Text('iPhone 5/5s/5c/SE'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('iPhone 6 Plus'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('iPhone 6S'), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('iPhone 6S Plus'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('iPhone 7'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('iPhone 7 Plus'), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('iPhone 8'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('iPhone 8 Plus'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('iPhone X'), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('iPhone XS'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('iPhone XS Max'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('iPhone XR'), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('iPhone 11'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('iPhone 11 Pro'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('iPhone 11 Pro Max'), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('В начало', payload={'cmd': 'menu'}),color=KeyboardButtonColor.NEGATIVE)
			#.add(OpenLink('https://blast.hk/', 'ЛУЧШИЙ ПОРТАЛ'))
		)
	)

# Нужно сделать

#@vk.on.private_message()
#async def main(message):
#    await message.answer('Я не знаю, что ответить на это =(\n\nВозможно потом когда нибудь я смогу ответить тебе на это =)')


# Толик видиорегистратор система мене
vk.run_forever()