from collections import Counter, defaultdict

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

# the tuple (0,1) means id: 0 and id: 1 are friend so on.
friendship_pairs = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9),
]

# instead above we create the dict where the keys are use "ids" and
# the values are lists of friend "ids"
friendships = {user["id"]: [] for user in users}


def number_of_friends(user):
    """How many friends does user have?"""
    user_id = user["id"]
    friends_ids = friendships[user_id]
    return len(friends_ids)


def Exec_find_key_connect():
    for i, j in friendship_pairs:
        friendships[i].append(j)
        friendships[j].append(i)

    print("friendships: ", friendships)

    total_connections = sum(number_of_friends(user) for user in users)  # 24
    print("total_connections: ", total_connections)

    num_users = len(users)
    avg_connections = total_connections / num_users  # 2.4
    print("avg_connections: ", avg_connections)

    # Since there aren't many users,
    # we can simply sort them from "most friends" to "least friends".
    num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
    num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)
    print("num_friends_by_id: ", num_friends_by_id)


# =================================================================
def Exec_DataScientists_You_May_Know():
    find_friend_overlap = foaf_ids_bad(users[0])
    print("find_friend_overlap: ", find_friend_overlap)

    find_friend = friends_of_friends(users[0])
    print("find_friend: ", find_friend)


def foaf_ids_bad(user):
    """foaf is short for "friend of a friend" """
    return [
        foaf_id
        for friend_id in friendships[user["id"]]
        for foaf_id in friendships[friend_id]
    ]


def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id  # who aren't me
        and foaf_id not in friendships[user_id]  # aren't my friends.
    )


interests = [
    (0, "Hadoop"),
    (0, "Big Data"),
    (0, "HBase"),
    (0, "Java"),
    (0, "Spark"),
    (0, "Storm"),
    (0, "Cassandra"),
    (1, "NoSQL"),
    (1, "MongoDB"),
    (1, "Cassandra"),
    (1, "HBase"),
    (1, "Postgres"),
    (2, "Python"),
    (2, "scikit-learn"),
    (2, "scipy"),
    (2, "numpy"),
    (2, "statsmodels"),
    (2, "pandas"),
    (3, "R"),
    (3, "Python"),
    (3, "statistics"),
    (3, "regression"),
    (3, "probability"),
    (4, "machine learning"),
    (4, "regression"),
    (4, "decision trees"),
    (4, "libsvm"),
    (5, "Python"),
    (5, "R"),
    (5, "Java"),
    (5, "C++"),
    (5, "Haskell"),
    (5, "programming languages"),
    (6, "statistics"),
    (6, "probability"),
    (6, "mathematics"),
    (6, "theory"),
    (7, "machine learning"),
    (7, "scikit-learn"),
    (7, "Mahout"),
    (7, "neural networks"),
    (8, "neural networks"),
    (8, "deep learning"),
    (8, "Big Data"),
    (8, "artificial intelligence"),
    (9, "Hadoop"),
    (9, "Java"),
    (9, "MapReduce"),
    (9, "Big Data"),
]


def Exec_data_scientists_who_like():
    # Keys are interests, values are lists of user_ids with that interest.
    user_ids_by_interest = defaultdict(list)

    for user_id, interest in interests:
        user_ids_by_interest[interest].append(user_id)

    print("user_ids_by_interest: ", user_ids_by_interest)

    # Keys are user_ids, values are lists of interests for that user_id.
    interests_by_user_id = defaultdict(list)

    for user_id, interest in interests:
        interests_by_user_id[user_id].append(interest)

    print("interests_by_user_id: ", interests_by_user_id)

    def most_common_interests_with(user):
        res = Counter(
            interested_user_id
            for interest in interests_by_user_id[user["id"]]
            for interested_user_id in user_ids_by_interest[interest]
            if interested_user_id != user["id"]
        )
        return res

    most_common_interest = most_common_interests_with
    print("most_common_interests_with: ", most_common_interest(users[0]))


def data_scientists_who_like(target_interest):
    """
    Find the ids of all users who like the target interest.
    """
    return [
        user_id
        for user_id, user_interest in interests
        if user_interest == target_interest
    ]


