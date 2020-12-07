


def add_new_user(username, password):
    from model.User import User
    try:
        new_user = User(username=username, password=password)
        new_user.add()
        return new_user.id
    except Exception as e:
        print(e)
        return None
