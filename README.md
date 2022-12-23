# gif-popup-menu

This app displays a menu to quickly look for GIFs from Tenor. It is meant to be used as a keybind to quickly look for GIFs.

## Usage

Once the menu is up, type your seach and hit enter. The menu will display the top 6 GIFs for that query. Click on a gif to copy its URL to your clipboard. Modify your search by retyping in the bar and hitting enter again. The menu will automatically close once you select a GIF.

### i3 config

Add the following to your i3 config file (typically in ~/.config/i3/config)

```bash
bindsym $mod+g exec python3 *INSTALL_PATH*/gif-popup-menu/gif-popup-menu.py
```

## Requirements

```bash
pip3 install -r requirements
```