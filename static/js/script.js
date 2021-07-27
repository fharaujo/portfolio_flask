var isname = document.querySelector('#name');
var email = document.querySelector('#email');
var message = document.querySelector('#message');
var btnSend = document.getElementById('send');

var okName = false;
var okEmail= false;
var okMsg = false;
btnSend.disabled = true;


isname.addEventListener('keyup', () =>{

    if(isname.value.length < 3){
        isname.style.borderColor = 'red';
        okName = false;
    }else{
        isname.style.borderColor = 'green';
        okName = true;
    }

    if(okName && okEmail && okMsg){
        btnSend.disabled = false;
    }else{
        btnSend.disabled = true;
    }

});

email.addEventListener('keyup', () =>{
    if(email.value.indexOf('@') == -1 || email.value.indexOf('.') == -1){  
        email.style.borderColor = 'red';
        
        okEmail = false;
    }else{
        email.style.borderColor = 'green';
        okEmail = true;
    }


    if(okName && okEmail && okMsg){
        btnSend.disabled = false;
    }else{
        btnSend.disabled = true;
    }

});

message.addEventListener('keyup', () =>{

    if(message.value.length > 100 || message.value.length < 3){
        message.style.borderColor = 'red';
        okMsg = false;
    }else{
        message.style.borderColor = 'green';
        okMsg = true;
    }

    if (okName && okEmail && okMsg) {
        btnSend.disabled = false;
     } else {
        btnSend.disabled = true;
     }
});

btnSend.addEventListener('click', () =>{
    alert('Mensagem enviada com sucesso!')
});





document.addEventListener("scroll", handleScroll);
// referencia do butão
var topBtn = document.querySelector("#btntop");

function handleScroll() {
  var scrollableHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var visible = 0.2;

  if ((document.documentElement.scrollTop / scrollableHeight ) > visible) {
    //show button
    topBtn.style.display = "block";
  } else {
    //hide button
    topBtn.style.display = "none";
  }
}

// evento click scrooll top 

topBtn.addEventListener("click", scrollToTop);

function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
}
