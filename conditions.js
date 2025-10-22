let coursemarks=24;
let exammarks =30;
let finalMarks = coursemarks + exammarks;
console.log(finalMarks);
// RANGE (0-49 F) (50-59 C) (60-69 B) (70 AND ABOVE A) 
// (=0 Expelled,1-10, Up your game, 11 above, Failed)
if (finalMarks <= 49){
console.log("Grade F");
}
else if(50 <= finalMarks <= 59){
console.log("Grade C");
}
else if(60 <=finalMarks<=69){
    console.log("Grade B");
}
 else{
    console.log("Grade A");
 }
if (finalMarks < 50){
  console.log("You have a retake");  
}
else{
    console.log("You have successfully passed");
}

let weekDayNumber= 20;
// 1="Monday", 2="Tuesday", 3="Wednesday",.....7="Sunday"
console.log(weekDayNumber);
switch(weekDayNumber){
    case 1:
        console.log("Monday");
        break;
    case 2:
        console.log("Tuesday");
        break;
            case 3:
        console.log("Wednesday");
        break;
            case 4:
        console.log("Thursday");
        break;
            case 5:
        console.log("Friday");
        break;
            case 6:
        console.log("Saturday");
        break;
            case 7:
        console.log("Sunday");
        break;
        default:
            console.log("Out of range");

}
LOOPS
let x = 0;
var x =0;
while (x<=10){
     if (x == 5) {
         x++;
         console.log(x);
         continue;
     }
     console.log(x);
     //x++;
     x = x+1}
 for(let myNumber = 0; myNumber <=10; myNumber++){
     if (myNumber % 2 !==0){
     console.log(myNumber);
 }}

function AddMarks(courseWorKmarks,examMarks, percentageofAttendance){
    return (courseWorKmarks + examMarks) * percentageofAttendance;
}
let result = AddMarks(30, 20,0.2)
console.log(result);
console.log(finalMarks);

// console.log(AddMarks(40,50,0.7));



