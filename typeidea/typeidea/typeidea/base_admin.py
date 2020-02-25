from django.contrib import admin

class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1.用来自动补充作者字段
    2.用来筛选当前用户下的内容
    """
    exclude = ('owner',)

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin,self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin,self).save_model(request,obj,form,change)