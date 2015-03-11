# thumbor-docker

Docker repository of a minimal working installation of thumbor on Ubuntu LTS
14.04 with default configuration. Use this as a base image for further
customization.

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

then try a thumbor url in the host browser:

    http://localhost:8888/unsafe/x50/www.google.com/logos/logo.gif

### Using your own thumbor configuration

    docker run \
      -p 8888:8888 -v <path to config file>:/etc/thumbor.conf \
      xamfoo/thumbor-docker \
      thumbor -c /etc/thumbor.conf -k <path to keyfile>

### Customization

There are various ways to customize this image to your needs. You might need to
refer to [phusion/baseimage](https://github.com/phusion/baseimage-docker) and
[docker](https://docs.docker.com/) documentation.

#### Modifying Dockerfile, Packages

- You can update `Dockerfile` with your own instructions.
- Add, remove, or comment out packages in `setup/requirements` to determine
  the packages installed in the image.

After modification, rebuild the image in the project root directory:

    docker build -t mynamespace/thumor-docker .

#### Reference to this image from another Dockerfile

Add this line to the top of your Dockerfile

    FROM xamfoo/thumbor-docker

## Dependencies

Docker base image:

- phusion/baseimage 0.9.16

Installed package:

- thumbor 4.11.1
