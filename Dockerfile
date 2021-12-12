FROM klakegg/hugo:0.83.1-ubuntu

RUN apt-get update
RUN apt-get install -y git

CMD ["tail", "-f", "/dev/null"]