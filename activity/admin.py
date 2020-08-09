from django.contrib import admin
from django.utils.html import format_html

from .models import Activity,Student

# Register your models here.
class ActivityAdmin(admin.ModelAdmin) :
    list_display = ['id','activity_name',
                    'act_type',
                    'activity_type',
                    'activity_date']
    list_display_links = ['id','activity_name']

    COLORDICT = {
        'AC' : 'red',
        'CU' : 'green',
        'SA' : 'blue',
    }
    save_as = True

    fields = ('activity_name',
              'activity_type',
              'activity_desc',
              'participant')

    def act_type(self,obj):
        return format_html(
            '<span style="color : {}">{}</span>',
            self.COLORDICT[obj.activity_type],
            obj.activity_type
        )
    search_fields = ['activity_name']

    pass

admin.site.register(Activity,ActivityAdmin)
admin.site.register(Student)
