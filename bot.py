#In The Name Of God
#Coder: @Salazar
#Channel: @GIOUTiN
import telebot
import redis
import re
import sys
import os
import string
import random
from time import sleep
from pyrogram import Client
from telebot import types
from redis import StrictRedis
from config import *
#########################
bot = bot = telebot.TeleBot(token)
app = Client("BOT",api_id, api_hash,bot_token = token)
redis = redis.StrictRedis(host='localhost', port=6379, db=10,charset='UTF-8', decode_responses=True)
#########################
def is_admin(userid,usern):
	var = False
	if redis.sismember('bot:sudo', "sd:{}:{}".format(userid,usern)):
		var = True
	return var

def Block(userid,usern):
	var = False
	if redis.sismember('bot:block', "bl:{}:{}".format(userid,usern)):
		var = True
	return var

def randomch(size=8, chars=string.ascii_letters + string.digits +
             string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


def ersaltext():
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('تنظیم متن',callback_data='ersalsp')
    b = types.InlineKeyboardButton('تنظیم متن پیشفرض',callback_data='ersalpish')
    c = types.InlineKeyboardButton('برگشت',callback_data='goback')
    d = types.InlineKeyboardButton('بستن پنل',callback_data='closesetting')
    m.add(a)
    m.add(b)
    m.add(c)
    m.add(d)
    return m



def setting():
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('تنظیم پیام استارت',callback_data='setstartmsg')
    aa = types.InlineKeyboardButton('تنظیم پیام ارسال',callback_data='setmatnersal')
    b = types.InlineKeyboardButton('لیست سودو',callback_data='sudolist')
    c = types.InlineKeyboardButton('لیست بلاک',callback_data='blocklist')
    d = types.InlineKeyboardButton('فوروارد',callback_data='frwrd')
    ddd = types.InlineKeyboardButton('ارسال',callback_data='sendpost')
    dd = types.InlineKeyboardButton('آمار',callback_data='stats')
    e = types.InlineKeyboardButton('مدیریت دکمه های استارت',callback_data='clickinline')
    j = types.InlineKeyboardButton('ارسال پیام تکی',callback_data='sendpostforone')
    f = types.InlineKeyboardButton('بستن پنل',callback_data='closesetting')
    m.add(a)
    m.add(aa)
    m.add(e)
    m.add(b,dd,c)
    m.add(d,ddd)
    m.add(j)
    m.add(f)
    return m

def sudol():
    m = types.InlineKeyboardMarkup()
    for gets in redis.smembers('bot:sudo'):
        userid, usern= gets.split(':')[1:]
        m.add(types.InlineKeyboardButton('[ {} ]'.format(usern),callback_data='sd:{userid}:{usern}'.format(userid=userid,usern=usern)))
    c = types.InlineKeyboardButton('افزودن سودو',callback_data='addsudopanel')
    a = types.InlineKeyboardButton('برگشت',callback_data='goback')
    b = types.InlineKeyboardButton('بستن پنل',callback_data='closesetting')
    m.add(c)
    m.add(a)
    m.add(b)
    return m

def blockl():
    m = types.InlineKeyboardMarkup()
    for gets in redis.smembers('bot:block'):
        userid, usern = gets.split(':')[1:]
        m.add(types.InlineKeyboardButton('[ {} ]'.format(usern),callback_data='bl:{userid}:{usern}'.format(userid=userid,usern=usern)))
    c = types.InlineKeyboardButton('افزودن بلاک',callback_data='addblockpanel')
    a = types.InlineKeyboardButton('برگشت',callback_data='goback')
    b = types.InlineKeyboardButton('بستن پنل',callback_data='closesetting')
    m.add(c)
    m.add(a)
    m.add(b)
    return m



def addkeyin():
    m = types.InlineKeyboardMarkup()
    for gets in redis.smembers('botkeys'):
        name, cldata= gets.split(':')[1:]
        m.add(types.InlineKeyboardButton('[ {} ]'.format(name),callback_data='keys:{name}:{cldata}'.format(name=name,cldata=cldata)))
    c = types.InlineKeyboardButton('افزودن دکمه',callback_data='addkeypanel')
    a = types.InlineKeyboardButton('برگشت',callback_data='goback')
    b = types.InlineKeyboardButton('بستن پنل',callback_data='closesetting')
    m.add(c)
    m.add(a)
    m.add(b)
    return m


def keysuser():
    m = types.InlineKeyboardMarkup()
    for gets in redis.smembers('botkeys'):
        name, cldata= gets.split(':')[1:]
        m.add(types.InlineKeyboardButton('[ {} ]'.format(name),callback_data='showuser:{name}:{cldata}'.format(name=name,cldata=cldata)))
    return m

def backwhow():
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('برگشت',callback_data='gobackshow')
    m.add(a)
    return m


def settingkeyp(name,clback):
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('حذف دکمه',callback_data='delkeys:{name}:{clback}'.format(name=name,clback=clback))
    b = types.InlineKeyboardButton('حذف متن',callback_data='delmatn:{name}:{clback}'.format(name=name,clback=clback))
    c = types.InlineKeyboardButton('تنظیم متن',callback_data='setmatn:{name}:{clback}'.format(name=name,clback=clback))
    e = types.InlineKeyboardButton('برگشت',callback_data='goback')
    f = types.InlineKeyboardButton('بستن پنل',callback_data='closesetting')
    m.add(b,c)
    m.add(a)
    m.add(e)
    m.add(f)
    return m

def taid():
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('تایید',callback_data='taidsudo')
    m.add(a)
    return m

def starttext():
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('تنظیم متن',callback_data='startsp')
    b = types.InlineKeyboardButton('تنظیم متن پیشفرض',callback_data='startpish')
    c = types.InlineKeyboardButton('برگشت',callback_data='goback')
    d = types.InlineKeyboardButton('بستن پنل',callback_data='closesetting')
    m.add(a)
    m.add(b)
    m.add(c)
    m.add(d)
    return m

def fwdpanel():
    m = types.InlineKeyboardMarkup()
    aa = types.InlineKeyboardButton('همه',callback_data='fwdall')
    a = types.InlineKeyboardButton('پیوی ها',callback_data='fwdpvs')
    cc = types.InlineKeyboardButton('گروه ها',callback_data='fwdgp')
    b = types.InlineKeyboardButton('سوپرگروه ها',callback_data='fwdsgps')
    c = types.InlineKeyboardButton('برگشت',callback_data='goback')
    d = types.InlineKeyboardButton('بستن پنل',callback_data='closesetting')
    m.add(aa)
    m.add(b,a,cc)
    m.add(c)
    m.add(d)
    return m

def taidblock():
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('تایید',callback_data='taidblock')
    m.add(a)
    return m

def taidsttext():
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('تایید',callback_data='taidsttext')
    m.add(a)
    return m

def taidfwd(loc):
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('تایید',callback_data='taid{}'.format(loc))
    m.add(a)
    return m

def taidkeys(loc,name,clback):
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('تایید',callback_data='taid{}:{}:{}'.format(loc,name,clback))
    m.add(a)
    return m

def cancsudo():
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('انصراف',callback_data='closesudo')
    m.add(a)
    return m

def cancblock():
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('انصراف',callback_data='closeblock')
    m.add(a)
    return m

def cancsttext():
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('انصراف',callback_data='closesttext')
    m.add(a)
    return m

def cancaddkey():
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('انصراف',callback_data='closekeysadd')
    m.add(a)
    return m

def cl():
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('انصراف',callback_data='close')
    m.add(a)
    return m

def cancfwd(loc):
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('انصراف',callback_data='close{}'.format(loc))
    m.add(a)
    return m

def canckeys(loc):
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('انصراف',callback_data='close{}'.format(loc))
    m.add(a)
    return m

def statspanel():
    m = types.InlineKeyboardMarkup()
    aa = types.InlineKeyboardButton('سودو ها: [ {} ]'.format(redis.scard('bot:sudo')),callback_data='stssudo')
    aaa = types.InlineKeyboardButton('لیست بلاک: [ {} ]'.format(redis.scard('bot:block')),callback_data='stsblock')
    a = types.InlineKeyboardButton('پیوی ها: [ {} ]'.format(redis.scard('bot:user')),callback_data='spv')
    bb = types.InlineKeyboardButton('گروه ها: [ {} ]'.format(redis.scard('bot:gp')),callback_data='gpa')
    b = types.InlineKeyboardButton('سوپرگروه ها: [ {} ]'.format(redis.scard('bot:sgps')),callback_data='sgp')
    c = types.InlineKeyboardButton('برگشت',callback_data='goback')
    d = types.InlineKeyboardButton('بستن پنل',callback_data='closesetting')
    m.add(aa)
    m.add(aaa)
    m.add(a)
    m.add(bb)
    m.add(b)
    m.add(c)
    m.add(d)
    return m

def sendpostp():
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('همه',callback_data='sendpostall')
    b = types.InlineKeyboardButton('پیوی ها',callback_data='sendpostpv')
    c = types.InlineKeyboardButton('گروه ها',callback_data='sendpostgp')
    d = types.InlineKeyboardButton('سوپرگروه ها',callback_data='sendpostsgps')
    e = types.InlineKeyboardButton('برگشت',callback_data='goback')
    f = types.InlineKeyboardButton('بستن پنل',callback_data='closesetting')
    m.add(a)
    m.add(d,b,c)
    m.add(e)
    m.add(f)
    return m

def ans(userid,usern):
    m = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton('جواب دادن',callback_data='ans:{userid}:{usern}'.format(userid=userid,usern=usern))
    if redis.sismember('bot:block',"bl:{}:{}".format(userid,usern)):
        b = types.InlineKeyboardButton('بلاک [ ✅ ]',callback_data='block:{userid}:{usern}'.format(userid=userid,usern=usern))
    else:
        b = types.InlineKeyboardButton('بلاک [ ❌ ]',callback_data='block:{userid}:{usern}'.format(userid=userid,usern=usern))
    m.add(a)
    m.add(b)
    return m

#########################             #        #         #          ##        #         #          #           #                     #         #
@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact','animation'])
def cmd(message):
    if message.text == "/start":
            if message.from_user.id == sudo or is_admin(message.from_user.id,message.from_user.first_name):
                bot.reply_to(message,"به پنل مدیران خوش آمدید!",reply_markup=setting())
                if message.chat.type == "group":
                    redis.srem('bot:gp',message.chat.id)
                    redis.sadd('bot:gp',message.chat.id)
                if message.chat.type == "private":
                    redis.srem('bot:user',message.from_user.id)
                    redis.sadd('bot:user',message.from_user.id)
                if message.chat.type == "supergroup":
                    redis.srem('bot:sgps',message.chat.id)
                    redis.sadd('bot:sgps',message.chat.id)
            else:
                if message.chat.type == "private":
                    redis.srem('bot:user',message.from_user.id)
                    txt = redis.get('bot:starttext') or "سلام \n پیام خود را ارسال کنید!"
                    bot.reply_to(message,"{}".format(txt),reply_markup=keysuser())
                    redis.sadd('bot:user',message.from_user.id)



    if message.chat.type == "private":
        if message.from_user.id == sudo or is_admin(message.from_user.id,message.from_user.first_name):
            pass
        else:
            if Block(message.from_user.id,message.from_user.first_name):
                bot.reply_to(message,"شما در لیست بلاک ربات وجود دارید و نمیتوانید پیام ارسال کنید!")
            else:
                if message.text and not message.text == "/start":
                    if not redis.sismember('bot:user',message.chat.id) or not redis.sismember('bot:gp',message.chat.id) or not redis.sismember('bot:sgps',message.chat.id):
                        if message.chat.type == "group":
                            redis.sadd('bot:gp',message.chat.id)
                        if message.chat.type == "private":
                            redis.sadd('bot:user',message.from_user.id)
                        if message.chat.type == "supergroup":
                            redis.sadd('bot:sgps',message.chat.id)
                    txt = redis.get('bot:ersaltext') or "پیام شما با موفقیت ارسال شد!"
                    bot.reply_to(message,"{}".format(txt))
                    userid = message.from_user.id
                    usern = message.from_user.first_name
                    bot.send_message(log,"پیام از طرف فرد : [ <a href='tg://user?id={}'>{}</a> ] \n \n محتوای پیام: \n {}".format(userid,"USER",message.text),parse_mode='HTML', disable_web_page_preview=True,reply_markup=ans(userid,usern))

                if message and not message.text:
                    if not redis.sismember('bot:user',message.chat.id) or not redis.sismember('bot:gp',message.chat.id) or not redis.sismember('bot:sgps',message.chat.id):
                        if message.chat.type == "group":
                            redis.sadd('bot:gp',message.chat.id)
                        if message.chat.type == "private":
                            redis.sadd('bot:user',message.chat.id)
                        if message.chat.type == "supergroup":
                            redis.sadd('bot:sgps',message.chat.id)
                    txt = redis.get('bot:ersaltext') or "پیام شما با موفقیت ارسال شد!"
                    bot.reply_to(message,"{}".format(txt))
                    userid = message.from_user.id
                    usern = message.from_user.first_name
                    a = bot.forward_message(log, message.chat.id,message.message_id)
                    bot.reply_to(a,"پیام از طرف فرد : [ <a href='tg://user?id={}'>{}</a> ] \n \n محتوای پیام: \n متفرقه!".format(userid,"USER"),parse_mode='HTML', disable_web_page_preview=True,reply_markup=ans(userid,usern))
###########################
    if message.from_user.id == sudo or is_admin(message.from_user.id,message.from_user.first_name):
        chatid = message.chat.id
        if redis.get('bot:ans'+str(chatid)) and redis.get('admin:ans'+str(chatid)) == str(message.from_user.id):
            if message.text and not message.text == "/start":
                a = redis.get('bot:ans'+str(chatid))
                b = "USER"
                try:
                    bot.send_message(a,"{}".format(message.text))
                    bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!".format(a,b),parse_mode='HTML', disable_web_page_preview=True)
                except:
                    bot.reply_to(message,"کاربر حساب ربات را بلاک کرده است و نمیتوانید پیامی به او برسانید!")
                redis.delete('bot:ans'+str(chatid))

            if message and not message.text:
                if message.sticker:
                    a = redis.get('bot:ans'+str(chatid))
                    b = "USER"
                    try:
                        bot.send_sticker(a,message.sticker.file_id)
                        bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!".format(a,b),parse_mode='HTML', disable_web_page_preview=True)
                    except:
                        bot.reply_to(message,"کاربر حساب ربات را بلاک کرده است و نمیتوانید پیامی به او برسانید!")
                    redis.delete('bot:ans'+str(chatid))


                if message.video_note:
                    a = redis.get('bot:ans'+str(chatid))
                    b = "USER"
                    try:
                        bot.send_video_note(a,message.video_note.file_id)
                        bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!".format(a,b),parse_mode='HTML', disable_web_page_preview=True)
                    except:
                        bot.reply_to(message,"کاربر حساب ربات را بلاک کرده است و نمیتوانید پیامی به او برسانید!")
                    redis.delete('bot:ans'+str(chatid))


                if message.contact:
                    a = redis.get('bot:ans'+str(chatid))
                    b = "USER"
                    try:
                        bot.send_contact(a,message.contact.phone_number,message.contact.first_name)
                        bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!".format(a,b),parse_mode='HTML', disable_web_page_preview=True)
                    except:
                        bot.reply_to(message,"کاربر حساب ربات را بلاک کرده است و نمیتوانید پیامی به او برسانید!")
                    redis.delete('bot:ans'+str(chatid))


                if message.document:
                    a = redis.get('bot:ans'+str(chatid))
                    b = "USER"
                    try:
                        bot.send_document(a,message.document.file_id,caption=message.caption or None)
                        bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!".format(a,b),parse_mode='HTML', disable_web_page_preview=True)
                    except:
                        bot.reply_to(message,"کاربر حساب ربات را بلاک کرده است و نمیتوانید پیامی به او برسانید!")
                    redis.delete('bot:ans'+str(chatid))


                if message.voice:
                    a = redis.get('bot:ans'+str(chatid))
                    b = "USER"
                    try:
                        bot.send_voice(a,message.voice.file_id,caption=message.caption or None)
                        bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!".format(a,b),parse_mode='HTML', disable_web_page_preview=True)
                    except:
                        bot.reply_to(message,"کاربر حساب ربات را بلاک کرده است و نمیتوانید پیامی به او برسانید!")
                    redis.delete('bot:ans'+str(chatid))


                if message.audio:
                    a = redis.get('bot:ans'+str(chatid))
                    b = "USER"
                    try:
                        bot.send_audio(a,message.audio.file_id,caption=message.caption or None)
                        bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!".format(a,b),parse_mode='HTML', disable_web_page_preview=True)
                    except:
                        bot.reply_to(message,"کاربر حساب ربات را بلاک کرده است و نمیتوانید پیامی به او برسانید!")
                    redis.delete('bot:ans'+str(chatid))


                if message.animation:
                    a = redis.get('bot:ans'+str(chatid))
                    b = "USER"
                    try:
                        bot.send_animation(a,message.animation.file_id,caption=message.caption or None)
                        bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!".format(a,b),parse_mode='HTML', disable_web_page_preview=True)
                    except:
                        bot.reply_to(message,"کاربر حساب ربات را بلاک کرده است و نمیتوانید پیامی به او برسانید!")
                    redis.delete('bot:ans'+str(chatid))


                if message.video:
                    a = redis.get('bot:ans'+str(chatid))
                    b = "USER"
                    try:
                        bot.send_video(a,message.video.file_id,caption=message.caption or None)
                        bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!".format(a,b),parse_mode='HTML', disable_web_page_preview=True)
                    except:
                        bot.reply_to(message,"کاربر حساب ربات را بلاک کرده است و نمیتوانید پیامی به او برسانید!")
                    redis.delete('bot:ans'+str(chatid))

                if message.photo:
                    a = redis.get('bot:ans'+str(chatid))
                    b = "USER"
                    try:
                        bot.send_photo(a,message.photo[0].file_id,caption=message.caption or None)
                        bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!".format(a,b),parse_mode='HTML', disable_web_page_preview=True)
                    except:
                        bot.reply_to(message,"{}".format(message.photo.json.photo.file_id))
                    redis.delete('bot:ans'+str(chatid))

###############fullsudo & is_admin#############
        if redis.get('bot:addblock'+str(chatid)):
            if message.text:
                app.start()
                ga = app.get_users((int(message.text)))
                if redis.sismember('bot:block',"bl:{}:{}".format(ga.id,ga.first_name)):
                    bot.reply_to(message,"این فرد از قبل در لیست بلاک بود!")
                    redis.delete('bot:addblock'+str(chatid))
                else:
                    bot.reply_to(message,"کاربر {} به لیست بلاک ربات اضافه شد! \n برای ادامه روی دکمه تایید بزنید!".format(ga.first_name),parse_mode='HTML', disable_web_page_preview=True,reply_markup=taidblock())
                    redis.delete('bot:addblock'+str(chatid))
                    redis.sadd('bot:block',"bl:{}:{}".format(ga.id,ga.first_name))
                app.stop()
            else:
                bot.reply_to(message,"لطفا آیدی عددی را درست وارد کنید!")

        if redis.get('sendiduser'+str(chatid)):
            if message.text:
                redis.delete('sendiduser'+str(chatid))
                user = int(message.text)
                if redis.sismember('bot:user',user) or redis.sismember('bot:gp',user) or redis.sismember('bot:sgps',user):
                    try:
                        redis.delete('sendpostid'+str(chatid))
                        b = bot.get_chat(user).first_name
                        loc = 'sendmsg'
                        redis.set('sendpostid'+str(chatid),user)
                        bot.delete_message(chatid,redis.get('shaksiid'+str(chatid)))
                        redis.delete('shaksiid'+str(chatid))
                        bot.reply_to(message,"در حال ارسال پیام شخصی به کاربر [ <a href='tg://user?id={}'>{}</a> ] هستید!\nلطفا پیام خود را ارسال کنید!".format(user,b),parse_mode='HTML', disable_web_page_preview=True)
                    except Exception as e:
                        print(e)
                else:
                    c = bot.reply_to(message,"این فرد درون لیست کاربران ربات نیست و تا به حال ربات را استارت نکرده!")
                    sleep(60)
                    bot.delete_message(chatid,c)

        if redis.get('sendpostid'+str(chatid)):
            user = redis.get('sendpostid'+str(chatid))
            b = bot.get_chat(user).first_name
            if message.text and not message.text == str(user):
                try:
                    loc = 'sendmsg'
                    bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!\nبرای ادامه بر روی دکمه تایید بزنید!".format(user,b),parse_mode='HTML', disable_web_page_preview=True,reply_markup=taidfwd(loc))
                    c = message.from_user.id
                    d = bot.get_chat(c).first_name
                    bot.send_message(user,"شما پیام جدیدی از مدیر ربات [ <a href='tg://user?id={}'>{}</a> ] دارید!\n محتوای پیام:\n {}".format(c,d,message.text),parse_mode='HTML', disable_web_page_preview=True)
                    redis.delete('sendpostid'+str(chatid))
                except Exception as e:
                    print(e)

            if message.photo:
                try:
                    loc = 'sendmsg'
                    bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!\nبرای ادامه بر روی دکمه تایید بزنید!".format(user,b),parse_mode='HTML', disable_web_page_preview=True,reply_markup=taidfwd(loc))
                    c = message.from_user.id
                    d = bot.get_chat(c).first_name
                    n = bot.send_photo(user,message.photo[0].file_id,caption=message.caption or None)
                    bot.reply_to(n,"شما پیام جدیدی از مدیر ربات [ <a href='tg://user?id={}'>{}</a> ] دارید!\n محتوای پیام:\n متفرقه!".format(c,d),parse_mode='HTML', disable_web_page_preview=True)
                    redis.delete('sendpostid'+str(chatid))
                except Exception as e:
                    print(e)

            if message.video:
                try:
                    loc = 'sendmsg'
                    bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!\nبرای ادامه بر روی دکمه تایید بزنید!".format(user,b),parse_mode='HTML', disable_web_page_preview=True,reply_markup=taidfwd(loc))
                    c = message.from_user.id
                    d = bot.get_chat(c).first_name
                    n = bot.send_video(user,message.video.file_id,caption=message.caption or None)
                    bot.reply_to(n,"شما پیام جدیدی از مدیر ربات [ <a href='tg://user?id={}'>{}</a> ] دارید!\n محتوای پیام:\n متفرقه!".format(c,d),parse_mode='HTML', disable_web_page_preview=True)
                    redis.delete('sendpostid'+str(chatid))
                except Exception as e:
                    print(e)

            if message.animation:
                try:
                    loc = 'sendmsg'
                    bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!\nبرای ادامه بر روی دکمه تایید بزنید!".format(user,b),parse_mode='HTML', disable_web_page_preview=True,reply_markup=taidfwd(loc))
                    c = message.from_user.id
                    d = bot.get_chat(c).first_name
                    n = bot.send_animation(user,message.animation.file_id,caption=message.caption or None)
                    bot.reply_to(n,"شما پیام جدیدی از مدیر ربات [ <a href='tg://user?id={}'>{}</a> ] دارید!\n محتوای پیام:\n متفرقه!".format(c,d),parse_mode='HTML', disable_web_page_preview=True)
                    redis.delete('sendpostid'+str(chatid))
                except Exception as e:
                    print(e)

            if message.voice:
                try:
                    loc = 'sendmsg'
                    bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!\nبرای ادامه بر روی دکمه تایید بزنید!".format(user,b),parse_mode='HTML', disable_web_page_preview=True,reply_markup=taidfwd(loc))
                    c = message.from_user.id
                    d = bot.get_chat(c).first_name
                    n = bot.send_voice(user,message.voice.file_id,caption=message.caption or None)
                    bot.reply_to(n,"شما پیام جدیدی از مدیر ربات [ <a href='tg://user?id={}'>{}</a> ] دارید!\n محتوای پیام:\n متفرقه!".format(c,d),parse_mode='HTML', disable_web_page_preview=True)
                    redis.delete('sendpostid'+str(chatid))
                except Exception as e:
                    print(e)

            if message.document:
                try:
                    loc = 'sendmsg'
                    bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!\nبرای ادامه بر روی دکمه تایید بزنید!".format(user,b),parse_mode='HTML', disable_web_page_preview=True,reply_markup=taidfwd(loc))
                    c = message.from_user.id
                    d = bot.get_chat(c).first_name
                    n = bot.send_document(user,message.document.file_id,caption=message.caption or None)
                    bot.reply_to(n,"شما پیام جدیدی از مدیر ربات [ <a href='tg://user?id={}'>{}</a> ] دارید!\n محتوای پیام:\n متفرقه!".format(c,d),parse_mode='HTML', disable_web_page_preview=True)
                    redis.delete('sendpostid'+str(chatid))
                except Exception as e:
                    print(e)

            if message.contact:
                try:
                    loc = 'sendmsg'
                    bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!\nبرای ادامه بر روی دکمه تایید بزنید!".format(user,b),parse_mode='HTML', disable_web_page_preview=True,reply_markup=taidfwd(loc))
                    c = message.from_user.id
                    d = bot.get_chat(c).first_name
                    n = bot.send_animation(user,message.animation.file_id,caption=message.caption or None)
                    bot.reply_to(n,"شما پیام جدیدی از مدیر ربات [ <a href='tg://user?id={}'>{}</a> ] دارید!\n محتوای پیام:\n متفرقه!".format(c,d),parse_mode='HTML', disable_web_page_preview=True)
                    redis.delete('sendpostid'+str(chatid))
                except Exception as e:
                    print(e)

            if message.sticker:
                try:
                    loc = 'sendmsg'
                    bot.reply_to(message,"پیام شما با موفقیت به [ <a href='tg://user?id={}'>{}</a> ] ارسال شد!\nبرای ادامه بر روی دکمه تایید بزنید!".format(user,b),parse_mode='HTML', disable_web_page_preview=True,reply_markup=taidfwd(loc))
                    c = message.from_user.id
                    d = bot.get_chat(c).first_name
                    n = bot.send_sticker(user,message.sticker.file_id)
                    bot.reply_to(n,"شما پیام جدیدی از مدیر ربات [ <a href='tg://user?id={}'>{}</a> ] دارید!\n محتوای پیام:\n متفرقه!".format(c,d),parse_mode='HTML', disable_web_page_preview=True)
                    redis.delete('sendpostid'+str(chatid))
                except Exception as e:
                    print(e)


##############Just Sudo##############
    if message.from_user.id == sudo:

        if message.text == "ریلود":
            bot.reply_to(message, 'ربات با موفقیت بروز شد!')
            python = sys.executable
            os.execl(python, python, *sys.argv)


        chatid = message.chat.id
        if redis.get('bot:addstarttext'+str(chatid)):
            if message.text:
                bot.reply_to(message,"متن شما با موفقیت برای استارت ربات تنظیم شد!\nبرای ادامه بر روی دکمه تایید بزنید!",reply_markup=taidsttext())
                redis.delete('bot:addstarttext'+str(chatid))
                redis.set('bot:starttext',message.text)


        if redis.get('bot:addersaltext'+str(chatid)):
            if message.text:
                loc = 'ersaltxt'
                bot.reply_to(message,"متن شما با موفقیت برای ارسال ربات تنظیم شد!\nبرای ادامه بر روی دکمه تایید بزنید!",reply_markup=taidfwd(loc))
                redis.delete('bot:addersaltext'+str(chatid))
                redis.set('bot:ersaltext',message.text)
                


        if redis.get('bot:addsudo'+str(chatid)):
            if message.text:
                app.start()
                ga = app.get_users((int(message.text)))
                if redis.sismember('bot:sudo',"sd:{}:{}".format(ga.id,ga.first_name)):
                    bot.reply_to(message,"این فرد از قبل در لیست سودو بود!")
                    redis.delete('bot:addsudo'+str(chatid))
                else:
                    bot.reply_to(message,"کاربر {} به لیست سودو های ربات اضافه شد! \n برای ادامه روی دکمه تایید بزنید!".format(ga.first_name),parse_mode='HTML', disable_web_page_preview=True,reply_markup=taid())
                    redis.delete('bot:addsudo'+str(chatid))
                    redis.sadd('bot:sudo',"sd:{}:{}".format(ga.id,ga.first_name))
                app.stop()
            else:
                bot.reply_to(message,"لطفا آیدی عددی را درست وارد کنید!")

        if redis.get('bot:addfwdpvs'+str(chatid)):
            if message:
                redis.delete('bot:addfwdpvs'+str(chatid))
                bot_pvs = redis.smembers('bot:user')
                bot.reply_to(message,'عملیات فوروارد به پیوی ها با موفقیت اجرا شد و {} ثانیه دیگر به اتمام میرسد!'.format(len(bot_pvs)))
                s = 0
                for all in bot_pvs:
                    try:
                        sleep(1)
                        bot.forward_message(all, message.chat.id, message.message_id)
                        s += 1
                    except Exception as e:
                        print("{}".format(e))
                n = redis.get('bot:msgfpid'+str(chatid))
                bot.delete_message(chatid,n)
                redis.delete('botmsgfpid'+str(chatid))
                loc = 'pv'
                bot.reply_to(message, "محتوای مورد نظر به {} پیوی ارسال شد! \nبرای ادامه بر روی دکمه تایید بزنید!".format(s),reply_markup=taidfwd(loc))

        if redis.get('bot:addfwdsgps'+str(chatid)):
            if message:
                redis.delete('bot:addfwdsgps'+str(chatid))
                bot_sgps = redis.smembers('bot:sgps')
                bot.reply_to(message,'عملیات فوروارد به سوپرگروه ها با موفقیت اجرا شد و {} ثانیه دیگر به اتمام میرسد!'.format(len(bot_sgps)))
                s = 0
                for all in bot_sgps:
                    try:
                        sleep(1)
                        bot.forward_message(all, message.chat.id, message.message_id)
                        s += 1
                    except Exception as e:
                        print("{}".format(e))
                n = redis.get('bot:msgfsid'+str(chatid))
                bot.delete_message(chatid,n)
                redis.delete('botmsgfsid'+str(chatid))
                loc = 'sgps'
                bot.reply_to(message, "محتوای مورد نظر به {} سوپرگروه ارسال شد! \nبرای ادامه بر روی دکمه تایید بزنید!".format(s),reply_markup=taidfwd(loc))

        if redis.get('bot:addfwdgp'+str(chatid)):
            if message:
                redis.delete('bot:addfwdgp'+str(chatid))
                bot_gp = redis.smembers('bot:gp')
                bot.reply_to(message,'عملیات فوروارد به گروه ها با موفقیت اجرا شد و {} ثانیه دیگر به اتمام میرسد!'.format(len(bot_gp)))
                s = 0
                for all in bot_gp:
                    try:
                        sleep(1)
                        bot.forward_message(all, message.chat.id, message.message_id)
                        s += 1
                    except Exception as e:
                        print("{}".format(e))
                n = redis.get('bot:msgfgpid'+str(chatid))
                bot.delete_message(chatid,n)
                redis.delete('bot:msgfgpid'+str(chatid))
                loc = 'gp'
                bot.reply_to(message, "محتوای مورد نظر به {} گروه ارسال شد! \nبرای ادامه بر روی دکمه تایید بزنید!".format(s),reply_markup=taidfwd(loc))


        if redis.get('bot:addfwdall'+str(chatid)):
            if message:
                redis.delete('bot:addfwdall'+str(chatid))
                bot_pvs = redis.smembers('bot:user')
                bot_sgps = redis.smembers('bot:sgps')
                bot_gp = redis.smembers('bot:gp')
                bot_all = len(bot_pvs) + len(bot_sgps) + len(bot_gp)
                bot.reply_to(message,'عملیات فوروارد به تمامی گفتگو ها با موفقیت اجرا شد و {} ثانیه دیگر به اتمام میرسد!'.format(bot_all))
                p = 0
                for all in bot_pvs:
                    try:
                        sleep(1)
                        bot.forward_message(all, message.chat.id, message.message_id)
                        p += 1
                    except Exception as e:
                        print("{}".format(e))
                s = 0
                for all in bot_sgps:
                    try:
                        sleep(1)
                        bot.forward_message(all, message.chat.id, message.message_id)
                        s += 1
                    except Exception as e:
                        print("{}".format(e))
                g = 0
                for all in bot_gp:
                    try:
                        sleep(1)
                        bot.forward_message(all, message.chat.id, message.message_id)
                        g += 1
                    except Exception as e:
                        print("{}".format(e))
                n = redis.get('bot:msgallid'+str(chatid))
                bot.delete_message(chatid,n)
                redis.delete('bot:msgallid'+str(chatid))
                loc = 'all'
                bot.reply_to(message,"محتوای مورد نظر با موفقیت به {} پیوی و {} گروه و {} سوپرگروه ارسال شد!\nبرای ادامه بر روی دکمه تایید بزنید!".format(p,g,s),reply_markup=taidfwd(loc))

        if redis.get('bot:addsendall'+str(chatid)):
            if message.text or message.photo or message.video or message.document:
                redis.delete('bot:addsendall'+str(chatid))
                bot_pvs = redis.smembers('bot:user')
                bot_sgps = redis.smembers('bot:sgps')
                bot_gp = redis.smembers('bot:gp')
                bot_all = len(bot_pvs) + len(bot_sgps) + len(bot_gp)
                bot.reply_to(message,'عملیات ارسال به تمامی گفتگو ها با موفقیت اجرا شد و {} ثانیه دیگر به اتمام میرسد!'.format(bot_all))
                p = 0
                for all in bot_pvs:
                    try:
                        sleep(1)
                        if message.text:
                            bot.send_message(all, "{}".format(message.text))
                        if message.photo:
                            bot.send_photo(all,message.photo[0].file_id,caption=message.caption or None)
                        if message.video:
                            bot.send_video(all,message.video.file_id,caption=message.caption or None)
                        if message.document:
                            bot.send_document(all,message.document.file_id,caption=message.caption or None)
                        p += 1
                    except Exception as e:
                        print("{}".format(e))
                s = 0
                for all in bot_sgps:
                    try:
                        sleep(1)
                        if message.text:
                            bot.send_message(all, "{}".format(message.text))
                        if message.photo:
                            bot.send_photo(all,message.photo[0].file_id,caption=message.caption or None)
                        if message.video:
                            bot.send_video(all,message.video.file_id,caption=message.caption or None)
                        if message.document:
                            bot.send_document(all,message.document.file_id,caption=message.caption or None)
                        s += 1
                    except Exception as e:
                        print("{}".format(e))
                g = 0
                for all in bot_gp:
                    try:
                        sleep(1)
                        if message.text:
                            bot.send_message(all, "{}".format(message.text))
                        if message.photo:
                            bot.send_photo(all,message.photo[0].file_id,caption=message.caption or None)
                        if message.video:
                            bot.send_video(all,message.video.file_id,caption=message.caption or None)
                        if message.document:
                            bot.send_document(all,message.document.file_id,caption=message.caption or None)
                        g += 1
                    except Exception as e:
                        print("{}".format(e))
                n = redis.get('bot:msgsendallid'+str(chatid))
                bot.delete_message(chatid,n)
                redis.delete('bot:msgsendallid'+str(chatid))
                loc = 'sendall'
                bot.reply_to(message,"محتوای مورد نظر با موفقیت به {} پیوی و {} گروه و {} سوپرگروه ارسال شد!\nبرای ادامه بر روی دکمه تایید بزنید!".format(p,g,s),reply_markup=taidfwd(loc))

        if redis.get('bot:addsendpv'+str(chatid)):
            if message.text or message.photo or message.video or message.document:
                redis.delete('bot:addsendpv'+str(chatid))
                bot_pvs = redis.smembers('bot:user')
                bot.reply_to(message,'عملیات  ارسال به پیوی ها با موفقیت اجرا شد و {} ثانیه دیگر به اتمام میرسد!'.format(len(bot_pvs)))
                p = 0
                for all in bot_pvs:
                    try:
                        sleep(1)
                        if message.text:
                            bot.send_message(all, "{}".format(message.text))
                        if message.photo:
                            bot.send_photo(all,message.photo[0].file_id,caption=message.caption or None)
                        if message.video:
                            bot.send_video(all,message.video.file_id,caption=message.caption or None)
                        if message.document:
                            bot.send_document(all,message.document.file_id,caption=message.caption or None)
                        p += 1
                    except Exception as e:
                        print("{}".format(e))
                n = redis.get('bot:msgsendpvid'+str(chatid))
                bot.delete_message(chatid,n)
                redis.delete('bot:msgsendpvid'+str(chatid))
                loc = 'sendpv'
                bot.reply_to(message, "محتوای مورد نظر به {} پیوی ارسال شد! \nبرای ادامه بر روی دکمه تایید بزنید!".format(s),reply_markup=taidfwd(loc))



        if redis.get('bot:addsendsgps'+str(chatid)):
            if message.text or message.photo or message.video or message.document:
                redis.delete('bot:addsendsgps'+str(chatid))
                bot_sgps = redis.smembers('bot:sgps')
                bot.reply_to(message,'عملیات  ارسال به سوپرگروه ها با موفقیت اجرا شد و {} ثانیه دیگر به اتمام میرسد!'.format(len(bot_sgps)))
                s = 0
                for all in bot_sgps:
                    try:
                        sleep(1)
                        if message.text:
                            bot.send_message(all, "{}".format(message.text))
                        if message.photo:
                            bot.send_photo(all,message.photo[0].file_id,caption=message.caption or None)
                        if message.video:
                            bot.send_video(all,message.video.file_id,caption=message.caption or None)
                        if message.document:
                            bot.send_document(all,message.document.file_id,caption=message.caption or None)
                        s += 1
                    except Exception as e:
                        print("{}".format(e))
                n = redis.get('bot:msgsendsgpsid'+str(chatid))
                bot.delete_message(chatid,n)
                redis.delete('bot:msgsendsgpsid'+str(chatid))
                loc = 'sendsgps'
                bot.reply_to(message,"محتوای مورد نظر به {} سوپرگروه ارسال شد! \nبرای ادامه بر روی دکمه تایید بزنید!".format(s),reply_markup=taidfwd(loc))




        if redis.get('bot:addsendgp'+str(chatid)):
            if message.text or message.photo or message.video or message.document:
                redis.delete('bot:addsendgp'+str(chatid))
                bot_gp = redis.smembers('bot:gp')
                bot.reply_to(message,'عملیات  ارسال به گروه ها با موفقیت اجرا شد و {} ثانیه دیگر به اتمام میرسد!'.format(len(bot_gp)))
                g = 0
                for all in bot_gp:
                    try:
                        sleep(1)
                        if message.text:
                            bot.send_message(all, "{}".format(message.text))
                        if message.photo:
                            bot.send_photo(all,message.photo[0].file_id,caption=message.caption or None)
                        if message.video:
                            bot.send_video(all,message.video.file_id,caption=message.caption or None)
                        if message.document:
                            bot.send_document(all,message.document.file_id,caption=message.caption or None)
                        g += 1
                    except Exception as e:
                        print("{}".format(e))
                n = redis.get('bot:msgsendgpid'+str(chatid))
                bot.delete_message(chatid,n)
                redis.delete('bot:msgsendgpid'+str(chatid))
                loc = 'sendgp'
                bot.reply_to(message, "محتوای مورد نظر به {} گروه ارسال شد! \nبرای ادامه بر روی دکمه تایید بزنید!".format(g),reply_markup=taidfwd(loc))




        if redis.get('bot:addkey'+str(chatid)):
            if message.text:
                name = message.text
                clb = randomch(int(8))
                clback = r"{}".format(clb)
                redis.delete('bot:addkey'+str(chatid))
                redis.sadd('botkeys',"keys:{}:{}".format(name,clback))
                a = redis.get('bot:msgkeyid'+str(chatid))
                bot.delete_message(chatid,a)
                redis.delete('bot:msgkeyid'+str(chatid))
                loc = 'keys'
                bot.reply_to(message, "دکمه موردنظر با اسم {} و کالبک {} ساخته شد!\nبرای ادامه بر روی دکمه تایید بزنید!".format(name,clback),reply_markup=taidfwd(loc))

        if redis.get('bottextktime:{}:{}'.format(chatid,message.from_user.id)):
            if message.text:
                gets = redis.get('bottextktime:{}:{}'.format(chatid,message.from_user.id))
                name, cldata = gets.split(':')[0:]
                redis.delete('keytxt:{}:{}'.format(name,cldata))
                redis.set('keytxt:{}:{}'.format(name,cldata),"{}".format(message.text))
                redis.delete('bottextktime:{}:{}'.format(chatid,message.from_user.id))
                b = redis.get('stmatntime'+str(chatid))
                try:
                    bot.delete_message(chatid,b)
                except Exception as e:
                    print(e)
                loc = 'kytx'
                bot.reply_to(message,"متن شما با موفقیت برای دکمه مورد نظر تنظیم شد!\nبرای ادامه بر روی دکمه تایید بزنید!",reply_markup=taidkeys(loc,name,cldata))
############################
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    chatid = call.message.chat.id
    if call.data.startswith("ans:"):
        userid, usern = call.data.split(':')[1:]
        if is_admin(call.from_user.id,call.from_user.first_name) or call.from_user.id == sudo:
            redis.delete('bot:ans'+str(chatid))
            redis.delete('admin:ans'+str(chatid))
            bot.reply_to(call.message,"درحال ارسال پیام به [ <a href='tg://user?id={}'>{}</a> ] هستید! \n \n لطفا پیامتون رو ارسال کنید! \n \n \n برای انصراف از ارسال پیام بر روی دکمه انصراف بزنید!".format(userid,usern),parse_mode='HTML', disable_web_page_preview=True,reply_markup=cl())
            redis.set('bot:ansmid'+str(chatid),call.message.message_id)
            redis.set('bot:ans'+str(chatid),userid)
            redis.set('admin:ans'+str(chatid),call.from_user.id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای مدیران ربات است!")

    if call.data.startswith("block:"):
        userid, usern = call.data.split(':')[1:]
        if is_admin(call.from_user.id,call.from_user.first_name) or call.from_user.id == sudo:
            if redis.sismember('bot:block', "bl:{}:{}".format(userid,usern)):
                redis.srem('bot:block',"bl:{}:{}".format(userid,usern))
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,reply_markup=ans(userid,usern))
            else:
                redis.sadd('bot:block',"bl:{}:{}".format(userid,usern))
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,reply_markup=ans(userid,usern))
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای مدیران ربات است!")

    if call.data.startswith("sd:"):
        if call.from_user.id == sudo:
            userid,usern = call.data.split(':')[1:]
            redis.srem('bot:sudo',"sd:{}:{}".format(userid,usern))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="کاربر {} از لیست سودو حذف شد!".format(usern))
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=sudol())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data.startswith("bl:"):
        if is_admin(call.from_user.id,call.from_user.first_name) or call.from_user.id == sudo:
            userid,usern = call.data.split(':')[1:]
            redis.srem('bot:block',"bl:{}:{}".format(userid,usern))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="کاربر {} از لیست بلاک حذف شد!".format(usern))
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=blockl())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای مدیران ربات است!")
############Inline###########
    if call.data.startswith("keys:"):
        name, clback = call.data.split(':')[1:]
        if call.from_user.id == sudo:
            txt = redis.get('keytxt:{}:{}'.format(name,clback)) or "None"
            bot.edit_message_text("به پنل تنظیمات دکمه [ {} ] خوش آمدید!\nکالبک دکمه: [   {}   ]\n \nمتن دکمه:\n [ {} ]".format(name,clback,txt),call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=settingkeyp(name,clback))
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data.startswith("delkeys:"):
        name, clback = call.data.split(':')[1:]
        if call.from_user.id == sudo:
            redis.srem('botkeys',"keys:{}:{}".format(name,clback))
            redis.delete('keytxt:{}:{}'.format(name,clback))
            bot.edit_message_text('به پنل مدیریت دکمه های بخش استارت خوش آمدید!\nبرای مدیریت هر دکمه روی آن بزنید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=addkeyin())
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت انجام شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data.startswith("setmatn:"):
        name, clback = call.data.split(':')[1:]
        if call.from_user.id == sudo:
            redis.delete('bottextk:{}:{}'.format(chatid,call.from_user.id))
            redis.delete('stmatntime'+str(chatid))
            loc = 'kytx'
            bot.edit_message_text('متن خود را وارد کنید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=cancfwd(loc))
            redis.set('bottextktime:{}:{}'.format(chatid,call.from_user.id),"{}:{}".format(name,clback))
            redis.set('stmatntime'+str(chatid),call.message.message_id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")


    if call.data.startswith("taidkytx:"):
        name, clback = call.data.split(':')[1:]
        if call.from_user.id == sudo:
            txt = redis.get('keytxt:{}:{}'.format(name,clback)) or "None"
            bot.edit_message_text("به پنل تنظیمات دکمه [ {} ] خوش آمدید!\nکالبک دکمه: [   {}   ]\n \nمتن دکمه:\n [ {} ]".format(name,clback,txt),call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=settingkeyp(name,clback))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت انجام شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data.startswith("delmatn:"):
        name, clback = call.data.split(':')[1:]
        if call.from_user.id == sudo:
            try:
                redis.delete('keytxt:{}:{}'.format(name,clback))
                txt = redis.get('keytxt:{}:{}'.format(name,clback)) or "None"
                bot.edit_message_text("به پنل تنظیمات دکمه [ {} ] خوش آمدید!\nکالبک دکمه: [   {}   ]\n \nمتن دکمه:\n [ {} ]".format(name,clback,txt),call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=settingkeyp(name,clback))
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت انجام شد!")
            except:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="هیچ متنی از قبل برای این دکمه تنظیم نشده بود!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")
 

    if call.data.startswith("showuser:"):
        name, clback = call.data.split(':')[1:]
        txt = redis.get('keytxt:{}:{}'.format(name,clback)) or "None"
        bot.edit_message_text(txt,call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=backwhow())

    if call.data == "gobackshow":
        txt = redis.get('bot:starttext') or "سلام \n پیام خود را ارسال کنید!"
        bot.edit_message_text(txt,call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=keysuser())

##############################
    if call.data == "frwrd":
        if is_admin(call.from_user.id,call.from_user.first_name) or call.from_user.id == sudo:
            bot.edit_message_text("لطفا مقصد فوروارد را مشخص کنید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=fwdpanel())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای مدیران ربات است!")


    if call.data == "sendpost":
        if is_admin(call.from_user.id,call.from_user.first_name) or call.from_user.id == sudo:
            bot.edit_message_text("لطفا مقصد ارسال را مشخص کنید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=sendpostp())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای مدیران ربات است!")



    if call.data == "goback":
        if is_admin(call.from_user.id,call.from_user.first_name) or call.from_user.id == sudo:
            bot.edit_message_text("به پنل مدیران خوش آمدید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=setting())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای مدیران ربات است!")



    if call.data == "sudolist":
        if call.from_user.id == sudo:
            if redis.scard('bot:sudo') == int(0):
                bot.edit_message_text('لیست سودوی ربات خالی است!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=sudol())
            else:
                bot.edit_message_text('به لیست سودو خوش آمدید! \n \nبرای حذف کردن هر فرد از لیست سودو بر روی اسم آن بزنید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=sudol())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "blocklist":
        if is_admin(call.from_user.id,call.from_user.first_name) or call.from_user.id == sudo:
            if redis.scard('bot:block') == int(0):
                bot.edit_message_text('لیست بلاک ربات خالی است!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=blockl())
            else:
                bot.edit_message_text('به لیست بلاک خوش آمدید! \n \nبرای حذف کردن هر فرد از لیست بلاک بر روی اسم آن بزنید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=blockl())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای مدیران ربات است!")


    if call.data == "addsudopanel":
        if call.from_user.id == sudo:
            redis.delete('bot:addsudo'+str(chatid))
            bot.edit_message_text('ایدی عددی فرد را ارسال کنید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=cancsudo())
            redis.set('bot:msgid'+str(chatid),call.message.message_id)
            redis.set('bot:addsudo'+str(chatid),call.from_user.id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "addblockpanel":
        if is_admin(call.from_user.id,call.from_user.first_name) or call.from_user.id == sudo:
            redis.delete('bot:addblock'+str(chatid))
            bot.edit_message_text('ایدی عددی فرد را ارسال کنید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=cancblock())
            redis.set('bot:msgbid'+str(chatid),call.message.message_id)
            redis.set('bot:addblock'+str(chatid),call.from_user.id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای مدیران ربات است!")

    if call.data == "addkeypanel":
        if call.from_user.id == sudo:
            redis.delete('bot:addkey'+str(chatid))
            redis.delete('bot:msgkeyid'+str(chatid))
            bot.edit_message_text('اسم دکمه را وارد کنید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=cancaddkey())
            redis.set('bot:addkey'+str(chatid),call.from_user.id)
            redis.set('bot:msgkeyid'+str(chatid),call.message.message_id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "closekeysadd":
        if call.from_user.id == sudo:
            redis.delete('bot:addkey'+str(chatid))
            redis.delete('bot:msgkeyid'+str(chatid))
            bot.edit_message_text('به پنل مدیریت دکمه های بخش استارت خوش آمدید!\nبرای مدیریت هر دکمه روی آن بزنید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=addkeyin())
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت کنسل شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")


    if call.data == "startsp":
        if call.from_user.id == sudo:
            redis.delete('bot:starttext')
            redis.delete('bot:addstarttext'+str(chatid))
            bot.edit_message_text('متن خود را ارسال نمایید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=cancsttext())
            redis.set('bot:addstarttext'+str(chatid),call.from_user.id)
            redis.set('bot:msgstid'+str(chatid),call.message.message_id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "ersalsp":
        if call.from_user.id == sudo:
            redis.delete('bot:ersaltext')
            redis.delete('bot:addersaltext'+str(chatid))
            loc = 'ersaltxt'
            bot.edit_message_text('متن خود را ارسال نمایید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=cancfwd(loc))
            redis.set('bot:addersaltext'+str(chatid),call.from_user.id)
            redis.delete('bot:msgerid'+str(chatid))
            redis.set('bot:msgerid'+str(chatid),call.message.message_id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")



    if call.data == "fwdpvs":
        if call.from_user.id == sudo:
            redis.delete('bot:addfwdpvs'+str(chatid))
            loc = 'pv'
            bot.edit_message_text('محتوای خود را ارسال نمایید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=cancfwd(loc))
            redis.set('bot:addfwdpvs'+str(chatid),call.from_user.id)
            redis.set('bot:msgfpid'+str(chatid),call.message.message_id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "fwdsgps":
        if call.from_user.id == sudo:
            redis.delete('bot:addfwdsgps'+str(chatid))
            loc = 'sgps'
            bot.edit_message_text('محتوای خود را ارسال نمایید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=cancfwd(loc))
            redis.set('bot:addfwdsgps'+str(chatid),call.from_user.id)
            redis.set('bot:msgfsid'+str(chatid),call.message.message_id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "fwdgp":
        if call.from_user.id == sudo:
            redis.delete('bot:addfwdgp'+str(chatid))
            loc = 'gp'
            bot.edit_message_text('محتوای خود را ارسال نمایید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=cancfwd(loc))
            redis.set('bot:addfwdgp'+str(chatid),call.from_user.id)
            redis.set('bot:msgfgpid'+str(chatid),call.message.message_id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "fwdall":
        if call.from_user.id == sudo:
            redis.delete('bot:addfwdall'+str(chatid))
            loc = 'all'
            bot.edit_message_text('محتوای خود را ارسال نمایید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=cancfwd(loc))
            redis.set('bot:addfwdall'+str(chatid),call.from_user.id)
            redis.set('bot:msgallid'+str(chatid),call.message.message_id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")


    if call.data == "sendpostall":
        if call.from_user.id == sudo:
            redis.delete('bot:addsendall'+str(chatid))
            loc = 'sendall'
            bot.edit_message_text('محتوای خود را ارسال نمایید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=cancfwd(loc))
            redis.set('bot:addsendall'+str(chatid),call.from_user.id)
            redis.set('bot:msgsendallid'+str(chatid),call.message.message_id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "sendpostpv":
        if call.from_user.id == sudo:
            redis.delete('bot:addsendpv'+str(chatid))
            loc = 'sendpv'
            bot.edit_message_text('محتوای خود را ارسال نمایید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=cancfwd(loc))
            redis.set('bot:addsendpv'+str(chatid),call.from_user.id)
            redis.set('bot:msgsendpvid'+str(chatid),call.message.message_id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")


    if call.data == "sendpostsgps":
        if call.from_user.id == sudo:
            redis.delete('bot:addsendsgps'+str(chatid))
            loc = 'sendsgps'
            bot.edit_message_text('محتوای خود را ارسال نمایید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=cancfwd(loc))
            redis.set('bot:addsendsgps'+str(chatid),call.from_user.id)
            redis.set('bot:msgsendsgpsid'+str(chatid),call.message.message_id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")


    if call.data == "sendpostgp":
        if call.from_user.id == sudo:
            redis.delete('bot:addsendgp'+str(chatid))
            loc = 'sendgp'
            bot.edit_message_text('محتوای خود را ارسال نمایید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=cancfwd(loc))
            redis.set('bot:addsendgp'+str(chatid),call.from_user.id)
            redis.set('bot:msgsendgpid'+str(chatid),call.message.message_id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")



    if call.data == "closepv":
        if call.from_user.id == sudo:
            redis.delete('bot:addfwdpvs'+str(chatid))
            redis.delete('bot:msgfpid'+str(chatid))
            bot.edit_message_text("لطفا مقصد فوروارد را مشخص کنید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=fwdpanel())
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت کنسل شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "closesgps":
        if call.from_user.id == sudo:
            redis.delete('bot:addfwdsgps'+str(chatid))
            redis.delete('bot:msgfsid'+str(chatid))
            bot.edit_message_text("لطفا مقصد فوروارد را مشخص کنید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=fwdpanel())
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت کنسل شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "closegp":
        if call.from_user.id == sudo:
            redis.delete('bot:addfwdgp'+str(chatid))
            redis.delete('bot:msgfgpid'+str(chatid))
            bot.edit_message_text("لطفا مقصد فوروارد را مشخص کنید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=fwdpanel())
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت کنسل شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "closeall":
        if call.from_user.id == sudo:
            redis.delete('bot:addfwdall'+str(chatid))
            redis.delete('bot:msgallid'+str(chatid))
            bot.edit_message_text("لطفا مقصد فوروارد را مشخص کنید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=fwdpanel())
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت کنسل شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")



    if call.data == "closesendall":
        if call.from_user.id == sudo:
            redis.delete('bot:addsendall'+str(chatid),call.from_user.id)
            redis.delete('bot:msgsendallid'+str(chatid),call.message.message_id)
            bot.edit_message_text("لطفا مقصد ارسال را مشخص کنید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=sendpostp())
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت کنسل شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "sendpostforone":
        if call.from_user.id == sudo:
            redis.delete('sendiduser'+str(chatid))
            loc = 'sendmsg'
            redis.delete('shaksiid'+str(chatid))
            bot.edit_message_text("لطفا ایدی عددی فرد را وارد کنید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=cancfwd(loc))
            redis.set('shaksiid'+str(chatid),call.message.message_id)
            redis.set('sendiduser'+str(chatid),call.from_user.id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "closesendmsg":
        if call.from_user.id == sudo:
            redis.delete('sendiduser'+str(chatid))
            redis.delete('sendpostid'+str(chatid))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت کنسل شد! \n به صفحه قبل برگشتید!")
            bot.edit_message_text("به پنل مدیران خوش آمدید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=setting())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")



    if call.data == "closesendpv":
        if call.from_user.id == sudo:
            redis.delete('bot:addsendpv'+str(chatid),call.from_user.id)
            redis.delete('bot:msgsendpvid'+str(chatid),call.message.message_id)
            bot.edit_message_text("لطفا مقصد ارسال را مشخص کنید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=sendpostp())
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت کنسل شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")


    if call.data == "closesendsgps":
        if call.from_user.id == sudo:
            redis.delete('bot:addsendsgps'+str(chatid),call.from_user.id)
            redis.delete('bot:msgsendsgpsid'+str(chatid),call.message.message_id)
            bot.edit_message_text("لطفا مقصد ارسال را مشخص کنید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=sendpostp())
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت کنسل شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "closesendgp":
        if call.from_user.id == sudo:
            redis.delete('bot:addsendgp'+str(chatid),call.from_user.id)
            redis.delete('bot:msgsendgpid'+str(chatid),call.message.message_id)
            bot.edit_message_text("لطفا مقصد ارسال را مشخص کنید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=sendpostp())
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت کنسل شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")



    if call.data == "taidsudo":
        if call.from_user.id == sudo:
            bot.edit_message_text('به لیست سودو خوش آمدید! \n \nبرای حذف کردن هر فرد از لیست سودو بر روی اسم آن بزنید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=sudol())
            a = redis.get('bot:msgid'+str(chatid))
            bot.delete_message(chatid,a)
            redis.delete('bot:msgid'+str(chatid))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت انجام شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "taidblock":
        if is_admin(call.from_user.id,call.from_user.first_name) or call.from_user.id == sudo:
            bot.edit_message_text('به لیست بلاک خوش آمدید! \n \nبرای حذف کردن هر فرد از لیست بلاک بر روی اسم آن بزنید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=blockl())
            try:
                a = redis.get('bot:msgbid'+str(chatid))
                bot.delete_message(chatid,a)
                redis.delete('bot:msgbid'+str(chatid))
            except Exception as e:
                print("{}".format(e))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت انجام شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای مدیران ربات است!")

    if call.data == "taidsttext":
        if call.from_user.id == sudo:
            txt = redis.get('bot:starttext') or "متن پیشفرض:\nسلام\n پیام خود را ارسال کنید!"
            bot.edit_message_text('به بخش تنظیم متن استارت خوش آمدید! \n \nمتن فعلی:\n  [ {} ]'.format(txt),call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=starttext())
            a = redis.get('bot:msgstid'+str(chatid))
            bot.delete_message(chatid,a)
            redis.delete('bot:msgstid'+str(chatid))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت انجام شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "taidersaltxt":
        if call.from_user.id == sudo:
            txt = redis.get('bot:ersaltext') or "متن پیشفرض:\nسلام\n پیام خود را ارسال کنید!"
            bot.edit_message_text('به بخش تنظیم متن ارسال خوش آمدید! \n \nمتن فعلی:\n  [ {} ]'.format(txt),call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=ersaltext())
            a = redis.get('bot:msgerid'+str(chatid))
            bot.delete_message(chatid,a)
            redis.delete('bot:msgerid'+str(chatid))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت انجام شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")


    if call.data == "taidpv" or call.data == "taidsgps"  or call.data == "taidgp" or call.data == "taidall":
        if call.from_user.id == sudo:
            bot.edit_message_text("لطفا مقصد فوروارد را مشخص کنید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=fwdpanel())
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت انجام شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "taidsendall" or call.data == "taidsendpv" or call.data == "taidsendsgps" or call.data == "taidsendgp":
        if call.from_user.id == sudo:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت انجام شد! \n به صفحه قبل برگشتید!")
            bot.edit_message_text("لطفا مقصد ارسال را مشخص کنید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=sendpostp())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")


    if call.data == "taidsendmsg":
        if call.from_user.id == sudo:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت انجام شد! \n به صفحه قبل برگشتید!")
            bot.edit_message_text("به پنل مدیران خوش آمدید!",call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=setting())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")


    if call.data == "taidkeys":
        if call.from_user.id == sudo:
            bot.edit_message_text('به پنل مدیریت دکمه های بخش استارت خوش آمدید!\nبرای مدیریت هر دکمه روی آن بزنید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=addkeyin())
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت انجام شد! \n به صفحه قبل برگشتید!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")


    if call.data == "closesudo":
        if call.from_user.id == sudo:
            redis.delete('bot:addsudo'+str(chatid))
            redis.delete('bot:msgid'+str(chatid))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت کنسل شد! \n به صفحه قبل برگشتید!")
            bot.edit_message_text('به لیست سودو خوش آمدید! \n \nبرای حذف کردن هر فرد از لیست سودو بر روی اسم آن بزنید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=sudol())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "closeblock":
        if is_admin(call.from_user.id,call.from_user.first_name) or call.from_user.id == sudo:
            redis.delete('bot:addblock'+str(chatid))
            redis.delete('bot:msgbid'+str(chatid))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت کنسل شد! \n به صفحه قبل برگشتید!")
            bot.edit_message_text('به لیست بلاک خوش آمدید! \n \nبرای حذف کردن هر فرد از لیست بلاک بر روی اسم آن بزنید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=blockl())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای مدیران ربات است!")

    if call.data == "closesttext":
        if call.from_user.id == sudo:
            redis.delete('bot:addstarttext'+str(chatid))
            redis.delete('bot:msgstid'+str(chatid))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت کنسل شد! \n به صفحه قبل برگشتید!")
            txt = redis.get('bot:starttext') or "متن پیشفرض:\nسلام\n پیام خود را ارسال کنید!"
            bot.edit_message_text('به بخش تنظیم متن استارت خوش آمدید! \n \nمتن فعلی:\n  [ {} ]'.format(txt),call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=starttext())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "closeersaltxt":
        if call.from_user.id == sudo:
            redis.delete('bot:addstarttext'+str(chatid))
            redis.delete('bot:msgstid'+str(chatid))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت کنسل شد! \n به صفحه قبل برگشتید!")
            txt = redis.get('bot:ersaltext') or "متن پیشفرض:\nسلام\n پیام خود را ارسال کنید!"
            bot.edit_message_text('به بخش تنظیم متن ارسال خوش آمدید! \n \nمتن فعلی:\n  [ {} ]'.format(txt),call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=ersaltext())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")



    if call.data == "stats":
        if is_admin(call.from_user.id,call.from_user.first_name) or call.from_user.id == sudo:
            bot.edit_message_text('به پنل آمار ربات خوش آمدید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=statspanel())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای مدیران ربات است!")

    if call.data == "setstartmsg":
        if call.from_user.id == sudo:
            txt = redis.get('bot:starttext') or "متن پیشفرض:\nسلام\n پیام خود را ارسال کنید!"
            bot.edit_message_text('به بخش تنظیم متن استارت خوش آمدید! \n \nمتن فعلی:\n  [ {} ]'.format(txt),call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=starttext())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "startpish":
        if call.from_user.id == sudo:
            try:
                redis.delete('bot:starttext')
                txt = redis.get('bot:starttext') or "متن پیشفرض:\nسلام\n پیام خود را ارسال کنید!"
                bot.edit_message_text('به بخش تنظیم متن استارت خوش آمدید! \n \nمتن فعلی:\n  [ {} ]'.format(txt),call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=starttext())
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="متن پیشفرض استارت جایگزین شد!")
            except:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="متن پیشفرض از قبل ست شده بود!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")

    if call.data == "ersalpish":
        if call.from_user.id == sudo:
            try:
                redis.delete('bot:ersaltext')
                txt = redis.get('bot:ersaltext') or "متن پیشفرض:\nپیام شما با موفقیت ارسال شد!"
                bot.edit_message_text('به بخش تنظیم متن ارسال خوش آمدید! \n \nمتن فعلی:\n  [ {} ]'.format(txt),call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=ersaltext())
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="متن پیشفرض ارسال جایگزین شد!")
            except:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="متن پیشفرض از قبل ست شده بود!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")




    if call.data == "setmatnersal":
        if call.from_user.id == sudo:
            txt = redis.get('bot:ersaltext') or "متن پیشفرض:\nپیام شما با موفقیت ارسال شد!"
            bot.edit_message_text('به بخش تنظیم متن ارسال خوش آمدید! \n \nمتن فعلی:\n  [ {} ]'.format(txt),call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=ersaltext())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")


    if call.data == "clickinline":
        if call.from_user.id == sudo:
            bot.edit_message_text('به پنل مدیریت دکمه های بخش استارت خوش آمدید!\nبرای مدیریت هر دکمه روی آن بزنید!',call.message.chat.id,call.message.message_id,call.inline_message_id,reply_markup=addkeyin())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای سازنده اصلی ربات است!")


    if call.data == "closesetting":
        if is_admin(call.from_user.id,call.from_user.first_name) or call.from_user.id == sudo:
            bot.delete_message(chatid,call.message.message_id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای مدیران ربات است!")

    if call.data == "close":
        if is_admin(call.from_user.id,call.from_user.first_name) or call.from_user.id == sudo:
            redis.delete('bot:ans'+str(chatid))
            bot.delete_message(call.message.chat.id,call.message.message_id)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="درخواست شما با موفقیت کنسل شد!")
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="این دستور فقط برای مدیران ربات است!")


bot.polling()