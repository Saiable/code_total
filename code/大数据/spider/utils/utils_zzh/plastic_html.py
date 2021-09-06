'''
@Author  ：Devil~华
@Date    ：2021/6/10 9:48 
@Function：
'''
import re


def plastic_html(content, script=True, attr=True, blank=True):
    """
    clean HTML
    :param content:
    :param script:
    :param attr:
    :param blank:
    :return:
    """
    if isinstance(content, list):
        html = ''.join(content)
    else:
        html = content
    if script:
        html = re.sub('<!--.*?-->', '', html, flags=re.DOTALL)
        html = re.sub('<script.*?</script>', '', html, flags=re.DOTALL)
        html = re.sub('<style.*?</style>', '', html, flags=re.DOTALL)
    if attr:
        html = re.sub('<(\w+) (.*?)>', r'<\1>', html, flags=re.DOTALL)
    if blank:
        html = re.sub(r'>\s+<', '><', html, flags=re.DOTALL)
    return html