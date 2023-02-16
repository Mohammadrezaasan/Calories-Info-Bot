![0C938652-DEFC-4ED4-8555-5DD956A236D7](https://user-images.githubusercontent.com/108104864/189498107-5ce8497a-5e5b-44a0-94b9-5d2119b95ba3.jpeg)



## <p align="center">با چند کلیک ساده و وارد کردن نام محصول غذایی مورد نظر خود، میزان کالری، پروتئین، چربی کل، چربی اشباع، کربوهیدرات کل، فیبر، شکر، سدیم، پتاسیم، کلسترول موجود در محصول غذایی را دریافت کنید, <a href="https://t.me/Calories_Info_Robot">ربات اطلاعات کالری</a>.</p>

## <p align="center">منبع API ربات : <a href="https://fdc.nal.usda.gov"> دپارتمان کشاورزی ایالات متحده</a>

## Contents
	
* [Languages and Tools used in bot](#languages-and-tools-used-in-bot) { زبان ها و ابزارهای مورد استفاده در ربات }
	
* [Getting started](#getting-started)  { شروع شدن }

* [Next step](#next-step)  { گام بعدی }
	
* [Codes docs](#codes-docs)  { اسناد کدها }
	
* [Keyword guide](#keyword-guide)  { راهنمای کلمات کلیدی }

* [List of information stored in the bot](#list-of-information-stored-in-the-bot)    { لیست اطلاعات ذخیره شده در ربات }
	
* [How does the bot respond to keywords?](#how-does-the-bot-respond-to-keywords)    { ربات چگونه به کلمات کلیدی پاسخ می دهد؟ }

## Languages and Tools used in bot
##  زبان ها و ابزارهای مورد استفاده در ربات
	
* Python 3.10
* REST API
* <a href="https://pypi.org/project/pyTelegramBotAPI/">Telebot Library</a>
* <a href="https://github.com/uliontse/translators#from-pypi">Translation Library</a>

	
## Getting started
## شروع شدن


* برای شروع پروژه، باید رباتی بسازیم که با کمک  <a href="https://t.me/BotFather">Bot Father</a> ساخته شده است
* هنگامی که ربات شما ساخته شد، Bot Father در پایان یک توکن به شما می دهد { شما آن توکن را در متغیر توکن در فایل config قرار می دهید }

```
bot = telebot.TeleBot(Token_bot)
```
## Next step
 ## گام بعدی
 * برای دریافت اطلاعات مورد نیاز خود باید به سایت منبع درخواست دهید تا پس از درخواست اطلاعات مورد نیاز خود را دریافت کنید {در حال حاضر از منبع آماده و ویرایش شده سایت
	<a href="https://rapidapi.com/calorieninjas/api/calorieninjas/">Rapid Api</a>  استفاده میکنم, چون زمان کمتری را تلف می کنید و کار شما را سریعتر می کند. }
 ```
 url = "https://nutrition-by-api-ninjas.p.rapidapi.com/v1/nutrition"
```
 ## Codes docs
## اسناد کدها



* کد زیر مربوط به قسمت شروع است
```
# با کمک این قسمت کد، نسخه مورد نظر کاربر را شروع می کنیم
@bot.message_handler(commands=['start'])
def handle_start(message):
   chat_id = message.chat.id 
   markup = telebot.types.ReplyKeyboardMarkup(True, False)
   markup.row("👉🏻👉🏻 Click to start the English version 👈🏻👈🏻")
   markup.row('👈🏻👈🏻 کلیک کنید تا نسخه فارسی برای شما شروع شود 👉🏻👉🏻')
   bot.send_message(chat_id,'Hello 🙋🏻‍♂️\nwelcome to the Calories Info Bot👾\nسلام 🙋🏻‍♂️\nبه ربات اطلاعات کالری 👾 خوش آمدید', reply_markup=markup)
 ```
 * کد زیر مربوط به قسمت مهم, بعد از قسمت شروع است.
 ```
 @bot.message_handler(content_types=['text']) # پیام handler = content_types=['text'] را اینجا قرار می دهیم { اگر کاربر متنی را وارد کند، تابع ما فعال می شود و پس از فعال سازی، شرایطی را که به صورت try، if و elif نوشته ایم بررسی می کند. در داخل آن تابع ببینید آیا متن وارد شده توسط کاربر با شرایط ما مطابقت دارد یا خیر ، اگر مطابقت داشته باشد، آن شرط را انجام می دهد. }
def handle_text(message):
    message.text = message.text.lower() # در این قسمت تمامی پیام های وارد شده توسط کاربر را به حروف کوچک تبدیل می کنیم تا دچار مشکل نشوند و کدهای خود را طبق استاندارد می نویسیم.
 ```
* کد زیر برای دریافت نام محصول غذایی از کاربر استفاده می شود. { نسخه انگلیسی } 

```
    elif 'food product name' in  message.text : 
        try :
	   # در اینجا نام محصول غذایی وارد شده توسط کاربر را ویرایش کرده و آن را برابر با متغیر query قرار می دهیم .
            query = message.text.replace('food product name','')
			
        
            querystring = {"query" : query.replace(":","")}
            headers = {
         "X-RapidAPI-Key": X_RapidAPI_Key,
         "X-RapidAPI-Host": "nutrition-by-api-ninjas.p.rapidapi.com"
        }
	    # و در این قسمت پس از درخواست به  سایت منبع، اطلاعات مورد نیاز خود را ویرایش می کنیم
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
 
 * کد زیر برای دریافت نام محصول غذایی از کاربر استفاده می شود. { نسخه فارسی } 
 ```
    elif 'نام محصول غذایی' in  message.text : 
        if 'نام محصول غذایی' in message.text:
    	    # در این قسمت با کمک گوگل ترنسلیت نام محصول غذایی وارد شده توسط کاربر را به انگلیسی ترجمه کرده و به سایت منبع ارسال می کنیم.
            food_tr = message.text.replace("نام محصول غذایی","")
            import translators as ts
            import translators.server as tss

            wyw_text = food_tr

            from_language, to_language = 'fa', 'en'


            tr_text = (tss.google(wyw_text, from_language, to_language))
            =
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

 * <a href="https://github.com/Mohammadrezaasan/Calories-Info-Bot/blob/main/Main.py">برای دریافت کامل کد اینجا کلیک کنید</a>
 
 * <a href="https://github.com/Mohammadrezaasan/Calories-Info-Bot/blob/main/calories_info_config.py">برای دریافت فایل کانفیگ اینجا کلیک کنید</a>
 ## Keyword guide
 ## راهنمای کلمات کلیدی

|نام کلمات کلیدی|چه کاری می توانند انجام دهند؟|
|:---:|------|
| نام محصول غذایی : | . نام محصول غذایی را ذخیره می کند|
|📒 لیست اطلاعات 📒|لیستی از اطلاعات جدول تغذیه که ربات به شما می دهد را نشان می دهد که با کلیک روی هر یک از سوالات زیر می توانید پاسخ آنها را دریافت کنید|
## List of information stored in the bot
## لیست اطلاعات ذخیره شده در ربات

|<p align="center"><img src="https://user-images.githubusercontent.com/108104864/189038358-1c07ee32-066f-4094-ae8c-00acd4694b01.gif" width="200" height="200"/>|
|:---:|
|قند میوه مضر است یا خوب؟|
|آیا فروکتوز یک قند طبیعی است یا افزودنی؟|
|کالری چیست؟|
|پروتئین چیست؟|
|چربی چیست؟|
|کربوهیدرات کل چیست؟|
|چربی اشباع چیست؟|
|فیبر غذایی چیست؟|
|سدیم چیست؟|
|پتاسیم چیست؟|
|کلسترول چیست؟|

 ## How does the bot respond to keywords?
 ## ربات چگونه به کلمات کلیدی پاسخ می دهد؟

|<p align="center"><video src="https://user-images.githubusercontent.com/108104864/189500747-8e7c1bed-fdb8-4087-a5f8-939f8759dc53.MP4" width="250" height="500"/>|
|:---:|
|!! کلمات کلیدی استفاده شده در ویدیو !!|
|نام محصول غذایی : |
|📒 لیست اطلاعات 📒|



