#-------------------------------------------------------------------------------
import dracula.draw
#-------------------------------------------------------------------------------
# Browser Configs

config.load_autoconfig(False)

# Notifications and Other Media Configs per Site
config.set('content.notifications.enabled', False, 'https://www.reddit.com')
config.set('content.notifications.enabled', False, 'https://calendar.google.com')
config.set('content.notifications.enabled', False, 'https://www.facebook.com')
config.set('content.notifications.enabled', False, 'https://www.youtube.com')
config.set('content.notifications.enabled', False, 'https://www.netflix.com')
config.set('content.notifications.enabled', False, 'https://thepiratebay.org')
config.set('content.media.audio_capture', True, 'https://www.meet.google.com')
config.set('content.media.video_capture', True, 'https://www.meet.google.com')
config.set('content.register_protocol_handler', True)

# Misc
c.tabs.mode_on_change = 'restore'
c.search.ignore_case = 'always'
c.statusbar.show = 'always'
c.auto_save.session = True
c.confirm_quit = ['downloads']
c.content.tls.certificate_errors = 'block'
c.downloads.location.directory = '/home/philippe/Downloads/'
c.editor.command = ['kitty', 'nvim', '{}']

# Colors & Media
monospace = '8px "Fira Code"'
c.colors.webpage.darkmode.enabled = True # requires a restart when changed
c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.bg = 'black'

# Tabs
c.tabs.title.format = '{index} {current_title}'
c.tabs.show = 'always'
c.tabs.background = True
c.tabs.last_close = "close"
c.tabs.select_on_remove = "prev"
#-------------------------------------------------------------------------------
# Themes

dracula.draw.blood(c, {
    'spacing': {
        'vertical':   6,
        'horizontal': 8
    }
})
#-------------------------------------------------------------------------------
# Search Engines

# my_search_engine = 'https://www.searx.bar'
my_search_engine = 'https://google.com'

c.url.start_pages = [my_search_engine]
c.url.default_page = my_search_engine

c.url.searchengines = {
        'DEFAULT': f'{my_search_engine}/search?q=' + '{}',
        ':am':      'https://www.amazon.com/s?k={}',
        ':ambr':    'https://www.amazon.com.br/s?k={}',
        ':aw':      'https://wiki.archlinux.org/?search={}',
        ':br':      'https://search.brave.com/search?={}',
        ':col':     'https://www.collinsdictionary.com/us/dictionary/english/{}',
        ':g':       'https://www.google.com/search?q={}',
        ':gh':      'https://github.com/search?q={}',
        ':gr':      'https://goodreads.com/search?q={}',
        ':grabcad': 'https://grabcad.com/library?page=1&time=all_time&sort=recent&query={}',
        ':h':       'https://hoogle.haskell.org/?hoogle={}',
        ':hw':      'https://wiki.haskell.org/index.php?search={}',
        ':isbn':    'https://isbnsearch.org/search?s={}',
        ':l':       'https://www.linguee.pt/portugues-ingles/search?query={}',
        ':lbry':    'https://lbry.tv/$/search?q={}',
        ':libgen':  'http://libgen.rs/search.php?req={}',
        ':od':      'https://odysee.com/$/search?q={}',
        ':pub':     'https://pub.dev/packages?q={}',
        ':pr':      'https://piratebay.party/search/{}',
        ':prib':    'https://dicionario.priberam.org/{}',
        ':re':      'https://www.reddit.com/search/?q={}',
        ':sensei':  'https://senseis.xmp.net/?search={}',
        ':sx':      'https://www.searx.bar/search?q={}',
        ':ub':      'https://www.urbandictionary.com/define.php?term={}',
        ':u':       'https://www.udemy.com/courses/search/?src={}',
        ':yt':      'https://www.youtube.com/results?search_query={}',
        ':w':       'https://en.wikipedia.org/wiki/{}',
        ':wfr':     'https://fr.wikipedia.org/wiki/{}',
        ':wpt':     'https://pt.wikipedia.org/wiki/{}',
        ':wq':      'https://en.wikiquote.org/wiki/Special:Search?search={}',

}
#-------------------------------------------------------------------------------
# Shortcuts

toggle_statusbar = 'config-cycle statusbar.show always never'
toggle_tabs      = 'config-cycle tabs.show always never'

player_div =  'document.querySelector("#movie_player")'
player_div_or_elem = 'document.querySelector("#movie_player, video")'
player_elem = 'document.querySelector("video")'

config.bind('<alt+r>',         'restart')
config.bind('(',              f'jseval -q {player_div_or_elem}.focus()')
config.bind(')',              f'jseval -q {player_div_or_elem}.blur()')
config.bind('f',               'hint all tab')
config.bind('F',               'hint all current')
config.bind('<ctrl+shift+x>',  'tab-pin')
config.bind('<alt+b>',         'back')
config.bind('<alt+f>',         'forward')
config.bind('yo',              'yank inline "[[{url}][{title}]]"')
config.bind('yml',             'yank inline "[{title}][url][url]: {url}"')
config.bind('t',               'set-cmd-text -s :open -t')
config.bind('M',               'hint links spawn mpv {hint-url}')
config.bind('Z',               'hint links spawn konsole -e youtube-dl {hint-url}')
config.bind('xt',               toggle_tabs)
config.bind('xb',               toggle_statusbar)
config.bind('xx',            f'{toggle_tabs};; {toggle_statusbar}')
config.bind('ba',             'bookmark-add')
config.bind('bd',             'bookmark-del')
config.bind('<alt+t>',        'set-cmd-text :tab-give ')
config.bind('<',             f'jseval {player_elem}.playbackRate-=.25')
config.bind('>',             f'jseval {player_elem}.playbackRate+=.25')
config.bind('ss',             'set-cmd-text -s :session-save -o')
config.unbind('b')
config.unbind('m')
config.unbind('d')
config.unbind('r')
config.unbind('<ctrl+shift+w>')
config.bind('<ctrl+r>',       'reload')

# Themes Shortcuts
config.bind(',ex', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/experimental.css ""')
config.bind(',ap', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized/css/apprentice/apprentice-all-sites.css ""')
config.bind(',dr', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized/css/darculized/darculized-all-sites.css ""')
config.bind(',gr', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized/css/gruvbox/gruvbox-all-sites.css ""')
config.bind(',sd', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized/css/solarized-dark/solarized-dark-all-sites.css ""')
config.bind(',sl', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized/css/solarized-light/solarized-light-all-sites.css ""')
#-------------------------------------------------------------------------------
