<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Inertia\Inertia;
use OpenAI;
use OpenAI\Client;
use Psr\Http\Message\RequestInterface;
use Psr\Http\Message\ResponseInterface;

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

    public function sendMessage(Request $request = null)
    {
        $message = 'PHP is';
        //$message = $request->input('message');
//        $client = OpenAI::factory()
//            ->withApiKey(getenv('YOUR_API_KEY'))
//            ->withOrganization(getenv('OPENAI_ORGANIZATION')) // default: null
//            ->withBaseUri('openai.example.com/v1') // default: api.openai.com/v1
//            ->withHttpClient($client = new \GuzzleHttp\Client([])) // default: HTTP client found using PSR-18 HTTP Client Discovery
//            ->withHttpHeader('X-My-Header', 'foo')
//            ->withQueryParam('my-param', 'bar')
//            ->withStreamHandler(fn (RequestInterface $request): ResponseInterface => $client->send($request, [
//                'stream' => true // Allows to provide a custom stream handler for the http client.
//            ]))
//            ->make();
        $response = $this->client->completions()->create([
            'model' => 'gpt-3.5-turbo',
            'prompt' => 'PHP is',
            'temperature' => 0.5,
            'max_tokens' => 50,
            'n' => 1,
            'stop' => ['\n'],
        ]);
        dump($response);

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

                $this->sendMessage();






        return Inertia::render('ChatGPT/Create', [
            'list' => $list// ['object' => 'list', 'data' => [...]]
        ]);
    }
}
