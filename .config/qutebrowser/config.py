# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
config.load_autoconfig()

# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
# Type: Dict
c.aliases = {'q': 'close', 'qa': 'quit', 'w': 'session-save', 'wq': 'quit --save', 'wqa': 'quit --save'}

# Name of the session to save by default. If this is set to null, the
# session which was last loaded is saved.
# Type: SessionName
c.session.default_name = None

# Automatically start playing `<video>` elements. Note: On Qt < 5.11,
# this option needs a restart and does not support URL patterns.
# Type: Bool
c.content.autoplay = False

# Limit fullscreen to the browser window (does not expand to fill the
# screen).
# Type: Bool
c.content.windowed_fullscreen = True

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
# Type: Bool
c.scrolling.smooth = True

# Hide the statusbar unless a message is shown.
# Type: Bool
c.statusbar.hide = False

# How to behave when the last tab is closed.
# Type: String
# Valid values:
#   - ignore: Don't do anything.
#   - blank: Load a blank page.
#   - startpage: Load the start page.
#   - default-page: Load the default page.
#   - close: Close the window.
c.tabs.last_close = 'close'

# Padding (in pixels) around text for tabs.
# Type: Padding
c.tabs.padding = {'bottom': 5, 'left': 5, 'right': 5, 'top': 3}

# Which tab to select when the focused tab is removed.
# Type: SelectOnRemove
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = 'last-used'

# Format to use for the tab title. The following placeholders are
# defined:  * `{perc}`: Percentage as a string like `[10%]`. *
# `{perc_raw}`: Raw percentage, e.g. `10`. * `{current_title}`: Title of
# the current web page. * `{title_sep}`: The string ` - ` if a title is
# set, empty otherwise. * `{index}`: Index of this tab. * `{id}`:
# Internal tab ID of this tab. * `{scroll_pos}`: Page scroll position. *
# `{host}`: Host of the current web page. * `{backend}`: Either
# ''webkit'' or ''webengine'' * `{private}`: Indicates when private mode
# is enabled. * `{current_url}`: URL of the current web page. *
# `{protocol}`: Protocol (http/https/...) of the current web page. *
# `{audio}`: Indicator for audio/mute status.
# Type: FormatString
c.tabs.title.format = '{perc}{audio}{current_title}'

# Minimum width (in pixels) of tabs (-1 for the default minimum size
# behavior). This setting only applies when tabs are horizontal. This
# setting does not apply to pinned tabs, unless `tabs.pinned.shrink` is
# False.
# Type: Int
c.tabs.min_width = 100

# Maximum width (in pixels) of tabs (-1 for no maximum). This setting
# only applies when tabs are horizontal. This setting does not apply to
# pinned tabs, unless `tabs.pinned.shrink` is False. This setting may
# not apply properly if max_width is smaller than the minimum size of
# tab contents, or smaller than tabs.min_width.
# Type: Int
c.tabs.max_width = 300

# Width (in pixels) of the progress indicator (0 to disable).
# Type: Int
c.tabs.indicator.width = 0

# Wrap when changing tabs.
# Type: Bool
c.tabs.wrap = False

# Search engines which can be used via the address bar. Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` signs. The search engine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'https://google.com/search?q={}', 'ddg': 'https://duckduckgo.com/?q={}'}

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = 'about:blank'

# Format to use for the window title. The same placeholders like for
# `tabs.title.format` are defined.
# Type: FormatString
c.window.title_format = '{perc}{current_title}'

c.window.hide_decoration = True

# Background color of the tab bar.
# Type: QssColor
c.colors.tabs.bar.bg = '#1a1a1a'

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = '#ff0000'

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = '#d0d0d0'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#1a1a1a'

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = '#d0d0d0'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#1a1a1a'

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = '#efefef'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#3c3c3c'

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = '#efefef'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#3c3c3c'

# Default monospace fonts. Whenever "monospace" is used in a font
# setting, it's replaced with the fonts listed here.
# Type: Font
c.fonts.monospace = '"DejaVu Sans Mono", Terminus, Monospace, "DejaVu Sans Mono", Monaco, "Bitstream Vera Sans Mono", "Andale Mono", "Courier New", Courier, "Liberation Mono", monospace, Fixed, Consolas, Terminal'

# Font used in the completion widget.
# Type: Font
c.fonts.completion.entry = '10pt dejavu sans mono'

# Font used in the completion categories.
# Type: Font
c.fonts.completion.category = 'bold 10pt dejavu sans mono'

# Font used for the debugging console.
# Type: QtFont
c.fonts.debug_console = '10pt dejavu sans mono'

# Font used for the downloadbar.
# Type: Font
c.fonts.downloads = '10pt dejavu sans mono'

# Font used for the hints.
# Type: Font
c.fonts.hints = 'bold 10pt dejavu sans mono'

# Font used in the keyhint widget.
# Type: Font
c.fonts.keyhint = '10pt dejavu sans mono'

# Font used for error messages.
# Type: Font
c.fonts.messages.error = '10pt dejavu sans mono'

# Font used for info messages.
# Type: Font
c.fonts.messages.info = '10pt dejavu sans mono'

# Font used for warning messages.
# Type: Font
c.fonts.messages.warning = '10pt dejavu sans mono'

# Font used for prompts.
# Type: Font
c.fonts.prompts = '10pt dejavu sans mono'

# Font used in the statusbar.
# Type: Font
c.fonts.statusbar = '10pt dejavu sans mono'

# Font used in the tab bar.
# Type: QtFont
c.fonts.tabs = '10pt dejavu sans mono'

# Font family for standard fonts.
# Type: FontFamily
c.fonts.web.family.standard = 'roboto'

# Font family for fixed fonts.
# Type: FontFamily
c.fonts.web.family.fixed = 'dejavu sans mono'

# Font family for serif fonts.
# Type: FontFamily
c.fonts.web.family.serif = 'roboto'

# Font family for sans-serif fonts.
# Type: FontFamily
c.fonts.web.family.sans_serif = 'noto sans'

# Font family for cursive fonts.
# Type: FontFamily
c.fonts.web.family.cursive = 'roboto'

# Font family for fantasy fonts.
# Type: FontFamily
c.fonts.web.family.fantasy = 'roboto'

# Bindings for normal mode
config.bind('<Ctrl+Shift+m>', 'hint links spawn --detach mpv {hint-url}')
config.bind('M', 'spawn --detach mpv {url}')

config.bind('<Ctrl+Shift+j>', 'tab-move +')
config.bind('<Ctrl+Shift+k>', 'tab-move -')
