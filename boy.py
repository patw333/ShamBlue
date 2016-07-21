# - *- coding: utf- 8 - *-
import tweepy
import requests
import os
import random

def raidCode():
	res=''.join([random.choice('0123456789ABCDEF') for x in range(8)])
	return res+"\n"


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


class TwitterAPI:
    def __init__(self):
        consumer_key = "xtQ6aVIjChUh8KZ5n6p9wsREg"
        consumer_secret = "FOTe8iDyGVGMLQklRqTklTAINP5gd5i8Gi5VTqnGtOZa1LelkB"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "3262061310-4AQphNwkUKz9SCYPb5RxIDz4lqarMN24QL6PKos"
        access_token_secret = "SU28iUiNddl8qV3YdG63Nv3GRqcMgsaU8sdGSIpsV38w4"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)


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
    url='https://pbs.twimg.com/media/B5DQsLyCYAEgRRT.jpg'
    #twitter.tweet()
    gen=imageGen()
    message = u"参加者募集！参戦ID："+raidCode()+gen[0]
    twitter.tweet_image(gen[1],message)
