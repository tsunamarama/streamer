function myFunction() {
  document.getElementById("actors-dropdown").classList.toggle("show");
}

function actorFilterFunction() {
  let input, filter, ul, li, a, i;
  input = document.getElementById("actors-input");
  filter = input.value.toUpperCase();
  div = document.getElementById("actors-dropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

function directorFilterFunction() {
  let input, filter, ul, li, a, i;
  input = document.getElementById("directors-input");
  filter = input.value.toUpperCase();
  div = document.getElementById("directors-dropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

function movieFilterFunction() {
  let input, filter, ul, li, a, i;
  input = document.getElementById("movies-input");
  filter = input.value.toUpperCase();
  div = document.getElementById("movies-dropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}
