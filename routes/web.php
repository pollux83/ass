<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::get('/assistant', function () {
    // Display a form for submitting a message to the assistant
    return view('assistant');
});
Route::post('/chat', 'ChatGPTController@sendMessage');



//Route::post('/assistant', function () {
//    // Process the submitted message and send it to ChatGPT
//    $message = request()->input('message');
//    $response = '';// Send $message to ChatGPT and get a response
//    return view('assistant', [
//        'message' => $message,
//        'response' => $response,
//    ]);
//});

//Route::post('/assistant', function (Request $request) {
//    $messages = $request->session()->get('messages', [
//        ['role' => 'system', 'content' => 'You are LaravelGPT - A ChatGPT clone. Answer as concisely as possible.']
//    ]);
//
//    $response = OpenAI::chat()->create([
//        'model' => 'gpt-3.5-turbo',
//        'messages' => $messages
//    ]);
//    return view('assistant', [
//        'message' => $message,
//        'response' => $response,
//    ]);
//});
