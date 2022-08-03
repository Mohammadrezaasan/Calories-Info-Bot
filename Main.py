from turtle import title
from telebot import TeleBot
import telebot
from telebot import types
from markupsafe import Markup
from rsa import PublicKey
import requests
import json
from decimal import *
"----------------------------------------------------------------------------------------------------------"
bot = telebot.TeleBot("Token")
api  = "https://nutrition-by-api-ninjas.p.rapidapi.com/v1/nutrition"
"----------------------------------------------------------------------------------------------------------"
info5 = {    
 '1-fruit sugar is bad or god?' : '1-Fruit Sugar Is Bad Or God?\nSugar in food and drinks comes in various forms. Sugar molecules are classified as monosaccharides (single sugar molecules such as glucose and fructose) and disaccharides (more complex structures such as sucrose and lactose).\nFruit contains natural sugars, which are a mix of sucrose, fructose and glucose. Many people have heard that sugar is bad, and think that this must also therefore apply to fruits.\nYou don,t need to quit sugar to improve your health\nBut fructose is only harmful in excess amounts, and not when it comes from fruit. It would be incredibly difficult to consume excessive amounts of fructose by eating whole fruits.\nIt’s much easier to consume excess sugar from foods and drinks that contain “free sugars”.\nFree sugars include these same sugars (fructose, glucose, sucrose), but in this case they have been removed from their naturally occurring source (rather than being eaten as natural parts of fruits, dairy products, and some vegetables and grains). This includes sugar that is added to food and drinks by food companies, cooks or consumers.\nHealth risks come from free sugars, not fruitsEvidence shows that the health risks from sugars, such as tooth decay and unhealthy weight gain, are related to consuming too many free sugars in the diet, not from eating sugars that are naturally present in fruits or milk.\n | source : theconversation.com |',  
 '2-is fructose a natural or added sugar?' : '2-Is Fructose A Natural Or Added Sugar?\nFructose can be a natural sugar or an added sugar, depending on its source. It is considered a natural sugar when we consume it directly from whole plant foods. It is considered an added sugar when we consume it from packaged foods and beverages to which fructose-containing sugars (such as crystalline fructose, high fructose corn syrup or sucrose) have been added during manufacturing.\n| source : foodinsight.org |', 
 '3-what is calories?' : '3-What Is Calories?\nThe amount of energy in an item of food or drink is measured in calories.\nWhen we eat and drink more calories than we use up, our bodies store the excess as body fat. If this continues, over time we may put on weight.\nAs a guide, an average man needs around 2,500kcal (10,500kJ) a day to maintain a healthy body weigh.\nFor an average woman, that figure is around 2,000kcal (8,400kJ) a day.\nThese values can vary depending on age, size and levels of physical activity, among other factors.\n | source  :  www.nhs.uk |' ,
 '4-what is protein?' : '4-What Is Protein?\nProtein is a nutrient your body needs to grow and repair cells, and to work properly.\n Protein is found in a wide range of food and it’s important that you get enough protein in your diet every day. How much protein you need from your diet varies depending on your weight, gender, age and health.\n Meeting your protein needs is easily achieved from eating a variety of foods. Protein from food comes from plant and animal sources such as:\nmeat and fish\neggs\ndairy products\nseeds and nuts\nlegumes like beans and lentils....\n | source  : www.betterhealth.vic.gov.au | ',
 '5-what is fat?' : '5-What Is Fat?\nThe foods we eat contain nutrients that provide energy and other substances the body needs. Most of the nutrients in food fall into three major groups: proteins, fats, and carbohydrates.\nThe body uses fat as a fuel source, and fat is the major storage form of energy in the body. Fat also has many other important functions in the body, and a moderate amount is needed in the diet for good health.\n!aturated fat guidelines!\nMost people in the world eat too much saturated fats.\nThe world health organization recommends that:\nmen should not eat more than 30g of saturated fat a day\nwomen should not eat more than 20g of saturated fat a day\nchildren should have less\n Trans fats\nTrans fats are found naturally at low levels in some foods, such as meat and dairy products.\nThey can also be found in partially hydrogenated vegetable oil. Hydrogenated vegetable oil must be declared on a foods ingredients list if its been included.\nLike saturated fats, trans fats can raise cholesterol levels in the blood.\nThe world health organization recommends that:\nadults should not have more than about 5g of trans fats a day\nMost of the supermarkets in the world have removed partially hydrogenated vegetable oil from all their own-brand products.\nPeople in the world tend to eat a lot more saturated fats than trans fats. This means that when youre looking at the amount of fat in your diet, its more important to focus on reducing the amount of saturated fats.\nUnsaturated fats\nIf you want to reduce your risk of heart disease, it,s best to reduce your overall fat intake and swap saturated fats for unsaturated fats.\nTheres good evidence that replacing saturated fats with some unsaturated fats can help to lower your cholesterol level.\nMostly found in oils from plants and fish, unsaturated fats can be either monounsaturated or polyunsaturated.\nMonounsaturated fats\nMonounsaturated fats help protect your heart by maintaining levels of "good" HDL cholesterol while reducing levels of "bad" LDL cholesterol in your blood.\nMonounsaturated fats are found in:\nolive oil, rapeseed oil and spreads made from these oils\navocados\nsome nuts, such as almonds, brazils, and peanuts\nPolyunsaturated fats\nPolyunsaturated fats can also help lower the level of "bad" LDL cholesterol in your blood.\nThere are 2 main types of polyunsaturated fats: omega-3 and omega-6.\nSome types of omega-3 and omega-6 fats cannot be made by your body, which means it,s essential to include small amounts of them in your diet.\nOmega-6 fats are found in vegetable oils, such as:\nrapeseed\ncorn\nsunflower\nsome nuts\nOmega-3 fats are found in oily fish, such as:\nkippers\nherring\ntrout\nsardines\nsalmon\nmackerel\nMost people get enough omega-6 in their diet, but it,s recommended to have more omega-3 by eating at least 2 portions of fish each week, with 1 portion being an oily fish.\nVegetable sources of omega-3 fats are not thought to have the same benefits on heart health as those found in fish. Find out more about healthy eating as a vegetarian.\n| sources  :  www.nhs.uk & kidshealth.org | ',
 '6-what is total carbs?' :'6-What Is Total Carbs?\ntotal carbohydrates\n includes all types of carbohydrate found in the food or beverage.\n Total carbohydrates consist of multiple nutrients, including dietary fiber, sugars and starches.\n Each of these types of carbohydrate is critical to sufficient energy intake and overall health, although excessive intake of some of these carbohydrates, like any other macronutrient, can have undesirable side effects.\n| source  : healthyeating.sfgate.com |',
 '7-what is saturated fat?':'7-what is Saturated fat?\nThere are different types of fat in the food we eat, and saturated fats are the type that raise blood cholesterol.\nMany foods contain saturated fat, especially animal foods such as meat, butter and dairy products, and foods that are made with them, such as cakes and biscuits. Theyre also found in some plant foods including coconut oil and palm oil.\nCutting down on foods high in saturated fat and replacing them with foods higher in unsaturated fat can help improve cholesterol levels. For example, plant-based fat spreads and oils, oily fish, nuts and seeds.\n| source : www.heartuk.org.uk | ',
 '8-what is dietary fiber?' : '8-What is Dietary Fiber?\nEat more fiber. Youve probably heard it before. But do you know why fiber is so good for your health? \nDietary fiber — found mainly in fruits, vegetables, whole grains and legumes — is probably best known for its ability to prevent or relieve constipation. But foods containing fiber can provide other health benefits as well, such as helping to maintain a healthy weight and lowering your risk of diabetes, heart disease and some types of cancer.\n| source  : www.mayoclinic.org |',
 '9-what is sodium ?' : '9-what is Sodium ?\nSodium is a mineral found in many foods. Your body needs sodium for normal muscle and nerve functions. It also helps keep body fluids in balance. Most table salts are made from sodium chloride. So, salt used when preparing or flavoring foods usually contains sodium. And, healthcare providers often use the words sodium and salt interchangeably.\n| source  : www.eatright.org | ',
 '10-what is potassium ?' : '10-what is potassium ?\nPotassium is essential to all living cells and is important for muscle and nerve functions in the body. It is found in most foods including legumes, whole grains, fruits, green vegetables, potatoes, meats, milk and yogurt. Although potassium is vital to the body, it is not wise to take potassium supplements in pill or liquid form without consulting your doctor and/or your renal dietician, especially if your kidney function is reduced.\n| source  : pkdcure.org |  ',
 '11-what is cholesterol ?' : "11-what is cholesterol ?\nIf you’re reading this, you probably care about your health and the role cholesterol can play. That’s an important first step.So, what is cholesterol? What does it do?Cholesterol is a waxy substance. It’s not inherently “bad.” Your body needs it to build cells and make vitamins and other hormones. But too much cholesterol can pose a problem.\nCholesterol comes from two sources. Your liver makes all the cholesterol you need. The remainder of the cholesterol in your body comes from foods from animals. For example, meat, poultry and dairy products all contain dietary cholesterol.\nThose same foods are high in saturated and trans fats. These fats cause your liver to make more cholesterol than it otherwise would. For some people, this added production means they go from a normal cholesterol level to one that’s unhealthy.\nSome tropical oils – such as palm oil, palm kernel oil and coconut oil – contain saturated fat that can increase bad cholesterol. These oils are often found in baked goods.\nWhy cholesterol matters\nCholesterol circulates in the blood. As the amount of cholesterol in your blood increases, so does the risk to your health. High cholesterol contributes to a higher risk of cardiovascular diseases, such as heart disease and stroke. That’s why it’s important to have your cholesterol tested, so you can know your levels.\nThe two types of cholesterol are: LDL cholesterol, which is bad, and HDL, which is good. Too much of the bad kind, or not enough of the good kind, increases the risk cholesterol will slowly build up in the inner walls of the arteries that feed the heart and brain.\nLearn more about LDL,DL and triglycerides.\nLDL (bad) cholesterol\nLDL cholesterol is considered the “bad” cholesterol, because it contributes to fatty buildups in arteries (atherosclerosis). This narrows the arteries and increases the risk for heart attack, stroke and peripheral artery disease (PAD).\nHDL (good) cholesterol\nHDL cholesterol can be thought of as the “good” cholesterol because a healthy level may protect against heart attack and stroke. \nHDL carries LDL (bad) cholesterol away from the arteries and back to the liver, where the LDL is broken down and passed from the body. But HDL cholesterol doesn't completely eliminate LDL cholesterol. Only one-third to one-fourth of blood cholesterol is carried by HDL.\nCholesterol can join with other substances to form a thick, hard deposit on the inside of the arteries. This can narrow the arteries and make them less flexible – a condition known as atherosclerosis. If a blood clot forms and blocks one of these narrowed arteries, a heart attack or stroke can result.\nhen it comes to cholesterol, remember: check, change and control. That is:\nCheck your cholesterol levels. It’s key to know your numbers and assess your risk.\nChange your diet and lifestyle to help improve your levels.Control your cholesterol, with help from your doctor if needed High cholesterol is one of the major controllable risk factors for coronary heart disease, heart attack and stroke. If you have other risk factors such as smoking, high blood pressure or diabetes, your risk increases even more.\n| sources  :  www.heart.org |"
}
"----------------------------------------------------------------------------------------------------------"
@bot.message_handler(commands=['start'])
def handle_start(message):
   chat_id = message.chat.id 
   markup = telebot.types.ReplyKeyboardMarkup(True, False)
   markup.row("🔴🔴 To do the steps correctly, pay attention to the example below 🔴🔴\n👇🏻👇🏻 For example,type like this 👇🏻👇🏻")
   markup.row('Food ProductName : 250g Grilled Chicken')
   markup.row("📒 List of information 📒")
   bot.send_message(chat_id,'Hello 🙋🏻‍♂️\nwelcome to the Calories Info Bot👾', reply_markup=markup)
