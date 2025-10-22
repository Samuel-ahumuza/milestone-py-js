// const Student = {
//   fullname: "John Abaho",
//   yob: 1962,
//   regNo: "M25B13/020",
//   accessNo: "B33227",
//   gender: "Male",
//   phone: "0783457932",
//   isRegistered: false,
// };
// console.log(Student.regNo, Student.fullname);
// console.log(Student.yob, Student.accessNo,Student.isRegistered);



class Student{
    constructor(fullname,yob,accessNo,regNo,gender,phone,isRegistered){
        this.fullname = fullname,
        this.yob = yob,
        this.accessNo = accessNo,
        this.gender = gender,
        this.phone = phone,
        this.regNo = regNo,
        this.isRegistered = isRegistered};
}
 StudentAge = function(){
// AGE = CURRENT YEAR - STUDENT YEAR OF BIRTH
const current_year = new Date().getFullYear();
const age = current_year - yob;
console.log("The student is ${age} years old");
 }
const Student = new Student("John Abaho", 1966, "B33227","M25B13/90",male,"073452667",isRegistered);

console.log(Student);

// DATA
const assignmentScores = [85,92,45,78,62,99,55,70,71,38,66,45,35,78,88];
const PASSING_SCORE = 60;

// Function: checkPassStatus is used because the logic for assigning a pass/fail
// status is a reusable step in the process, making the main code cleaner.

function checkPassStatus(score) {
// Condition: Simple if/else is the easiest way to check a single threshold.
    if (score >= PASSING_SCORE) {
        return 'Pass';
    } else {
        return 'Fail';
    }
}
// Function: processStatus is the main processing function. It encapsulates the core
// logic, including the loop and the final output, making it easy to execute.

function processStatus(scoresArray, passMark) {
    let results = [];
    let passCount = 0;
    let failCount = 0;

    // Loop: for...of
    // Justification: A for...of loop will iterate over all
    // elements in an array when score is required.

    for (const score of scoresArray) {
        const status = checkPassStatus(score); 

        // This counts Pass/Fail based on the result of the function call
        if (status === 'Pass') {
            passCount++;
        } else {
            failCount++;
        }

        results.push({
            score: score,
            status: status
        });
    }
console.log("--- Assignment Grading Summary ---");
    console.log("Passing Score: " + passMark);
    console.log("Total Assignments: " + scoresArray.length);
    console.log("Total Passed: " + passCount);
    console.log("Total Failed: " + failCount);
    console.log("----------------------------------");
    console.log("Detailed Results:");
    return results;
}
const detailedResults = processStatus(assignmentScores, PASSING_SCORE);
for (const result of detailedResults) {
    console.log("Score: " + result.score + " -> Status: " + result.status);
}
