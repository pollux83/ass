<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use Illuminate\Support\Facades\File;

class Service extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'make:service {name}';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Create a new service class.';

    /**
     * Execute the console command.
     *
     * @return int
     */
    public function handle()
    {
        $name = $this->argument('name');
        $path = app_path('Services/' . $name . '.php');

        if (File::exists($path)) {
            $this->error('Service already exists!');
            return 1;
        }

        File::ensureDirectoryExists(app_path('Services'));

        File::put($path, $this->buildClass($name));

        $this->info('Service created successfully.');

        $permissions = $this->ask("Set file permissions for ChatGPTService.php (e.g. 644):");
        File::chmod($path, $permissions);

        return 0;
    }

    /**
     * Build the class with the given name.
     *
     * @param  string  $name
     * @return string
     */
    protected function buildClass($name)
    {
        $stub = File::get(__DIR__ . '/stubs/service.stub');
        return str_replace('{{name}}', $name, $stub);
    }
}
