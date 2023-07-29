from app.models import db, environment, SCHEMA, User, Friend
from sqlalchemy.sql import text

def seed_friends():
    user1 = User.query.get(1)
    user2 = User.query.get(2)
    user3 = User.query.get(3)
    user4 = User.query.get(4)
    user5 = User.query.get(5)
    user6 = User.query.get(6)
    user7 = User.query.get(7)
    user8 = User.query.get(8)
    user9 = User.query.get(9)
    user10 = User.query.get(10)

    # User1 is friends with User2
    friend1 = Friend(user=user1, friend=user2, status='friends')
    # User1 has pending friend request to User3
    friend2 = Friend(user=user1, friend=user3, status='pending')
    # User2 has pending friend request to User3
    friend3 = Friend(user=user2, friend=user3, status='pending')
    # User1 is friends with User4
    friend4 = Friend(user=user1, friend=user4, status='friends')
    # User2 is friends with User4
    friend5 = Friend(user=user2, friend=user4, status='friends')
    # User3 has pending friend request to User4
    friend6 = Friend(user=user3, friend=user4, status='pending')
    # User1 is friends with User5
    friend7 = Friend(user=user1, friend=user5, status='friends')
    # User4 has pending friend request to User5
    friend8 = Friend(user=user4, friend=user5, status='pending')
    # User2 is friends with User6
    friend9 = Friend(user=user2, friend=user6, status='friends')
    # User5 has pending friend request to User6
    friend10 = Friend(user=user5, friend=user6, status='pending')
    # User3 is friends with User7
    friend11 = Friend(user=user3, friend=user7, status='friends')
    # User1 has pending friend request to User7
    friend12 = Friend(user=user1, friend=user7, status='pending')
    # User8 is friends with User9
    friend13 = Friend(user=user8, friend=user9, status='friends')
    # User9 has pending friend request to User10
    friend14 = Friend(user=user9, friend=user10, status='pending')

    user1.friends.append(friend1)
    user1.friends.append(friend2)
    user1.friends.append(friend4)
    user1.friends.append(friend7)
    user1.friends.append(friend12)
    user2.friends.append(friend1)
    user2.friends.append(friend3)
    user2.friends.append(friend5)
    user2.friends.append(friend9)
    user3.friends.append(friend2)
    user3.friends.append(friend3)
    user3.friends.append(friend6)
    user3.friends.append(friend11)
    user4.friends.append(friend4)
    user4.friends.append(friend5)
    user4.friends.append(friend6)
    user4.friends.append(friend8)
    user5.friends.append(friend7)
    user5.friends.append(friend8)
    user5.friends.append(friend10)
    user6.friends.append(friend9)
    user6.friends.append(friend10)
    user7.friends.append(friend11)
    user7.friends.append(friend12)
    user8.friends.append(friend13)
    user9.friends.append(friend13)
    user9.friends.append(friend14)

    db.session.add(friend1)
    db.session.add(friend2)
    db.session.add(friend3)
    db.session.add(friend4)
    db.session.add(friend5)
    db.session.add(friend6)
    db.session.add(friend7)
    db.session.add(friend8)
    db.session.add(friend9)
    db.session.add(friend10)
    db.session.add(friend11)
    db.session.add(friend12)
    db.session.add(friend13)
    db.session.add(friend14)

    db.session.commit()

def undo_friends():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.friends RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM friends"))

    db.session.commit()
