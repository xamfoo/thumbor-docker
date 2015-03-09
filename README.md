# thumbor-docker

Dockerfile of minimal working installation of `thumbor` on Ubuntu LTS with
default configuration. Use this as a base image for further customization.

### thumbor

From https://github.com/thumbor/thumbor

> thumbor is a smart imaging service. It enables on-demand crop, resizing and flipping of images.
>
> It also features a VERY smart detection of important points in the image for better cropping and resizing, using state-of-the-art face and feature detection algorithms (more on that in Detection Algorithms).
>
> Using thumbor is very easy (after it is running). All you have to do is access it using an URL for an image, like this:
>
> ```
> http://<thumbor-server>/300x200/smart/s.glbimg.com/et/bb/f/original/2011/03/24/VN0JiwzmOw0b0lg.jpg
> ```
>
> That URL would show an image of the big brother brasil participants in 300x200 using smart crop.
>
> There are several other options to the image URL configuration. You can check them in the Usage page.
>
> For more information check [thumbor's
> documentation](https://github.com/globocom/thumbor/wiki "thumbor docs").

### Docker

From https://github.com/docker/docker

> Docker is an open source project to pack, ship and run any application as a lightweight container
>
> Docker containers are both hardware-agnostic and platform-agnostic. This means they can run anywhere, from your laptop to the largest EC2 compute instance and everything in between - and they don't require you to use a particular language, framework or packaging system. That makes them great building blocks for deploying and scaling web apps, databases, and backend services without depending on a particular stack or provider.

## Usage

### Testing with default configuration

Run the image in a container:

    docker run -p 8888:8888 xamfoo/thumbor-docker thumbor

then try a thumbor url in the host browser for example:

    http://localhost:8888/unsafe/x50/www.google.com/logos/logo.gif

### Customization

Modify the provided `Dockerfile` and rebuild.

Or reference to this image from another `Dockerfile` like so

    FROM xamfoo/thumbor-docker

For more information refer to Docker documentation.

## Dependencies

All packages in `Dockerfile` are version-specified so each build is
reproducible.

Docker base image:

- phusion/baseimage 0.9.16

Installed package:

- thumbor 4.10.3
