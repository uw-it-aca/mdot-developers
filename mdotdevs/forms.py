from django.utils.safestring import mark_safe
from django import forms
    
class ReviewForm(forms.Form):
    campus_audience = forms.CharField(widget=forms.widgets.Textarea(),label='Please describe what UW audiences your application is targeting.')
    campus_need = forms.CharField(widget=forms.widgets.Textarea(),label='Please describe how your application addresses a broad UW campus need.')
    sponsor_name = forms.CharField(label='Name')
    sponsor_netid = forms.CharField(label='UW NetID')
    sponsor_email = forms.EmailField(label='Email')
    dev_name = forms.CharField(label='UW NetID')
    dev_email = forms.EmailField(label='Email')  
    support_name = forms.CharField(label='Name')
    support_email = forms.EmailField(label='Email')  
    support_contact = forms.CharField(widget=forms.widgets.Textarea(),label='Other contact information')
    ats_review = forms.BooleanField(required=False, label=mark_safe('Accessibility review with <a href="http://www.washington.edu/accessibility/" title="Accessible Technology Services">UW-IT ATS</a>'), label_suffix='')
    ux_review = forms.BooleanField(required=False, label=mark_safe('Usability review with <a href="http://depts.washington.edu/ux/consultation/" title="ACA User Experience Team">ACA UX team</a>'), label_suffix='')
    brand_review = forms.BooleanField(required=False, label=mark_safe('Consulted <a href="http://www.washington.edu/brand/">UW Brand Guidelines</a>'), label_suffix='')
    app_documentation = forms.URLField(label='Provide URL for app documentation')  
    app_code = forms.CharField(widget=forms.widgets.Textarea(),label='How might we be able to review the app?')
    anything_else = forms.CharField(widget=forms.widgets.Textarea(),label='Anything else that we should know?')
    