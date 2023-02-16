![7CC975D7-0771-41D4-A30F-5F676ED1C7CF](https://user-images.githubusercontent.com/108104864/188773080-4df88b6d-957e-4b58-a86a-b2a2f628dc5d.jpeg)


## <p align="center"> <a href="https://github.com/Mohammadrezaasan/Calories-Info-Bot/blob/main/README_FA.md">برای دریافت نسخه فارسی اینجا کلیک کنید </a></p>


## <p align="center">With a few simple clicks and entering the name of the food product you want, get the amount of calories, protein, total fat, saturated fat, total carbohydrate, fiber, sugar, sodium, potassium, cholesterol contained in the food product <a href="https://t.me/Calories_Info_Robot">Calories Info Bot</a>.</p>

## <p align="center">Bot API Source : <a href="https://fdc.nal.usda.gov"> U.S. DEPARTMENT OF AGRICULTURE</a>

## Contents

* [Languages and Tools used in bot](#languages-and-tools-used-in-bot)

* [Getting started](#getting-started)

* [Next step](#next-step)
	
* [Codes docs](#codes-docs)
	
* [Keyword guide](#keyword-guide)

* [List of information stored in the bot](#list-of-information-stored-in-the-bot)
	
* [How does the bot respond to keywords?](#how-does-the-bot-respond-to-keywords)
## Languages and Tools used in bot

* Python 3.10
* REST API
* <a href="https://pypi.org/project/pyTelegramBotAPI/">Telebot Library</a>
* <a href="https://github.com/uliontse/translators#from-pypi">Translation Library</a>

## Getting started


* To start the project, we need to build a robot that was built with the help of the <a href="https://t.me/BotFather">Bot Father</a> 

* When your bot is built, the Bot Father will give you a token at the end { You put that token in the token variable in the config file } 

```
bot = telebot.TeleBot(Token_bot)
```
 ## Next step
 * To get the information you need, you must apply to the source site to receive the information you need after the request { Currently, I am using the prepared and edited source of <a href="https://rapidapi.com/calorieninjas/api/calorieninjas/">Rapid Api</a> site because you waste less time and it makes your work faster. }
 ```
 url = "https://nutrition-by-api-ninjas.p.rapidapi.com/v1/nutrition"
```
  
## Codes docs



* The following code is related to the beginning part
```
# With the help of this part of the code, we start the desired version of the user
@bot.message_handler(commands=['start'])
def handle_start(message):
   chat_id = message.chat.id 
   markup = telebot.types.ReplyKeyboardMarkup(True, False)
   markup.row("👉🏻👉🏻 Click to start the English version 👈🏻👈🏻")
   markup.row('👈🏻👈🏻 کلیک کنید تا نسخه فارسی برای شما شروع شود 👉🏻👉🏻')
   bot.send_message(chat_id,'Hello 🙋🏻‍♂️\nwelcome to the Calories Info Bot👾\nسلام 🙋🏻‍♂️\nبه ربات اطلاعات کالری 👾 خوش آمدید', reply_markup=markup)
 ```
 * The code below is for the important part after the start part
 ```
 @bot.message_handler(content_types=['text']) # We put the message handler = content_types=['text'] here { If the user enters any text, our function will be activated and after activation, it will check the conditions that we have written in the form of try, if, and elif inside that function to see if the text entered by the user matches our conditions. or not? , if it matches, it fulfills that condition. }
def handle_text(message):
    message.text = message.text.lower() # In this section, we convert all the messages entered by the user into lowercase letters so that they don't have problems, and we write our codes according to the standard.
 ```
 * The following code is used to get the food product name from the user { English version }
 ```
    elif 'food product name' in  message.text : 
        try :
	   # Here we edit the name of the food product entered by the user and set it equal to the value variable
            query = message.text.replace('food product name','')
			
        
            querystring = {"query" : query.replace(":","")}
            headers = {
         "X-RapidAPI-Key": X_RapidAPI_Key,
         "X-RapidAPI-Host": "nutrition-by-api-ninjas.p.rapidapi.com"
        }
	    # And in this section, after requesting the source site, we edit the information we need
            response = requests.request("GET", api, headers=headers, params=querystring)
            if  response.status_code == 200 :   
                info_calories = (response.text.replace("_"," ").strip("[ ]"))
                info_calories_v2 = { }
                info_calories_v2 = info_calories
                final_calories_info = json.loads(info_calories_v2)   
                bot.reply_to(message,"Food Product Name : " +str(final_calories_info['name'].title())+"\n-----------------------------------------------------------------------"+"\nServing Size : " + str(final_calories_info["serving size g"])+"g"+"\n-----------------------------------------------------------------------"+"\nCalories : " + str(final_calories_info["calories"])+'kcal'+"\n-----------------------------------------------------------------------"+"\nProtein : " + str(final_calories_info["protein g"])+'g'+"\n-----------------------------------------------------------------------"+"\nTotal Fat : " + str(final_calories_info["fat total g"])+'g'+"\n-----------------------------------------------------------------------"+"\nSaturated Fat : " + str(final_calories_info["fat saturated g"])+'g'+"\n-----------------------------------------------------------------------"+"\nTotal Carbohydrates : " + str(final_calories_info["carbohydrates total g"])+'g'+"\n-----------------------------------------------------------------------"+"\nFiber : " + str(final_calories_info["fiber g"])+'g'+"\n-----------------------------------------------------------------------"+"\nSugar : " + str(final_calories_info["sugar g"])+'g'+"\n-----------------------------------------------------------------------"+"\nSodium : " + str(final_calories_info["sodium mg"])+'mg'+"\n-----------------------------------------------------------------------"+"\nPotassium : " + str(final_calories_info["potassium mg"])+'mg'+"\n-----------------------------------------------------------------------"+"\nCholesterol: " + str(final_calories_info["cholesterol mg"])+'mg'+"\n-----------------------------------------------------------------------"+"\nNutritional information available at :\n"+query.replace(":","").title()+"\n-----------------------------------------------------------------------"+"\nsources : \nfdc.nal.usda.gov \nwww.nutritionix.com")
        except :
            bot.reply_to(message,'🔴🔴 Make sure your sentence is spelled correctly 🔴🔴')    
    
 ```
 
 * The following code is used to get the food product name from the user { Persian version }
 ```
    elif 'نام محصول غذایی' in  message.text : 
        if 'نام محصول غذایی' in message.text:
    	    # In this section, with the help of Google Translate, we translate the name of the food product entered by the user into English and send it to the source site.
            food_tr = message.text.replace("نام محصول غذایی","")
            import translators as ts
            import translators.server as tss

            wyw_text = food_tr

            from_language, to_language = 'fa', 'en'


            tr_text = (tss.google(wyw_text, from_language, to_language))
            # And in this section, like the English version, we edit the information we need
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

 ```

 * <a href="https://github.com/Mohammadrezaasan/Calories-Info-Bot/blob/main/Main.py">Click here to get the full code</a>
 
 * <a href="https://github.com/Mohammadrezaasan/Calories-Info-Bot/blob/main/calories_info_config.py">Click here to get the config file</a>
 ## Keyword guide
	
|Keyword names|What can they do?|
|:---:|------|
|Food Product Name :|Saves the food product name.|
|📒 List of information 📒|It shows a list of feeding table information that the bot gives you, which you can get answers to by clicking on any of the questions below.|

## List of information stored in the bot

|<p align="center"><img src="https://user-images.githubusercontent.com/108104864/189038358-1c07ee32-066f-4094-ae8c-00acd4694b01.gif" width="200" height="200"/>|
|:---:|
|Fruit sugar is Bad or Good?|
|Is Fructose a natural or added sugar?|
|What Is Calories?|
|What Is Protein?|
|What Is Fat?'|
|What Is Total Carbs?|
|What Is Saturated Fat?|
|What Is Dietary Fiber?|
|What Is Sodium ?|
|What Is Potassium ?|
|What Is Cholesterol ?|


 ## How does the bot respond to keywords?

|<p align="center"><video src="https://user-images.githubusercontent.com/108104864/189472180-9323fef0-6063-439e-82af-e07ec53c3ef2.MP4" width="250" height="500"/>|
|:---:|
|!!Keywords used in the video!!|
|Food Product Name :|Saves the food product name.|
|📒 List of information 📒|It shows a list of feeding table information that the bot gives you, which you can get answers to by clicking on any of the questions below.|

