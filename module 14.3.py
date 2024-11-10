from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

keyboard = ReplyKeyboardMarkup([
    [KeyboardButton(text='Информация')],
    [KeyboardButton(text='Рассчитать')],
    [KeyboardButton(text='Купить')]
], resize_keyboard=True)

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='raschet')
button2 = InlineKeyboardButton(text='Формула расчета', callback_data='formula')

kb.add(button)
kb.add(button2)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data="product_buying")],
        [InlineKeyboardButton(text='Product2', callback_data="product_buying")],
        [InlineKeyboardButton(text='Product3', callback_data="product_buying")],
        [InlineKeyboardButton(text='Product4', callback_data="product_buying")]
    ]
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=keyboard)


@dp.message_handler(text='Информация')
async def inform(message: types.Message):
    await message.answer('Информация о боте')


@dp.message_handler(text='Рассчитать')
async def ask_for_option(message: types.Message):
    await message.reply('Выберите опцию:', reply_markup=kb)


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    with open('D:\pytonlesson\pythonProject2\homework1\homeworkmod4\phoro/2.jpg', 'rb') as img:
        await message.answer_photo(img, 'Название: Product1 | Описание: описание 1 | Цена: 100', )
    with open('D:\pytonlesson\pythonProject2\homework1\homeworkmod4\phoro/3.jpg', 'rb') as img:
        await message.answer_photo(img, 'Название: Product2 | Описание: описание 2 | Цена: 200')
    with open('D:\pytonlesson\pythonProject2\homework1\homeworkmod4\phoro/4.jpg', 'rb') as img:
        await message.answer_photo(img, 'Название: Product3 | Описание: описание 3 | Цена: 2300')
    with open('D:\pytonlesson\pythonProject2\homework1\homeworkmod4\phoro/5.jpg', 'rb') as img:
        await message.answer_photo(img, 'Название: Product3 | Описание: описание 3 | Цена: 2300')
        await message.answer("Выберите продукт для покупки:", reply_markup=catalog_kb)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.callback_query_handler(text='formula')
async def show_formula(call: types.CallbackQuery):
    await call.message.answer('Формула расчета: 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) -161.')
    await call.answer()


@dp.callback_query_handler(text='raschet')
async def start_calculation(call: types.CallbackQuery):
    await UserState.age.set()
    await call.message.reply("Введите свой возраст:")


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)
    await UserState.next()
    await message.reply("Введите свой рост:")


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    growth = message.text
    await state.update_data(growth=growth)
    await UserState.next()
    await message.reply("Введите свой вес:")


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    weight = message.text
    await state.update_data(weight=weight)

    data = await state.get_data()
    age = int(data.get('age'))
    growth = float(data.get('growth'))
    weight = float(data.get('weight'))

    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.reply(f"Ваша норма калорий: {calories:.2f} ккал.")
    await state.finish()


@dp.message_handler()
async def all_massage(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение!')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
