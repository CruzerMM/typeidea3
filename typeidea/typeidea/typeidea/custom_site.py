from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea后台管理'
    index_title = '首页'

custom_site = CustomSite(name='cus_admin')