Beehve
======

[![Build
Status](https://travis-ci.org/powellc/beehve.svg?branch=master)](https://travis-ci.org/Code4Maine/beehve)

Inspired and heavily copied from
[laddr](http://github.com/CfABrigadePhiladelphia/laddr), Beehve aims to be a
one-stop-shop for what's going in our Code for America Bridage in Maine: Code 4
Maine. 

Features include:

  * Project tracking
  * Members directory
  * Github integration
  * Project buzz
  * Big screen for public events

Not all of these work yet, but we're on way to a 1.0.


Deployment
----------

Need some instructions for deploying this baby here.

Easy bootstrapping!
-------------------

Powered by the ubiquitous Makefile ... this should be pretty easy:

1. make install
2. make run
3. open your browser to: http://127.0.0.1:45000


Librarys, librarys, librarys!
-----------------------------

Of course, we could provide a vagrant file and a provisoner and all 
that jazz. But I'd rather provide a make file for installing everything
into a venv and let you muck about with libraries. Those of you on
Linux shouldn't have too much trouble installing the requisite development
libraries below. The names are for debian-based distros, but they 
exist for all major distros. 

On Mac it may be a little tricker. Homebrew will get you quite far, but
first you have to install the bloated XCode and the CLI tools.

The libraries are:

  * libmemcached-dev
  * libfreetype6-dev
  * libjpeg-dev

