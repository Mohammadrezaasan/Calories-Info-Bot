from turtle import title
from telebot import TeleBot
import telebot
from telebot import types
from markupsafe import Markup
from rsa import PublicKey
import requests
import json
from decimal import *
from config_calories_info_bot import*
"----------------------------------------------------------------------------------------------------------"
bot = telebot.TeleBot(Token)
api  = "https://nutrition-by-api-ninjas.p.rapidapi.com/v1/nutrition"
url = "https://text-translator2.p.rapidapi.com/translate"
"----------------------------------------------------------------------------------------------------------"
@bot.message_handler(commands=['start'])
def handle_start(message):
   chat_id = message.chat.id 
   markup = telebot.types.ReplyKeyboardMarkup(True, False)
   markup.row("👉🏻👉🏻 Click here to start the English version for you 👈🏻👈🏻")
   markup.row('👈🏻👈🏻 اینجا را کلیک کنید تا نسخه فارسی برای شما شروع شود 👉🏻👉🏻')
   bot.send_message(chat_id,'Hello 🙋🏻‍♂️\nwelcome to the Calories Info Bot👾\nسلام 🙋🏻‍♂️\nبه ربات اطلاعات کالری 👾 خوش آمدید', reply_markup=markup)
"----------------------------------------------------------------------------------------------------------"
@bot.message_handler(content_types=['text'])
def handle_text(message):
    message.text = message.text.lower()
    if message.text == "👉🏻👉🏻 click here to start the english version for you 👈🏻👈🏻" : 
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
                info = (response.text.replace("_"," ").strip("[ ]"))
                info1 = { }
                info1 = info
                info2 = json.loads(info1)   
                bot.reply_to(message,"Food Product Name : " +str(info2['name'].title())+"\nServing Size : " + str(info2["serving size g"])+"g"+"\nCalories : " + str(info2["calories"])+'kcal'+"\nProtein : " + str(info2["protein g"])+'g'+"\nTotal Fat : " + str(info2["fat total g"])+'g'+"\nSaturated Fat : " + str(info2["fat saturated g"])+'g'+"\nTotal Carbohydrates : " + str(info2["carbohydrates total g"])+'g'+"\nFiber : " + str(info2["fiber g"])+'g'+"\nSugar : " + str(info2["sugar g"])+'g'+"\nSodium : " + str(info2["sodium mg"])+'mg'+"\nPotassium : " + str(info2["potassium mg"])+'mg'+"\nCholesterol: " + str(info2["cholesterol mg"])+'mg'+"\nNutritional information available at :"+query.replace(":","").title()+"\n-----------------------------------------------------------------------"+"\nsources : \nfdc.nal.usda.gov \nwww.nutritionix.com")
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
    
    elif message.text == '👈🏻👈🏻 اینجا را کلیک کنید تا نسخه فارسی برای شما شروع شود 👉🏻👉🏻' :
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

            name = message.text.replace("نام محصول غذایی","")
            payload = "source_language=fa&target_language=en&text="+name
            headers = {
	     "content-type": "application/x-www-form-urlencoded",
	     "X-RapidAPI-Key":X_RapidAPI_Key,
	     "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
         }

            response1 = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
            info11 = json.loads(response1.text)
            info11=info11['data']['translatedText']
            try :
                
                
            
                querystring = {"query" : info11.replace(":","")}
                headers = {
             "X-RapidAPI-Key": X_RapidAPI_Key,
             "X-RapidAPI-Host": "nutrition-by-api-ninjas.p.rapidapi.com"
            }
                response = requests.request("GET", api, headers=headers, params=querystring)
                if  response.status_code == 200 :   
                    info = (response.text.replace("_"," ").strip("[ ]"))
                    info1 = { }
                    info1 = info
                    info2 = json.loads(info1)   
                    bot.reply_to(message,"نام محصول غذایی :" +name.replace(":","")+"\nمقدار سرو کردن : " + str(info2["serving size g"])+"گرم"+"\nکالری : " + str(info2["calories"])+'کیلو کالری'+"\nپروتئین : " + str(info2["protein g"])+'گرم'+"\nچربی کل : " + str(info2["fat total g"])+'گرم'+"\nچربی های اشباع شده : " + str(info2["fat saturated g"])+'گرم'+"\nکربوهیدرات کل : " + str(info2["carbohydrates total g"])+'گرم'+"\nفیبر : " + str(info2["fiber g"])+'گرم'+"\nقند : " + str(info2["sugar g"])+'گرم'+"\nسدیم : " + str(info2["sodium mg"])+'میلی گرم'+"\nپتاسیم : " + str(info2["potassium mg"])+'میلی گرم'+"\nکلسترول : " + str(info2["cholesterol mg"])+'میلی گرم'+"\nاطلاعات تغذیه ای موجود در :"+name.replace(":","")+"\n-----------------------------------------------------------------------"+"\nمنابع: \nfdc.nal.usda.gov\nwww.nutritionix.com")
            except :
                bot.reply_to(message,"🔴🔴 مطمئن شوید که غلط املایی وجود ندارد 🔴🔴")    

    elif message.text == "بازگشت به صفحه انتخاب نسخه 🔙" :
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("👉🏻👉🏻 Click here to start the English version for you 👈🏻👈🏻")
        markup.row('👈🏻👈🏻 اینجا را کلیک کنید تا نسخه فارسی برای شما شروع شود 👉🏻👉🏻')
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
        markup.row("👉🏻👉🏻 Click here to start the English version for you 👈🏻👈🏻")
        markup.row('👈🏻👈🏻 اینجا را کلیک کنید تا نسخه فارسی برای شما شروع شود 👉🏻👉🏻')
        bot.send_message(chat_id,'Return to version selection page was successful ✅', reply_markup=markup)


    
"----------------------------------------------------------------------------------------------------------"
bot.polling(none_stop=True)
