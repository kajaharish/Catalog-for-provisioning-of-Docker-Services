FROM ubuntu:16.04

MAINTAINER Gaurav Gandhi <grv.gandhi.27@gmail.com>

RUN apt-get update
RUN apt-get upgrade -y


COPY debconf.selections /tmp/

RUN apt-get install apt-utils -y

RUN debconf-set-selections /tmp/debconf.selections

RUN apt-get install -y \
	php7.0 \
	php7.0-bz2 \
	php7.0-cgi \
	php7.0-cli \
	php7.0-common \
	php7.0-curl \
	php7.0-dev \
	php7.0-enchant \
	php7.0-fpm \
	php7.0-gd \
	php7.0-gmp \
	php7.0-imap \
	php7.0-interbase \
	php7.0-intl \
	php7.0-json \
	php7.0-ldap \
	php7.0-mcrypt \
	php7.0-mysql \
	php7.0-odbc \
	php7.0-opcache \
	php7.0-pgsql \
	php7.0-phpdbg \
	php7.0-pspell \
	php7.0-readline \
	php7.0-recode \
	php7.0-snmp \
	php7.0-sqlite3 \
	php7.0-sybase \
	php7.0-tidy \
	php7.0-xmlrpc \
	php7.0-xsl


RUN apt-get install apache2 libapache2-mod-php7.0 -y

ENV LOG_STDOUT **Boolean**
ENV LOG_STDERR **Boolean**
ENV LOG_LEVEL warn
ENV ALLOW_OVERRIDE All
ENV DATE_TIMEZONE UTC
ENV TERM dumb

COPY index.html /var/www/html/
COPY run-server.sh /usr/sbin/

RUN a2enmod rewrite
RUN chmod +x /usr/sbin/run-server.sh
RUN chown -R www-data:www-data /var/www/html

VOLUME /var/www/html
VOLUME /var/log/httpd

EXPOSE 80

CMD ["/usr/sbin/run-server.sh"]
