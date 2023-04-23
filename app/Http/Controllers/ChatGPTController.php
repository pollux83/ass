<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Inertia\Inertia;
use OpenAI\Client;

class ChatGPTController extends Controller
{
    /**
     * @var Client
     */
    protected Client $client;

    public function __construct(Client $client)
    {
        $this->client = $client;
    }

    public function sendMessage(Request $request, Client $client)
    {
        $message = $request->input('message');
        $response = $client->completions()->create([
            'model' => 'davinci',
            'prompt' => $message,
            'temperature' => 0.5,
            'max_tokens' => 50,
            'n' => 1,
            'stop' => ['\n'],
        ]);
        return response()->json([
            'message' => $message,
            'response' => $response->choices[0]->text,
        ]);
    }

    public function create(){
        $response = $this->client->models()->list();

//        $response->object; // 'list'
//
//        foreach ($response->data as $result) {
//            $result->id; // 'text-davinci-003'
//            $result->object; // 'model'
//            // ...
//        }
        $list = $response->toArray();
        return Inertia::render('ChatGPT/Create', [
            'list' => $list// ['object' => 'list', 'data' => [...]]
        ]);
    }
}
