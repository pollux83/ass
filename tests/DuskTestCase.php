<?php

namespace Tests;

use Facebook\WebDriver\Chrome\ChromeOptions;
use Illuminate\Support\Collection;
use Facebook\WebDriver\ChromeChromeOptions;
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\Remote\RemoteWebDriver;
use Laravel\Dusk\TestCase as BaseTestCase;

abstract class DuskTestCase extends BaseTestCase
{
    use CreatesApplication;

    /**
     * The base URL to use while testing the application.
     *
     * @var string
     */
    protected $baseUrl = '0.0.0.0:8889';

    /**
     * Prepare for Dusk test execution.
     *
     * @beforeClass
     * @return void
     */
    public static function prepare()
    {
//        static::startChromeDriver();
    }

    /**
     * Create the RemoteWebDriver instance.
     *
     * @return RemoteWebDriver
     */
    protected function driver()
    {
        $capabilities = DesiredCapabilities::chrome();
        $options = new ChromeOptions();
        $options->addArguments([
            '--disable-gpu',
            '--headless',
            '--no-sandbox',
//            '--disable-dev-shm-usage'
        ]);

        $capabilities->setCapability(ChromeOptions::CAPABILITY, $options);

        // Set acceptInsecureCerts to true
        $capabilities->setCapability('acceptInsecureCerts', true);

        return RemoteWebDriver::create(
            'http://selenium:4444/wd/hub',
            $capabilities
        );
    }
}
