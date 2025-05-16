

def check_need_back_linked(app, need, needs, *args, **kwargs):
    """
    :param app: sphinx app
    :param need: current need
    :param needs: dictionary of all needs. Key is the need id
    :return: str,int,float or list of elements of type str,int,float
    """

    needs_dict = {}
    for n in needs:
        id = n['id_complete']
        needs_dict[id] = n

    if len(kwargs) > 0:
        print('kwargs: ', kwargs)
        print('need: ', need)
    else:
        print('kwargs: ', kwargs)
        print('need: ', need)




needs_functions = [
    check_need_back_linked,
]
