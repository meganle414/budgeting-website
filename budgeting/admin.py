from django.contrib import admin

from .models import Transaction


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {"fields": ["question_text"]}),
#         ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ["question_text", "pub_date", "was_published_recently"]
#     list_filter = ["pub_date"]
#     search_fields = ["question_text"]

class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["transaction_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    # inlines = [ChoiceInline]
    list_display = ["transaction_text", "transaction_amount", "pub_date", "was_published_recently"]
    list_filter = ["pub_date", "transaction_text", "transaction_amount"]
    search_fields = ["transaction_text", "transaction_amount"]


# admin.site.register(Question, QuestionAdmin)
admin.site.register(Transaction, TransactionAdmin)