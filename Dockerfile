FROM php:8.1-fpm

# Install system dependencies
RUN apt-get update && \
    apt-get install -y curl git  zlib1g-dev libpng-dev libpq-dev libxml2-dev libzip-dev gnupg

# Install PHP extensions
RUN docker-php-ext-install pdo pdo_pgsql gd xml zip


#Install Google Chrome
#RUN apt-get -y install libxpm4 libxrender1 libgtk2.0-0 libnss3 libgconf-2-4 gnupg
#RUN apt-get -y install zip unzip

RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update
RUN apt-get -y install google-chrome-stable

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
# Set the working directory
WORKDIR /var/www/html

# Install Node.js and npm
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs

# Copy project files
#COPY . /var/www/html

# Install project dependencies
#RUN composer install --no-interaction --optimize-autoloader --no-suggest

# Set permissions
#RUN chown -R www-data:www-data /var/www/html/storage /var/www/html/bootstrap/cache

# Expose port 8889
#EXPOSE 8889

# Start the server
#CMD php artisan serve --host=0.0.0.0 --port=8889

