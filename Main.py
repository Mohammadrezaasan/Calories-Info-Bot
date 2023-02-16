
from turtle import title
from telebot import TeleBot
import telebot
from telebot import types
from markupsafe import Markup
from rsa import PublicKey
import requests
import json
from decimal import *
from calories_info_config import*
"----------------------------------------------------------------------------------------------------------"
bot = telebot.TeleBot(Token)
api  = "https://nutrition-by-api-ninjas.p.rapidapi.com/v1/nutrition"
"----------------------------------------------------------------------------"
@bot.message_handler(commands=['start'])
def handle_start(message):
   chat_id = message.chat.id 
   markup = telebot.types.ReplyKeyboardMarkup(True, False)
   markup.row("👉🏻👉🏻 Click to start the English version 👈🏻👈🏻")
   markup.row('👈🏻👈🏻 کلیک کنید تا نسخه فارسی برای شما شروع شود 👉🏻👉🏻')
   bot.send_message(chat_id,'Hello 🙋🏻‍♂️\nwelcome to the Calories Info Bot👾\nسلام 🙋🏻‍♂️\nبه ربات اطلاعات کالری 👾 خوش آمدید', reply_markup=markup)
"----------------------------------------------------------------------------------------------------------"
@bot.message_handler(content_types=['text'])
def handle_text(message):
    message.text = message.text.lower()
    if message.text == "👉🏻👉🏻 click to start the english version 👈🏻👈🏻" : 
        text = "`"+"Food Product Name : "+"`"
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("🔴To do the steps correctly,pay attention to🔴\nthe example below")
        markup.row('👇🏻👇🏻 For example,type like this 👇🏻👇🏻')
        markup.row("Food Product Name : 250g Grilled Chicken ")
        markup.row("📒 List of information 📒")
        markup.row("Return to version selection page 🔙")
        bot.send_message(chat_id,'English version started successfully ✅',reply_markup=markup) 
        bot.send_message(chat_id,"🔴🔴 IMPORTANT 🔴🔴\nTo enter the name of the food product you want, click on the text below and add the name of the food product you want to the end of the text.",reply_markup=markup) 
        bot.send_message(chat_id,text,parse_mode='MarkdownV2')      
    
    elif 'food product name' in  message.text : 
        try :
            query = message.text.replace('food product name','')
			
        
            querystring = {"query" : query.replace(":","")}
            headers = {
         "X-RapidAPI-Key": X_RapidAPI_Key,
         "X-RapidAPI-Host": "nutrition-by-api-ninjas.p.rapidapi.com"
        }
            response = requests.request("GET", api, headers=headers, params=querystring)
            if  response.status_code == 200 :   
                info_calories = (response.text.replace("_"," ").strip("[ ]"))
                info_calories_v2 = { }
                info_calories_v2 = info_calories
                final_calories_info = json.loads(info_calories_v2)   
                bot.reply_to(message,"Food Product Name : " +str(final_calories_info['name'].title())+"\n-----------------------------------------------------------------------"+"\nServing Size : " + str(final_calories_info["serving size g"])+"g"+"\n-----------------------------------------------------------------------"+"\nCalories : " + str(final_calories_info["calories"])+'kcal'+"\n-----------------------------------------------------------------------"+"\nProtein : " + str(final_calories_info["protein g"])+'g'+"\n-----------------------------------------------------------------------"+"\nTotal Fat : " + str(final_calories_info["fat total g"])+'g'+"\n-----------------------------------------------------------------------"+"\nSaturated Fat : " + str(final_calories_info["fat saturated g"])+'g'+"\n-----------------------------------------------------------------------"+"\nTotal Carbohydrates : " + str(final_calories_info["carbohydrates total g"])+'g'+"\n-----------------------------------------------------------------------"+"\nFiber : " + str(final_calories_info["fiber g"])+'g'+"\n-----------------------------------------------------------------------"+"\nSugar : " + str(final_calories_info["sugar g"])+'g'+"\n-----------------------------------------------------------------------"+"\nSodium : " + str(final_calories_info["sodium mg"])+'mg'+"\n-----------------------------------------------------------------------"+"\nPotassium : " + str(final_calories_info["potassium mg"])+'mg'+"\n-----------------------------------------------------------------------"+"\nCholesterol: " + str(final_calories_info["cholesterol mg"])+'mg'+"\n-----------------------------------------------------------------------"+"\nNutritional information available at :\n"+query.replace(":","").title()+"\n-----------------------------------------------------------------------"+"\nsources : \nfdc.nal.usda.gov \nwww.nutritionix.com")
        except :
            bot.reply_to(message,'🔴🔴 Make sure your sentence is spelled correctly 🔴🔴')    
    
    elif message.text == '📒 list of information 📒' :
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('Fruit Sugar Is Bad Or Good?')
        markup.row('Is Fructose A Natural Or Added Sugar?')
        markup.row('What Is Calories?')
        markup.row('What Is Protein?')
        markup.row('What Is Fat?')
        markup.row('What Is Total Carbs?')
        markup.row('What Is Saturated Fat?')
        markup.row('What Is Dietary Fiber?')
        markup.row('What Is Sodium ?')
        markup.row('What Is Potassium ?')
        markup.row('What Is Cholesterol ?')
        markup.row('Return to main page ↩️')
        bot.send_message(chat_id,'List of information opened successfully ✅', reply_markup=markup)
    
    elif message.text == 'return to main page ↩️' : 
        text = "`"+"Food Product Name : "+"`"
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("🔴To do the steps correctly,pay attention to🔴\nthe example below")
        markup.row('👇🏻👇🏻 For example,type like this 👇🏻👇🏻')
        markup.row("Food Product Name : 250g Grilled Chicken ")
        markup.row("📒 List of information 📒")
        markup.row("Return to version selection page 🔙")
        bot.send_message(chat_id,'Return to main page was successful ✅', reply_markup=markup)
        bot.send_message(chat_id,"🔴🔴 IMPORTANT 🔴🔴\nTo enter the name of the food product you want, click on the text below and add the name of the food product you want to the end of the text.",reply_markup=markup) 
        bot.send_message(chat_id,text,parse_mode='MarkdownV2')      
    
    
    elif message.text in info_en : 
        bot.reply_to(message,info_en[message.text])
    
    elif message.text == '👈🏻👈🏻 کلیک کنید تا نسخه فارسی برای شما شروع شود 👉🏻👉🏻' :
        text2 = "`"+"نام محصول غذایی :"+"`"
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("🔴برای انجام صحیح مراحل به مثال زیر توجه کنید🔴")
        markup.row("👇🏻👇🏻مثلا اینجوری تایپ کنید👇🏻👇🏻")
        markup.row('نام محصول غذایی : 250 گرم مرغ گریل شده')
        markup.row("📒 لیست اطلاعات 📒")
        markup.row("بازگشت به صفحه انتخاب نسخه 🔙")
        bot.send_message(chat_id,'نسخه فارسی با موفقیت شروع شد ✅', reply_markup=markup) 
        bot.send_message(chat_id,"🔴🔴 مهم 🔴🔴\nبرای وارد کردن نام محصول غذایی مورد نظر خود بر روی متن زیر کلیک کنید و نام محصول غذایی مورد نظر خود را به انتهای متن اضافه کنید.")
        bot.send_message(chat_id,text2,parse_mode='MarkdownV2')      
    
    elif 'نام محصول غذایی' in  message.text : 
        if 'نام محصول غذایی' in message.text:

            food_tr = message.text.replace("نام محصول غذایی","")
            import translators as ts
            import translators.server as tss

            wyw_text = food_tr

            from_language, to_language = 'fa', 'en'


            tr_text = (tss.google(wyw_text, from_language, to_language))
            try :
                
                
            
                querystring = {"query" : tr_text.replace(":","")}
                headers = {
                 "X-RapidAPI-Key": X_RapidAPI_Key,
                 "X-RapidAPI-Host": "nutrition-by-api-ninjas.p.rapidapi.com"
                 }
                response_food = requests.request("GET", api, headers=headers, params=querystring)
           
                if  response_food.status_code == 200 :   
                    info_calories = (response_food.text.replace("_"," ").strip("[ ]"))
                    info_calories_v2 = { }
                    info_calories_v2 = info_calories
                    final_calories_info = json.loads(info_calories_v2) 
                    wyw_text = final_calories_info['name']
                    from_language, to_language = 'en', 'fa'
                    tr_text_fa = (tss.google(wyw_text, from_language, to_language))
                    
                    bot.reply_to(message,"نام محصول غذایی : " +tr_text_fa+"\n-----------------------------------------------------------------------"+"\nمقدار سرو کردن : " + str(final_calories_info["serving size g"])+"گرم"+"\n-----------------------------------------------------------------------"+"\nکالری : " + str(final_calories_info["calories"])+'کیلو کالری'+"\n-----------------------------------------------------------------------"+"\nپروتئین : " + str(final_calories_info["protein g"])+'گرم'+"\n-----------------------------------------------------------------------"+"\nچربی کل : " + str(final_calories_info["fat total g"])+'گرم'+"\n-----------------------------------------------------------------------"+"\nچربی های اشباع شده : " + str(final_calories_info["fat saturated g"])+'گرم'+"\n-----------------------------------------------------------------------"+"\nکربوهیدرات کل : " + str(final_calories_info["carbohydrates total g"])+'گرم'+"\n-----------------------------------------------------------------------"+"\nفیبر : " + str(final_calories_info["fiber g"])+'گرم'+"\n-----------------------------------------------------------------------"+"\nقند : " + str(final_calories_info["sugar g"])+'گرم'+"\n-----------------------------------------------------------------------"+"\nسدیم : " + str(final_calories_info["sodium mg"])+'میلی گرم'+"\n-----------------------------------------------------------------------"+"\nپتاسیم : " + str(final_calories_info["potassium mg"])+'میلی گرم'+"\n-----------------------------------------------------------------------"+"\nکلسترول : " + str(final_calories_info["cholesterol mg"])+'میلی گرم'+"\n-----------------------------------------------------------------------"+"\nاطلاعات تغذیه ای موجود در : \n"+tr_text_fa+"\n-----------------------------------------------------------------------"+"\nمنابع: \nfdc.nal.usda.gov\nwww.nutritionix.com")
            except :
                bot.reply_to(message,"🔴🔴 مطمئن شوید که غلط املایی وجود ندارد 🔴🔴")    

    elif message.text == "بازگشت به صفحه انتخاب نسخه 🔙" :
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("👉🏻👉🏻 Click to start the English version 👈🏻👈🏻")
        markup.row('👈🏻👈🏻 کلیک کنید تا نسخه فارسی برای شما شروع شود 👉🏻👉🏻')
        bot.send_message(chat_id,'بازگشت به صفحه انتخاب نسخه با موفقیت انجام شد ✅', reply_markup=markup)

    elif message.text == '📒 لیست اطلاعات 📒' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('قند میوه مضر است یا خوب؟')
        markup.row('آیا فروکتوز یک قند طبیعی است یا افزودنی؟' )
        markup.row('کالری چیست؟')
        markup.row('پروتئین چیست؟')
        markup.row('چربی چیست؟')
        markup.row('کربوهیدرات کل چیست؟')
        markup.row('چربی اشباع چیست؟')
        markup.row('فیبر غذایی چیست؟')
        markup.row('سدیم چیست؟')
        markup.row('پتاسیم چیست؟')
        markup.row('کلسترول چیست؟')
        markup.row('بازگشت به صفحه اصلی ↩️')
        bot.send_message(chat_id,'لیست اطلاعات با موفقیت باز شد✅', reply_markup=markup)
    

    elif message.text in info_fa :
        bot.reply_to(message,info_fa[message.text]+("\nبرای ترجمه این متن انگلیسی آن را کپی کنید و روی آدرس این سایت کلیک کنید |translate.google.com/?sl=en&tl=fa&op=translate|  و آن متن را در قسمت انگلیسی قرار دهید و ترجمه آن را دریافت خواهید کرد. "))

    elif message.text =="بازگشت به صفحه اصلی ↩️":
        text2 = "`"+"نام محصول غذایی :"+"`"
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("🔴برای انجام صحیح مراحل به مثال زیر توجه کنید🔴")
        markup.row("👇🏻👇🏻مثلا اینجوری تایپ کنید👇🏻👇🏻")
        markup.row('نام محصول غذایی : 250 گرم مرغ گریل شده')
        markup.row("📒 لیست اطلاعات 📒")
        markup.row("بازگشت به صفحه انتخاب نسخه 🔙")
        bot.send_message(chat_id,'بازگشت به صفحه اصلی با موفقیت انجام شد ✅', reply_markup=markup) 
        bot.send_message(chat_id,"🔴🔴 مهم 🔴🔴\nبرای وارد کردن نام محصول غذایی مورد نظر خود بر روی متن زیر کلیک کنید و نام محصول غذایی مورد نظر خود را به انتهای متن اضافه کنید.")
        bot.send_message(chat_id,text2,parse_mode='MarkdownV2')      
    
    
    elif message.text == "return to version selection page 🔙" : 
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("👉🏻👉🏻 Click to start the English version 👈🏻👈🏻")
        markup.row('👈🏻👈🏻 کلیک کنید تا نسخه فارسی برای شما شروع شود 👉🏻👉🏻')
        bot.send_message(chat_id,'Return to version selection page was successful ✅', reply_markup=markup)


    
"----------------------------------------------------------------------------------------------------------"
bot.polling(none_stop=True)
