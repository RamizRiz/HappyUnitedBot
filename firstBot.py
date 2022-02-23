import praw
import random
import time

reddit = praw.Reddit(client_id='S70xI5N3PHJkMI2C59EZrQ',
                     client_secret='5PMG5GI6Nyq67WZ1iCCDyHu8nz4k8A',
                     user_agent='<console:RamiFirstBot:2.0>',
                     username='Happy-United-Bot',
                     password= 'Drizwan10')

subreddit = reddit.subreddit("ManchesterUnited")
happy_times = ["[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=k1Q7NRDYPDo&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=1)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=VU-6Q_uh5Uw&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=2)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=HXWUjwsw8F0&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=3)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=Ot48fFEUwHc&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=4)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=l6niYS3Be1E&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=5)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=o0yb73LPWHg&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=6)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=0WBZO3QhDgQ&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=7)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=zDdcNMa-Mh0&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=8)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=Ph8MFmrIDDY&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=9)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=AQbv57vhXx8&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=10)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=GJLKm6WhvxI&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=11)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=QAW_lFJ3dIY&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=12)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=-nOSXXFJLYA&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=13)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=jLgUDICcC_Y&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=14)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=wjoS-qfM0uQ&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=15)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=ZYPySk-tS3c&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=16)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=EUisfknangI&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=17)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=xB0IM8tC5vw&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=18)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=gwMHomafQvA&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=20)",
               "[Cheer up, here's a reminder of the happy times](https://www.youtube.com/watch?v=bVCeEk-z7f0&list=PLLS2188qzFrcDjqt4lWkZlO_k90eIrjLR&index=21)", ]

for submission in subreddit.hot(limit=10):
    #print("**************") 
    #print(submission.title) 
    for comment in submission.comments:
         if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " sad " in comment_lower:
                print("_______") 
                print (comment.body)
                random_index = random.randint(0, len(happy_times)-1)
                comment.reply(happy_times[random_index])
                #time.sleep(60000)