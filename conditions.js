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
