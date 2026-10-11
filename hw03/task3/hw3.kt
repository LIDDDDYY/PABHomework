package com.example.hw03.task3

fun printStudentInfo(studentName: String?) {
    // 1. Safe length check
    println("Length: ${studentName?.length}")

    // 2. Elvis operator for default value
    println("Name: ${studentName ?: "Unknown"}")

    // 3. ?.let to execute only if non-null
    studentName?.let {
        println("Hello, $it!")
    }
}

fun main() {
    var studentName: String? = null
    printStudentInfo(studentName)

    println() // Baris kosong pemisah

    studentName = "Ayu"
    printStudentInfo(studentName)
}