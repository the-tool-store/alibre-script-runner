# Alibre Script Runner

A launcher that connects to a running Alibre Design session and runs IronPython automation scripts from a menu. It scans the configured script folders and exposes each `.py` file as a menu item, executing the selected script against the live Alibre Script API.

## Features

- Connects to an already-running Alibre Design session via the `AlibreX.AutomationHook` automation object.
- Presents a Windows Forms window with menus generated from the script folders.
- Scans the `scripts`, `prototypes`, `randd`, and `examples` subfolders of the base path, plus loose `.py` files in the base folder, and lists each script as a menu item. A menu appears only when its folder contains `.py` files; loose scripts (other than `main.py`) are listed under "Root Scripts".
- Runs the chosen script in the global scope so it has access to the Alibre Script API (`Part`, `Assembly`, `Windows`, `Units`, etc.) and the active `alibre`/`root` objects.
- A "File > Set Base Path..." menu item opens a folder browser to point the runner at a different base folder at runtime and rebuilds the menus.
- Reports script errors in a dialog instead of failing silently.
- Includes example scripts (`main_ex1.py`, `main_ex2.py`, `main_ex3.py`, and `scripts/ex_as_fun_1.py`, `scripts/ex_as_fun_2.py`) covering Alibre Script tasks such as bolts, gears, lofts, sketches, and reference geometry.

## Requirements

- Alibre Design 29.0.0.29060 (the bundled AlibreScript add-on supplies the `AlibreX`, `AlibreScriptAddOn`, and `AlibreScript.API` assemblies). The scripts reference the install path `C:\Program Files\Alibre Design 29.0.0.29060`.
- IronPython, as provided by the Alibre Script add-on (the engine Alibre Script uses to run `.py` files).
- Windows with .NET Windows Forms (`System.Windows.Forms`, `System.Drawing`).

## Installation

There is no installer, build step, or `.adc` add-on manifest in this project. It is a collection of IronPython scripts run through Alibre Script.

1. Clone this repository, including its submodule:

   ```
   git clone --recurse-submodules <repo-url>
   ```

2. Open `source/main.py` and update the paths if the Alibre Design install differs from `C:\Program Files\Alibre Design 29.0.0.29060`.
3. Set `base_path` in `source/main.py` to the folder that holds the `scripts`, `prototypes`, `randd`, and `examples` subfolders (or change it later from the runner's "Set Base Path..." menu). The default in the file is `T:\a\alibre-script-runner` and will likely need to be changed.

## Usage

1. Start Alibre Design and leave it running.
2. In Alibre Script, open and run `source/main.py`.
3. The "Alibre Script Runner" window opens. Use the generated menus to select a script. Menu titles map to folders as follows: Scripts (`scripts`), Prototypes (`prototypes`), R&D Tools (`randd`), Examples (`examples`), and Root Scripts (loose `.py` files in the base folder). Only menus whose folder contains `.py` files are shown.
4. The selected script executes against the live Alibre session; any errors are shown in a dialog.

## License

See [LICENSE](../LICENSE).
