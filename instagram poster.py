from instabot import Bot

bot = Bot()



user = input("enter  your username:")

pwd   = input("enter your password: ")
bot.login(username=user, password= pwd)

print("please make sure that the photo and the code are in the same directory before typing the name")
photo_name = input("enter the photo name: ")
post_caption = input("enter the caption of your post")
bot.upload_photo(photo_name, post_caption)