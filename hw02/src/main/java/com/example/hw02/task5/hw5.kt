package com.example.hw02.task5

fun main() {
    print("Assignment score: ")
    val assignment = readln().toInt()

    print("Exam score: ")
    val exam = readln().toInt()

    val average = (assignment + exam) / 2.0
    val status = if (average >= 60.0) "Pass" else "Needs improvement"

    println("Average: $average")
    println("Status: $status")
}