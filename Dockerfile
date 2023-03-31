FROM php:8.1-fpm

# Install system dependencies
RUN apt-get update && \
    apt-get install -y git curl zlib1g-dev libpng-dev libpq-dev libxml2-dev libzip-dev

# Install PHP extensions
RUN docker-php-ext-install pdo pdo_pgsql gd xml zip

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

