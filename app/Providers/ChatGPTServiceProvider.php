<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use OpenAI\Client;

class ChatGPTServiceProvider extends ServiceProvider
{
    /**
     * Register services.
     */
    public function register()
    {
        $this->app->singleton(Client::class, function () {
            return new Client(env('OPENAI_API_KEY'));
        });
    }

    /**
     * Bootstrap services.
     */
    public function boot()
    {
        //
    }

}
