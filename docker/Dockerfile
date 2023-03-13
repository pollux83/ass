# Base image
FROM php:8.1-fpm-alpine

# Install system dependencies
RUN apk add --no-cache git curl zlib-dev libpng-dev libxml2-dev libzip-dev postgresql-dev

# Install PHP extensions
RUN docker-php-ext-install pdo pdo_pgsql gd xml zip

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Set the working directory
WORKDIR /var/www/html

# Copy project files
COPY ./composer.json /var/www/html/

# Install project dependencies
RUN composer install --no-interaction --optimize-autoloader #--no-suggest

# Set permissions
RUN chown -R www-data:www-data /var/www/html/storage /var/www/html/bootstrap/cache

# Expose port 9000
EXPOSE 9000

# Start the server
#CMD php artisan serve --host=0.0.0.0 --port=9000

