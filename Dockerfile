FROM ubuntu:18.04
ENV TZ=Asia/Seoul

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update
RUN apt -y install apache2
RUN apt -y install software-properties-common
RUN add-apt-repository ppa:ondrej/php
RUN apt update
RUN apt -y install php7.4
RUN rm /var/www/html/index.html

ADD ./src/ /var/www/html/
ADD ./env/php.ini /etc/php/7.4/apache2/php.ini
ADD ./start.sh /entrypoint.sh
ADD ./flag /flag

RUN chmod 111 /flag

ENTRYPOINT '/entrypoint.sh'