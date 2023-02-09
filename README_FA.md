![0C938652-DEFC-4ED4-8555-5DD956A236D7](https://user-images.githubusercontent.com/108104864/189498107-5ce8497a-5e5b-44a0-94b9-5d2119b95ba3.jpeg)



## <p align="center">با چند کلیک ساده و وارد کردن نام محصول غذایی مورد نظر خود، میزان کالری، پروتئین، چربی کل، چربی اشباع، کربوهیدرات کل، فیبر، شکر، سدیم، پتاسیم، کلسترول موجود در محصول غذایی را دریافت کنید, <a href="https://t.me/Calories_Info_Robot">ربات اطلاعات کالری</a>.</p>

## <p align="center">منبع API ربات : <a href="https://fdc.nal.usda.gov"> دپارتمان کشاورزی ایالات متحده</a>

## Contents

* [Getting started](#getting-started)  { شروع شدن }

* [Next step](#next-step)  { گام بعدی }
	
* [Codes docs](#codes-docs)  { اسناد کدها }
	
* [Keyword guide](#keyword-guide)  { راهنمای کلمات کلیدی }

* [List of information stored in the bot](#list-of-information-stored-in-the-bot)    { لیست اطلاعات ذخیره شده در ربات }
	
* [How does the bot respond to keywords?](#how-does-the-bot-respond-to-keywords)    { ربات چگونه به کلمات کلیدی پاسخ می دهد؟ }

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
   markup.row("👉🏻👉🏻 Click here to start the English version for you 👈🏻👈🏻")
   markup.row('👈🏻👈🏻 اینجا را کلیک کنید تا نسخه فارسی برای شما شروع شود 👉🏻👉🏻')
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
                info = (response.text.replace("_"," ").strip("[ ]"))
                info1 = { }
                info1 = info
                info2 = json.loads(info1)   
                bot.reply_to(message,"Food Product Name : " +str(info2['name'].title())+"\nServing Size : " + str(info2["serving size g"])+"g"+"\nCalories : " + str(info2["calories"])+'kcal'+"\nProtein : " + str(info2["protein g"])+'g'+"\nTotal Fat : " + str(info2["fat total g"])+'g'+"\nSaturated Fat : " + str(info2["fat saturated g"])+'g'+"\nTotal Carbohydrates : " + str(info2["carbohydrates total g"])+'g'+"\nFiber : " + str(info2["fiber g"])+'g'+"\nSugar : " + str(info2["sugar g"])+'g'+"\nSodium : " + str(info2["sodium mg"])+'mg'+"\nPotassium : " + str(info2["potassium mg"])+'mg'+"\nCholesterol: " + str(info2["cholesterol mg"])+'mg'+"\nNutritional information available at :"+query.replace(":","").title()+"\n-----------------------------------------------------------------------"+"\nsources : \nfdc.nal.usda.gov \nwww.nutritionix.com")
        except :
            bot.reply_to(message,'🔴🔴 Make sure your sentence is spelled correctly 🔴🔴')    
    
 ```
 
 * کد زیر برای دریافت نام محصول غذایی از کاربر استفاده می شود. { نسخه فارسی } 
 ```
 elif 'نام محصول غذایی' in  message.text : 
        if 'نام محصول غذایی' in message.text:
    	    # در این قسمت با کمک گوگل ترنسلیت نام محصول غذایی وارد شده توسط کاربر را به انگلیسی ترجمه کرده و به سایت منبع ارسال می کنیم.
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



