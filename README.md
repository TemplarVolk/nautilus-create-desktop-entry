# nautilus-create-desktop-entry

Nautilus extension that adds an option to create a desktop entry on the submenu of executable files

## Requirements:

Python extensions require `nautilus-python`.

## Installing

RPM packages coming soon, for now see [building](#building) to install it manually.

## Building

```bash
mkdir build && cd build
meson .. # to install it locally use --prefix=$HOME/.local
ninja
sudo ninja install
```

## License

   [GPL-3.0](LICENSE.md)
