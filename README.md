# python-gtk-app

Demo for ProtonMail job opening: https://careers.protonmail.com/o/senior-pythongtk-linux-client-developer

This is a demo of a GTK+ 3 application written in Python and packaged into a
Debian package.

## Runtime prerequisites

To be able to run the application, you need to [set up PyGObject](https://pygobject.readthedocs.io/en/latest/getting_started.html).
For Ubuntu/Debian, these are the package you currently need:

```sh
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
```

## Build prerequisites

I'm using pybuild to build the debian package. You can install it with:

```sh
sudo apt install dh-python
```

To ease the build of the debian package, I'm using dh-virtualenv:

```sh
sudo apt-get install build-essential debhelper devscripts equivs dh-virtualenv
```

To build the debian package:

```sh
( deactivate ; dpkg-buildpackage -us -uc -b )
```
