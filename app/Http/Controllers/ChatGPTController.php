<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Inertia\Inertia;
use OpenAI\Client;

class ChatGPTController extends Controller
{
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
        return Inertia::render('ChatGPT/Create');
    }
}
