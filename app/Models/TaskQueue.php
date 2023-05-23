<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class TaskQueue extends Model
{
    use HasFactory;

    protected $fillable = [
        'task_id',
        'status',
        'added_at',
    ];

    public function task()
    {
        return $this->belongsTo(Task::class);
    }
}
