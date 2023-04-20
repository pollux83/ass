<?php

namespace Tests\Browser;

use Illuminate\Foundation\Testing\DatabaseMigrations;
use Laravel\Dusk\Browser;
use Tests\DuskTestCase;

class ExampleTest extends DuskTestCase
{
    /**
     * A basic browser test example.
     */
    public function testBasicExample(): void
    {
        $this->browse(function (Browser $browser) {
            $browser->visit('/');
//                    ->assertSee('Laravel');
        });
//        $user = User::factory()->create([
//            'email' => 'taylor@laravel.com',
//        ]);
//
//        $this->browse(function ($browser) use ($user) {
//            $browser->visit('/login')
//                ->type('email', $user->email)
//                ->type('password', 'password')
//                ->press('Login')
//                ->assertPathIs('/home');
//        });
    }
}
