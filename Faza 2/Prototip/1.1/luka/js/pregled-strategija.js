var elementList;

$(document).ready(function(){
    elementList = -1;
})

function brisanjeModal(id){
    var modal = document.getElementById("myModal");
    modal.style.display = 'block';

    elementList = id;
}

function daBrisanje(){
    var listEl = document.getElementById("li"+elementList);
    listEl.parentNode.removeChild(listEl);
    neBrisanje();
}

function neBrisanje(){
    var modal = document.getElementById("myModal");
    modal.style.display = 'none';
}

function kreiraj(){
    var ime = document.getElementById('strategy').value;
    if(ime === '') 
    {
        alert("Naziv strategije nije u validnom formatu!");
        return;
    }

    var entry = document.createElement('li');
    entry.className = "list-group-item";

    var duzinaListe = $('ul#lista li').length;
    entry.id = "li" + duzinaListe;

    document.getElementById('strategy').value = '';
    entry.appendChild(document.createTextNode(ime + " "));

    var dugmeOtvori = document.createElement('button');
    dugmeOtvori.type = 'button';
    dugmeOtvori.className = 'btn btn-success';
    dugmeOtvori.innerHTML = 'Otvori';
    dugmeOtvori.onclick = function() {
        window.location.href='otvorena-strategija.html';
    }

    entry.appendChild(dugmeOtvori);

    entry.appendChild(document.createTextNode(" "));
    
    var dugmeZatvori = document.createElement('button');
    dugmeZatvori.type = 'button';
    dugmeZatvori.className = 'btn btn-danger';
    dugmeZatvori.innerHTML = 'Izbrisi';
    dugmeZatvori.onclick = function(){
        var modal = document.getElementById("myModal");
        modal.style.display = 'block';

        elementList = duzinaListe;
    }

    entry.appendChild(dugmeZatvori);

    var listPosl = document.getElementById("poslednji");
    listPosl.parentNode.insertBefore(entry, listPosl);
}