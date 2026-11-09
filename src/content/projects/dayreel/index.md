---
published: true
title: "Dayreel"
category: "Software I built"
order: 12
summary: "A Mac menu-bar app that saves a screenshot of every screen on a timer, so I can scroll back through my day."
lede: "A small macOS menu-bar app. Every few seconds or minutes it saves one JPEG of all my screens, sorted into a folder per day."
cover: ./cover.png
coverAlt: "The Dayreel app icon, a white ring around a red dot on a black square, above two copies of the Settings form: light on the left, dark on the right. The form shows the save folder Screenshots, JPEG quality 80%, every 30 seconds, capture all displays, and an Open at login switch."
caption: "The app icon from the repo, above the Settings form in light and dark. The form was rendered offscreen from the app's own Swift code at commit c0290af, with a sample save folder. The slider shows grey because the window was not the active window."
stats:
  - value: "399"
    label: "lines of Swift in one file, with no outside packages"
  - value: "5 s to 1 h"
    label: "capture interval, 30 seconds by default"
  - value: "31"
    label: "commits, all on 2 November 2026"
when: "November 2026"
builtWith: "Swift, AppKit, SwiftUI, ScreenCaptureKit, Core Graphics, ImageIO, swiftc"
links:
  - label: "Code"
    href: "https://github.com/greenporsche/dayreel"
---

## How I built it

Dayreel lives in the menu bar as a small ring. The ring fills red while it is capturing. On a timer it takes a still image of each display with ScreenCaptureKit. With more than one display, Core Graphics stitches them onto one canvas in the same arrangement as System Settings › Displays, each at full resolution. ImageIO writes the result as one JPEG. Files go into one folder per day, named by the time, for example `261102/261102-143022.jpg`.

The Settings window is a SwiftUI form. It sets the save folder, the JPEG quality, the interval (5 seconds to 1 hour) and whether to capture all displays or only the main one. There is also a switch to open the app at login. Changes apply at once. Only a change to the interval restarts the timer. Once a save folder is set, the app starts capturing as soon as it launches.

There is no Xcode project. A short shell script compiles the one Swift file with `swiftc`, builds the `.app` bundle by hand and signs it. Another small Swift script draws the app icon.

I built it by directing AI coding agents. The commits record my product calls as "PO decision", for example the name, the bundle ID and the license.

## The hard part

Screen Recording permission. At first, if the app did not have permission, every timer tick called ScreenCaptureKit, and every call raised the macOS permission prompt again. The fix checks for access before touching ScreenCaptureKit. Without access, the timer stops, the menu says what is missing, and you get one prompt per press of Start.

Rebuilding caused the same prompt in another way. A build signed ad hoc gets a new identity each time, so macOS forgets the permission after every rebuild. The build script can now sign with a self-made certificate instead. If one is configured but missing from the keychain, the build stops with an error rather than quietly falling back.

Stitching every display at full resolution makes large files. In one measured setup, two displays stitched to 9984 × 3456 pixels at quality 60 gave images of about 2.7 MB. At the default 30 seconds that is about 2,880 images and several GB a day. The README says so and suggests a lower quality or a longer interval.

## What I did

- Set what the app should do and decided its name, Dayreel. It started as InstantShot.
- Made the product calls recorded in the commits: the `app.dayreel` bundle ID and the MIT license.

## Where it stands

It works on Macs with Apple silicon and macOS 14 or later. You build it from source with Apple's Command Line Tools. There is no downloadable release, and the app is not notarized.
