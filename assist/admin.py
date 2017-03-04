from django.contrib import admin
from .models import Course, Department, User, Student, ExamPaper, Material, Announcement, CourseAllotment,Bookmark
admin.site.empty_value_display = '(None)'
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','dept','code' )
    list_display_links = ('name',)
admin.site.register(Course,CourseAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    fields = ('name','acronym')
    list_display = ('name','acronym', )
    list_display_links = ('name',)
admin.site.register(Department,DepartmentAdmin)

class UserAdmin(admin.ModelAdmin):
    fields = ('first_name','last_name','email','user_role')
    list_display = ('name','email','user_role' )
    list_display_links = ('name','email')
    def name(self,obj):
        return 'None' if(obj.first_name +' '+ obj.last_name==' ') else obj.first_name +' '+ obj.last_name
admin.site.register(User,UserAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('registration_no','semester','user')
    list_display_links = ('registration_no',)
admin.site.register(Student,StudentAdmin)

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('course','description','updated_on','added_on','files','title','author' )
    list_display_links = ('course','title')
admin.site.register(Announcement,AnnouncementAdmin)

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('course','title','added_on','files','author' )
    list_display_links = ('course',)
admin.site.register(Material,MaterialAdmin)

class ExamPapersAdmin(admin.ModelAdmin):
    list_display = ('course','files','term','author' )
    list_display_links = ('course',)
admin.site.register(ExamPaper,ExamPapersAdmin)

class CourseAllotmentAdmin(admin.ModelAdmin):
    list_display = ('course','semester' )
    list_display_links = ('course',)
admin.site.register(CourseAllotment,CourseAllotmentAdmin)

class BookmarksAdmin(admin.ModelAdmin):
    list_display = ('course','user' )
    list_display_links = ('course',)
admin.site.register(Bookmark,BookmarksAdmin)
