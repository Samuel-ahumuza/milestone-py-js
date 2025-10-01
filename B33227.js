// Name:Samuel Ahumuza
// Access Number: B33227
// Registration Number: M25B13/020
// PROBLEM: The difficulty in quickly and accurately determining 
// the final academic status (Pass/Fail)  for a large batch of student
// scores against a fixed minimum standard, leading to slow reporting 
// times and potential human error in compliance checking.
// SOLUTION: Pass/Fail Compliance Checker.
// The program instantly eliminates the manual burden of determining 
// the final academic status of students in a given institution.

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