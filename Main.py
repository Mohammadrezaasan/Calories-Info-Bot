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
   markup.row("ðð»ðð» Click here to start the English version for you ðð»ðð»")
   markup.row('ðð»ðð» Ø§ÛÙØ¬Ø§ Ø±Ø§ Ú©ÙÛÚ© Ú©ÙÛØ¯ ØªØ§ ÙØ³Ø®Ù ÙØ§Ø±Ø³Û Ø¨Ø±Ø§Û Ø´ÙØ§ Ø´Ø±ÙØ¹ Ø´ÙØ¯ ðð»ðð»')
   bot.send_message(chat_id,'Hello ðð»ââï¸\nwelcome to the Calories Info Botð¾\nØ³ÙØ§Ù ðð»ââï¸\nØ¨Ù Ø±Ø¨Ø§Øª Ø§Ø·ÙØ§Ø¹Ø§Øª Ú©Ø§ÙØ±Û ð¾ Ø®ÙØ´ Ø¢ÙØ¯ÛØ¯', reply_markup=markup)
"----------------------------------------------------------------------------------------------------------"
@bot.message_handler(content_types=['text'])
def handle_text(message):
    message.text = message.text.lower()
    if message.text == "ðð»ðð» click here to start the english version for you ðð»ðð»" : 
        text = "`"+"Food Product Name : "+"`"
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("ð´To do the steps correctly,pay attention toð´\nthe example below")
        markup.row('ðð»ðð» For example,type like this ðð»ðð»')
        markup.row("Food Product Name : 250g Grilled Chicken ")
        markup.row("ð List of information ð")
        markup.row("Return to version selection page ð")
        bot.send_message(chat_id,'English version started successfully â',reply_markup=markup) 
        bot.send_message(chat_id,"ð´ð´ IMPORTANT ð´ð´\nTo enter the name of the food product you want, click on the text below and add the name of the food product you want to the end of the text.",reply_markup=markup) 
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
                bot.reply_to(message,"Food Product Name : " +str(final_calories_info['name'].title())+"\nServing Size : " + str(final_calories_info["serving size g"])+"g"+"\nCalories : " + str(final_calories_info["calories"])+'kcal'+"\nProtein : " + str(final_calories_info["protein g"])+'g'+"\nTotal Fat : " + str(final_calories_info["fat total g"])+'g'+"\nSaturated Fat : " + str(final_calories_info["fat saturated g"])+'g'+"\nTotal Carbohydrates : " + str(final_calories_info["carbohydrates total g"])+'g'+"\nFiber : " + str(final_calories_info["fiber g"])+'g'+"\nSugar : " + str(final_calories_info["sugar g"])+'g'+"\nSodium : " + str(final_calories_info["sodium mg"])+'mg'+"\nPotassium : " + str(final_calories_info["potassium mg"])+'mg'+"\nCholesterol: " + str(final_calories_info["cholesterol mg"])+'mg'+"\nNutritional information available at :"+query.replace(":","").title()+"\n-----------------------------------------------------------------------"+"\nsources : \nfdc.nal.usda.gov \nwww.nutritionix.com")
        except :
            bot.reply_to(message,'ð´ð´ Make sure your sentence is spelled correctly ð´ð´')    
    
    elif message.text == 'ð list of information ð' :
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
        markup.row('Return to main page â©ï¸')
        bot.send_message(chat_id,'List of information opened successfully â', reply_markup=markup)
    
    elif message.text == 'return to main page â©ï¸' : 
        text = "`"+"Food Product Name : "+"`"
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("ð´To do the steps correctly,pay attention toð´\nthe example below")
        markup.row('ðð»ðð» For example,type like this ðð»ðð»')
        markup.row("Food Product Name : 250g Grilled Chicken ")
        markup.row("ð List of information ð")
        markup.row("Return to version selection page ð")
        bot.send_message(chat_id,'Return to main page was successful â', reply_markup=markup)
        bot.send_message(chat_id,"ð´ð´ IMPORTANT ð´ð´\nTo enter the name of the food product you want, click on the text below and add the name of the food product you want to the end of the text.",reply_markup=markup) 
        bot.send_message(chat_id,text,parse_mode='MarkdownV2')      
    
    
    elif message.text in info_en : 
        bot.reply_to(message,info_en[message.text])
    
    elif message.text == 'ðð»ðð» Ø§ÛÙØ¬Ø§ Ø±Ø§ Ú©ÙÛÚ© Ú©ÙÛØ¯ ØªØ§ ÙØ³Ø®Ù ÙØ§Ø±Ø³Û Ø¨Ø±Ø§Û Ø´ÙØ§ Ø´Ø±ÙØ¹ Ø´ÙØ¯ ðð»ðð»' :
        text2 = "`"+"ÙØ§Ù ÙØ­ØµÙÙ ØºØ°Ø§ÛÛ :"+"`"
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("ð´Ø¨Ø±Ø§Û Ø§ÙØ¬Ø§Ù ØµØ­ÛØ­ ÙØ±Ø§Ø­Ù Ø¨Ù ÙØ«Ø§Ù Ø²ÛØ± ØªÙØ¬Ù Ú©ÙÛØ¯ð´")
        markup.row("ðð»ðð»ÙØ«ÙØ§ Ø§ÛÙØ¬ÙØ±Û ØªØ§ÛÙ¾ Ú©ÙÛØ¯ðð»ðð»")
        markup.row('ÙØ§Ù ÙØ­ØµÙÙ ØºØ°Ø§ÛÛ : 250 Ú¯Ø±Ù ÙØ±Øº Ú¯Ø±ÛÙ Ø´Ø¯Ù')
        markup.row("ð ÙÛØ³Øª Ø§Ø·ÙØ§Ø¹Ø§Øª ð")
        markup.row("Ø¨Ø§Ø²Ú¯Ø´Øª Ø¨Ù ØµÙØ­Ù Ø§ÙØªØ®Ø§Ø¨ ÙØ³Ø®Ù ð")
        bot.send_message(chat_id,'ÙØ³Ø®Ù ÙØ§Ø±Ø³Û Ø¨Ø§ ÙÙÙÙÛØª Ø´Ø±ÙØ¹ Ø´Ø¯ â', reply_markup=markup) 
        bot.send_message(chat_id,"ð´ð´ ÙÙÙ ð´ð´\nØ¨Ø±Ø§Û ÙØ§Ø±Ø¯ Ú©Ø±Ø¯Ù ÙØ§Ù ÙØ­ØµÙÙ ØºØ°Ø§ÛÛ ÙÙØ±Ø¯ ÙØ¸Ø± Ø®ÙØ¯ Ø¨Ø± Ø±ÙÛ ÙØªÙ Ø²ÛØ± Ú©ÙÛÚ© Ú©ÙÛØ¯ Ù ÙØ§Ù ÙØ­ØµÙÙ ØºØ°Ø§ÛÛ ÙÙØ±Ø¯ ÙØ¸Ø± Ø®ÙØ¯ Ø±Ø§ Ø¨Ù Ø§ÙØªÙØ§Û ÙØªÙ Ø§Ø¶Ø§ÙÙ Ú©ÙÛØ¯.")
        bot.send_message(chat_id,text2,parse_mode='MarkdownV2')      
    
    elif 'ÙØ§Ù ÙØ­ØµÙÙ ØºØ°Ø§ÛÛ' in  message.text : 
        if 'ÙØ§Ù ÙØ­ØµÙÙ ØºØ°Ø§ÛÛ' in message.text:

            food_tr = message.text.replace("ÙØ§Ù ÙØ­ØµÙÙ ØºØ°Ø§ÛÛ","")
            payload = "source_language=fa&target_language=en&text="+food_tr
            headers = {
	     "content-type": "application/x-www-form-urlencoded",
	     "X-RapidAPI-Key":X_RapidAPI_Key,
	     "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
         }

            response_tr = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
            tr_text = json.loads(response_tr.text)
            tr_text=tr_text['data']['translatedText']
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
                    payload = "source_language=en&target_language=fa&text="+final_calories_info['name']
                    headers = {
                "content-type": "application/x-www-form-urlencoded",
                "X-RapidAPI-Key":X_RapidAPI_Key,
                "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
                }
                    response_tr = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
                    tr_text_fa = json.loads(response_tr.text)
                    tr_text_fa = tr_text_fa['data']['translatedText']  
                    
                    bot.reply_to(message,"ÙØ§Ù ÙØ­ØµÙÙ ØºØ°Ø§ÛÛ : " +tr_text_fa+"\nÙÙØ¯Ø§Ø± Ø³Ø±Ù Ú©Ø±Ø¯Ù : " + str(final_calories_info["serving size g"])+"Ú¯Ø±Ù"+"\nÚ©Ø§ÙØ±Û : " + str(final_calories_info["calories"])+'Ú©ÛÙÙ Ú©Ø§ÙØ±Û'+"\nÙ¾Ø±ÙØªØ¦ÛÙ : " + str(final_calories_info["protein g"])+'Ú¯Ø±Ù'+"\nÚØ±Ø¨Û Ú©Ù : " + str(final_calories_info["fat total g"])+'Ú¯Ø±Ù'+"\nÚØ±Ø¨Û ÙØ§Û Ø§Ø´Ø¨Ø§Ø¹ Ø´Ø¯Ù : " + str(final_calories_info["fat saturated g"])+'Ú¯Ø±Ù'+"\nÚ©Ø±Ø¨ÙÙÛØ¯Ø±Ø§Øª Ú©Ù : " + str(final_calories_info["carbohydrates total g"])+'Ú¯Ø±Ù'+"\nÙÛØ¨Ø± : " + str(final_calories_info["fiber g"])+'Ú¯Ø±Ù'+"\nÙÙØ¯ : " + str(final_calories_info["sugar g"])+'Ú¯Ø±Ù'+"\nØ³Ø¯ÛÙ : " + str(final_calories_info["sodium mg"])+'ÙÛÙÛ Ú¯Ø±Ù'+"\nÙ¾ØªØ§Ø³ÛÙ : " + str(final_calories_info["potassium mg"])+'ÙÛÙÛ Ú¯Ø±Ù'+"\nÚ©ÙØ³ØªØ±ÙÙ : " + str(final_calories_info["cholesterol mg"])+'ÙÛÙÛ Ú¯Ø±Ù'+"\nØ§Ø·ÙØ§Ø¹Ø§Øª ØªØºØ°ÛÙ Ø§Û ÙÙØ¬ÙØ¯ Ø¯Ø± : "+tr_text_fa+"\n-----------------------------------------------------------------------"+"\nÙÙØ§Ø¨Ø¹: \nfdc.nal.usda.gov\nwww.nutritionix.com")
            except :
                bot.reply_to(message,"ð´ð´ ÙØ·ÙØ¦Ù Ø´ÙÛØ¯ Ú©Ù ØºÙØ· Ø§ÙÙØ§ÛÛ ÙØ¬ÙØ¯ ÙØ¯Ø§Ø±Ø¯ ð´ð´")    

    elif message.text == "Ø¨Ø§Ø²Ú¯Ø´Øª Ø¨Ù ØµÙØ­Ù Ø§ÙØªØ®Ø§Ø¨ ÙØ³Ø®Ù ð" :
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("ðð»ðð» Click here to start the English version for you ðð»ðð»")
        markup.row('ðð»ðð» Ø§ÛÙØ¬Ø§ Ø±Ø§ Ú©ÙÛÚ© Ú©ÙÛØ¯ ØªØ§ ÙØ³Ø®Ù ÙØ§Ø±Ø³Û Ø¨Ø±Ø§Û Ø´ÙØ§ Ø´Ø±ÙØ¹ Ø´ÙØ¯ ðð»ðð»')
        bot.send_message(chat_id,'Ø¨Ø§Ø²Ú¯Ø´Øª Ø¨Ù ØµÙØ­Ù Ø§ÙØªØ®Ø§Ø¨ ÙØ³Ø®Ù Ø¨Ø§ ÙÙÙÙÛØª Ø§ÙØ¬Ø§Ù Ø´Ø¯ â', reply_markup=markup)

    elif message.text == 'ð ÙÛØ³Øª Ø§Ø·ÙØ§Ø¹Ø§Øª ð' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('ÙÙØ¯ ÙÛÙÙ ÙØ¶Ø± Ø§Ø³Øª ÛØ§ Ø®ÙØ¨Ø')
        markup.row('Ø¢ÛØ§ ÙØ±ÙÚ©ØªÙØ² ÛÚ© ÙÙØ¯ Ø·Ø¨ÛØ¹Û Ø§Ø³Øª ÛØ§ Ø§ÙØ²ÙØ¯ÙÛØ' )
        markup.row('Ú©Ø§ÙØ±Û ÚÛØ³ØªØ')
        markup.row('Ù¾Ø±ÙØªØ¦ÛÙ ÚÛØ³ØªØ')
        markup.row('ÚØ±Ø¨Û ÚÛØ³ØªØ')
        markup.row('Ú©Ø±Ø¨ÙÙÛØ¯Ø±Ø§Øª Ú©Ù ÚÛØ³ØªØ')
        markup.row('ÚØ±Ø¨Û Ø§Ø´Ø¨Ø§Ø¹ ÚÛØ³ØªØ')
        markup.row('ÙÛØ¨Ø± ØºØ°Ø§ÛÛ ÚÛØ³ØªØ')
        markup.row('Ø³Ø¯ÛÙ ÚÛØ³ØªØ')
        markup.row('Ù¾ØªØ§Ø³ÛÙ ÚÛØ³ØªØ')
        markup.row('Ú©ÙØ³ØªØ±ÙÙ ÚÛØ³ØªØ')
        markup.row('Ø¨Ø§Ø²Ú¯Ø´Øª Ø¨Ù ØµÙØ­Ù Ø§ØµÙÛ â©ï¸')
        bot.send_message(chat_id,'ÙÛØ³Øª Ø§Ø·ÙØ§Ø¹Ø§Øª Ø¨Ø§ ÙÙÙÙÛØª Ø¨Ø§Ø² Ø´Ø¯â', reply_markup=markup)
    

    elif message.text in info_fa :
        bot.reply_to(message,info_fa[message.text]+("\nØ¨Ø±Ø§Û ØªØ±Ø¬ÙÙ Ø§ÛÙ ÙØªÙ Ø§ÙÚ¯ÙÛØ³Û Ø¢Ù Ø±Ø§ Ú©Ù¾Û Ú©ÙÛØ¯ Ù Ø±ÙÛ Ø¢Ø¯Ø±Ø³ Ø§ÛÙ Ø³Ø§ÛØª Ú©ÙÛÚ© Ú©ÙÛØ¯ |translate.google.com/?sl=en&tl=fa&op=translate|  Ù Ø¢Ù ÙØªÙ Ø±Ø§ Ø¯Ø± ÙØ³ÙØª Ø§ÙÚ¯ÙÛØ³Û ÙØ±Ø§Ø± Ø¯ÙÛØ¯ Ù ØªØ±Ø¬ÙÙ Ø¢Ù Ø±Ø§ Ø¯Ø±ÛØ§ÙØª Ø®ÙØ§ÙÛØ¯ Ú©Ø±Ø¯. "))

    elif message.text =="Ø¨Ø§Ø²Ú¯Ø´Øª Ø¨Ù ØµÙØ­Ù Ø§ØµÙÛ â©ï¸":
        text2 = "`"+"ÙØ§Ù ÙØ­ØµÙÙ ØºØ°Ø§ÛÛ :"+"`"
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("ð´Ø¨Ø±Ø§Û Ø§ÙØ¬Ø§Ù ØµØ­ÛØ­ ÙØ±Ø§Ø­Ù Ø¨Ù ÙØ«Ø§Ù Ø²ÛØ± ØªÙØ¬Ù Ú©ÙÛØ¯ð´")
        markup.row("ðð»ðð»ÙØ«ÙØ§ Ø§ÛÙØ¬ÙØ±Û ØªØ§ÛÙ¾ Ú©ÙÛØ¯ðð»ðð»")
        markup.row('ÙØ§Ù ÙØ­ØµÙÙ ØºØ°Ø§ÛÛ : 250 Ú¯Ø±Ù ÙØ±Øº Ú¯Ø±ÛÙ Ø´Ø¯Ù')
        markup.row("ð ÙÛØ³Øª Ø§Ø·ÙØ§Ø¹Ø§Øª ð")
        markup.row("Ø¨Ø§Ø²Ú¯Ø´Øª Ø¨Ù ØµÙØ­Ù Ø§ÙØªØ®Ø§Ø¨ ÙØ³Ø®Ù ð")
        bot.send_message(chat_id,'Ø¨Ø§Ø²Ú¯Ø´Øª Ø¨Ù ØµÙØ­Ù Ø§ØµÙÛ Ø¨Ø§ ÙÙÙÙÛØª Ø§ÙØ¬Ø§Ù Ø´Ø¯ â', reply_markup=markup) 
        bot.send_message(chat_id,"ð´ð´ ÙÙÙ ð´ð´\nØ¨Ø±Ø§Û ÙØ§Ø±Ø¯ Ú©Ø±Ø¯Ù ÙØ§Ù ÙØ­ØµÙÙ ØºØ°Ø§ÛÛ ÙÙØ±Ø¯ ÙØ¸Ø± Ø®ÙØ¯ Ø¨Ø± Ø±ÙÛ ÙØªÙ Ø²ÛØ± Ú©ÙÛÚ© Ú©ÙÛØ¯ Ù ÙØ§Ù ÙØ­ØµÙÙ ØºØ°Ø§ÛÛ ÙÙØ±Ø¯ ÙØ¸Ø± Ø®ÙØ¯ Ø±Ø§ Ø¨Ù Ø§ÙØªÙØ§Û ÙØªÙ Ø§Ø¶Ø§ÙÙ Ú©ÙÛØ¯.")
        bot.send_message(chat_id,text2,parse_mode='MarkdownV2')      
    
    
    elif message.text == "return to version selection page ð" : 
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("ðð»ðð» Click here to start the English version for you ðð»ðð»")
        markup.row('ðð»ðð» Ø§ÛÙØ¬Ø§ Ø±Ø§ Ú©ÙÛÚ© Ú©ÙÛØ¯ ØªØ§ ÙØ³Ø®Ù ÙØ§Ø±Ø³Û Ø¨Ø±Ø§Û Ø´ÙØ§ Ø´Ø±ÙØ¹ Ø´ÙØ¯ ðð»ðð»')
        bot.send_message(chat_id,'Return to version selection page was successful â', reply_markup=markup)


    
"----------------------------------------------------------------------------------------------------------"
bot.polling(none_stop=True)
