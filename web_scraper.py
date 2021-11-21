def save_html(html, path):
    """
    Save html to path
    """
    with open(path, 'wb') as f:
        f.write(html)

save_html(r.content, 'google_com')

def open_html(path):
    """
    Open html file
    """
    with open(path, 'rb') as f:
        html = f.read()

html = open_html('google_com')

