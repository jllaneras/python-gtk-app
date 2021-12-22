# Python GTK3 demo application

Demo for ProtonMail job opening:
https://careers.protonmail.com/o/senior-pythongtk-linux-client-developer

This is a demo of a GTK+ 3 application written in Python and packaged into a
Debian package.

For now is just a dummy app. I focused on the debian package build first.

## Development

### Prerequisites

[PyGObject](https://pygobject.readthedocs.io/en/latest/getting_started.html)
is needed to run the application.

```sh
sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0
```

### Installing the pip dependencies

```sh
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

### Running the application

```sh
python3 -m gtk3demo
```

## Debian package build

This section explains how I build the debian package.

FIXME: The build could be more repeatable and straightforward doing it in a docker container.

### Prerequisites

[dh-virtualenv](https://dh-virtualenv.readthedocs.io/en/latest/tutorial.html#step-1-install-dh-virtualenv)
is needed to build the debian package.

```sh
sudo apt-get install \
    build-essential debhelper devscripts equivs dh-virtualenv \
    libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0
```

### Build

To build the debian package:

```sh
( deactivate ; dpkg-buildpackage -us -uc -b )
```

### Installing the application

```sh
sudo dpkg -i ../gtk3demo_*.deb
```

### Launching application

Run the following command on the terminal.

```sh
gtk3-demo-app
```
