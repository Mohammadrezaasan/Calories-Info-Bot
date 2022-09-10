![0C938652-DEFC-4ED4-8555-5DD956A236D7](https://user-images.githubusercontent.com/108104864/189498107-5ce8497a-5e5b-44a0-94b9-5d2119b95ba3.jpeg)



## <p align="center">با چند کلیک ساده و وارد کردن نام محصول غذایی مورد نظر خود، میزان کالری، پروتئین، چربی کل، چربی اشباع، کربوهیدرات کل، فیبر، شکر، سدیم، پتاسیم، کلسترول موجود در محصول غذایی را دریافت کنید, <a href="https://t.me/Calories_Info_Robot">ربات اطلاعات کالری</a>.</p>

## <p align="center">منبع API ربات : <a href="https://fdc.nal.usda.gov"> دپارتمان کشاورزی ایالات متحده</a>

## Contents

* [Getting started](#getting-started)

* [Next step](#next-step)
	
* [Codes docs](#codes-docs)
	
* [Keyword guide](#keyword-guide)

* [List of information stored in the bot](#list-of-information-stored-in-the-bot)
	
* [How does the bot respond to keywords?](#how-does-the-bot-respond-to-keywords)

## Getting started


* برای شروع پروژه، باید رباتی بسازیم که با کمک  <a href="https://t.me/BotFather">Bot Father</a> ساخته شده است
* هنگامی که ربات شما ساخته شد، Bot Father در پایان یک توکن به شما می دهد { شما آن توکن را در متغیر توکن در فایل config قرار می دهید }

```
bot = telebot.TeleBot(Token_bot)
```
 ## Next step
 * برای دریافت اطلاعات مورد نیاز خود باید به سایت منبع درخواست دهید تا پس از درخواست اطلاعات مورد نیاز خود را دریافت کنید {در حال حاضر از منبع آماده و ویرایش شده سایت
	<a href="https://rapidapi.com/calorieninjas/api/calorieninjas/">Rapid Api</a>  استفاده میکنم, چون زمان کمتری را تلف می کنید و کار شما را سریعتر می کند. }
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
   markup.row("👉🏻👉🏻 Click here to start the English version for you 👈🏻👈🏻")
   markup.row('👈🏻👈🏻 اینجا را کلیک کنید تا نسخه فارسی برای شما شروع شود 👉🏻👉🏻')
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
                info = (response.text.replace("_"," ").strip("[ ]"))
                info1 = { }
                info1 = info
                info2 = json.loads(info1)   
                bot.reply_to(message,"Food Product Name : " +str(info2['name'].title())+"\nServing Size : " + str(info2["serving size g"])+"g"+"\nCalories : " + str(info2["calories"])+'kcal'+"\nProtein : " + str(info2["protein g"])+'g'+"\nTotal Fat : " + str(info2["fat total g"])+'g'+"\nSaturated Fat : " + str(info2["fat saturated g"])+'g'+"\nTotal Carbohydrates : " + str(info2["carbohydrates total g"])+'g'+"\nFiber : " + str(info2["fiber g"])+'g'+"\nSugar : " + str(info2["sugar g"])+'g'+"\nSodium : " + str(info2["sodium mg"])+'mg'+"\nPotassium : " + str(info2["potassium mg"])+'mg'+"\nCholesterol: " + str(info2["cholesterol mg"])+'mg'+"\nNutritional information available at :"+query.replace(":","").title()+"\n-----------------------------------------------------------------------"+"\nsources : \nfdc.nal.usda.gov \nwww.nutritionix.com")
        except :
            bot.reply_to(message,'🔴🔴 Make sure your sentence is spelled correctly 🔴🔴')    
    
 ```
 
 * The following code is used to get the food product name from the user { Persian version }
 ```
 elif 'نام محصول غذایی' in  message.text : 
        if 'نام محصول غذایی' in message.text:
    	    # In this section, with the help of Google Translate, we translate the name of the food product entered by the user into English and send it to the source site.
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
            # And in this section, like the English version, we edit the information we need
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
|Fruit Sugar Is Bad Or Good?|
|Is Fructose A Natural Or Added Sugar?|
|What Is Calories?|
|What Is Protein?|
|What Is Fat?'|
|What Is Total Carbs?|
|What Is Saturated Fat?|
|What Is Dietary Fiber?|
|What Is Sodium ?|
|What Is Potassium ?|
|What Is Cholesterol ?'|


 ## How does the bot respond to keywords?

|<p align="center"><video src="https://user-images.githubusercontent.com/108104864/189472180-9323fef0-6063-439e-82af-e07ec53c3ef2.MP4" width="250" height="500"/>|
|:---:|
|!!Keywords used in the video!!|
|Food Product Name :|Saves the food product name.|
|📒 List of information 📒|It shows a list of feeding table information that the bot gives you, which you can get answers to by clicking on any of the questions below.|


