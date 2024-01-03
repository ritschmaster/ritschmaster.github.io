---
layout: post
title:  Setting up FreeBSD with KDE
author: Richard Bäck
---

# Introduction

I switched to macOS a while ago. I use and view macOS as a highly optimized tool for entering data into a computer. It therefore is - in my world view - the best tool for the job.

During the period of determining if macOS is the best tool available I stumbled upon FreeBSD. Actually again, because I had a brief period in which i tried to get into FreeBSD about 15 years ago. I failed miserably. But after all, I was only 13 years old at that time. And I am not a native English speaker. The internet was also pretty foreign for me at that time.

Anyway, I stumbled upon FreeBSD and thought to myself if it would be worthwhile to setup a secondary PC for legacy tasks like accessing old DVDs and transferring them to my new Macbook.

So I did exactly that and boy was that a hard journey. I intentionally used FreeBSD for that instead of Ubuntu etc to learn something new. And I did learn many things:
1. The most important thing is that documentation is king. 
    1. The [FreeBSD Handbook](https://docs.freebsd.org/en/books/handbook/) is the best documentation I have ever read. It walks you perfectly through everything you will need to get a system up and running.
    2. The `man` pages within FreeBSD are fantastic too. It further showed me how important it is to have good documentation easily available within a product.  
2. System design matters. In Linux you get what is happening by reading a plethora of Stackoverflow Q&A to your specific questions. In FreeBSD you walk through the FreeBSD Handbook and you know what your system is up to. A product has therefore only the following options to be successful:
    1. Be as easy as possible to understand on a low level. This allows more people to get into it. This can be achieved either by a good documentation or by good product designs. (macOS & FreeBSD way)
    2. Have already a large user base avilable. This allows more people to state fixes to most common use cases. (Windows & Linux/systemd way)
3. KDE allows keybindings almost like in macOS by switching left Alt with left Win and then using the Windows key for Copy, Paste etc. Those default actions can be overwritten for all KDE applications using the _Edit_ section in the application _Settings_ under _Keyboard shorctuts_.
4. Using the best tool available for the job is king if you are under time or budget pressure. Invest money to save time.
    1. Example: playing games on Linux or FreeBSD just does not work as good as under Windows. Get over it and install Windows with Steam or whatever.
5. Trying to achieve something with a tool that is not specifically tasked for that job has a lot of learning potential. Invest time to later better invest money to save time.
    1. Example: trying to get Steam on FreeBSD up and running is a lot more challengning to run it on Windows or on Linux. But you will learn way more!

Now let's get into how I achieved a good setup of FreeBSD using KDE as desktop environment.

# Setting up the system

## Installation

Perform a clean installation.

## Enable sudo

First install `sudo`:

    # pkg install sudo
    
Now add your user to the group `wheel`:

    # pw group mod wheel -m <your-user>
    
Finally enable `sudo` for the group `wheel` by executing `visudo` and uncommenting the line stating that `wheel` may have access to `sudo`. Optionally you can enable the line with no password requirement. 

As a result we can safely disable the root account using the following command:

    $ sudo pw lock root

## Setup ZSH

I like to use ZSH over Bash or shells since I am on macOS and it is the default there. Get it by performing the following command:

    $ sudo pkg install zsh
    
To use it as the default shell:

    $ chsh -s /usr/lcoal/bin/zsh
    
Enable shutdown for user

Add user to the `operator` group:

    $ pw group mod operator -m <user>
    
## Faster boot

Add the following options to the file `/boot/loader.conf`:

    autoboot_delay="0"
    hw.usb.no_boot_wait="1"

Add the following options fo the file `/etc/rc.conf`:

    defaultroute_delay="0"

## Setup the graphics card

Follow [this section in the FreeBSD handbook](https://docs.freebsd.org/en/books/handbook/book/#x-graphic-card-drivers).

Hint: You may use `kldload` to probe for the graphics card driver before permantely adding it doing `sysrc kld_list+=` and breaking the system. I broke my first installation by persisting the change using `sysrc`.

## Install KDE

Install KDE and SDDM:

    pkg install kde5 sddm
    
Enable KDE and SDDM:

    sysrc dbus_enable="YES"
    sysrc sddm_enable="YES"
    sysrc sddm_lang="en_US"

Add your user to the group `video`:

    pw group mod video -m <your-user>
 
## Enable shutdown etc in KDE

KDE does not allow the user to perform any computer state actions by default on FreeBSD. This leads to missing entries in the application launcher for e.g. shutting down the system.

To enable shutdown and reboot create the new polkit configuration file `/usr/local/etc/polkit-1/rules.d/40-wheel-group.rules` with the following contents:

    polkit.addRule(function(action, subject) {
        if (subject.isInGroup(“operator”)) {
            return polkit.Result.YES;
        }
    });
   
Make sure that the new file is assigned to the user `root` and the group `wheel` by peforming

    chown root:wheel /usr/local/etc/polkit-1/rules.d/40-wheel-group.rules
    
afterwards.

This tells polkit and also KDE to allow the shutdown operation for anyone who is in the group `operator`.

## SDDM Autlogin

Create the new file `/usr/local/etc/sddm.conf` with the following contents:

    [Autologin]
    User=<your-user>
    Session=plasma-x11

Make sure that the new file is assigned to the user `root` and the group `wheel` by peforming

    chown root:wheel /usr/local/etc/sddm.conf
    
afterwards.

## Auto mount for USB sticks

1. Run the command `sudo pkg install --regex dsbmc-cli dsbmc dsbmd  'fusefs.*’` to install FUSE.
2. Add the option `dsbmd_enable=“YES”` to `/etc/rc.conf`.
3. Add the option `vfs.usermount=1` to `/etc/sysctl.conf`.

Hint: If no file manager (e.g. Dolphin) is used then add `dsbmc-cli &` and `dsbmc &` as new lines to the file `~/.xinitrc` or `~/.xsession`.

## Change default audio output

Determine the available audio outputs/inputs by performing `cat /dev/sndstat`. After determining the device which should be the default output set the default output by performing sudo `sysctl hw.snd.default_unit=X`. The same parameter can be set in the file `/etc/sysctl.conf` permanently.

# Bonus: Using K3B with FreeBSD

Checkout the following [blog post](https://bastian.rieck.me/blog/posts/2009/k3b/).

# Bonus: Manually suspend the machine

Run the following in the terminal:

    $ acpiconf -s 3

