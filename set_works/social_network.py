

users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab","rahul"]

sanju_followers=["kohli","rohit","pandya"]

#follow_suggestion[sanju,pandya,siraj]

rahul_followers_suggestion=set(users).difference(set(rahul_followers))

mutual_friends=set(rahul_followers).intersection(set(sanju_followers))

print(mutual_friends)

print(rahul_followers_suggestion)



