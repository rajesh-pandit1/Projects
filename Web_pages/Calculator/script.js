let string = ""
let buttons = document.querySelectorAll('.keyboard');
console.log(buttons);
Array.from(buttons).forEach((button)=>{
    button.addEventListener('click', (e)=>{
        if(e.target.value == "="){
            string = eval(string);
            document.querySelector('input').value = string;
        }
        else if(e.target.innerHTML == "C"){
            string = "";
            document.querySelector('input').value = string;
        }
        else if(e.target.innerHTML == "B"){
            string = string.slice(0, -1)
            document.querySelector('input').value = string;
        }
        else if(e.target.innerHTML == "%"){
            string = (eval(string))*1/100;
            document.querySelector('input').value = string;
        }
        else{
        string = string + e.target.innerHTML;
        document.querySelector('input').value = string;
        }
    })
})