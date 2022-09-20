from CountVectorizer import CountVectorizer


def test(corpus):
    try:
        print('Initializing CountVectorizer...')
        vectorizer = CountVectorizer()
        print('Successful!')
    except Exception:
        print('Oops... Something went wrong with __init__!!!')
        raise Exception

    try:
        print('Starting fit_transform()...')
        count_matrix = vectorizer.fit_transform(corpus)
        if count_matrix == [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]:
            print('fit_transform() tested - OK!')
            print('Successful!')
    except Exception:
        print('Oops... Something went wrong with fit_transform!!!')
        raise Exception

    try:
        print('Initializing CountVectorizer...')
        if vectorizer.get_feature_names() == ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
                                              'fresh',
                                              'ingredients', 'parmesan', 'to', 'taste']:
            print('get_feature_names() tested - OK!')
    except Exception:
        print('Oops... Something went wrong with get_feature_names!!!')
        raise Exception
    print('All is OK! Perfect!')
