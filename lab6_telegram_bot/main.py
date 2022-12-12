import os
import numpy as np
from typing import List
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ContentTypes, Message
from aiogram.dispatcher.filters import Text
from PIL import Image
from config import token

c_photos = []
final_photos = []


bot = Bot(token)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/png2pdf')
b2 = KeyboardButton('/info')
kb.add(b1).insert(b2)

kb_m = ReplyKeyboardMarkup(resize_keyboard=True)
bc1 = KeyboardButton(text='Main menu')
kb_m.add(bc1)


@dp.message_handler(Text(equals="Main menu"))
async def open_kb(message: types.Message):
    await message.answer(text="Main menu",reply_markup=kb)
    
@dp.message_handler(Text(equals="Cancel"))
async def open_kb_m(message: types.Message):
    await message.answer(text="Operation cancelled",reply_markup=kb_m)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Hello, I'm a png-pdf converter bot",reply_markup=kb)
   

@dp.message_handler(commands=['info'])
async def info_command(message: types.Message):
    answer = "This bot is an educational project of the BKIT course of the IU5 department of Bauman Moscow State Technical University\n\nBot was developed by @danila_nikulin\nCode for this bot located on my GitHub: https://github.com/DanilaNik/IU5_BKIT2022/tree/main/lab5_telegram_bot"
    await message.answer(answer,reply_markup=kb)

@dp.message_handler(commands=['png2pdf'])
async def png2pdf_command(message: types.Message):
    await message.answer('Send photo to convert to pdf',reply_markup=kb_m)
    @dp.message_handler(content_types=['photo'])
    async def handle_docs_photo(message: Message):
        if photo := message.photo[-1]:
            await photo.download(str(photo.file_unique_id)+".jpg")
            convert_photo(str(photo.file_unique_id)+".jpg")
            im1 = c_photos[0]
            if(len(c_photos) != 1):
                final_photos.append(c_photos[len(c_photos)-1])
            im1.save(r'file.pdf', save_all=True, append_images=final_photos)
        await message.answer_document(open("file.pdf", 'rb'),reply_markup=kb)
        c_photos.clear()
        final_photos.clear()
        os.remove("file.pdf")
        @dp.message_handler(Text(equals="Main menu"))
        async def open_kb(message: types.Message):
            os.remove(str(photo.file_unique_id)+".jpg")
            os.remove("file.pdf")
            await message.answer(text="Main menu",reply_markup=kb)
    await message.answer_document(open("file.pdf", 'rb'),reply_markup=kb)
    os.remove("file.pdf")
    return
            
def convert_photo(p):
    photo_open = Image.open(p)
    photo_converted = photo_open.convert('RGB')
    c_photos.append(photo_converted)
    os.remove(p)
      
@dp.message_handler()
async def error_message(message: types.Message):
    await message.answer('Please select a command on the keyboard',reply_markup=kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)