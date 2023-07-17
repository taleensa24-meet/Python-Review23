def create_youtube_video(title,description):
	ytvideo = {"title":title,"description": descriptipon,"likes":0,"dislikes" : 0, "comments":{}}
	return ytvideo


def likes(ytvideo):
	if "likes" in ytvideo:
		ytvideo["likes"]+=1
		return ytvideo


def dislikes(ytvideo):
	if "dislikes" in ytvideo:
		ytvideo["dislikes"]+=1
		return ytvideo


def add_comment(ytvideo,username,comment_text):
	ytvideo["comments"]["username"]=comment_text
	return ytvideo

a_new_ytvideo=create_youtube_video{"new video","In this video i'll be taking u to a tour at iasa"}