# ===========================================
salaries_and_tenures = [
    (83000, 8.7),
    (88000, 8.1),
    (48000, 0.7),
    (76000, 6),
    (69000, 6.5),
    (76000, 7.5),
    (60000, 2.5),
    (83000, 10),
    (48000, 1.9),
    (63000, 4.2),
]

paid_Accounts = {
    0.7: "paid",
    1.9: "unpaid",
    2.5: "paid",
    4.2: "unpaid",
    6.0: "unpaid",
    6.5: "unpaid",
    7.5: "unpaid",
    8.1: "unpaid",
    8.7: "paid",
    10.0: "paid",
}


def Exec_salary_by_tenure():
    # Keys are years, values are lists of the salaies for each tenure.
    salary_by_tenure = defaultdict(list)

    for salary, tenure in salaries_and_tenures:
        salary_by_tenure[tenure].append(salary)

    # Keys are years, each value is average salary for that tenure.
    average_salary_by_tenure = {
        tenure: sum(salaries) / len(salaries)
        for tenure, salaries in sorted(
            salary_by_tenure.items(), key=lambda item: item[1]
        )
    }

    print("average_salary_by_tenure: ", average_salary_by_tenure)

    salary_by_tenure_bucket = defaultdict(list)

    for salary, tenure in salaries_and_tenures:
        bucket = tenure_bucket(tenure)
        salary_by_tenure_bucket[bucket].append(salary)

    print("salary_by_tenure_bucket: ", salary_by_tenure_bucket)

    # Keys are tenure buckets, values are average salary for that bucket
    average_salary_by_bucket = {
        tenure_bucket: sum(salaries) / len(salaries)
        for tenure_bucket, salaries in salary_by_tenure_bucket.items()
    }

    print("average_salary_by_bucket: ", average_salary_by_bucket)

    ## Paid Accounts
    tenure_paid_Account = {
        expreience: predict_paid_or_unpaid(expreience)
        for expreience, _ in sorted(paid_Accounts.items(), key=lambda item: item[0])
    }
    print("tenure_paid_Account: ", tenure_paid_Account)

    interests = [
        (0, "Hadoop"),
        (0, "Big Data"),
        (0, "HBase"),
        (0, "Java"),
        (0, "Spark"),
        (0, "Storm"),
        (0, "Cassandra"),
        (1, "NoSQL"),
        (1, "MongoDB"),
        (1, "Cassandra"),
        (1, "HBase"),
        (1, "Postgres"),
        (2, "Python"),
        (2, "scikit-learn"),
        (2, "scipy"),
        (2, "numpy"),
        (2, "statsmodels"),
        (2, "pandas"),
        (3, "R"),
        (3, "Python"),
        (3, "statistics"),
        (3, "regression"),
        (3, "probability"),
        (4, "machine learning"),
        (4, "regression"),
        (4, "decision trees"),
        (4, "libsvm"),
        (5, "Python"),
        (5, "R"),
        (5, "Java"),
        (5, "C++"),
        (5, "Haskell"),
        (5, "programming languages"),
        (6, "statistics"),
        (6, "probability"),
        (6, "mathematics"),
        (6, "theory"),
        (7, "machine learning"),
        (7, "scikit-learn"),
        (7, "Mahout"),
        (7, "neural networks"),
        (8, "neural networks"),
        (8, "deep learning"),
        (8, "Big Data"),
        (8, "artificial intelligence"),
        (9, "Hadoop"),
        (9, "Java"),
        (9, "MapReduce"),
        (9, "Big Data"),
    ]
    # for _, interest in interests:
    #     print("interest: ", interest)
    #     for word in interest.lower().split():
    #         print("word: ", word)

    # for word in interest.lower().split():
    #     print("word: ", word)

    # Topics of Interest in which using space to split and counter each word.
    words_and_counts = Counter(
        word for _, interest in interests for word in interest.lower().split()
    )
    print("words_and_counts: ", words_and_counts)

    for word, count in words_and_counts.most_common():
        if count > 1:
            print(word, count)


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


# Paid Accounts
def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"
