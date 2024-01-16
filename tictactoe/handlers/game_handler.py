from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from aiogram.filters.callback_data import CallbackData
from tictactoe import TicTacToe

class BoardCallback(CallbackData, prefix="b"):
    bx: int
    by: int

router = Router()
tictac = TicTacToe()

def get_inline_markup():
    kb = [[], [], []]
    for x in range(3):
        for y in range(3):
            kb[x].append(InlineKeyboardButton(text=tictac.get(x, y), callback_data=BoardCallback(bx=x, by=y).pack()))
    return InlineKeyboardMarkup(inline_keyboard=kb)

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Поставьте {}".format(tictac.turn), reply_markup=get_inline_markup())

@router.callback_query()
async def placement(c: CallbackQuery):
    data = BoardCallback.unpack(c.data)
    text = ""
    if tictac.is_empty(data.bx, data.by):
        text = tictac.place(data.bx, data.by)
        if tictac.is_win("x"):
            await c.answer("Крестики победили")
            await c.message.answer("Игра закончена, отправьте /start чтобы начать снова")
        elif tictac.is_win("o"):
            await c.answer("Нолики победили")
            await c.message.answer("Игра закончена, отправьте /start чтобы начать снова")
        else:
            await c.answer(text)
            await c.message.answer("Поставьте {}".format(tictac.turn), reply_markup=get_inline_markup())
    else:
        text = "клетка занята " + tictac.get(data.bx, data.by)
        await c.answer(text)
        await c.message.answer("Поставьте {}".format(tictac.turn), reply_markup=get_inline_markup())