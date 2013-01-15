from django.contrib import admin
from faraja.website.models import *
from faraja.website.forms import *
from tinymce.widgets import TinyMCE


class WhoWeAreAdmin(admin.ModelAdmin):    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }
    
class TrusteeAdmin(admin.ModelAdmin):    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

class WhatWeDoAdmin(admin.ModelAdmin):    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

class WhatWeDoActivityAdmin(admin.ModelAdmin):    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

class TherapistAdmin(admin.ModelAdmin):    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

class InvolvedAdmin(admin.ModelAdmin):    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }
     
class TestimonialAdmin(admin.ModelAdmin):    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }
    
class FAQAdmin(admin.ModelAdmin):    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }
    
admin.site.register(WhatWeDo, WhatWeDoAdmin)
admin.site.register(WhatWeDoActivity, WhatWeDoActivityAdmin)
admin.site.register(WhoWeAre, WhoWeAreAdmin)
admin.site.register(Therapist, TherapistAdmin)
admin.site.register(Trustee, TrusteeAdmin)
admin.site.register(Involved, InvolvedAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(CancerTreatment)
admin.site.register(CancerSpecific)
