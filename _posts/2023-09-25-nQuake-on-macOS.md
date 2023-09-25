---

layout: post

title: nQuake on macOS

author: Richard Bäck

---

[nQuake](https://nquake.com) is in my opinion the best distribution for [QuakeWorld](https://en.wikipedia.org/wiki/Quake_(video_game)#QuakeWorld) currently available. It works out of the box on Windows and Linux. It further claims to work out of the box on macOS too but at least on my MacBook Air M2 I cannot confirm that.

The installation process works flawless. But the first minor  annoyance that happens is that the application is placed under `/Users/<Your user>/Applications` instead of `/Applications`. It is therefore only installed for the current user. Which is not a deal breaker but you have to know it as you otherwise will not find it.

After finding `ezQuake.app` in `/Users/<Your user>/Applications/nQuake` one would think that it works right away. As of September 2023 it does not. First you have to confirm that you trust the developer and allow runing the application. After doing so it just closes right away. Which is most likely not the fault of the nQuake packagers but the upstream ezQuake package. Unfortunately this is irrelevant for the result as the application will just not start.

To fix this download the latest stable version of ezQuake from [here](https://ezquake.com/info/downloads.html). As of September 2023 this is ezQuake 3.2.3. Then replace `/Users/<Your user>/Applications/nQuake/ezQuake.app` with the downloaded version. This enables you to have at least the possibility to start ezQuake.

Now comes the hard part. Double clicking ezQuake will result in starting its own package. You do not want that. You want to start the package of nQuake. Why? Because if you start ezQuake's package, then you will use the configuration hidden within the `.app`. But you want to use the configuration shipped with nQuake which is sitting right next to `ezQuake.app`. To achieve this we will create a new application using the Automator:
1. Open Automator via Spotlight<br><img src="/assets/2023-09-25-nQuake-on-macOS/step1.png"  alt="Open Automator via Spotlight" />
2. Create a new application<br><img src="/assets/2023-09-25-nQuake-on-macOS/step2.png"  alt="Create a new application" />
3. Add a *Run Shell Script* step with the following contents:<br><br><img src="/assets/2023-09-25-nQuake-on-macOS/step3.png"  alt="Run Shell Script" />
4. Save the application as `/Users/<Your user>/Applications/nQuake/nQuake.app`

You may now use the `nQuake.app` to play QuakeWorld (or Quake).

