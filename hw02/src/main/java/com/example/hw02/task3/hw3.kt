package com.example.hw02.task3

fun main() {
    // Part A
    val numberOfDays = 5
    for (day in 1..numberOfDays) {
        println("Day $day: Study for 20 minutes")
    }

    // Part B
    for (day in 1..numberOfDays step 2) {
        println("Day $day: Study for 20 minutes")
    }
}