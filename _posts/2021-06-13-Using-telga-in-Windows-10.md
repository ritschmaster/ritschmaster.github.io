---
layout: post
title:  Using telega in Windows 10
author: Richard Bäck
---

[telega](https://github.com/zevlg/telega.el) is an Emacs package supplying a
full Telegram client. The package and idea is not only great, it works almost
out-of-the-box. The biggest challenge is to keep up with the correct tdlib
version.

Under Linux this can be annoying but is rather easy. Under Windows it is a bit
more difficult but nevertheless possible!

# Prerequisites

To get everything up and running we will utilize [Msys2](https://www.msys2.org/)
which is a wonderful application supplying
[pacman](https://en.wikipedia.org/wiki/Arch_Linux#Pacman) for Windows. It also
includes many GNU Utils, a full [MinGW](http://mingw.osdn.io/index.html)
environment and plenty libraries for MinGW. Additionally we use the Emacs
version it supplies.

As we will build some stuff by ourselves and MinGW ships 32 Bit and 64 Bit
versions of all of its libraries, I will only mention one version. This will be
the 64 Bit version. __If you are still running a 32 Bit machine, then please
replace each occurrence of 64 in the next statements by yourself.__

## Installing Msys2

This is straight forward. Get it [here](https://www.msys2.org/#installation) and
follow the instructions described there.

__Important__: There is a difference in the terminals Msys2 supplies. Therefore
use the terminal mentioned in the instructions!

## Installing Emacs

Open a __Msys2 MinGW 64-bit__ Terminal. Then enter the following instructions:

    pacman -S msys/emacs mingw64/mingw-w64-x86_64-emacs
    
This will install the Msys2 and the MinGW64 version of Emacs. The MinGW64
version will be used to actually work with Emacs. The Msys2 version is only
needed to build telega.

## Installing library dependencies

The following packages are needed to get tdlib up and running:

    pacman -S msys/git msys/gcc mingw64/mingw-w64-x86_64-gcc mingw64/mingw-w64-x86_64-cmake mingw64/mingw-w64-x86_64-gperf
    
## Building tdlib

As switching to a specific commit of tdlib might be necessary, I recommend using
the git version directly.

Open a __Msys2 MinGW 64-bit__ Terminal:

    git clone https://github.com/tdlib/td.git /usr/src/tdlib
    cd /usr/src/tdlib
    mkdir build
    cd build
    cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX="C:/msys64/mingw64" ..
    make install
    
The build might fail due a string table overflow (built file getting too big).
If so then change the CMake configuration:

    cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX="C:/msys64/mingw64" -DCMAKE_CXX_FLAGS="-O2" ..
    make install
    
This will disable the possibility to debug tdlib. But since this guide is about
getting telega up and running and not developing tdlib, this should be fine.
   
## Installing telega

First we need to get telega. Open a __Msys2 MinGW 64-bit__ Terminal. Then enter

    emacs
    
This will result in opening the MinGW version of Emacs. Switch to the
*\*scratch\** buffer and enter:

    (package-initialize)
    (add-to-list 'package-archives
           '("melpa-stable" . "https://stable.melpa.org/packages/"))
    (add-to-list 'package-pinned-packages '(telega . "melpa-stable"))
    (package-refresh-contents)
    (package-install 'telega)
    (package-install 'all-the-icons)
    (all-the-icons-install-fonts t) ; Use ~/.emacs.d when prompted for the installation directory!
   
Afterwards run <kbd>M-x</kbd> *eval-buffer*

To finalize the installation open the file `~/.emacs` and place the following in
it:

    (add-to-list 'package-archives
           '("melpa-stable" . "https://stable.melpa.org/packages/"))
    (add-to-list 'package-pinned-packages '(telega . "melpa-stable"))
    (require 'telega)

This will make sure that telega is ready to be started when Emacs is ready.
    
__Important__: Do not run <kbd>M-x</kbd> *telega* yet.

## Building the telega server

telega is using an external application which actually communicates with the
Telegram server. That application is using the tdlib. But it also use an API not
available to MinGW. Luckily that API is available to Msys2. We have even more
luck as Msys2 built applications can be called by MinGW built applications.

Therefore we build the telega server using Msys2 but continue using the MinGW
Emacs. To do that we open a `Msys2 MSYS` Terminal:

    cd ~/.emacs.d/elpa/telega-<the_installed_version>/
    LIBS_PREFIX=/mingw64 make install
    
## Starting telega

Done! telega can now safely be started. Open a __Msys2 MinGW 64-bit__ Terminal.
Then enter

    emacs
    
Now run <kbd>M-x</kbd> *telega*, enter your phone number and enjoy chatting on
Telegram using Emacs!

