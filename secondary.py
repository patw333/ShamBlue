# - *- coding: utf- 8 - *-
import tweepy
import requests
import os
import random

def raidCode():
	res=''.join([random.choice('0123456789ABCDEF') for x in range(8)])
	return res+"\n"


#Add HL raids+ Ghost Light
def imageGen():
	num=random.randint(0,8)
	array=["https://raw.githubusercontent.com/patw333/ShamBlue/master/celeste.jpg","https://raw.githubusercontent.com/patw333/ShamBlue/master/coloss.jpg","https://raw.githubusercontent.com/patw333/ShamBlue/master/levia.jpg","https://raw.githubusercontent.com/patw333/ShamBlue/master/tiamat.jpg","https://raw.githubusercontent.com/patw333/ShamBlue/master/proto.jpg"]
	text=[u"Lv75 セレスト・マグナ",u"Lv70 コロッサス・マグナ",u"Lv60 リヴァイアサン・マグナ",u"Lv50 ティアマト・マグナ",u"Lv100 プロトバハムート"]
	res=[]
	if num>=4:
		res.append(text[4])
		res.append(array[4])
	else:
		res.append(text[num])
		res.append(array[num])
	return res


def randTweet():
    lines = open('roytxt.txt').read().splitlines()
    myline =random.choice(lines)
    return myline


class TwitterAPI:
    def __init__(self):
        consumer_key = "Find it out yourself!"
        consumer_secret = "Find it out yourself!"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "Find it out yourself!"
	access_token_secret = "Find it out yourself!"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)


        users=self.api.followers_ids(self.api)
        friends=self.api.friends_ids(self.api)

        for follower in users:
            if follower not in friends:
                try:
                    self.api.create_friendship(follower)
                except:
                    print()

#        for follower in tweepy.Cursor(self.api.followers).items():
#            if tweepy.API.exists_friendship(self.api,follow)==false:
#               follower.follow()

    def tweet(self, message):
        self.api.update_status(status=message)

    def tweet_image(self,url,message):
    	request=requests.get(url,stream=True)
    	filename='roy.jpg'
    	if request.status_code == 200:
    		with open(filename,'wb') as image:
    			for chunk in request:
    				image.write(chunk)
    		self.api.update_with_media(filename,status=message)
    		os.remove(filename)
    	else:
    		print("image error")





if __name__ == "__main__":
    twitter = TwitterAPI()
    #twitter.tweet()
    gen=imageGen()
    message = randTweet();
    twitter.tweet(message)
