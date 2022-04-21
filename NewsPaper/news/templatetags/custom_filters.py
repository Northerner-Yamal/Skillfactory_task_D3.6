from django import template


register = template.Library()

BAD_WORDS = [
    'Premier',
    'premier',
    'Champions',
    'champions',
    'will',
    'Will',
    'home',
    'Home'
]

@register.filter()
def censor(NEW_WORD):
    for word in BAD_WORDS:
        if word in BAD_WORDS:
            repl_word = word[0] + (len(word)-1) * '*'
            NEW_WORD = NEW_WORD.replace(word, repl_word)

    return NEW_WORD

