import yaml

config.load_autoconfig()

with (config.configdir / 'colors.yml').open() as f:
    yaml_data = yaml.safe_load(f)

def dict_attrs(obj, path=''):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from dict_attrs(v, '{}.{}'.format(path, k) if path else k)
    else:
        yield path, obj

for k, v in dict_attrs(yaml_data):
    config.set(k, v)

c.colors.webpage.prefers_color_scheme_dark = True

c.aliases = {'q': 'close', 'qa': 'quit', 'w': 'session-save', 'wq': 'quit --save', 'wqa': 'quit --save'}

c.session.default_name = None

c.content.autoplay = False

c.scrolling.smooth = True

c.tabs.last_close = 'close'

c.tabs.padding = {'bottom': 5, 'left': 5, 'right': 5, 'top': 3}
c.tabs.select_on_remove = 'last-used'
c.tabs.title.format = '{perc}{audio}{current_title}'
c.tabs.min_width = 100
c.tabs.max_width = 300
c.tabs.indicator.width = 0
c.tabs.wrap = False
config.bind('<Ctrl+Shift+j>', 'tab-move +')
config.bind('<Ctrl+Shift+k>', 'tab-move -')

c.hints.auto_follow_timeout = 500
c.hints.mode = 'word'
c.hints.uppercase = True

c.url.searchengines = {'DEFAULT': 'https://google.com/search?q={}', 'ddg': 'https://duckduckgo.com/?q={}'}
c.url.start_pages = 'about:blank'

c.window.title_format = '{perc}{current_title}'
c.window.hide_decoration = True

c.fonts.default_family = ['Source Code Pro', 'Roboto']
c.fonts.web.family.sans_serif = 'roboto'
c.fonts.web.family.serif = 'noto serif'
c.fonts.web.family.standard = 'roboto'
c.fonts.prompts = 'default_size default_family'

config.bind('<Ctrl+Shift+m>', 'hint links spawn --detach mpv {hint-url}')
config.bind('M', 'spawn --detach mpv {url}')

