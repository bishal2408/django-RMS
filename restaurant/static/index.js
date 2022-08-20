function validate() {
    var name = document.getElementById("name").value;
    var password = document.getElementById("password").value;
    var repassword = document.getElementById("repassword").value;
    var email = document.getElementById("email").value;
    var username = document.getElementById("username").value;
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    var ch = document.getElementById("term-check");

    if (name == "") {
        document.getElementById("dis_name").innerHTML = "Name Field is required";
        return false;
    } else {
        document.getElementById("dis_name").innerHTML = "";
    }

    if (!email.match(validRegex)) {
        document.getElementById("dis_email").innerHTML = "Enter email in correct format";
        return false;
    } else{
        document.getElementById("dis_email").innerHTML = "";
    }

     if (username.length < 5) {
        document.getElementById("dis_username").innerHTML = "Username must have atleast 5 characters";
        return false;
    } else{
        document.getElementById("dis_username").innerHTML = "";
    }
    
    if (password.length < 6) {
        document.getElementById("dis_pass").innerHTML = "Password must have ateast 6 characters";
        return false;
    } else{
        document.getElementById("dis_pass").innerHTML = "";
    }
    
    if (password != repassword) {
        document.getElementById("dis_repass").innerHTML = "Password and repassword must be same";
        return false;
    }else{
        document.getElementById("dis_repass").innerHTML = "";
    }

    if(!ch.checked){
        alert("Please accept terms and conditions to continue!");
        return false;
    }
    else{
        return true;
    }
}