"----------------------------------------------------------------------------------------------------------"
@bot.message_handler(content_types=['text'])
def handle_text(message):
    message.text = message.text.lower()
    if 'foodproductname:' in  message.text.replace(' ','') : 
        try :
            'foodproductname:' in  message.text.replace(' ','') 
        
            querystring = {"query" : message.text.replace('food product name:','')}
            headers = {
         "X-RapidAPI-Key": "API-Key",
         "X-RapidAPI-Host": "nutrition-by-api-ninjas.p.rapidapi.com"
        }
            response = requests.request("GET", api, headers=headers, params=querystring)
            if  response.status_code == 200 :   
                info = (response.text.replace("_"," ").strip("[ ]"))
                info1 = { }
                info1 = info
                info2 = json.loads(info1)   
                bot.reply_to(message,"Name: " + str(info2["name"])+"\nServing Size : " + str(info2["serving size g"])+"g"+"\nCalories : " + str(info2["calories"])+'kcal'+"\nProtein : " + str(info2["protein g"])+'g'+"\nTotal Fat : " + str(info2["fat total g"])+'g'+"\nSaturated Fat : " + str(info2["fat saturated g"])+'g'+"\nTotal Carbohydrates : " + str(info2["carbohydrates total g"])+'g'+"\nFiber : " + str(info2["fiber g"])+'g'+"\nSugar : " + str(info2["sugar g"])+'g'+"\nSodium : " + str(info2["sodium mg"])+'mg'+"\nPotassium : " + str(info2["potassium mg"])+'mg'+"\nCholesterol: " + str(info2["cholesterol mg"])+'mg')
        except :
            bot.reply_to(message,'🔴🔴 Make sure your sentence is spelled correctly 🔴🔴')    
    
    elif message.text == '📒 list of information 📒' :
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('1-Fruit Sugar Is Bad Or God?')
        markup.row('2-Is Fructose A Natural Or Added Sugar?')
        markup.row('3-What Is Calories?')
        markup.row('4-What Is Protein?')
        markup.row('5-What Is Fat?')
        markup.row('6-What Is Total Carbs?')
        markup.row('7-What Is Saturated Fat?')
        markup.row('8-What Is Dietary Fiber?')
        markup.row('9-What Is Sodium ?')
        markup.row('10-What Is Potassium ?')
        markup.row('11-What Is Cholesterol ?')
        markup.row('Return to main page ↩️')
        bot.send_message(chat_id,'List of information opened successfully ✅', reply_markup=markup)
    
    elif message.text == 'return to main page ↩️' : 
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("🔴🔴 To do the steps correctly, pay attention to the example below 🔴🔴\n👇🏻👇🏻 For example,type like this 👇🏻👇🏻")
        markup.row('Food ProductName : 250g Grilled Chicken')
        markup.row("📒 List of information 📒")
        bot.send_message(chat_id,'Return to main page was successful ✅', reply_markup=markup)
    
    elif message.text in info5 : 
        bot.reply_to(message,info5[message.text])
    
    
"----------------------------------------------------------------------------------------------------------"
bot.polling(none_stop=True)
