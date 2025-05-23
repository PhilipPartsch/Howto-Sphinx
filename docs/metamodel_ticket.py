from sphinx_needs.config import NeedsSphinxConfig

def check_if_need_is_in_link(need, link):
    need_id = need['id']
    need_id_complete = need['id_complete']

    return need_id in link or need_id_complete in link


def check_need_linked(app, need, needs, *args, **kwargs):
    """
    :param app: sphinx app
    :param need: current need
    :param needs: dictionary of all needs. Key is the need id
    :return: str,int,float or list of elements of type str,int,float
    """

    # todo:
    # check linked:
    # - need
    # - need part
    # - need variant

    needs_config = NeedsSphinxConfig(app.config)
    needs_config_extra_links = needs_config.extra_links

    result: bool = False

    print('kwargs: ', kwargs)
    print('args: ', args)

    if len(args) > 0:
        for k, v in needs.items():
            for link in needs_config_extra_links:
                if link['option'] in args:
                    result = check_if_need_is_in_link(need, link = v[link['option']])
                    if result:
                        break
            if result:
                break
    else:
        for k, v in needs.items():
            for link in needs_config_extra_links:
                result = check_if_need_is_in_link(need, link = v[link['option']])
                if result:
                    break
            if result:
                break

    return result

def if_set_else_set(app, need, needs, *args, **kwargs):
    print('kwargs: ', kwargs)
    print('need: ', need)

    return ''



needs_functions = [
    check_need_linked,
    if_set_else_set,
]
