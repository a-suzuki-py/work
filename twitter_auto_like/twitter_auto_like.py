#===================================================
# coding: UTF-8
# Twitterから検索ワードのTweetを取得して自動で「いいね」をする機能
#===================================================
import tweepy


#================================
# 設定していただくもの
#================================
# TwitterAPIの各種Key
Consumer_Key    = "お客様の【Consumer Key】を設定します"
Consumer_Secret = "お客様の【Consumer Secret】を設定します"
Access_Token    = "お客様の【Access_Token】を設定します"
Access_Secret   = "お客様の【Access_Secret】を設定します"

#　検索したいワード
Serch_Word = "【検索したいワード】を設定します"
#　検索する最大数
Serch_Max_Count = 10
#　いいねする数
Like_Max_Count = 2


#=====================================
# main
#=====================================
def main():

    # API情報を取得します
    auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
    auth.set_access_token(Access_Token, Access_Secret)
    api = tweepy.API(auth)

    #　検索ワードで検索した情報を取得します
    results = api.search(q=Serch_Word, count=Serch_Max_Count)
    Auto_Like(api, results)


#=====================================
# 自動「いいね」をする処理
# Like_Max_Countで指定分いいねをするか
# Serch_Max_Count分チェックしたら終了します
#=====================================
def Auto_Like(api, results):
    like_count = 0
    
    #　取得したTweetを1件ずつ見ていきます
    for tweet in results:
        
        #　Tweetの情報を取得
        tweet_id = tweet.id
        tweet_status = api.get_status(tweet_id)
        
        # すでにいいね済みの場合はスルーします
        if tweet_status.favorited:
            continue
        
        # 「いいね」をします
        try:
            api.create_favorite(tweet_id)
            like_count += 1
            
            # 「いいね」をしたTweet内容確認用
            print("="*30)
            print(tweet.text)
        except:
            pass
        
        # 指定のいいね数に達したら処理を終了します
        if like_count >= Like_Max_Count:
            break




if __name__ == "__main__":
    main()
