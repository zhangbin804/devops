from django.conf import settings


def init_permission(user, request):
    permission_list = user.roles.values('permissions__id',
                                        'permissions__title',
                                        'permissions__url',
                                        'permissions__codes',
                                        'permissions__menu_gp_id',
                                        'permissions__group_id',
                                        'permissions__group__menu_id',
                                        'permissions__group__menu__caption',
                                        ).distinct()
    url_dict = {}
    for item in permission_list:
        group_id = item["permissions__group_id"]
        url = item["permissions__url"]
        code = item["permissions__codes"]

        if group_id in url_dict:
            url_dict[group_id]["code"].append(code)
            url_dict[group_id]["urls"].append(url)
        else:
            url_dict[group_id] = {
                "code": [code, ],
                "urls": [url, ]
            }
    request.session[settings.PERMISSION_URL_DICT] = url_dict

    menu_list = []
    for item in permission_list:
        tpl = {
            "id": item["permissions__id"],
            "title": item["permissions__title"],
            "url": item["permissions__url"],
            "menu_gp_id": item["permissions__menu_gp_id"],
            "menu_id": item["permissions__group__menu_id"],
            "menu_title": item["permissions__group__menu__caption"]
        }
        menu_list.append(tpl)
    request.session[settings.PERMISSION_MENU_KEY] = menu_list
    request.session["user"] = str(user)
    request.session["is_login"] = True
    request.session["total_num"] = 5
    request.session["avatar"] = user.head_img


