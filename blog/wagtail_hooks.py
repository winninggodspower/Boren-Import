from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from core.models import Gallery
from newsletter.models import Newsletter

class NewsletterAdmin(ModelAdmin):
    model = Newsletter
    menu_label = 'Newsletter' 
    menu_icon = 'mail'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('email',)
    list_filter = ('email',)
    search_fields = ('email', )

class GalleryAdmin(ModelAdmin):
    model = Gallery
    menu_label = 'Gallery' 
    menu_icon = 'image'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('date_added',)
    list_filter = ('date_added',)
    search_fields = ('date_added', )

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(GalleryAdmin)
modeladmin_register(NewsletterAdmin)