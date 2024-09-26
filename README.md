# The Automagical Marvel - A Hybridization of the Page Object Model and Logical Functions

<div style="text-align: center;">"Take chances, make mistakes, get messy!" - Ms. Valerie Frizzle, The Magic School Bus</div>

Welcome to The Automagical Marvel, a 2024 Pacific Northwest Software Quality Conference (PNSQC) workshop.

## Table of Contents
<!-- TOC -->
* [The Automagical Marvel - A Hybridization of the Page Object Model and Logical Functions](#the-automagical-marvel---a-hybridization-of-the-page-object-model-and-logical-functions)
  * [Table of Contents](#table-of-contents)
* [Introduction](#introduction)
  * [Goals of the Workshop](#goals-of-the-workshop)
  * [Expectations of You](#expectations-of-you)
* [Getting Started](#getting-started)
  * [The Website Under Test](#the-website-under-test)
  * [Prerequisites](#prerequisites)
  * [Creating a Virtual Environment](#creating-a-virtual-environment)
    * [POSIX Environments (Linux, macOS, Unix, etc)](#posix-environments-linux-macos-unix-etc)
    * [Windows Environments](#windows-environments)
      * [Powershell](#powershell)
      * [CommandLine](#commandline)
  * [Installing the Requirements](#installing-the-requirements)
    * [Install via Poetry](#install-via-poetry)
    * [Install via PIP](#install-via-pip)
  * [Building in the Workshop](#building-in-the-workshop)
  * [Checking Your Work](#checking-your-work)
* [Troubleshooting](#troubleshooting)
    * [Driver does not install with `DriverHelper.get_driver("browser", install=True, update=True)`](#driver-does-not-install-with-driverhelperget_driverbrowser-installtrue-updatetrue)
    * [I get a BrowserNotSupportedError when using X browser that's not Chrome, Firefox, Edge, or Safari](#i-get-a-browsernotsupportederror-when-using-x-browser-thats-not-chrome-firefox-edge-or-safari)
    * [The website under test has some weird ads](#the-website-under-test-has-some-weird-ads)
    * [Selenium crashes when I try to reach an element that is on page](#selenium-crashes-when-i-try-to-reach-an-element-that-is-on-page)
      * [Through Selenium's API](#through-seleniums-api)
      * [Through Javascript Injection:](#through-javascript-injection)
    * [Help, the website under test went blank](#help-the-website-under-test-went-blank)
<!-- TOC -->

# Introduction

This introduces the concept of the hybridization of Page Object Model with a Logical Function Model, shortened to Hybrid POM/LFM, which allows for the usage of UI elements through standard data types (such as `String`, `Integer`, `DateTime`, `Boolean`, etc.).

Although this particular version of the workshop and Hybrid POM/LFM concept is geared for [Selenium](https://www.selenium.dev/documentation/) and [Python](https://www.python.org), the concept can be applied across Object Oriented Programming Langauges and any UI automation suite that utilizes a form of UI Element class, such as:
- [Appium](http://appium.io/docs/en/latest/)
- [XCUI/XCTest](https://developer.apple.com/documentation/xctest/user_interface_tests)
- [GameDriver](https://www.gamedriver.io)
- [Windows UI Automation](https://learn.microsoft.com/en-us/dotnet/framework/ui-automation/ui-automation-fundamentals)
- [PlayWright](https://playwright.dev/docs/intro)
- [Cypress](https://www.cypress.io)
- And many more!

## Goals of the Workshop

This workshop aims to fulfill the following goals as you work through it:

- Reaffirm the concept of Page Object Model while introducing a new layer to it.
- Introduce the concept of wrapping UI Elements with getters and setters for common data types that reflect how the UI Element is intended to be used.
- Introduce more complex ways of wrapping elements while creating an intuitive usage experience.
- Provide a new paradigm for UI automation that reduces the complexity of use while maintaining the ease of development and maintenance of the standard Page Object Model paradigm.
- Provide a means of building a framework that will allow a developer of any skill level to make tests from simply through using common data types and intuitive syntax.
- Show, through the framework's foundations ([BasePage](./pnsqc_workshop_2024/core/bases/base_page.py)) a means to enable the framework to accommodate different WebDriver's during the same test pass in both single and multithreaded applications/tests.

## Expectations of You

During the course of this workshop you are expected to:
- Ask Questions! Get stuck?  Need to confirm something?  Ask!  The only 'dumb' question is the one not asked!
- Get tangible, hands-on experience with the concept of Hybrid POM/LFM
- Add a personal touch to your code!  [Writing code is as much an act of artistic expression](https://www.youtube.com/watch?v=LNASeY0lc2w) as it is a scientific endeavor.  Be creative, challenge the expected, try something new!
- Learn a new skill and grow a new muscle in terms of UI automation.
- Most importantly - <u>**_Have fun!_**</u>

# Getting Started

To get started, follow along with these various sections.

## The Website Under Test

To perform this workshop, we'll be using the following website to build our framework: https://demoqa.com/automation-practice-form

_**Note:** This website can have some questionable ads sometimes.  If they get too annoying, you can remove them with the instructions found in [the Troubleshooting section](#the-website-under-test-has-some-weird-ads)._

## Prerequisites

Before beginning, make sure you meet the following prerequisites:
- Required:
  - Have [Python 3.11 or later](https://www.python.org/downloads/) installed
  - Be connected to WiFi or mobile hotspot
  - One of the following browsers installed:
    - [Google Chrome](https://www.google.com/chrome/)
    - [FireFox](https://www.mozilla.org/en-US/firefox/)
    - [Microsoft Edge](https://www.microsoft.com/en-us/edge)
    - [Safari](https://www.apple.com/safari/) - macOS Only, preinstalled.
  - Clone the source repository
    - SSH: `git clone git@github.com:Snip3rM00n/pnsqc_workshop_2024.git`
    - HTTP: `git clone https://github.com/Snip3rM00n/pnsqc_workshop_2024.git`
  - Have you preferred IDE installed and ready!
  - Create and activate a Virtual Environment
- Optional:
  - Have [Python Poetry](https://python-poetry.org) installed
    - If you don't have it installed, you can still install the requirements via `pip install`
  - Have some form of [GNU Make](https://www.gnu.org/software/make/) installed
    - This will make it easier to install the requirements.

## Creating a Virtual Environment

To create a virtual environment, follow the steps for your given OS.

### POSIX Environments (Linux, macOS, Unix, etc)

```shell
cd ~/path/to/workshop
python3 -m venv ./venv
source ./venv/bin/activate
```

### Windows Environments

Chose the console app you're most comfortable in in

#### Powershell
```powershell
cd C:\path\to\workshop
python3 -m venv ./venv
.\venv\Scripts\activate.ps1
```

#### CommandLine
```cmd
cd C:\path\to\workshop
python3 -m venv ./venv
.\venv\Scripts\activate.bat
```

## Installing the Requirements

There are multiple methods of installing the requirements, choose the set of commands that make sense for your setup.

- [Install via Poetry](#install-via-poetry)
- [Install via PIP](#install-via-pip)

### Install via Poetry

_**Note:** The lock file is already compiled and committed to the repository, so you shouldn't need to run the lock command to generate it._

If you have GNU Make installed, simply run: `make install-deps-poetry`

If you do not have GNU Make, you can install by running `poetry install`

### Install via PIP

If you have GNU Make installed, simply run: `make install-deps-pip`

If you do not have GNU Make, you can install by running `python3 -m pip install -r requirements.txt`

## Building in the Workshop

Most work in this workshop will be centered around building out the `PracticeForm` class in [./pnsqc_workshop_2024/framework/pages/practice_form.py](./pnsqc_workshop_2024/framework/pages/practice_form.py).  In this file you will find some boilerplate code along with some `#region` tags that outline a section for each element and its requirements.  Follow the requirements defined in the region for each element and it's wrapper.

## Checking Your Work

To check your work, simply run the tests using one of the following commands.

If you have GNU Make, simply run one of these commands:
* `make test-workshop` - Test's specifically your modifications to the page by setting and getting the properties.  This will have false positives as, if you do not define the property, it gets set in the class due to Python's meta programming.
* `make test-io` - Validates your changes against a fully functional version of the page built by the Workshop Facilitator.  This is a comprehensive test as it will use your version of the page to fill out the form and use the facilitators version to validate the inputs.
* `make test-all` - Runs both sets of tests.

If you do not have GNU Make, simply run one of these commands:
* `python3 -m pytest ./tests/test_workshop.py` - Test's specifically your modifications to the page by setting and getting the properties.  This will have false positives as, if you do not define the property, it gets set in the class due to Python's meta programming.
* `python3 -m pytest ./tests/test_io.py` - Validates your changes against a fully functional version of the page built by the Workshop Facilitator.  This is a comprehensive test as it will use your version of the page to fill out the form and use the facilitators version to validate the inputs.
* `python3 -m pytest ./tests/` - Runs both sets of tests.

Similarly, if you want to test things on the fly you can either create a throw-away scratch file or have a version of the [Python REPL](https://python.land/introduction-to-python/the-repl) open and import the practice form to test your changes interactively.

# Troubleshooting

In the case an issue arises, here are some troubleshooting steps to try for various scenarios.

### Driver does not install with `DriverHelper.get_driver("browser", install=True, update=True)`

Although this workshop utilizes a package that _should_ install the driver, the package can sometimes error out when it cannot parse the websites the driver can be downloaded from.  When this happens, install the driver manually from:
- Google Chrome: https://googlechromelabs.github.io/chrome-for-testing/
- FireFox (Gecko): https://github.com/mozilla/geckodriver/releases
- Microsoft Edge (Chromium): https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- Safari: No need to install, it's supplied by macOS natively in `/System/Cryptexes/App/usr/bin/safaridriver`
  - You can confirm this in macOS by running the `which safaridriver` command.

### I get a BrowserNotSupportedError when using X browser that's not Chrome, Firefox, Edge, or Safari

This lab only supports the four major browsers out of the box (Google Chrome, Mozilla Firefox, Microsoft Edge, or Apple Safari).  If you want to use a browser other than those, you will need to add it to the `DriverHelper` class yourself.  Note that support for this browser during the lab will be limited at best.

### The website under test has some weird ads

This is unfortunate and true.  If the ads get distracting while developing and inspecting elements, open up the browser's development console and execute the following javascript to remove them.

```javascript
var all = document.getElementsByTagName("*");

for (var i = 0; i < all.length; i++){
    element = all[i];
    for (var j = 0; j < element.attributes.length; j++){
        if (element.attributes[j].value.includes("Ad.")){
            element.remove();
        }
    }
}

var rightAd = document.getElementById("RightSide_Advertisement");
rightAd.remove();
```

### Selenium crashes when I try to reach an element that is on page

It could be the element is not in the viewport depending on your screen resolution.  You may need to implement a little scrolling logic to get it to work properly.  Scrolling can be done by a feature provided by [Selenium's API](https://www.selenium.dev/documentation/webdriver/actions_api/wheel/) or through JavaScript injection.

#### Through Selenium's API

As part of a function call or daisy-chain.  This is one example by scrolling directly to an element, refer to the [Selenium Documentation](https://www.selenium.dev/documentation/webdriver/actions_api/wheel/) for other methods.

_**Note:** Per Selenium's documentation, this is only supported by Chromium browsers so Gecko and WebKit based browsers cannot use this._

```python
ActionChains(self.driver).scroll_to_element(self.some_element).perform()
```

Or in Element reference:

```python
@property
def some_element(self):
    element = self.driver.find_element(By.ID, "some-element")
    ActionChains(self.driver).scroll_to_element(element).perform()
    return element
```

#### Through Javascript Injection:

_**Note:** Compatible with all browsers._

```python
self.driver.execute_script(script="window.scrollBy(0, x);") # Let x represent the number of pixels to scroll by.
```

### Help, the website under test went blank

This is a known issue and can happen if certain elements are cleared inadvertently.  Simply refresh the page to get all the content back.  In the future, avoid completely clearing out a field, rather add any kind of content for it to keep the page alive.

### A modal appeared while running one of the test commands and broke the tests

This occasionally happens on this page under test because it has elements overlap each other that can also just disappear without warning (known issue).  Try re-running the tests.
