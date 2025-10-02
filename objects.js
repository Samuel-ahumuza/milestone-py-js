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