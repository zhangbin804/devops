class PagerHelper:
    def __init__(self,total_count,current_page,base_url,per_page=10):
        self.total_count = total_count
        self.current_page = current_page
        self.base_url = base_url
        self.per_page = per_page
        if self.base_url.find('?') == -1:
            self.get_flag = '?'
        else:
            self.get_flag = '&'

    @property
    def db_start(self):
        return (self.current_page -1) * self.per_page

    @property
    def db_end(self):
        return self.current_page * self.per_page

    def total_page(self):
        v, a = divmod(self.total_count, self.per_page)
        if a != 0:
            v += 1
        return v

    def pager_str(self):
        v = self.total_page()
        pager_list = []
        if self.current_page == 1:
            pager_list.append('<li><a href="javascript:void(0);">上一页</a></li>')
        else:
            pager_list.append('<li><a href="%s%sp=%s">上一页</a></li>' % (self.base_url, self.get_flag,self.current_page - 1,))

        if v <= 11:
            pager_range_start = 1
            pager_range_end = v
        else:
            if self.current_page < 6:
                pager_range_start = 1
                pager_range_end = 11 + 1
            else:
                pager_range_start = self.current_page - 5
                pager_range_end = self.current_page + 5 + 1
                if pager_range_end > v:
                    pager_range_start = v - 10
                    pager_range_end = v + 1

        for i in range(pager_range_start, pager_range_end+1):
            if i == self.current_page:
                pager_list.append('<li class="active"><a class="active" href="%s%sp=%s" >%s</a></li>' % (self.base_url, self.get_flag,i, i,))
            else:
                pager_list.append('<li><a href="%s%sp=%s">%s</a></li>' % (self.base_url, self.get_flag,i, i,))

        if self.current_page == v:
            pager_list.append('<li><a href="javascript:void(0);">下一页</a></li>')
        else:
            pager_list.append('<li><a href="%s%sp=%s">下一页</a></li>' % (self.base_url, self.get_flag,self.current_page + 1,))

        pager = "".join(pager_list)
        return pager

class PagerObj(PagerHelper):

    def __init__(self,current_page,base_url,models_all,per_page=10):
        self.current_page = current_page
        self.base_url = base_url
        self.per_page = per_page
        self.models_all = models_all
        self.page_count = self.models_all.count()
        self.pager = PagerHelper(self.page_count,self.current_page,self.base_url,self.per_page)

    def pages(self):
        pager = self.pager.pager_str()
        models_list = self.models_all[self.pager.db_start:self.pager.db_end]
        last_integer = self.page_count // self.per_page
        last_remainder = self.page_count % self.per_page

        if last_integer < 1:
            last_page = 1
        else:
            if last_remainder == 0:
                last_page = last_integer
            else:
                last_page = last_integer + 1
        return pager,models_list

