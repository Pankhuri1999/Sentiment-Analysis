class TweetAnalysis:

    def __init__(self):
        self.tweets = []
        self.tweetText = []

    def runInfo(self):
        # Verification requirements
        APIKey = input('Your API key here: ')
        APISecret = input('Your API Secret here: ')
        accessToken = input('Your access token here: ')
        accessTokenSecret = input('Your access token secret here: ')
        # OAuthHandler authentication
        auth = tweepy.OAuthHandler(APIKey, APISecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        
        api = tweepy.API(auth)

        # user types the term he wants to search and analyse number of tweets
        keyword = input("Enter Keyword to search about: ")
        NoOfTweet = int(input("Enter how many tweets to search: "))

        # Cursor object creation to search number of tweets
        self.tweets = tweepy.Cursor(api.search, q=keyword, lang = "en").items(NoOfTweet)

        # Creating a csv file
        csvFile = open('tweets.csv', 'a')

        # Use csv writer (writing csv files) 
        csvWriter = csv.writer(csvFile)


        # Variables  used for furthet analyzing
        polarity = 0      # Polarity
        positive = 0     # Positive
        wpositive = 0     # Weakly positive
        spositive = 0     # Strongly positive
        negative = 0    # Negative
        wnegative = 0    # Weakly negative
        snegative = 0    # Strongly neagtive
        neutral = 0      # Neutral


        # Checking out each tweet
        for tweet in self.tweets:
            #Append to temp so that we can store in csv later. 'UTF-8' can also be used in place of 'utf8'
            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf8'))
            
            analysis = TextBlob(tweet.text)
            # print(analysis.sentiment)  # print tweet's polarity
            polarity += analysis.sentiment.polarity  # Summing up the polatities of individual tweets

            if (analysis.sentiment.polarity == 0):  # Adding reactions of people in different categories
                neutral += 1
            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
                wpositive += 1
            elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
                positive += 1
            elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
                spositive += 1
            elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
                wnegative += 1
            elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                negative += 1
            elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                snegative += 1


        # writing and closing csv file
        csvWriter.writerow(self.tweetText)
        csvFile.close()

        # average of individual category of tweets
        positive = self.percentage(positive, NoOfTweet)
        wpositive = self.percentage(wpositive, NoOfTweet)
        spositive = self.percentage(spositive, NoOfTweet)
        negative = self.percentage(negative, NoOfTweet)
        wnegative = self.percentage(wnegative, NoOfTweet)
        snegative = self.percentage(snegative, NoOfTweet)
        neutral = self.percentage(neutral, NoOfTweet)

        # Overall and final reaction
        polarity = polarity / NoOfTweet

        # Output 
        print("How people are reacting on " + keyword + " by analyzing " + str(NoOfTweet) + " tweets.")
        print()
        print("Average reaction: ")

        if (polarity == 0):
            print("Neutral",'\U0001F636')
        elif (polarity > 0 and polarity <= 0.3):
            print("Weakly Positive",'\U0001F642')
        elif (polarity > 0.3 and polarity <= 0.6):
            print("Positive",'\U0001F60A')
        elif (polarity > 0.6 and polarity <= 1):
            print("Strongly Positive",'\U0001F604')
        elif (polarity > -0.3 and polarity <= 0):
            print("Weakly Negative",'\U0001F615')
        elif (polarity > -0.6 and polarity <= -0.3):
            print("Negative",'\U0001F61F')
        elif (polarity > -1 and polarity <= -0.6):
            print("Strongly Negative",'\U0001F61E')
            
        print()
        print("More info of report: ")
        print(positive , "% of tweets pointed it to be  positive")
        print(wpositive ,  "% of tweets pointed it to be weakly positive")
        print(spositive ,  "% of tweets pointed it to be strongly positive")
        print(negative , "% of tweets pointed it to be negative")
        print(wnegative ,  "% of tweets pointed it to be weakly negative")
        print(snegative ,  "% of tweets pointed it to be strongly negative")
        print(neutral , "% of tweets pointed it to be neutral")

            
        
        sizes = [float(positive),float(wpositive),float(spositive),float(neutral),float(negative),float(wnegative),float(snegative)]
        # labelling each category of reactions
        label=["positive", "weakly \n positive", "strongly \n positive", "neutral" , "negative" , "weakly \n negative" , "strongly \n negative"]
        l = len(sizes) # finding length of list-'size'
        for i in range(l):   # loop to iterate over each element in list-'size'
            if (sizes[i] == 0):
                sizes.remove(sizes[i])   # removing thoses elements from list whose value is zero
        # plotting the graph
        squarify.plot(sizes=sizes, label=["positive", "weakly \n positive", "strongly \n positive", "neutral" , "negative" , "weakly \n negative" , "strongly \n negative"], alpha=.5 )
        plt.axis('off')
        plt.show()
        
    
        

    def cleanTweet(self, tweet):
        # Remove Links, Special Characters etc from tweet
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

    # function to calculate percentage
    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')
        

    
        
if __name__== "__main__":
    call = TweetAnalysis()
    call.runInfo()
    
    
