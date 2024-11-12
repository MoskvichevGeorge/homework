from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from crud_functions import initate_db, get_all_products


async def on_startup():
    initate_db()


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
        [InlineKeyboardButton(text='Product1', callback_data="productbuying")],
        [InlineKeyboardButton(text='Product2', callback_data="productbuying")],
        [InlineKeyboardButton(text='Product3', callback_data="productbuying")],
        [InlineKeyboardButton(text='Product4', callback_data="productbuying")]
    ]
)


@dp.message_handler(text="Купить")
async def get_buying_list(message: types.Message):
    products = get_all_products()
    if not products:
        await message.reply("Список продуктов пуст.")
        return

    image_paths = [
        ('D:\\\\pytonlesson\\\\pythonProject2\\\\homework1\\\\homeworkmod4\\\\phoro\\\\2.jpg',
         'Название: Product1 | Описание: описание 1 | Цена: 100'),
        ('D:\\\\pytonlesson\\\\pythonProject2\\\\homework1\\\\homeworkmod4\\\\phoro\\\\3.jpg',
         'Название: Product2 | Описание: описание 2 | Цена: 200'),
        ('D:\\\\pytonlesson\\\\pythonProject2\\\\homework1\\\\homeworkmod4\\\\phoro\\\\4.jpg',
         'Название: Product3 | Описание: описание 3 | Цена: 2300'),
        ('D:\\\\pytonlesson\\\\pythonProject2\\\\homework1\\\\homeworkmod4\\\\phoro\\\\5.jpg',
         'Название: Product4 | Описание: описание 4 | Цена: 3000'),
    ]

    for image_path, caption in image_paths:
        with open(image_path, 'rb') as img:
            await message.answer_photo(img, caption)
    await message.answer("Выберите продукт для покупки:", reply_markup=catalog_kb)


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
