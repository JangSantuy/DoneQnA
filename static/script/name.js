const swals = Swal.mixin({
backdrop: 'rgba(0,0,123,0.4)', cancelButtonColor: '#909090', allowOutsideClick: false,
});

async function mulai(){
  var { value: nama } = await swals.fire({
  
    title: 'Nama kamu?',
    input: 'text',
    confirmButtonText: 'Lanjut',
    showCancelButton: false,
    
});
window.nama = nama;
var i =0;
var txt = `Hai ${nama} `;

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("sapa").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, 200);
  }
}

if(nama && nama.length < 11){
    
var img = document.getElementById("name");
img.setAttribute("value", nama);
typeWriter();

  
var myTimeout = setTimeout(function() {
document.getElementById("hide").style.display = "block";
}, 2000);
play();



} else{

await swals.fire('Ups!', 'Nama tidak boleh kosong atau lebih dari 10 karakter, ya!');

    mulai();
}
}
mulai();


